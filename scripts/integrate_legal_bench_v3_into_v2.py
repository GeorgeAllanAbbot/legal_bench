#!/usr/bin/env python3
"""Create an integrated CourtListener v2 + Legal Bench v3 SQLite database."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sqlite3
import time
from pathlib import Path
from typing import Any


SCHEMA = """
CREATE TABLE IF NOT EXISTS annotation_release (
    release_id TEXT PRIMARY KEY,
    taxonomy_version TEXT NOT NULL,
    feature_version TEXT NOT NULL,
    created_at TEXT NOT NULL,
    taxonomy_record_count INTEGER NOT NULL,
    feature_job_count INTEGER NOT NULL,
    metadata_json TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS case_taxonomy_v3 (
    case_id TEXT PRIMARY KEY,
    annotation_status TEXT NOT NULL,
    primary_practice_area TEXT,
    secondary_practice_areas_json TEXT NOT NULL,
    matter_types_json TEXT NOT NULL,
    legal_issues_json TEXT NOT NULL,
    unmapped_matter_types_json TEXT NOT NULL,
    unmapped_legal_issues_json TEXT NOT NULL,
    needs_review INTEGER NOT NULL,
    review_applied INTEGER NOT NULL,
    review_status TEXT,
    raw_annotation_json TEXT NOT NULL,
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);

CREATE TABLE IF NOT EXISTS case_practice_area_v3 (
    case_id TEXT NOT NULL,
    practice_area TEXT NOT NULL,
    area_role TEXT NOT NULL,
    confidence REAL,
    evidence_json TEXT NOT NULL,
    PRIMARY KEY(case_id, practice_area, area_role),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);

CREATE TABLE IF NOT EXISTS case_matter_type_v3 (
    case_id TEXT NOT NULL,
    matter_type TEXT NOT NULL,
    practice_area TEXT,
    confidence REAL,
    needs_review INTEGER NOT NULL,
    evidence_json TEXT NOT NULL,
    PRIMARY KEY(case_id, matter_type),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);

CREATE TABLE IF NOT EXISTS case_legal_issue_v3 (
    case_id TEXT NOT NULL,
    issue_id TEXT NOT NULL,
    issue_status TEXT,
    mention_confidence REAL,
    adjudication_confidence REAL,
    evidence_json TEXT NOT NULL,
    PRIMARY KEY(case_id, issue_id),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);

CREATE TABLE IF NOT EXISTS matter_type_feature_job_v1_1 (
    job_id TEXT PRIMARY KEY,
    case_id TEXT NOT NULL,
    case_name TEXT,
    annotation_source TEXT,
    annotation_status TEXT NOT NULL,
    review_history_json TEXT NOT NULL,
    human_review_json TEXT,
    raw_annotation_json TEXT NOT NULL,
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);

CREATE TABLE IF NOT EXISTS matter_type_annotation_v1_1 (
    job_id TEXT NOT NULL,
    case_id TEXT NOT NULL,
    matter_type TEXT NOT NULL,
    matter_occurrence INTEGER NOT NULL,
    matter_status TEXT,
    matter_target_json TEXT NOT NULL,
    PRIMARY KEY(job_id, matter_type, matter_occurrence),
    FOREIGN KEY(job_id) REFERENCES matter_type_feature_job_v1_1(job_id),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);

CREATE TABLE IF NOT EXISTS matter_type_feature_value_v1_1 (
    job_id TEXT NOT NULL,
    case_id TEXT NOT NULL,
    matter_type TEXT NOT NULL,
    matter_occurrence INTEGER NOT NULL,
    feature_key TEXT NOT NULL,
    feature_occurrence INTEGER NOT NULL,
    value_status TEXT NOT NULL,
    value_json TEXT,
    value_text TEXT,
    value_number REAL,
    unit TEXT,
    confidence REAL,
    missing_reason TEXT,
    evidence_json TEXT NOT NULL,
    PRIMARY KEY(job_id, matter_type, matter_occurrence, feature_key, feature_occurrence),
    FOREIGN KEY(job_id) REFERENCES matter_type_feature_job_v1_1(job_id),
    FOREIGN KEY(case_id) REFERENCES case_record(case_id)
);

CREATE TABLE IF NOT EXISTS annotation_registry_snapshot (
    registry_name TEXT PRIMARY KEY,
    registry_version TEXT,
    sha256 TEXT NOT NULL,
    content_json TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_taxonomy_v3_practice ON case_taxonomy_v3(primary_practice_area, needs_review);
CREATE INDEX IF NOT EXISTS idx_practice_area_v3 ON case_practice_area_v3(practice_area, area_role, case_id);
CREATE INDEX IF NOT EXISTS idx_matter_type_v3 ON case_matter_type_v3(matter_type, needs_review, case_id);
CREATE INDEX IF NOT EXISTS idx_legal_issue_v3 ON case_legal_issue_v3(issue_id, issue_status, case_id);
CREATE INDEX IF NOT EXISTS idx_feature_job_case ON matter_type_feature_job_v1_1(case_id, annotation_status);
CREATE INDEX IF NOT EXISTS idx_feature_annotation_type ON matter_type_annotation_v1_1(matter_type, case_id);
CREATE INDEX IF NOT EXISTS idx_feature_value_key_status ON matter_type_feature_value_v1_1(feature_key, value_status, case_id);
CREATE INDEX IF NOT EXISTS idx_feature_value_numeric ON matter_type_feature_value_v1_1(feature_key, value_number, case_id)
    WHERE value_number IS NOT NULL;
CREATE INDEX IF NOT EXISTS idx_feature_value_text ON matter_type_feature_value_v1_1(feature_key, value_text, case_id)
    WHERE value_text IS NOT NULL;
"""


TABLES = (
    "annotation_release",
    "case_taxonomy_v3",
    "case_practice_area_v3",
    "case_matter_type_v3",
    "case_legal_issue_v3",
    "matter_type_feature_value_v1_1",
    "matter_type_annotation_v1_1",
    "matter_type_feature_job_v1_1",
    "annotation_registry_snapshot",
)


def compact(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def scalar_columns(value: Any) -> tuple[str | None, float | None]:
    if isinstance(value, bool):
        return ("true" if value else "false", float(value))
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return (str(value), float(value))
    if isinstance(value, str):
        try:
            return value, float(value.replace(",", ""))
        except ValueError:
            return value, None
    return None, None


def drop_existing(connection: sqlite3.Connection) -> None:
    for table in TABLES:
        connection.execute(f"DROP TABLE IF EXISTS {table}")


def insert_taxonomy(connection: sqlite3.Connection, path: Path, progress_every: int) -> int:
    count = 0
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            item = json.loads(line)
            case_id = item["case_id"]
            practice = item.get("practice_area") or {}
            primary = practice.get("primary")
            secondary = practice.get("secondary") or []
            connection.execute(
                """INSERT INTO case_taxonomy_v3 VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",
                (
                    case_id, item.get("annotation_status", "unknown"), primary, compact(secondary),
                    compact(item.get("matter_types") or []), compact(item.get("legal_issues") or []),
                    compact(item.get("unmapped_matter_types") or []), compact(item.get("unmapped_legal_issues") or []),
                    int(bool(item.get("needs_review"))), int(bool(item.get("review_applied"))),
                    item.get("review_status"), compact(item),
                ),
            )
            for role, values in (("primary", [primary] if primary else []), ("secondary", secondary)):
                for value in values:
                    area = value.get("id") if isinstance(value, dict) else value
                    if not area:
                        continue
                    confidence = value.get("confidence") if isinstance(value, dict) else practice.get("confidence")
                    evidence = value.get("evidence", []) if isinstance(value, dict) else practice.get("evidence", [])
                    connection.execute(
                        "INSERT OR REPLACE INTO case_practice_area_v3 VALUES (?,?,?,?,?)",
                        (case_id, area, role, confidence, compact(evidence)),
                    )
            for value in item.get("matter_types") or []:
                connection.execute(
                    "INSERT OR REPLACE INTO case_matter_type_v3 VALUES (?,?,?,?,?,?)",
                    (case_id, value.get("id"), value.get("practice_area"), value.get("confidence"),
                     int(bool(value.get("needs_review"))), compact(value.get("evidence") or [])),
                )
            for value in item.get("legal_issues") or []:
                connection.execute(
                    "INSERT OR REPLACE INTO case_legal_issue_v3 VALUES (?,?,?,?,?,?)",
                    (case_id, value.get("issue_id"), value.get("status"), value.get("mention_confidence"),
                     value.get("adjudication_confidence"), compact(value.get("evidence") or [])),
                )
            count += 1
            if progress_every and count % progress_every == 0:
                print(f"Integrated taxonomy: {count:,}", flush=True)
    return count


def insert_features(connection: sqlite3.Connection, path: Path, progress_every: int) -> int:
    count = 0
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            item = json.loads(line)
            job_id, case_id = item["job_id"], item["case_id"]
            connection.execute(
                "INSERT INTO matter_type_feature_job_v1_1 VALUES (?,?,?,?,?,?,?,?)",
                (job_id, case_id, item.get("case_name"), item.get("annotation_source"),
                 item.get("annotation_status", "unknown"), compact(item.get("review_history") or []),
                 compact(item.get("human_review")) if item.get("human_review") is not None else None, compact(item)),
            )
            matter_occurrences: dict[str, int] = {}
            for annotation in item.get("matter_type_feature_annotations") or []:
                matter_type = annotation.get("matter_type_id")
                matter_occurrence = matter_occurrences.get(matter_type, 0)
                matter_occurrences[matter_type] = matter_occurrence + 1
                connection.execute(
                    "INSERT INTO matter_type_annotation_v1_1 VALUES (?,?,?,?,?,?)",
                    (job_id, case_id, matter_type, matter_occurrence, annotation.get("matter_status"), compact(annotation.get("matter_target") or {})),
                )
                occurrences: dict[str, int] = {}
                for feature in annotation.get("features") or []:
                    feature_key = feature.get("feature_key")
                    feature_occurrence = occurrences.get(feature_key, 0)
                    occurrences[feature_key] = feature_occurrence + 1
                    value = feature.get("value")
                    value_text, value_number = scalar_columns(value)
                    connection.execute(
                        "INSERT INTO matter_type_feature_value_v1_1 VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                        (job_id, case_id, matter_type, matter_occurrence, feature_key, feature_occurrence, feature.get("status", "unknown"),
                         compact(value) if value is not None else None, value_text, value_number, feature.get("unit"),
                         feature.get("confidence"), feature.get("not_mentioned_or_not_applicable_reason"),
                         compact(feature.get("evidence") or [])),
                    )
            count += 1
            if progress_every and count % progress_every == 0:
                print(f"Integrated feature jobs: {count:,}", flush=True)
    return count


