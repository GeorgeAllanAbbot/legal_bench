# Integrated Legal RAG Database

This directory publishes the complete CourtListener 20k v2 corpus merged with
Legal Bench v3 taxonomy annotations and Matter Type Feature v1.1 annotations.
The SQLite database is losslessly compressed with Zstandard and split into
four parts to remain below GitHub's per-file size limit.

## Restore

From the repository root:

```bash
./scripts/restore_integrated_db.sh
```

The restored database is written to:

```text
data/integrated/legal_rag_dataset_v3.db
```

The script verifies the compressed and uncompressed SHA-256 hashes and runs
SQLite `PRAGMA quick_check`.

## Contents

- Original v2 tables: courts, cases, opinions, legacy case features, and search chunks.
- `case_taxonomy_v3`: one final taxonomy projection per case.
- `case_practice_area_v3`: normalized Practice Area labels.
- `case_matter_type_v3`: normalized Matter Type labels.
- `case_legal_issue_v3`: normalized simplified Legal Issues.
- `matter_type_feature_job_v1_1`: feature annotation job lineage.
- `matter_type_annotation_v1_1`: Matter Type annotation targets.
- `matter_type_feature_value_v1_1`: queryable feature values, units, confidence, and evidence.
- `annotation_registry_snapshot`: frozen registries used for the release.
- `annotation_release`: release version and counts.

Repeated model outputs are preserved with `matter_occurrence` and
`feature_occurrence`; they are not silently overwritten.

## Example

```sql
SELECT COUNT(DISTINCT f.case_id)
FROM matter_type_feature_value_v1_1 AS f
WHERE f.matter_type = 'foreclosure_mortgage'
  AND f.feature_key = 'attorney_fees_usd'
  AND f.value_status = 'present'
  AND f.value_number > 50000;
```

This query returns one case in the published build.
