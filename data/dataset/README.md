# Integrated Legal RAG Database v3.1

This directory contains the complete CourtListener 20k corpus and v3.3 Matter Type / v1.1 Feature
annotations in one SQLite database. It includes 21,261 opinion texts; no separate opinion download
is required.

## Restore

From the repository root:

```bash
./scripts/restore_integrated_db.sh
```

The script concatenates four archive parts, verifies compressed and uncompressed SHA-256 hashes,
decompresses `data/dataset/legal_rag_dataset_v3.db`, and runs SQLite `PRAGMA quick_check`.

## Documentation

- `SCHEMA.sql`: executable database schema.
- `FIELD_CATALOG.json`: generated SQL types, constraints, keys, indexes, and row counts.
- `FIELD_DICTIONARY_en.md` / `FIELD_DICTIONARY_zh.md`: business meaning of every table and field.
- `COVERAGE_REPORT.json`: coverage and distributions calculated from this exact database.
- `manifest.json`: database hashes, archive-part hashes, versions, and counts.

Open the restored database read-only. Do not modify the released copy in place.