def insert_registry(connection: sqlite3.Connection, name: str, path: Path) -> None:
    raw = path.read_bytes()
    content = json.loads(raw)
    connection.execute(
        "INSERT INTO annotation_registry_snapshot VALUES (?,?,?,?)",
        (name, content.get("version"), hashlib.sha256(raw).hexdigest(), compact(content)),
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--taxonomy", required=True, type=Path)
    parser.add_argument("--features", required=True, type=Path)
    parser.add_argument("--practice-registry", required=True, type=Path)
    parser.add_argument("--matter-registry", required=True, type=Path)
    parser.add_argument("--issue-registry", required=True, type=Path)
    parser.add_argument("--feature-registry", required=True, type=Path)
    parser.add_argument("--replace", action="store_true")
    parser.add_argument("--progress-every", type=int, default=2500)
    args = parser.parse_args()

    if args.output.exists():
        if not args.replace:
            parser.error(f"Output exists: {args.output}; pass --replace")
        args.output.unlink()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    print(f"Copying source database ({args.source.stat().st_size / 2**30:.2f} GiB)...", flush=True)
    shutil.copy2(args.source, args.output)

    started = time.time()
    connection = sqlite3.connect(args.output)
    try:
        connection.execute("PRAGMA foreign_keys=ON")
        connection.execute("PRAGMA journal_mode=DELETE")
        connection.execute("PRAGMA synchronous=NORMAL")
        drop_existing(connection)
        connection.executescript(SCHEMA)
        with connection:
            taxonomy_count = insert_taxonomy(connection, args.taxonomy, args.progress_every)
            feature_count = insert_features(connection, args.features, args.progress_every)
            for name, path in (
                ("practice_area_registry_v3", args.practice_registry),
                ("matter_type_registry_v3", args.matter_registry),
                ("legal_issue_registry_v3_1_simplified", args.issue_registry),
                ("matter_type_feature_registry_v1_1", args.feature_registry),
            ):
                insert_registry(connection, name, path)
            connection.execute(
                "INSERT INTO annotation_release VALUES (?,?,?,?,?,?,?)",
                ("legal_bench_v3_integrated", "3.2.0", "1.1", time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                 taxonomy_count, feature_count, compact({"source_database": args.source.name})),
            )
        connection.execute("ANALYZE")
        connection.commit()
        foreign_key_errors = connection.execute("PRAGMA foreign_key_check").fetchall()
        integrity = connection.execute("PRAGMA quick_check").fetchone()[0]
        if foreign_key_errors or integrity != "ok":
            raise RuntimeError(f"Database validation failed: integrity={integrity}, foreign_keys={foreign_key_errors[:5]}")
        counts = {
            "case_record": connection.execute("SELECT COUNT(*) FROM case_record").fetchone()[0],
            "case_taxonomy_v3": connection.execute("SELECT COUNT(*) FROM case_taxonomy_v3").fetchone()[0],
            "case_matter_type_v3": connection.execute("SELECT COUNT(*) FROM case_matter_type_v3").fetchone()[0],
            "case_legal_issue_v3": connection.execute("SELECT COUNT(*) FROM case_legal_issue_v3").fetchone()[0],
            "matter_type_feature_job_v1_1": connection.execute("SELECT COUNT(*) FROM matter_type_feature_job_v1_1").fetchone()[0],
            "matter_type_feature_value_v1_1": connection.execute("SELECT COUNT(*) FROM matter_type_feature_value_v1_1").fetchone()[0],
        }
    finally:
        connection.close()
    print(json.dumps({"output": str(args.output), "elapsed_seconds": round(time.time() - started, 2), "counts": counts}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
