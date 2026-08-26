#!/usr/bin/env python3
"""Summarize a full Legal Issue feature annotation run.

The batch runner appends retries to a checkpoint JSONL. This report uses the
latest record per job_id so failed-only reruns do not double count earlier
attempts.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_RUN_DIR = Path("data/courtlistener_legal_20k/analytics_v1/feature_full_runs")
DEFAULT_JOB_PATH = Path(
    "data/courtlistener_legal_20k/analytics_v1/feature_jobs/"
    "legal_issue_feature_jobs_v1.full_plus_v3_1_16k.jsonl"
)


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def latest_checkpoint_rows(path: Path) -> dict[str, dict[str, Any]]:
    latest: dict[str, dict[str, Any]] = {}
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            job_id = row.get("job_id")
            if job_id:
                latest[job_id] = row
    return latest


def pct(n: int | float, d: int | float) -> float:
    return round((n / d * 100.0), 2) if d else 0.0


def compact_counter(counter: Counter, limit: int = 30) -> list[dict[str, Any]]:
    return [{"value": key, "count": value} for key, value in counter.most_common(limit)]


def feature_rows(annotation: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for issue_ann in annotation.get("legal_issue_feature_annotations") or []:
        issue_id = issue_ann.get("issue_id")
        issue_status = issue_ann.get("issue_status")
        for feature in issue_ann.get("features") or []:
            item = dict(feature)
            item["_issue_id"] = issue_id
            item["_issue_status"] = issue_status
            rows.append(item)
    return rows


def build_report(jobs: list[dict[str, Any]], latest: dict[str, dict[str, Any]]) -> dict[str, Any]:
    job_ids = {job.get("job_id") for job in jobs}
    missing_checkpoint = sorted(j for j in job_ids if j and j not in latest)
    status_counts = Counter(row.get("status", "unknown") for row in latest.values())
    warning_counts: Counter[str] = Counter()
    error_counts: Counter[str] = Counter()
    issue_status_counts: Counter[str] = Counter()
    issue_counts: Counter[str] = Counter()
    issue_by_status: dict[str, Counter[str]] = defaultdict(Counter)
    feature_status_counts: Counter[str] = Counter()
    feature_key_counts: Counter[str] = Counter()
    feature_present_counts: Counter[str] = Counter()
    feature_warning_counts: dict[str, Counter[str]] = defaultdict(Counter)
    case_ids = set()
    usage = Counter()
    latencies: list[float] = []
    failed_jobs = []
    needs_review_jobs = []

    for row in latest.values():
        case_id = row.get("case_id")
        if case_id:
            case_ids.add(case_id)
        for key, value in (row.get("usage") or {}).items():
            if isinstance(value, (int, float)):
                usage[key] += value
        if isinstance(row.get("latency_seconds"), (int, float)):
            latencies.append(float(row["latency_seconds"]))

        status = row.get("status")
        for warning in row.get("validation_warnings") or []:
            if isinstance(warning, dict):
                name = warning.get("code") or warning.get("type") or warning.get("warning")
                feature_key = warning.get("feature_key")
            else:
                name = str(warning)
                feature_key = None
            if name:
                warning_counts[str(name)] += 1
                if feature_key:
                    feature_warning_counts[str(feature_key)][str(name)] += 1

        if status == "failed":
            err = row.get("error") or row.get("exception") or row.get("message") or "unknown"
            error_counts[str(err)] += 1
            failed_jobs.append(
                {
                    "job_id": row.get("job_id"),
                    "case_id": row.get("case_id"),
                    "case_name": row.get("case_name"),
                    "issue_ids": row.get("issue_ids"),
                    "error": err,
                }
            )
            continue

        if status == "needs_review":
            needs_review_jobs.append(
                {
                    "job_id": row.get("job_id"),
                    "case_id": row.get("case_id"),
                    "case_name": row.get("case_name"),
                    "issue_ids": row.get("issue_ids"),
                    "warnings": row.get("validation_warnings") or [],
                }
            )

        annotation = row.get("annotation") or {}
        for issue_ann in annotation.get("legal_issue_feature_annotations") or []:
            issue_id = issue_ann.get("issue_id") or "unknown"
            issue_status = issue_ann.get("issue_status") or "unknown"
            issue_counts[issue_id] += 1
            issue_status_counts[issue_status] += 1
            issue_by_status[issue_id][issue_status] += 1

        for feature in feature_rows(annotation):
            key = feature.get("feature_key") or "unknown"
            f_status = feature.get("status") or "unknown"
            feature_key_counts[key] += 1
            feature_status_counts[f_status] += 1
            if f_status == "present":
                feature_present_counts[key] += 1

    per_issue = []
    for issue_id, count in issue_counts.most_common():
        statuses = issue_by_status[issue_id]
        decided_like = statuses.get("decided", 0)
        per_issue.append(
            {
                "issue_id": issue_id,
                "annotations": count,
                "issue_status_counts": dict(statuses),
                "decided_rate": pct(decided_like, count),
            }
        )

    per_feature = []
    for key, count in feature_key_counts.most_common():
        present = feature_present_counts.get(key, 0)
        per_feature.append(
            {
                "feature_key": key,
                "annotations": count,
                "present": present,
                "present_rate": pct(present, count),
                "warning_counts": dict(feature_warning_counts.get(key, Counter())),
            }
        )

    latency_summary = {}
    if latencies:
        ordered = sorted(latencies)
        latency_summary = {
            "count": len(ordered),
            "avg_seconds": round(sum(ordered) / len(ordered), 3),
            "p50_seconds": round(ordered[int(len(ordered) * 0.50)], 3),
            "p90_seconds": round(ordered[int(len(ordered) * 0.90)], 3),
            "max_seconds": round(max(ordered), 3),
        }

    total_jobs = len(jobs)
    latest_total = len(latest)
    valid = status_counts.get("valid", 0)
    needs_review = status_counts.get("needs_review", 0)
    failed = status_counts.get("failed", 0)
    usable = valid + needs_review

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "jobs_total": total_jobs,
            "checkpoint_latest_jobs": latest_total,
            "missing_checkpoint_jobs": len(missing_checkpoint),
        },
        "overall": {
            "total_jobs": total_jobs,
            "unique_cases": len(case_ids),
            "valid": valid,
            "needs_review": needs_review,
            "failed": failed,
            "usable_annotations": usable,
            "completion_rate": pct(latest_total, total_jobs),
            "valid_rate": pct(valid, total_jobs),
            "needs_review_rate": pct(needs_review, total_jobs),
            "failed_rate": pct(failed, total_jobs),
            "usable_rate": pct(usable, total_jobs),
        },
        "status_counts": dict(status_counts),
        "warning_counts": dict(warning_counts),
        "error_counts": dict(error_counts),
        "issue_status_counts": dict(issue_status_counts),
        "feature_status_counts": dict(feature_status_counts),
        "top_issues": compact_counter(issue_counts, 50),
        "top_features": compact_counter(feature_key_counts, 50),
        "per_issue": per_issue,
        "per_feature": per_feature,
        "latency": latency_summary,
        "usage": dict(usage),
        "failed_jobs": failed_jobs,
        "needs_review_sample": needs_review_jobs[:50],
        "missing_checkpoint_job_ids": missing_checkpoint[:100],
    }


def write_markdown(report: dict[str, Any], path: Path) -> None:
    overall = report["overall"]
    lines = [
        "# Legal Issue Feature Full Run Quality Report",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        "## Overall",
        "",
        f"- Total jobs: `{overall['total_jobs']}`",
        f"- Unique cases: `{overall['unique_cases']}`",
        f"- Completion rate: `{overall['completion_rate']}%`",
        f"- Valid: `{overall['valid']}` (`{overall['valid_rate']}%`)",
        f"- Needs review: `{overall['needs_review']}` (`{overall['needs_review_rate']}%`)",
        f"- Failed: `{overall['failed']}` (`{overall['failed_rate']}%`)",
        f"- Usable annotations: `{overall['usable_annotations']}` (`{overall['usable_rate']}%`)",
        "",
        "## Warning Counts",
        "",
    ]
    if report["warning_counts"]:
        for key, value in sorted(report["warning_counts"].items(), key=lambda x: (-x[1], x[0])):
            lines.append(f"- `{key}`: `{value}`")
    else:
        lines.append("- None")
    lines.extend(["", "## Failed Jobs", ""])
    if report["failed_jobs"]:
        for job in report["failed_jobs"]:
            lines.append(f"- `{job['job_id']}`: {job['error']}")
    else:
        lines.append("- None")
    lines.extend(["", "## Issue Status Counts", ""])
    for key, value in sorted(report["issue_status_counts"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Feature Status Counts", ""])
    for key, value in sorted(report["feature_status_counts"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Top Legal Issues", ""])
    for item in report["top_issues"][:30]:
        lines.append(f"- `{item['value']}`: `{item['count']}`")
    lines.extend(["", "## Top Feature Keys", ""])
    for item in report["top_features"][:30]:
        lines.append(f"- `{item['value']}`: `{item['count']}`")
    lines.extend(["", "## Latency And Usage", ""])
    lines.append("```json")
    lines.append(json.dumps({"latency": report["latency"], "usage": report["usage"]}, ensure_ascii=False, indent=2))
    lines.append("```")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--jobs", type=Path, default=DEFAULT_JOB_PATH)
    parser.add_argument("--checkpoint", type=Path, default=DEFAULT_RUN_DIR / "legal_issue_feature_full_v1_16k.checkpoint.jsonl")
    parser.add_argument("--output-json", type=Path, default=DEFAULT_RUN_DIR / "legal_issue_feature_full_v1_16k.quality_report.json")
    parser.add_argument("--output-md", type=Path, default=DEFAULT_RUN_DIR / "LEGAL_ISSUE_FEATURE_FULL_V1_16K_QUALITY_REPORT.md")
    args = parser.parse_args()

    jobs = read_jsonl(args.jobs)
    latest = latest_checkpoint_rows(args.checkpoint)
    report = build_report(jobs, latest)
    args.output_json.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    write_markdown(report, args.output_md)
    print(json.dumps(report["overall"], ensure_ascii=False, indent=2))
    print(f"Wrote {args.output_json}")
    print(f"Wrote {args.output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
