# English Legal Descriptive Benchmark v6

This benchmark contains 120 descriptive legal analytics questions over the frozen CourtListener 20k dataset.

## Tasks

Each query defines two separate tasks:

1. **Case-set retrieval**: retrieve cases relevant to the complete structured and semantic query.
2. **Answer generation**: produce the count, percentage, or comparison result derived from the relevant set.

Retrieval and answer generation must be evaluated separately. A correct aggregate answer does not prove that the supporting cases were retrieved correctly.

## Qrel states

- `positive`: adjudicated relevant case, relevance grade 2.
- `negative`: explicitly adjudicated hard negative, relevance grade 0.
- `unjudged`: pooled retrieval candidate that has not been adjudicated. It must not be treated as a negative.

SQL queries use `exhaustive_structured_projection`. Hybrid queries use `partial_pool` because semantic relevance has not been exhaustively judged across all 20,000 opinions.

## Evidence size and metrics

- `small`: up to 50 positives; use Recall@50 and Recall@100.
- `medium`: 51–200 positives; use Recall@100 and Recall@500.
- `large`: over 200 positives; use Recall@500, Recall@1000, and answer accuracy.

Precision@10 and nDCG@10 are retained across all size buckets. Recall@100 alone is not suitable for queries with more than 100 relevant cases.

## Splits

- Development: 60 queries
- Validation: 30 queries
- Test: 30 queries

The split is deterministic and stratified across query family, SQL/Hybrid type, difficulty, and evidence-size bucket. The test split should remain frozen.

## Files

- `benchmark_full.json`: complete research artifact.
- `queries_public.json`: queries and evaluation metadata without answers or qrels.
- `qrels_private.json`: answers, positive/negative/unjudged pools, and task definitions.
- `splits.json`: frozen query IDs for each split.
- `quality_report.json`: deterministic validation and distribution report.
- `manifest.json`: checksums, lineage, random seed, and frozen-split status.

## Query quality and limitations

- There are no exact duplicate questions and no query has an empty positive evidence set.
- Every query combines two to four constraint dimensions; 80 of 120 use three or four.
- The benchmark covers 16 Matter Type groupings and is not intended to represent every Matter Type
  in the source database.
- Explicit negatives are unevenly distributed: 522 belong to SQL queries and 22 to Hybrid queries.
  Consequently, judged precision is conditional on a sparse judged pool and must not be presented
  as ordinary retrieval precision. Prefer Recall, nDCG, and bpref, and report judged rate.

All labels and qrels are research annotations, not legal advice or human gold labels. The current release remains Silver.
