# Descriptive Query Field Dictionary

`queries_public.json` contains model-visible fields: `id`, `query`, `instruction`, `query_family`,
`type`, `difficulty`, `split`, `evidence_size_bucket`, `recommended_metrics`, and
`constraint_dimensions`.

`qrels_private.json` contains hidden evaluation data:

- `qrel_states.positive`: relevant `case_id -> 2` mappings.
- `qrel_states.negative`: explicitly rejected hard negatives (`case_id -> 0`).
- `qrel_states.unjudged`: pooled candidates that must not be treated as negatives.
- `benchmark_tasks.retrieval`: case/document IDs and qrel completeness.
- `benchmark_tasks.answer`: answer type, ground truth, derivation, evaluation rule, and population
  provenance.
- `qrel_confidence`: current annotation grade (`silver`).

`benchmark_full.json` additionally retains executable structured filters/SQL, semantic concept
definitions and exclusions, evidence details, Query IR, research rationale, snapshot lineage, and
validation results. It is an internal reproducibility artifact and must not be shown to evaluated
systems.

Retrieval is evaluated at deduplicated case level with Recall, nDCG, and bpref. Count answers use
integer exact match; proportions use exact numerator/denominator plus numeric tolerance; comparison
answers use winner/tie and group counts. Conditional judged precision is not ordinary precision
because the Hybrid negative pool is sparse.
