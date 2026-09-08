#!/usr/bin/env python3
"""Verify hashes and semantic integrity of the Legal Bench v3.1 release."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def check(condition: bool, message: str) -> None:
    print(f"{'PASS' if condition else 'FAIL'} {message}")
    if not condition:
        raise AssertionError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--full-database", action="store_true",
                        help="Restore/decompress SQLite before running database checks")
    args = parser.parse_args()
    manifest = json.loads((ROOT / "manifest.json").read_text())
    for item in manifest["artifacts"]:
        path = ROOT / item["path"]
        check(path.is_file(), f"exists: {item['path']}")
        check(path.stat().st_size == item["bytes"], f"size: {item['path']}")
        check(sha256(path) == item["sha256"], f"sha256: {item['path']}")

    query_dir = ROOT / "query/descriptive_query"
    public = json.loads((query_dir / "queries_public.json").read_text())
    private = json.loads((query_dir / "qrels_private.json").read_text())
    splits = json.loads((query_dir / "splits.json").read_text())
    public_ids = {row["id"] for row in public}
    private_ids = {row["id"] for row in private}
    split_ids = [query_id for values in splits.values() for query_id in values]
    check(len(public) == 120 and len(private) == 120, "120 public/private queries")
    check(public_ids == private_ids == set(split_ids), "query IDs align across public/private/splits")
    check(len(split_ids) == len(set(split_ids)), "query splits do not overlap")
    check({name: len(values) for name, values in splits.items()} ==
          {"dev": 60, "validation": 30, "test": 30}, "frozen 60/30/30 split")
    qrel_states_valid = True
    for row in private:
        states = row["qrel_states"]
        positive = set(states["positive"])
        negative = set(states["negative"])
        unjudged = set(states["unjudged"])
        qrel_states_valid &= not (positive & negative or positive & unjudged or negative & unjudged)
    check(qrel_states_valid, "disjoint qrel states for all 120 queries")

    if args.full_database:
        subprocess.run([str(ROOT / "scripts/restore_integrated_db.sh")], check=True)
        db_path = ROOT / "data/dataset/legal_rag_dataset_v3.db"
        db = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        check(db.execute("PRAGMA quick_check").fetchone()[0] == "ok", "SQLite quick_check")
        check(db.execute("SELECT COUNT(*) FROM case_record").fetchone()[0] == 20000, "20,000 cases")
        check(db.execute("SELECT COUNT(*) FROM opinion_record").fetchone()[0] == 21261, "21,261 opinions")
        check(db.execute("SELECT COUNT(DISTINCT case_id) FROM case_matter_type_v3").fetchone()[0] == 20000,
              "20,000 cases with Matter Type")
        check(not db.execute("SELECT 1 FROM sqlite_master WHERE name='case_matter_type_v3_2_backup'").fetchone(),
              "migration backup table removed")
        db.close()
    print("Release verification complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
