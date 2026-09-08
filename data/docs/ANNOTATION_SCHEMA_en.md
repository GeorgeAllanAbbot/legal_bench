
# Annotation Schema

## 1. Case Taxonomy

One JSON object per case.

- `case_id`, `case_name`: stable join key and display name.
- `annotation_status`: record-level projection status.
- `practice_area`: primary/secondary broad legal domains, confidence, and evidence.
- `matter_types`: concrete case or proceeding types with confidence and evidence.
- `legal_issues`: legal questions addressed by the current court, including mention and adjudication confidence.
- `unmapped_matter_types`, `unmapped_legal_issues`: preserved concepts outside the frozen canonical registry.
- `needs_review`, `review_applied`, `review_status`: audit state.
- `moved_legal_issues`, `legal_issue_simplification`: lineage from Legal Issue simplification.

Matter Type and Legal Issue are intentionally separate. For example, `breach_of_contract` may describe what kind of dispute the case is, while jurisdiction or evidence questions may be the Legal Issues decided in the opinion.

## 2. Matter Type Features

One JSON object per `case_id × matter_type_id` job.

- `job_id`: unique composite key.
- `case_id`, `case_name`: link to taxonomy and source corpus.
- `matter_type_ids`: Matter Type scope for the job.
- `annotation_source`, `annotation_status`: model/review lineage and final state.
- `review_history`, `human_review`: audit trail.
- `matter_type_feature_annotations`: Matter Type target and feature values.

Feature definitions, types, units, allowed values, and Matter Type membership are in `matter_type_feature_registry_v1_1.json`. The bilingual feature reference reports the number of values whose status is not `not_mentioned`; this is an effective instance count, not necessarily a unique-case count.

## Evidence and Missingness

Evidence text is retained where emitted by the annotation pipeline. A missing or `not_mentioned` value means the opinion did not provide sufficient support for that field; it must not be interpreted as zero, false, or a negative legal holding.

## Versioning

- Package: v3.1 integrated SQLite dataset release.
- Practice Area and Matter Type registries: v3.2.0.
- Simplified Legal Issue registry: v3.1-simplified.
- Matter Type feature registry/data: v1.1.
