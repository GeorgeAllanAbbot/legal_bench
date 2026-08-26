#!/usr/bin/env python3
"""Analyze final merged Legal Issue feature annotation results."""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RESULTS = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_full_runs/"
    "legal_issue_feature_full_v1_16k_final_merged.json"
)
DEFAULT_PROJECTION = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/full_runs/"
    "taxonomy_v3_full_20k.projection_plus_v3_1_issues.jsonl"
)
DEFAULT_OUT_JSON = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_full_runs/"
    "legal_issue_feature_full_v1_16k_distribution_analysis.json"
)
DEFAULT_OUT_MD = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_full_runs/"
    "LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md"
)


def pct(n: int | float, d: int | float) -> float:
    return round(n / d * 100, 2) if d else 0.0


def top(counter: Counter, n: int = 30) -> list[dict[str, Any]]:
    return [{"value": k, "count": v} for k, v in counter.most_common(n)]


def atom(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, (str, int, float, bool)):
        return str(value)
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def iter_projection(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def extract_projection_lists(row: dict[str, Any]) -> dict[str, list[str]]:
    # Projection files in this project evolved over time; support the common
    # top-level and nested names without assuming one exact schema.
    tax = row.get("taxonomy") or row.get("classification") or row
    def normalize_item(item: Any) -> str | None:
        if isinstance(item, str):
            return item or None
        if isinstance(item, dict):
            for key in ("id", "issue_id", "primary", "value"):
                value = item.get(key)
                if isinstance(value, str) and value:
                    return value
        return None

    def listish(*keys: str) -> list[str]:
        for key in keys:
            value = tax.get(key)
            if isinstance(value, dict):
                values = []
                primary = normalize_item(value.get("primary"))
                if primary:
                    values.append(primary)
                secondary = value.get("secondary")
                if isinstance(secondary, list):
                    values.extend(x for x in (normalize_item(item) for item in secondary) if x)
                item = normalize_item(value)
                if item and item not in values:
                    values.append(item)
                if values:
                    return values
            if isinstance(value, list):
                return [x for x in (normalize_item(item) for item in value) if x]
            if isinstance(value, str) and value:
                return [value]
        return []
    return {
        "practice_area": listish("practice_area", "practice_areas"),
        "matter_type": listish("matter_type", "matter_types"),
        "legal_issue": listish("legal_issues", "legal_issue"),
    }


def feature_annotations(record: dict[str, Any]) -> list[dict[str, Any]]:
    rows = []
    annotation = record.get("annotation") or {}
    for issue in annotation.get("legal_issue_feature_annotations") or []:
        issue_id = issue.get("issue_id") or "unknown"
        issue_status = issue.get("issue_status") or "unknown"
        issue_outcome = issue.get("issue_specific_outcome")
        for feature in issue.get("features") or []:
            rows.append({
                "case_id": record.get("case_id"),
                "job_id": record.get("job_id"),
                "issue_id": issue_id,
                "issue_status": issue_status,
                "issue_specific_outcome": issue_outcome,
                "feature_key": feature.get("feature_key") or "unknown",
                "feature_status": feature.get("status") or "unknown",
                "value": feature.get("value"),
                "unit": feature.get("unit"),
                "confidence": feature.get("confidence"),
                "evidence": feature.get("evidence") or [],
            })
    return rows


def numeric_summary(values: list[float]) -> dict[str, Any]:
    if not values:
        return {}
    ordered = sorted(values)
    def q(p: float) -> float:
        idx = min(len(ordered) - 1, max(0, int(math.floor((len(ordered) - 1) * p))))
        return round(ordered[idx], 3)
    return {
        "count": len(values),
        "min": round(ordered[0], 3),
        "p25": q(0.25),
        "median": q(0.50),
        "p75": q(0.75),
        "max": round(ordered[-1], 3),
        "mean": round(sum(values) / len(values), 3),
    }


def analyze(results: dict[str, Any], projection_rows: list[dict[str, Any]]) -> dict[str, Any]:
    records = results.get("results") or []
    total_jobs = len(records)
    case_ids = {r.get("case_id") for r in records if r.get("case_id")}
    source_counts = Counter(r.get("final_source_run") or "unknown" for r in records)
    status_counts = Counter(r.get("status") or "unknown" for r in records)
    issue_counts: Counter[str] = Counter()
    issue_status_counts: Counter[str] = Counter()
    issue_outcome_counts: Counter[str] = Counter()
    issue_by_status: dict[str, Counter] = defaultdict(Counter)
    issue_by_outcome: dict[str, Counter] = defaultdict(Counter)
    court_action_counts: Counter[str] = Counter()
    feature_counts: Counter[str] = Counter()
    feature_status_counts: Counter[str] = Counter()
    feature_present_counts: Counter[str] = Counter()
    feature_value_counts: dict[str, Counter] = defaultdict(Counter)
    feature_units: dict[str, Counter] = defaultdict(Counter)
    evidence_role_counts: Counter[str] = Counter()
    assertion_scope_counts: Counter[str] = Counter()
    provenance_scope_counts: Counter[str] = Counter()
    confidence_values: list[float] = []
    feature_confidence: dict[str, list[float]] = defaultdict(list)
    numeric_values: dict[str, list[float]] = defaultdict(list)

    cases_with_decided = set()
    cases_with_present = set()
    cases_by_issue: dict[str, set[str]] = defaultdict(set)

    for record in records:
        annotation = record.get("annotation") or {}
        for issue in annotation.get("legal_issue_feature_annotations") or []:
            issue_id = issue.get("issue_id") or "unknown"
            issue_status = issue.get("issue_status") or "unknown"
            outcome = atom(issue.get("issue_specific_outcome"))
            issue_counts[issue_id] += 1
            issue_status_counts[issue_status] += 1
            issue_outcome_counts[outcome] += 1
            issue_by_status[issue_id][issue_status] += 1
            issue_by_outcome[issue_id][outcome] += 1
            court_action_counts[issue.get("court_action") or "unknown"] += 1
            case_id = record.get("case_id")
            if case_id:
                cases_by_issue[issue_id].add(case_id)
                if issue_status == "decided":
                    cases_with_decided.add(case_id)

        for row in feature_annotations(record):
            key = row["feature_key"]
            fstatus = row["feature_status"]
            feature_counts[key] += 1
            feature_status_counts[fstatus] += 1
            if fstatus == "present":
                feature_present_counts[key] += 1
                if row["case_id"]:
                    cases_with_present.add(row["case_id"])
                feature_value_counts[key][atom(row["value"])] += 1
                if isinstance(row["value"], (int, float)) and not isinstance(row["value"], bool):
                    numeric_values[key].append(float(row["value"]))
            if row["unit"]:
                feature_units[key][str(row["unit"])] += 1
            conf = row.get("confidence")
            if isinstance(conf, (int, float)):
                confidence_values.append(float(conf))
                feature_confidence[key].append(float(conf))
            for ev in row["evidence"]:
                if isinstance(ev, dict):
                    evidence_role_counts[ev.get("role") or "unknown"] += 1
                    assertion_scope_counts[ev.get("assertion_scope") or "unknown"] += 1
                    provenance_scope_counts[ev.get("provenance_scope") or "unknown"] += 1

    projection_case_count = len(projection_rows)
    projection_by_case = {r.get("case_id"): r for r in projection_rows if r.get("case_id")}
    pa_counts: Counter[str] = Counter()
    mt_counts: Counter[str] = Counter()
    li_counts: Counter[str] = Counter()
    cases_with_projected_li = set()
    feature_job_case_set = set(case_ids)
    for row in projection_rows:
        case_id = row.get("case_id")
        lists = extract_projection_lists(row)
        pa_counts.update(lists["practice_area"])
        mt_counts.update(lists["matter_type"])
        li_counts.update(lists["legal_issue"])
        if lists["legal_issue"] and case_id:
            cases_with_projected_li.add(case_id)

    issue_detail = []
    for issue_id, count in issue_counts.most_common():
        issue_detail.append({
            "issue_id": issue_id,
            "jobs": count,
            "unique_cases": len(cases_by_issue[issue_id]),
            "issue_status_counts": dict(issue_by_status[issue_id]),
            "top_outcomes": top(issue_by_outcome[issue_id], 10),
        })

    # Avoid the expensive per-issue feature recomputation above in user-facing
    # metrics; keep issue_detail focused on issue-level distributions.
    feature_detail = []
    for key, count in feature_counts.most_common():
        present = feature_present_counts[key]
        conf_summary = numeric_summary(feature_confidence[key])
        values = top(feature_value_counts[key], 15)
        feature_detail.append({
            "feature_key": key,
            "annotations": count,
            "present": present,
            "present_rate": pct(present, count),
            "status_counts": {
                status: cnt for status, cnt in Counter(
                    row["feature_status"]
                    for rec in records
                    for row in feature_annotations(rec)
                    if row["feature_key"] == key
                ).most_common()
            },
            "top_present_values": values,
            "units": dict(feature_units[key]),
            "confidence": conf_summary,
            "numeric_summary": numeric_summary(numeric_values[key]),
        })

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "overall": {
            "feature_jobs": total_jobs,
            "feature_job_cases": len(case_ids),
            "valid_jobs": status_counts.get("valid", 0),
            "needs_review_jobs": status_counts.get("needs_review", 0),
            "failed_jobs": status_counts.get("failed", 0),
            "cases_with_decided_issue": len(cases_with_decided),
            "cases_with_present_feature": len(cases_with_present),
            "projection_cases": projection_case_count,
            "projection_cases_with_legal_issue": len(cases_with_projected_li),
            "projection_li_cases_with_feature_jobs": len(cases_with_projected_li & feature_job_case_set),
            "feature_coverage_vs_projection_cases": pct(len(feature_job_case_set), projection_case_count),
            "feature_coverage_vs_projected_li_cases": pct(len(cases_with_projected_li & feature_job_case_set), len(cases_with_projected_li)),
        },
        "source_counts": dict(source_counts),
        "job_status_counts": dict(status_counts),
        "issue_counts": top(issue_counts, 80),
        "issue_status_counts": dict(issue_status_counts),
        "issue_outcome_counts": top(issue_outcome_counts, 50),
        "court_action_counts": top(court_action_counts, 50),
        "feature_counts": top(feature_counts, 100),
        "feature_status_counts": dict(feature_status_counts),
        "feature_present_counts": top(feature_present_counts, 100),
        "evidence_role_counts": dict(evidence_role_counts),
        "assertion_scope_counts": dict(assertion_scope_counts),
        "provenance_scope_counts": dict(provenance_scope_counts),
        "confidence_summary": numeric_summary(confidence_values),
        "projection_distribution": {
            "practice_area": top(pa_counts, 50),
            "matter_type": top(mt_counts, 80),
            "legal_issue": top(li_counts, 100),
        },
        "per_issue": issue_detail,
        "per_feature": feature_detail,
    }


