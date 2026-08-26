# Legal Bench v3.0 Release

This directory is the cleaned v3.0 release package for the CourtListener-based Legal Bench dataset work.

## Contents

- `data/legal_issue_feature_full_v1_16k_final_merged.json.xz`: compressed final merged Legal Issue feature annotations. Restore with `scripts/restore_v3_0_feature_annotations.sh`.
- `data/legal_issue_feature_full_v1_16k_final_merged.summary.json`: final annotation summary.
- `reports/LEGAL_ISSUE_FEATURE_DISTRIBUTION_ANALYSIS.md`: distribution analysis.
- `reports/legal_issue_feature_full_v1_16k_distribution_analysis.json`: machine-readable distribution analysis.
- `registry/`: registry snapshots used by this release.
- `docs/LEGAL_ISSUE_CATALOG_en.md`: Legal Issue definitions and feature-pack membership.
- `docs/FEATURE_CATALOG_en.md`: analytical feature definitions and inclusion mapping.

## Current Status

- Total feature jobs: `9023`
- Valid jobs: `9023`
- Needs review: `0`
- Failed: `0`
- Manual review items: `0`

## Excluded From Git

Large SQLite databases, provider caches, checkpoint logs, smoke runs, and raw intermediate runs are intentionally excluded from this clean release package.

## Restore Final Annotation JSON

```bash
./scripts/restore_v3_0_feature_annotations.sh
```
