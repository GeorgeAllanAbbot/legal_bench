# SQLite Field Dictionary

`FIELD_CATALOG.json` is generated directly from SQLite PRAGMAs and exhaustively records column
types, defaults, nullability, primary keys, foreign keys, indexes, and table row counts. This file
summarizes business semantics.

## Identifiers and hierarchy

- `case_id`: local key `cluster_<CourtListener cluster id>`.
- `cluster_id`: source Opinion Cluster identifier; joins cases to opinions.
- `opinion_id`: source Opinion identifier; a case may have multiple opinions.
- `document_id`: locally generated retrieval-chunk identifier.
- `*_json`: JSON serialized as SQLite text.
- `confidence`: model/rule confidence, not calibrated correctness probability.

The hierarchy is Court (`dim_court`) → Case (`case_record`) → Opinion (`opinion_record`) → Chunk
(`search_document`). A case may have multiple Practice Areas, Matter Types, and Legal Issues. A
Matter Type selects Matter occurrences and Feature values.

## Source tables

### `dim_court`

`court_id` is the key; names are in `court_name`/`court_name_short`; source and normalized
jurisdiction are `jurisdiction_raw`, `jurisdiction_type`, and `court_level`; `circuit` and
`state_code` support geographic filtering; `is_active`, `start_date`, and `end_date` describe court
history; `raw_json` and `provenance_json` preserve lineage.

### `case_record`

`case_id`, `cluster_id`, `docket_id`, `docket_number`, and `court_id` identify and join a case.
`case_name` and `case_name_docket` are display/source names. `decision_date` and `decision_year`
define benchmark time. `publication_status_raw` and `precedential_status` store raw/normalized
status. `judges_raw`, `syllabus`, `posture`, and `procedural_history` retain source metadata.
`jurisdiction_type` and `court_level` are filter projections. `opinion_ids_json` lists opinions.
`citations_json` is empty in this snapshot. `source`, `raw_json`, and `provenance_json` retain source
lineage.

### `opinion_record`

`opinion_id` is the key and `cluster_id` joins its case. `opinion_type_raw`, `opinion_type`, and
`opinion_group` describe document role. `author_id` and `per_curiam` describe authorship.
`html_with_citations` and `plain_text` retain source variants; `preferred_text` is the normalized
RAG text and `preferred_text_source` records its origin. `text_length`, `text_sha1`,
`has_usable_text`, and `quality_metrics_json` support quality control. `cited_opinion_ids_json`,
`raw_json`, and `provenance_json` retain source relationships and lineage.

### `search_document`

`document_id`, `case_id`, `opinion_id`, and `cluster_id` identify a chunk and its parents.
`case_name`, court/jurisdiction fields, date/year, precedent status, and opinion type are denormalized
filters. `section_type`, `section_weight`, `chunk_index`, `chunk_text`, and `chunk_token_count`
describe chunking. `bm25_text` supports lexical indexing. `primary_topic` and `statutes_json` are v2
weak features. `embedding_json` is an empty placeholder; vectors should live in an external index.

## Annotation tables

`case_features` contains legacy v2 rule candidates: topic fields, statutes, constitutional
provisions, tail-based dispositions, relief, confidence, evidence spans, and rule signals. Prefer
normalized v3 tables for analytics.

`case_taxonomy_v3` stores one final projection per case: annotation status, primary/secondary
Practice Areas, Matter Types, retained/unmapped Legal Issues, review state, and raw annotation.

`case_practice_area_v3` stores `case_id`, canonical `practice_area`, primary/secondary `area_role`,
confidence, and evidence.

`case_matter_type_v3` stores `case_id`, canonical `matter_type`, parent `practice_area`, confidence,
review flag, and evidence. Matter Type is the primary case-type and Feature-Pack selector.

`case_legal_issue_v3` stores `case_id`, canonical `issue_id`, issue status, separate mention and
adjudication confidence, and court-analysis/holding evidence. Absence is unknown, not a negative.

## Matter Type Feature tables

`matter_type_feature_job_v1_1` stores job ID, case identity, annotation source/status, review history,
human review, and raw output. `matter_type_annotation_v1_1` identifies each Matter Type occurrence,
its status, and target. `matter_type_feature_value_v1_1` stores feature key/occurrence, value status,
JSON/text/numeric projections, explicit unit, confidence, missing reason, and evidence.

`not_mentioned` means unavailable from the opinion, not zero or false. Numeric filters must check
both `value_number` and `unit`. Full Feature types, enums, units, effective counts, and bidirectional
Matter Type membership are documented in `../docs/MATTER_TYPE_FEATURE_REFERENCE_en.md` and the
frozen Feature Registry.

`annotation_release` and `annotation_registry_snapshot` store release lineage and exact Registry
content/checksums. `build_state` retains source-builder state. The migration-only backup table is
excluded from the cleaned release database.
