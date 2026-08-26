# Legal Bench: CourtListener Legal Dataset

This repository publishes the CourtListener-based legal retrieval dataset and
the newer Legal Bench v3.0 analytical taxonomy/feature annotations.

## Contents

### Phase1 SQLite Dataset

- `data/courtlistener_legal_20k/phase1/legal_cases.db.xz.part-*`: Git LFS
  parts of the authoritative Phase1 SQLite database.
- `data/courtlistener_legal_20k/phase1/SCHEMA.sql`: schema snapshot.
- `data/courtlistener_legal_20k/phase1/DATASET_GUIDE_zh.md`: Chinese dataset
  guide, data boundaries, SQL examples, and RAG/benchmark workflows.
- Quality and validation reports for the published build.
- `scripts/build_phase1_dataset.py`: Phase1 build script.

### Legal Bench v3.0 Analytical Features

- `data/courtlistener_legal_20k/analytics_v1/v3_0_release/`: cleaned v3.0
  release package.
- `v3_0_release/docs/LEGAL_ISSUE_CATALOG_en.md` and
  `v3_0_release/docs/LEGAL_ISSUE_CATALOG_zh.md`: bilingual Legal Issue
  definitions, boundaries, and feature-pack membership.
- `v3_0_release/docs/FEATURE_CATALOG_en.md` and
  `v3_0_release/docs/FEATURE_CATALOG_zh.md`: bilingual analytical feature
  definitions and inclusion mapping.
- `v3_0_release/data/legal_issue_feature_full_v1_16k_final_merged.json.xz`:
  compressed final merged feature annotations.
- `v3_0_release/reports/LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md`:
  result and distribution analysis.

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

Restore the v3.0 final analytical feature JSON:

```bash
./scripts/restore_v3_0_feature_annotations.sh
```

The database is compressed and split into four Git LFS parts so each object is
portable through the publishing environment. The restore script verifies the
reconstructed SQLite SHA-256 before writing it to the Phase1 directory.

The current release contains 20,000 Opinion Cluster cases and 21,755 opinion
documents. It is an opinion-led retrieval corpus, not a complete litigation
docket archive. See the dataset guide for field definitions, limitations, and
provenance requirements.

The v3.0 analytical feature layer contains 9,023 final merged Legal Issue
feature jobs. The final validation state is 9,023 valid, 0 needs review, and 0
failed. It covers 59.13% of cases with projected Legal Issues and is designed
for analytical retrieval, constrained RAG, and benchmark query construction.

## Source and Provenance

The data is derived from CourtListener bulk legal data. Each published case
retains source/provenance fields and a CourtListener URL for review. Downstream
research should retain `case_id`, `document_id` where applicable, and source
links in reported results.
