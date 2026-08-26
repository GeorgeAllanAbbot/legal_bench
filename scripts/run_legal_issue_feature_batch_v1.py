#!/usr/bin/env python3
"""Run resumable concurrent Legal Issue feature annotation jobs."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from provider_circuit_breaker import breaker_from_config, is_http_503
from run_legal_issue_feature_annotation_jobs_v1 import (
    call_job,
    iter_jsonl,
    response_schema,
)
from run_taxonomy_pilot_v3 import model_config


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/configs/"
    "analytical_feature_llm_v1_3.yaml"
)
DEFAULT_JOBS = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_jobs/"
    "legal_issue_feature_jobs_v1.full_plus_v3_1.jsonl"
)
DEFAULT_OUTPUT_DIR = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_full_runs"
)

THREAD_LOCAL = threading.local()


class JobCache:
    """Persistent cache for successful API calls keyed by full job prompt."""

    def __init__(self, path: Path):
        self.path = path
        self.lock = threading.Lock()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with sqlite3.connect(self.path) as connection:
            connection.execute("PRAGMA journal_mode=WAL")
            connection.execute("""
                CREATE TABLE IF NOT EXISTS job_cache (
                    cache_key TEXT PRIMARY KEY,
                    job_id TEXT NOT NULL,
                    case_id TEXT NOT NULL,
                    payload_json TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
            connection.execute(
                "CREATE INDEX IF NOT EXISTS idx_job_cache_job_id "
                "ON job_cache(job_id)"
            )

    @staticmethod
    def key(model: str, job: dict[str, Any]) -> str:
        material = json.dumps({
            "task": "legal_issue_feature_annotation_v1",
            "prompt_version": "1.1",
            "model": model,
            "messages": job.get("messages", []),
            "expected_feature_keys_by_issue": job.get(
                "expected_feature_keys_by_issue", {}
            ),
            "schema": response_schema(),
        }, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(material.encode("utf-8")).hexdigest()

    def get(self, cache_key: str) -> dict[str, Any] | None:
        with self.lock, sqlite3.connect(self.path) as connection:
            row = connection.execute(
                "SELECT payload_json FROM job_cache WHERE cache_key = ?",
                (cache_key,),
            ).fetchone()
        return json.loads(row[0]) if row else None

    def put(self, cache_key: str, job: dict[str, Any], payload: dict[str, Any]) -> None:
        with self.lock, sqlite3.connect(self.path) as connection:
            connection.execute(
                "INSERT OR REPLACE INTO job_cache "
                "(cache_key, job_id, case_id, payload_json, created_at) "
                "VALUES (?, ?, ?, ?, ?)",
                (
                    cache_key,
                    job["job_id"],
                    job["case_id"],
                    json.dumps(payload, ensure_ascii=False),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )


def thread_client(config: dict[str, Any], env_file: Path) -> tuple[Any, str]:
    if not hasattr(THREAD_LOCAL, "client"):
        THREAD_LOCAL.client, THREAD_LOCAL.model = model_config(config, env_file)
    return THREAD_LOCAL.client, THREAD_LOCAL.model


def load_checkpoint(path: Path) -> dict[str, dict[str, Any]]:
    completed: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return completed
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            # Treat every non-failed API result as complete. "needs_review" is
            # a valid artifact for later repair and should not trigger another
            # paid call during ordinary resume.
            if record.get("status") != "failed" and record.get("job_id"):
                completed[record["job_id"]] = record
    return completed


def load_latest_checkpoint(path: Path) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return latest
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            record = json.loads(line)
            job_id = record.get("job_id")
            if job_id:
                latest[job_id] = record
    return latest


def run_one(
    job: dict[str, Any],
    config: dict[str, Any],
    env_file: Path,
    cache: JobCache,
) -> dict[str, Any]:
    client, model = thread_client(config, env_file)
    cache_key = cache.key(model, job)
    cached = cache.get(cache_key)
    if cached is not None:
        cached = dict(cached)
        cached["response_mode"] = "job_cache"
        return cached

    started = time.perf_counter()
    max_attempts = int(config.get("provider", {}).get("max_retries", 3)) + 3
    provider_errors: list[str] = []
    for attempt in range(1, max_attempts + 1):
        try:
            breaker = breaker_from_config(config)
            original_create = client.chat.completions.create

            def create_with_breaker(**kwargs: Any) -> Any:
                return breaker.call(original_create, **kwargs)

            client.chat.completions.create = create_with_breaker
            try:
                record = call_job(client, model, config, job)
            finally:
                client.chat.completions.create = original_create
            record["response_mode"] = "api"
            record["elapsed_seconds_total"] = round(time.perf_counter() - started, 3)
            if provider_errors:
                record["provider_retry_errors"] = provider_errors
            cache.put(cache_key, job, record)
            return record
        except Exception as error:  # noqa: BLE001 - checkpoint failed jobs.
            if not is_retryable_provider_error(error) or attempt >= max_attempts:
                return {
                    "job_id": job.get("job_id"),
                    "case_id": job.get("case_id"),
                    "case_name": job.get("case_name"),
                    "issue_ids": job.get("issue_ids", []),
                    "status": "failed",
                    "error_type": type(error).__name__,
                    "error": f"{type(error).__name__}: {error}",
                    "provider_retry_errors": provider_errors,
                    "elapsed_seconds_total": round(time.perf_counter() - started, 3),
                }
            provider_errors.append(f"{type(error).__name__}: {error}")
            sleep_seconds = min(
                float(config.get("runtime", {}).get("provider_503_pause_seconds", 300)),
                15.0 * attempt,
            )
            print(
                f"Provider overload/rate-limit on {job.get('job_id')} "
                f"attempt {attempt}/{max_attempts}; sleeping {sleep_seconds:.0f}s.",
                flush=True,
            )
            time.sleep(sleep_seconds)


def is_retryable_provider_error(error: BaseException) -> bool:
    error_type = type(error).__name__.lower()
    if "connection" in error_type or "timeout" in error_type:
        return True
    if is_http_503(error):
        return True
    status = getattr(error, "status_code", None)
    if status == 429:
        return True
    response = getattr(error, "response", None)
    if getattr(response, "status_code", None) == 429:
        return True
    message = str(error).lower()
    return (
        "rate_limit" in message
        or "connection error" in message
        or "timed out" in message
        or "timeout" in message
        or "too many pending requests" in message
        or "too many requests" in message
    )


def summarize(records: list[dict[str, Any]]) -> dict[str, Any]:
    status_counts: dict[str, int] = {}
    warning_counts: dict[str, int] = {}
    total_usage: dict[str, int] = {}
    for record in records:
        status = record.get("status", "unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
        for warning in record.get("validation_warnings", []) or []:
            code = warning.get("code", "unknown")
            warning_counts[code] = warning_counts.get(code, 0) + 1
        for key, value in (record.get("usage") or {}).items():
            if isinstance(value, int):
                total_usage[key] = total_usage.get(key, 0) + value
    return {
        "status_counts": status_counts,
        "warning_counts": warning_counts,
        "total_usage": total_usage,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", type=Path, default=DEFAULT_JOBS)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--env-file", type=Path, default=ROOT / ".env")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--run-name", default="legal_issue_feature_full_v1")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--concurrency", type=int, default=None)
    parser.add_argument("--progress-every", type=int, default=10)
    parser.add_argument("--resume", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument(
        "--failed-only",
        action="store_true",
        help="Run only jobs whose latest checkpoint record is failed.",
    )
    parser.add_argument(
        "--needs-review-only",
        action="store_true",
        help="Run only jobs whose latest checkpoint record is needs_review.",
    )
    parser.add_argument(
        "--source-checkpoint",
        type=Path,
        default=None,
        help=(
            "Checkpoint used to select failed/needs_review jobs. Defaults to "
            "the destination run checkpoint."
        ),
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Override provider.model for this invocation without editing config.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    if args.model:
        config.setdefault("provider", {})["model"] = args.model
        config["provider"]["model_env"] = ""
    concurrency = args.concurrency or int(config["runtime"].get("concurrency", 2))
    if concurrency < 1:
        raise SystemExit("--concurrency must be at least 1")

    jobs = iter_jsonl(args.jobs)
    if args.limit > 0:
        jobs = jobs[:args.limit]

    args.output_dir.mkdir(parents=True, exist_ok=True)
    checkpoint = args.output_dir / f"{args.run_name}.checkpoint.jsonl"
    output = args.output_dir / f"{args.run_name}.json"
    summary_path = args.output_dir / f"{args.run_name}.summary.json"
    cache = JobCache(args.output_dir / f"{args.run_name}.job_cache.sqlite")

    completed = load_checkpoint(checkpoint) if args.resume else {}
    source_checkpoint = args.source_checkpoint or checkpoint
    if args.failed_only or args.needs_review_only:
        latest = load_latest_checkpoint(source_checkpoint)
        target_status = "failed" if args.failed_only else "needs_review"
        target_ids = {
            job_id for job_id, record in latest.items()
            if record.get("status") == target_status
        }
        pending = [job for job in jobs if job["job_id"] in target_ids]
    else:
        pending = [job for job in jobs if job["job_id"] not in completed]

    client, model = model_config(config, args.env_file)
    del client
    started = time.perf_counter()
    print(
        f"Starting {args.run_name}: total={len(jobs)} completed={len(completed)} "
        f"pending={len(pending)} model={model} concurrency={concurrency}",
        flush=True,
    )

    with checkpoint.open("a", encoding="utf-8") as handle:
        pool = ThreadPoolExecutor(max_workers=concurrency)
        futures = {
            pool.submit(run_one, job, config, args.env_file.resolve(), cache): job
            for job in pending
        }
        done_now = 0
        try:
            for future in as_completed(futures):
                record = future.result()
                handle.write(json.dumps(record, ensure_ascii=False) + "\n")
                handle.flush()
                if record.get("status") != "failed":
                    completed[record["job_id"]] = record
                done_now += 1
                elapsed = time.perf_counter() - started
                rate = done_now / elapsed if elapsed else 0
                remaining = len(pending) - done_now
                eta = remaining / rate if rate else 0
                if (
                    done_now == 1
                    or done_now == len(pending)
                    or done_now % max(args.progress_every, 1) == 0
                    or record.get("status") == "failed"
                ):
                    print(
                        f"Completed {done_now}/{len(pending)} this run | "
                        f"latest={record.get('status')} | "
                        f"{rate * 60:.2f} jobs/min | ETA {eta / 60:.1f}m",
                        flush=True,
                    )
        except KeyboardInterrupt:
            for future in futures:
                future.cancel()
            pool.shutdown(wait=False, cancel_futures=True)
            print(
                "Interrupted; checkpoint contains completed non-failed jobs. "
                "Rerun with --resume to continue.",
                flush=True,
            )
            raise
        else:
            pool.shutdown(wait=True)

    final_completed = load_checkpoint(checkpoint)
    ordered = [final_completed[job["job_id"]] for job in jobs if job["job_id"] in final_completed]
    summary = {
        "run_name": args.run_name,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "jobs_path": str(args.jobs.resolve()),
        "checkpoint": str(checkpoint.resolve()),
        "cache": str(cache.path.resolve()),
        "total_jobs": len(jobs),
        "completed_jobs": len(ordered),
        "remaining_jobs": len(jobs) - len(ordered),
        "concurrency": concurrency,
        "elapsed_seconds_this_invocation": round(time.perf_counter() - started, 3),
        **summarize(ordered),
    }
    output.write_text(
        json.dumps({"summary": summary, "results": ordered}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
