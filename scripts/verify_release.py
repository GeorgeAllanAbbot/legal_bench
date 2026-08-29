#!/usr/bin/env python3
import hashlib, json, lzma
from pathlib import Path

root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "manifest.json").read_text())
failed = False
decoded = {}
for item in manifest["artifacts"]:
    path = root / item["path"]
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    rows = []
    with lzma.open(path, "rt", encoding="utf-8") as handle:
        for line in handle:
            rows.append(json.loads(line))
    decoded[item["path"]] = rows
    ok = digest == item["sha256"] and len(rows) == item["record_count"]
    print(f"{'PASS' if ok else 'FAIL'} {item['path']}: {len(rows)} records")
    failed |= not ok

taxonomy = decoded["data/taxonomy/case_taxonomy_v3.jsonl.xz"]
features = decoded["data/features/matter_type_features_v1_1.jsonl.xz"]
case_ids = [row["case_id"] for row in taxonomy]
job_ids = [row["job_id"] for row in features]
unique_ok = len(case_ids) == len(set(case_ids)) and len(job_ids) == len(set(job_ids))
print(f"{'PASS' if unique_ok else 'FAIL'} unique case_id and job_id constraints")
failed |= not unique_ok
raise SystemExit(1 if failed else 0)
