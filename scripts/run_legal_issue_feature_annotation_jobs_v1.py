#!/usr/bin/env python3
"""Run a small batch of Legal Issue feature annotation prompt jobs."""

from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from run_taxonomy_pilot_v3 import model_config, parse_json


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/configs/"
    "analytical_feature_llm_v1_3.yaml"
)
DEFAULT_JOBS = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_jobs/"
    "legal_issue_feature_jobs_v1.sample5.jsonl"
)
DEFAULT_OUTPUT = (
    ROOT / "data/courtlistener_legal_20k/analytics_v1/feature_pilots/"
    "legal_issue_feature_annotation_v1_sample.json"
)

PLACEHOLDER_VALUES = {
    "none", "unknown", "unclear", "not_mentioned", "not_applicable",
}
ALLOWED_FEATURE_STATUSES = {
    "present", "absent", "uncertain", "not_applicable", "not_mentioned",
}
ALLOWED_ISSUE_STATUSES = {
    "decided", "raised_not_decided", "not_reached", "background_only",
    "quoted_authority", "false_match",
}
CURRENT_COURT_DECISION_ROLES = {"court_analysis", "court_holding"}
EMPTY_VALUES = (None, "", [], {})
MUTUALLY_EXCLUSIVE_PAIRS = [
    {"applies", "does_not_apply"},
    {"owed", "not_owed"},
    {"exists", "absent"},
    {"timely", "untimely"},
    {"triggered", "not_triggered"},
    {"covered", "not_covered"},
    {"violation", "no_violation"},
    {"established", "not_established"},
    {"shown", "not_shown"},
    {"proper", "improper"},
    {"valid", "invalid"},
    {"admitted", "excluded"},
    {"granted", "denied"},
    {"enforced", "not_enforced"},
    {"sufficient", "insufficient"},
    {"exhausted", "not_exhausted"},
]


def iter_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def response_schema() -> dict[str, Any]:
    evidence_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "paragraph_id", "role", "assertion_scope",
            "provenance_scope", "text",
        ],
        "properties": {
            "paragraph_id": {"type": "string"},
            "role": {"type": "string"},
            "assertion_scope": {"type": "string"},
            "provenance_scope": {"type": "string"},
            "text": {"type": "string"},
        },
    }
    feature_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "feature_key", "status", "value", "unit", "confidence",
            "not_mentioned_or_not_decided_reason", "evidence",
        ],
        "properties": {
            "feature_key": {"type": "string"},
            "status": {
                "type": "string",
                "enum": [
                    "present", "absent", "uncertain",
                    "not_applicable", "not_mentioned",
                ],
            },
            "value": {
                "anyOf": [
                    {"type": "null"},
                    {"type": "string"},
                    {"type": "number"},
                    {"type": "boolean"},
                    {"type": "array"},
                    {"type": "object"},
                ]
            },
            "unit": {"anyOf": [{"type": "null"}, {"type": "string"}]},
            "confidence": {"type": "number"},
            "not_mentioned_or_not_decided_reason": {"type": "string"},
            "evidence": {"type": "array", "items": evidence_schema},
        },
    }
    annotation_schema = {
        "type": "object",
        "additionalProperties": False,
        "required": [
            "issue_id", "issue_status", "issue_specific_outcome",
            "issue_target", "court_action", "features",
        ],
        "properties": {
            "issue_id": {"type": "string"},
            "issue_status": {
                "type": "string",
                "enum": [
                    "decided", "raised_not_decided", "not_reached",
                    "background_only", "quoted_authority", "false_match",
                ],
            },
            "issue_specific_outcome": {
                "anyOf": [{"type": "null"}, {"type": "string"}]
            },
            "issue_target": {"type": "object"},
            "court_action": {"type": "string"},
            "features": {"type": "array", "items": feature_schema},
        },
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["case_id", "legal_issue_feature_annotations"],
        "properties": {
            "case_id": {"type": "string"},
            "legal_issue_feature_annotations": {
                "type": "array",
                "items": annotation_schema,
            },
        },
    }


