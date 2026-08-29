# Legal Bench v3: CourtListener Annotation Data

Legal Bench v3 is an annotation-only release for 20,000 English-language CourtListener opinion-cluster cases. It contains taxonomy projections and Matter Type analytical features, but does **not** redistribute opinion text, a SQLite corpus, embeddings, retrieval indexes, prompts, provider logs, or model credentials.

## Annotation Layers

- **Practice Area**: broad area of law, such as `criminal_law` or `tax_law`.
- **Matter Type**: concrete case, claim, dispute, or proceeding type. This is the primary layer used to select analytical feature packs.
- **Legal Issue**: a legal question actually addressed by the court. It is not a case-type classification.
- **Matter Type Features**: structured facts, outcomes, dates, amounts, rates, actors, and other fields selected for a Matter Type.

## Files

- `data/taxonomy/case_taxonomy_v3.jsonl.xz`: 20,000 case-level taxonomy projections.
- `data/features/matter_type_features_v1_1.jsonl.xz`: 12,714 case-by-Matter-Type feature records.
- `data/registry/`: frozen registries and schema used by this release.
- `data/reports/`: release-level quality and coverage reports.
- `docs/ANNOTATION_SCHEMA_en.md`: field semantics, joins, and limitations.
- `docs/MATTER_TYPE_FEATURE_REFERENCE_en.md`: all feature keys and effective counts.
- `data/query/`: queryable-field catalog and English Query IR templates for later RAG work.

## Restore and Verify

```bash
./scripts/restore_annotations.sh
python3 scripts/verify_release.py
```

Restored JSONL files are written under `restored/`, which is ignored by Git.

## Joining to Source Cases

Join annotations to a separately obtained CourtListener corpus by `case_id`. IDs use the local normalized form `cluster_<CourtListener cluster id>`. Feature rows also have a `job_id` in the form `<case_id>::<matter_type_id>`.

## Scope

This release is suitable for retrieval filters, benchmark construction, stratified sampling, weak supervision, and structured legal analytics. The labels are model-assisted research annotations, not human gold labels or legal advice. The taxonomy projection retains 9,284 `needs_review=true` audit flags; high-confidence analytics should filter or separately report them. Two expected Matter Type feature jobs remain explicitly marked as missing after retries; see the final report.
