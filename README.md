# Legal Bench: CourtListener Phase1 Dataset

This repository publishes the stable Phase1 SQLite interface for the
CourtListener-based legal retrieval dataset.

## Contents

- `data/courtlistener_legal_20k/phase1/legal_cases.db.xz.part-*`: Git LFS
  parts of the authoritative Phase1 SQLite database.
- `data/courtlistener_legal_20k/phase1/SCHEMA.sql`: schema snapshot.
- `data/courtlistener_legal_20k/phase1/DATASET_GUIDE_zh.md`: Chinese dataset
  guide, data boundaries, SQL examples, and RAG/benchmark workflows.
- Quality and validation reports for the published build.
- `scripts/build_phase1_dataset.py`: Phase1 build script.

## Getting Started

Install Git LFS before cloning:

```bash
git lfs install
git clone git@github.com:GeorgeAllanAbbot/legal_bench.git
cd legal_bench
./scripts/restore_phase1_db.sh
sqlite3 data/courtlistener_legal_20k/phase1/legal_cases.db \
  "SELECT COUNT(*) FROM cases;"
```

The database is compressed and split into four Git LFS parts so each object is
portable through the publishing environment. The restore script verifies the
reconstructed SQLite SHA-256 before writing it to the Phase1 directory.

The current release contains 20,000 Opinion Cluster cases and 21,755 opinion
documents. It is an opinion-led retrieval corpus, not a complete litigation
docket archive. See the dataset guide for field definitions, limitations, and
provenance requirements.

## Source and Provenance

The data is derived from CourtListener bulk legal data. Each published case
retains source/provenance fields and a CourtListener URL for review. Downstream
research should retain `case_id`, `document_id` where applicable, and source
links in reported results.
