#!/usr/bin/env python3
"""Generate release field catalogs and coverage reports from frozen artifacts."""

from __future__ import annotations

import json
import sqlite3
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "data/dataset/legal_rag_dataset_v3.db"
QUERY_DIR = ROOT / "query/descriptive_query"


def scalar(db: sqlite3.Connection, sql: str, params: tuple = ()):
    return db.execute(sql, params).fetchone()[0]


def distribution(db: sqlite3.Connection, sql: str) -> dict[str, int]:
    return {str(key): count for key, count in db.execute(sql)}


def percent(value: int, total: int) -> float:
    return round(100 * value / total, 2) if total else 0.0


def build_database_reports() -> None:
    db = sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)
    tables = [row[0] for row in db.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    )]
    field_catalog = {"database": DB_PATH.name, "tables": {}}
    for table in tables:
        columns = [
            {"position": cid, "name": name, "declared_type": dtype, "not_null": bool(notnull),
             "default": default, "primary_key_position": pk}
            for cid, name, dtype, notnull, default, pk in db.execute(f"PRAGMA table_info('{table}')")
        ]
        foreign_keys = [
            {"id": fid, "sequence": seq, "referenced_table": target, "from": source,
             "to": target_col, "on_update": on_update, "on_delete": on_delete}
            for fid, seq, target, source, target_col, on_update, on_delete, _ in
            db.execute(f"PRAGMA foreign_key_list('{table}')")
        ]
        indexes = [row[1] for row in db.execute(f"PRAGMA index_list('{table}')")]
        field_catalog["tables"][table] = {
            "row_count": scalar(db, f'SELECT COUNT(*) FROM "{table}"'),
            "columns": columns,
            "foreign_keys": foreign_keys,
            "indexes": indexes,
        }

    cases = scalar(db, "SELECT COUNT(*) FROM case_record")
    opinions = scalar(db, "SELECT COUNT(*) FROM opinion_record")
    coverage_counts = {
        "case_name": scalar(db, "SELECT COUNT(*) FROM case_record WHERE TRIM(COALESCE(case_name,''))<>''"),
        "court_id": scalar(db, "SELECT COUNT(*) FROM case_record WHERE TRIM(COALESCE(court_id,''))<>''"),
        "decision_date": scalar(db, "SELECT COUNT(*) FROM case_record WHERE decision_date IS NOT NULL"),
        "decision_year": scalar(db, "SELECT COUNT(*) FROM case_record WHERE decision_year IS NOT NULL"),
        "citation": scalar(db, "SELECT COUNT(*) FROM case_record WHERE citations_json NOT IN ('[]','null','')"),
        "docket_id": scalar(db, "SELECT COUNT(*) FROM case_record WHERE TRIM(COALESCE(docket_id,''))<>''"),
        "usable_opinion_text": scalar(db, "SELECT COUNT(*) FROM opinion_record WHERE has_usable_text=1"),
        "nonempty_opinion_text": scalar(db, "SELECT COUNT(*) FROM opinion_record WHERE LENGTH(COALESCE(preferred_text,''))>0"),
        "practice_area_cases": scalar(db, "SELECT COUNT(DISTINCT case_id) FROM case_practice_area_v3"),
        "matter_type_cases": scalar(db, "SELECT COUNT(DISTINCT case_id) FROM case_matter_type_v3"),
        "legal_issue_cases": scalar(db, "SELECT COUNT(DISTINCT case_id) FROM case_legal_issue_v3"),
        "matter_type_feature_cases": scalar(db, "SELECT COUNT(DISTINCT case_id) FROM matter_type_feature_job_v1_1 WHERE annotation_status='accepted'"),
    }
    coverage = {
        "release": "legal_bench_v3.1",
        "integrity": {
            "quick_check": scalar(db, "PRAGMA quick_check"),
            "foreign_key_errors": len(list(db.execute("PRAGMA foreign_key_check"))),
        },
        "counts": {
            "cases": cases,
            "courts": scalar(db, "SELECT COUNT(*) FROM dim_court"),
            "opinions": opinions,
            "search_documents": scalar(db, "SELECT COUNT(*) FROM search_document"),
            "taxonomy_records": scalar(db, "SELECT COUNT(*) FROM case_taxonomy_v3"),
            "practice_area_rows": scalar(db, "SELECT COUNT(*) FROM case_practice_area_v3"),
            "matter_type_rows": scalar(db, "SELECT COUNT(*) FROM case_matter_type_v3"),
            "legal_issue_rows": scalar(db, "SELECT COUNT(*) FROM case_legal_issue_v3"),
            "feature_jobs": scalar(db, "SELECT COUNT(*) FROM matter_type_feature_job_v1_1"),
            "feature_values": scalar(db, "SELECT COUNT(*) FROM matter_type_feature_value_v1_1"),
        },
        "coverage": {
            key: {
                "count": value,
                "denominator": opinions if "opinion_text" in key else cases,
                "percent": percent(value, opinions if "opinion_text" in key else cases),
            }
            for key, value in coverage_counts.items()
        },
        "distributions": {
            "jurisdiction_type": distribution(db, "SELECT jurisdiction_type,COUNT(*) FROM case_record GROUP BY 1 ORDER BY 2 DESC"),
            "court_level": distribution(db, "SELECT court_level,COUNT(*) FROM case_record GROUP BY 1 ORDER BY 2 DESC"),
            "decision_decade": distribution(db, "SELECT CAST(decision_year/10 AS INT)*10,COUNT(*) FROM case_record GROUP BY 1 ORDER BY 1"),
            "precedential_status": distribution(db, "SELECT precedential_status,COUNT(*) FROM case_record GROUP BY 1 ORDER BY 2 DESC"),
            "opinion_type": distribution(db, "SELECT opinion_type,COUNT(*) FROM opinion_record GROUP BY 1 ORDER BY 2 DESC"),
            "primary_practice_area": distribution(db, "SELECT COALESCE(primary_practice_area,'null'),COUNT(*) FROM case_taxonomy_v3 GROUP BY 1 ORDER BY 2 DESC"),
            "matter_type": distribution(db, "SELECT matter_type,COUNT(DISTINCT case_id) FROM case_matter_type_v3 GROUP BY 1 ORDER BY 2 DESC"),
            "legal_issue": distribution(db, "SELECT issue_id,COUNT(DISTINCT case_id) FROM case_legal_issue_v3 GROUP BY 1 ORDER BY 2 DESC"),
            "feature_value_status": distribution(db, "SELECT value_status,COUNT(*) FROM matter_type_feature_value_v1_1 GROUP BY 1 ORDER BY 2 DESC"),
            "feature_job_status": distribution(db, "SELECT annotation_status,COUNT(*) FROM matter_type_feature_job_v1_1 GROUP BY 1 ORDER BY 2 DESC"),
        },
        "semantics": {
            "matter_type_coverage": "At least one projected Matter Type per case; not human-gold accuracy.",
            "legal_issue_coverage": "Only cases with a retained, adjudicated canonical Legal Issue; absence means unlabelled/not retained, not no legal issue.",
            "feature_coverage": "Feature cases are valid case-by-Matter-Type extraction jobs; not every Matter Type requires a feature job.",
            "missing_values": "not_mentioned is unknown from the opinion and must not be interpreted as zero or false.",
        },
    }
    db.close()
    (ROOT / "data/dataset/FIELD_CATALOG.json").write_text(json.dumps(field_catalog, indent=2) + "\n")
    (ROOT / "data/dataset/COVERAGE_REPORT.json").write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n")


