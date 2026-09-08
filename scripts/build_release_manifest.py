#!/usr/bin/env python3
"""Build the root release manifest after all release files are finalized."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
def digest(path: Path) -> str:
    value = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            value.update(block)
    return value.hexdigest()


def included(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if relative.as_posix() == "manifest.json":
        return False
    excluded_names = {"legal_rag_dataset_v3.db", "legal_rag_dataset_v3.db.zst"}
    return ".git" not in relative.parts and "__pycache__" not in relative.parts and path.name not in excluded_names


artifacts = []
for path in sorted(item for item in ROOT.rglob("*") if item.is_file() and included(item)):
    artifacts.append({
        "path": path.relative_to(ROOT).as_posix(),
        "bytes": path.stat().st_size,
        "sha256": digest(path),
    })

manifest = {
    "release_id": "legal_bench_v3.1_descriptive_v6",
    "release_date": "2026-09-09",
    "source": {
        "provider": "CourtListener / Free Law Project",
        "bulk_snapshot": "2026-06-30",
        "inputs": ["opinion-clusters", "opinions", "courts", "dockets"]
    },
    "versions": {
        "taxonomy_projection": "3.3.0",
        "practice_area_registry": "3.2.0",
        "matter_type_registry": "3.2.0",
        "legal_issue_registry": "3.1-simplified",
        "matter_type_features": "1.1",
        "descriptive_benchmark": "6"
    },
    "scope": {
        "cases": 20000,
        "opinions": 21261,
        "search_documents": 94314,
        "matter_type_case_coverage": 20000,
        "descriptive_queries": 120
    },
    "release_roots": ["data", "query"],
    "artifacts": artifacts
}
(ROOT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
print(f"Wrote manifest for {len(artifacts)} artifacts")
