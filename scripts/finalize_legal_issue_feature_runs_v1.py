#!/usr/bin/env python3
"""Merge Legal Issue feature run repairs and revalidate final annotations."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from run_legal_issue_feature_annotation_jobs_v1 import (
    iter_jsonl,
    validation_warnings_for_annotation,
)


ROOT = Path(__file__).resolve().parents[1]
RUN_DIR = ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_full_runs"
JOBS = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_jobs/"
    "legal_issue_feature_jobs_v1.full_plus_v3_1_16k.jsonl"
)
DEFAULT_RUNS = [
    "legal_issue_feature_full_v1_16k",
    "legal_issue_feature_full_v1_16k_gpt54_review",
    "legal_issue_feature_full_v1_16k_gpt55_failed_review",
    "legal_issue_feature_full_v1_16k_gpt55_needs_review",
    "legal_issue_feature_full_v1_16k_gpt56sol_failed_final",
    "legal_issue_feature_full_v1_16k_gpt56sol_needs_review_final",
]


def read_latest_checkpoint(path: Path) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    if not path.exists():
        return latest
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            job_id = row.get("job_id")
            if job_id:
                latest[job_id] = row
    return latest


def revalidated_record(record: dict[str, Any], job: dict[str, Any]) -> dict[str, Any]:
    record = dict(record)
    if record.get("status") == "failed":
        return record
    warnings = validation_warnings_for_annotation(
        record.get("annotation") or {},
        job.get("expected_feature_keys_by_issue", {}),
    )
    record["validation_warnings"] = warnings
    record["status"] = "valid" if not warnings else "needs_review"
    record["final_revalidated"] = True
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=Path, default=JOBS)
    parser.add_argument("--run-dir", type=Path, default=RUN_DIR)
    parser.add_argument("--runs", nargs="*", default=DEFAULT_RUNS)
    parser.add_argument(
        "--output",
        type=Path,
        default=RUN_DIR / "legal_issue_feature_full_v1_16k_final_merged.json",
    )
    parser.add_argument(
        "--summary",
        type=Path,
        default=RUN_DIR / "legal_issue_feature_full_v1_16k_final_merged.summary.json",
    )
    parser.add_argument(
        "--manual-review",
        type=Path,
        default=RUN_DIR / "legal_issue_feature_full_v1_16k_final_manual_review.json",
    )
    args = parser.parse_args()

    jobs = iter_jsonl(args.jobs)
    jobs_by_id = {job["job_id"]: job for job in jobs}
    merged: dict[str, dict[str, Any]] = {}
    lineage: dict[str, str] = {}

    for run_name in args.runs:
        checkpoint = args.run_dir / f"{run_name}.checkpoint.jsonl"
        for job_id, record in read_latest_checkpoint(checkpoint).items():
            if job_id in jobs_by_id:
                merged[job_id] = dict(record)
                lineage[job_id] = run_name

    ordered: list[dict[str, Any]] = []
    for job in jobs:
        record = merged.get(job["job_id"])
        if not record:
            continue
        record = revalidated_record(record, job)
        record["final_source_run"] = lineage.get(job["job_id"])
        ordered.append(record)

    status_counts = Counter(row.get("status", "unknown") for row in ordered)
    warning_counts: Counter[str] = Counter()
    source_counts = Counter(row.get("final_source_run", "unknown") for row in ordered)
    for row in ordered:
        for warning in row.get("validation_warnings") or []:
            warning_counts[warning.get("code", "unknown")] += 1

    manual = [
        row for row in ordered
        if row.get("status") in {"failed", "needs_review"}
    ]
    summary = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "total_jobs": len(jobs),
        "merged_jobs": len(ordered),
        "missing_jobs": len(jobs) - len(ordered),
        "status_counts": dict(status_counts),
        "warning_counts": dict(warning_counts),
        "source_counts": dict(source_counts),
        "manual_review_count": len(manual),
        "manual_review_job_ids": [row.get("job_id") for row in manual],
    }

    args.output.write_text(
        json.dumps({"summary": summary, "results": ordered}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.summary.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    args.manual_review.write_text(
        json.dumps({"count": len(manual), "items": manual}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