def write_markdown(report: dict[str, Any], path: Path) -> None:
    o = report["overall"]
    lines = [
        "# Legal Issue Feature Result Analysis",
        "",
        f"Generated: `{report['generated_at']}`",
        "",
        "## Executive Summary",
        "",
        f"- Feature jobs: `{o['feature_jobs']}`",
        f"- Feature job cases: `{o['feature_job_cases']}`",
        f"- Valid / needs_review / failed: `{o['valid_jobs']}` / `{o['needs_review_jobs']}` / `{o['failed_jobs']}`",
        f"- Cases with decided Legal Issue: `{o['cases_with_decided_issue']}`",
        f"- Cases with at least one present feature: `{o['cases_with_present_feature']}`",
        f"- Projection cases: `{o['projection_cases']}`",
        f"- Projection cases with Legal Issue: `{o['projection_cases_with_legal_issue']}`",
        f"- Feature coverage vs all projection cases: `{o['feature_coverage_vs_projection_cases']}%`",
        f"- Feature coverage vs projected Legal-Issue cases: `{o['feature_coverage_vs_projected_li_cases']}%`",
        "",
        "## Repair Source Distribution",
        "",
    ]
    for key, value in sorted(report["source_counts"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{key}`: `{value}`")
    lines += ["", "## Issue Status Distribution", ""]
    for key, value in sorted(report["issue_status_counts"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{key}`: `{value}`")
    lines += ["", "## Feature Status Distribution", ""]
    for key, value in sorted(report["feature_status_counts"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{key}`: `{value}`")
    lines += ["", "## Top Legal Issues In Feature Jobs", ""]
    for item in report["issue_counts"][:30]:
        lines.append(f"- `{item['value']}`: `{item['count']}`")
    lines += ["", "## Top Present Features", ""]
    for item in report["feature_present_counts"][:30]:
        lines.append(f"- `{item['value']}`: `{item['count']}`")
    lines += ["", "## Top Feature Keys", ""]
    for item in report["feature_counts"][:30]:
        lines.append(f"- `{item['value']}`: `{item['count']}`")
    lines += ["", "## Evidence Distribution", ""]
    lines.append("### Role")
    for key, value in sorted(report["evidence_role_counts"].items(), key=lambda x: (-x[1], x[0])):
        lines.append(f"- `{key}`: `{value}`")
    lines.append("")
    lines.append("### Assertion Scope")
    for key, value in sorted(report["assertion_scope_counts"].items(), key=lambda x: (-x[1], x[0]))[:30]:
        lines.append(f"- `{key}`: `{value}`")
    lines += ["", "## Projection Distribution", "", "### Practice Area"]
    for item in report["projection_distribution"]["practice_area"][:25]:
        lines.append(f"- `{item['value']}`: `{item['count']}`")
    lines += ["", "### Matter Type"]
    for item in report["projection_distribution"]["matter_type"][:25]:
        lines.append(f"- `{item['value']}`: `{item['count']}`")
    lines += ["", "## Confidence", "", "```json"]
    lines.append(json.dumps(report["confidence_summary"], ensure_ascii=False, indent=2))
    lines.append("```")
    lines += ["", "## Numeric Feature Summaries", ""]
    numeric = [x for x in report["per_feature"] if x.get("numeric_summary")]
    if not numeric:
        lines.append("- No numeric feature values detected as raw numeric JSON values.")
    for item in numeric[:40]:
        lines.append(f"- `{item['feature_key']}`: `{json.dumps(item['numeric_summary'], ensure_ascii=False)}`")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results", type=Path, default=DEFAULT_RESULTS)
    parser.add_argument("--projection", type=Path, default=DEFAULT_PROJECTION)
    parser.add_argument("--output-json", type=Path, default=DEFAULT_OUT_JSON)
    parser.add_argument("--output-md", type=Path, default=DEFAULT_OUT_MD)
    args = parser.parse_args()

    results = json.loads(args.results.read_text(encoding="utf-8"))
    projection_rows = iter_projection(args.projection)
    report = analyze(results, projection_rows)
    args.output_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_markdown(report, args.output_md)
    print(json.dumps(report["overall"], ensure_ascii=False, indent=2))
    print(f"Wrote {args.output_json}")
    print(f"Wrote {args.output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