def build_query_report() -> None:
    queries = json.loads((QUERY_DIR / "benchmark_full.json").read_text())
    report = {
        "release": "descriptive_v6",
        "queries": len(queries),
        "query_family": dict(Counter(row["query_family"] for row in queries)),
        "query_type": dict(Counter(row["type"] for row in queries)),
        "difficulty": dict(Counter(row["difficulty"] for row in queries)),
        "split": dict(Counter(row["split"] for row in queries)),
        "evidence_size_bucket": dict(Counter(row["evidence_size_bucket"] for row in queries)),
        "constraint_dimension_count": dict(Counter(str(len(row.get("constraint_dimensions", []))) for row in queries)),
        "matter_types_referenced": sorted({
            row.get("structured_filters", {}).get("matter_type") for row in queries
            if row.get("structured_filters", {}).get("matter_type")
        }),
        "qrels": {
            state: sum(len(row["qrel_states"][state]) for row in queries)
            for state in ("positive", "negative", "unjudged")
        },
        "evidence_count": {
            "minimum": min(len(row["evidence"]) for row in queries),
            "maximum": max(len(row["evidence"]) for row in queries),
            "total_occurrences": sum(len(row["evidence"]) for row in queries),
        },
        "validation": {
            "exact_duplicate_query_texts": len(queries) - len({row["query"].strip().lower() for row in queries}),
            "queries_without_positive_evidence": sum(not row["evidence"] for row in queries),
            "queries_with_validation_errors": sum(bool(row.get("validation_errors")) for row in queries),
        },
        "qrel_policy": {
            "sql": "exhaustive structured projection over the frozen database",
            "hybrid": "partially adjudicated semantic pool (Silver)",
            "unjudged": "must not be treated as a negative",
        },
    }
    (QUERY_DIR / "COVERAGE_REPORT.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    build_database_reports()
    build_query_report()