def call_job(client: Any, model: str, config: dict[str, Any], job: dict[str, Any]) -> dict[str, Any]:
    started = time.perf_counter()
    kwargs = {
        "model": model,
        "messages": job["messages"],
        "temperature": 0,
        "max_tokens": int(config["capabilities"].get("max_output_tokens", 7000)),
    }
    if config.get("capabilities", {}).get("structured_output") == "json_schema":
        kwargs["response_format"] = {
            "type": "json_schema",
            "json_schema": {
                "name": "legal_issue_feature_annotation_v1",
                "schema": response_schema(),
                "strict": False,
            },
        }
    else:
        kwargs["response_format"] = {"type": "json_object"}

    response = client.chat.completions.create(**kwargs)
    content = response.choices[0].message.content or ""
    usage = response.usage.model_dump() if getattr(response, "usage", None) else {}
    annotation = parse_json(content)
    validation_warnings = validation_warnings_for_annotation(
        annotation, job.get("expected_feature_keys_by_issue", {})
    )
    return {
        "job_id": job["job_id"],
        "case_id": job["case_id"],
        "case_name": job.get("case_name"),
        "issue_ids": job.get("issue_ids", []),
        "status": "valid" if not validation_warnings else "needs_review",
        "latency_seconds": round(time.perf_counter() - started, 3),
        "usage": usage,
        "validation_warnings": validation_warnings,
        "annotation": annotation,
    }


def atom_values(value: Any) -> set[str]:
    atoms: set[str] = set()
    if isinstance(value, str):
        atoms.add(value.strip().lower())
    elif isinstance(value, (int, float, bool)) or value is None:
        if value is None:
            atoms.add("null")
    elif isinstance(value, list):
        for item in value:
            atoms.update(atom_values(item))
    elif isinstance(value, dict):
        for item in value.values():
            atoms.update(atom_values(item))
    return {atom for atom in atoms if atom}


def validation_warnings_for_annotation(
    annotation: dict[str, Any],
    expected_feature_keys_by_issue: dict[str, list[str]] | None = None,
) -> list[dict[str, Any]]:
    warnings: list[dict[str, Any]] = []
    expected_feature_keys_by_issue = expected_feature_keys_by_issue or {}
    for issue in annotation.get("legal_issue_feature_annotations", []):
        issue_id = issue.get("issue_id")
        issue_status = issue.get("issue_status")
        if issue_status not in ALLOWED_ISSUE_STATUSES:
            warnings.append({
                "code": "invalid_issue_status",
                "issue_id": issue_id,
                "status": issue_status,
            })
        if issue_status != "decided" and issue.get("issue_specific_outcome") not in EMPTY_VALUES:
            warnings.append({
                "code": "issue_outcome_on_non_decided_issue",
                "issue_id": issue_id,
                "issue_status": issue_status,
                "issue_specific_outcome": issue.get("issue_specific_outcome"),
            })
        issue_atoms = atom_values(issue.get("issue_specific_outcome"))
        features = issue.get("features", [])
        expected_keys = set(expected_feature_keys_by_issue.get(issue_id, []))
        actual_keys = {
            item.get("feature_key") for item in features if isinstance(item, dict)
        }
        if expected_keys:
            missing = sorted(expected_keys - actual_keys)
            extra = sorted(actual_keys - expected_keys)
            if missing:
                warnings.append({
                    "code": "missing_expected_feature_keys",
                    "issue_id": issue_id,
                    "missing": missing,
                })
            if extra:
                warnings.append({
                    "code": "unsupported_feature_keys",
                    "issue_id": issue_id,
                    "extra": extra,
                })
        for feature in features:
            key = feature.get("feature_key")
            status = feature.get("status")
            result_like_feature = bool(
                isinstance(key, str)
                and (key.endswith("_result") or key.endswith("_outcome"))
            )
            if status not in ALLOWED_FEATURE_STATUSES:
                warnings.append({
                    "code": "invalid_feature_status",
                    "issue_id": issue_id,
                    "feature_key": key,
                    "status": status,
                })
            evidence = feature.get("evidence")
            if status == "present" and not evidence:
                warnings.append({
                    "code": "present_without_evidence",
                    "issue_id": issue_id,
                    "feature_key": key,
                })
            if status == "not_mentioned" and evidence:
                warnings.append({
                    "code": "not_mentioned_with_evidence",
                    "issue_id": issue_id,
                    "feature_key": key,
                })
            value = feature.get("value")
            if status == "not_mentioned" and value not in EMPTY_VALUES:
                warnings.append({
                    "code": "not_mentioned_with_value",
                    "issue_id": issue_id,
                    "feature_key": key,
                    "value": value,
                })
            if issue_status != "decided" and result_like_feature and status == "present":
                warnings.append({
                    "code": "result_feature_present_on_non_decided_issue",
                    "issue_id": issue_id,
                    "feature_key": key,
                    "issue_status": issue_status,
                    "value": value,
                })
            if result_like_feature and status == "present":
                evidence_roles = {
                    item.get("role") for item in evidence or [] if isinstance(item, dict)
                }
                if not (evidence_roles & CURRENT_COURT_DECISION_ROLES):
                    warnings.append({
                        "code": "result_without_current_court_evidence",
                        "issue_id": issue_id,
                        "feature_key": key,
                        "evidence_roles": sorted(role for role in evidence_roles if role),
                    })
            if not isinstance(value, list):
                values = atom_values(value)
            else:
                values = atom_values(value)
                placeholders = values & PLACEHOLDER_VALUES
                substantive = values - PLACEHOLDER_VALUES - {"null"}
                if placeholders and substantive:
                    warnings.append({
                        "code": "placeholder_mixed_with_substantive",
                        "issue_id": issue_id,
                        "feature_key": key,
                        "values": sorted(values),
                    })
            for pair in MUTUALLY_EXCLUSIVE_PAIRS:
                if pair <= values:
                    warnings.append({
                        "code": "mutually_exclusive_values",
                        "issue_id": issue_id,
                        "feature_key": key,
                        "values": sorted(values),
                        "conflict_pair": sorted(pair),
                    })
                # Component-level standing elements are not logically required
                # to match the overall standing outcome one-to-one. For example,
                # injury may be established while redressability fails, so
                # standing is not established; some state declaratory-standing
                # doctrines can also diverge from federal element framing.
                if (
                    issue_id == "standing"
                    and key in {"injury_in_fact", "causation", "redressability"}
                ):
                    continue
                if pair <= (issue_atoms | values):
                    warnings.append({
                        "code": "issue_outcome_feature_value_conflict",
                        "issue_id": issue_id,
                        "feature_key": key,
                        "issue_specific_outcome": issue.get("issue_specific_outcome"),
                        "feature_value": value,
                        "conflict_pair": sorted(pair),
                    })
    return warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--jobs", type=Path, default=DEFAULT_JOBS)
    parser.add_argument("--config", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--env-file", type=Path, default=ROOT / ".env")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--limit", type=int, default=2)
    parser.add_argument(
        "--job-indexes",
        type=str,
        default="1,5",
        help="1-based comma-separated job indexes to run before limit is applied.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run jobs sequentially from the start; --limit=0 means all jobs.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    config = yaml.safe_load(args.config.read_text(encoding="utf-8"))
    client, model = model_config(config, args.env_file)
    jobs = iter_jsonl(args.jobs)
    if args.all:
        selected = jobs if args.limit == 0 else jobs[:args.limit]
    else:
        indexes = [
            int(value.strip()) for value in args.job_indexes.split(",")
            if value.strip()
        ]
        selected = [jobs[index - 1] for index in indexes if 0 < index <= len(jobs)]
        selected = selected[:args.limit]

    results = []
    for job in selected:
        try:
            print(f"Running {job['job_id']} issues={job.get('issue_ids')}", flush=True)
            results.append(call_job(client, model, config, job))
        except Exception as exc:  # noqa: BLE001 - keep pilot artifact useful.
            results.append({
                "job_id": job.get("job_id"),
                "case_id": job.get("case_id"),
                "case_name": job.get("case_name"),
                "issue_ids": job.get("issue_ids", []),
                "status": "failed",
                "error": repr(exc),
            })

    payload = {
        "run_type": "legal_issue_feature_annotation_v1_sample",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "model": model,
        "jobs_path": str(args.jobs.resolve()),
        "result_count": len(results),
        "validation_warning_count": sum(
            len(item.get("validation_warnings", [])) for item in results
        ),
        "results": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({
        "output": str(args.output.resolve()),
        "result_count": len(results),
        "statuses": [item["status"] for item in results],
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
