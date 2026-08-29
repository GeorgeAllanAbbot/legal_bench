
# Query Preparation for RAG

The annotation release supports a future two-channel query layer.

## Structured Channel

Use canonical fields for exact filters, counts, grouping, and sorting:

- taxonomy: `practice_area.primary`, `matter_types[].id`, `legal_issues[].issue_id`;
- audit: `annotation_status`, `needs_review`, confidence thresholds;
- analytical features: `feature_key`, status, normalized value, unit, and evidence;
- source metadata, when joined from CourtListener: court, court level, jurisdiction, and year.

Only values with a status other than `not_mentioned` should normally satisfy a feature filter. Missing values are unknown, not negative.

## Semantic Channel

Use opinion chunks from a separately maintained source corpus for questions about facts, arguments, holdings, and legal reasoning. Apply structured constraints before or after vector/BM25 retrieval, then require answer citations to source cases.

## Recommended Query IR

```json
{
  "intent": "count_cases | find_cases | aggregate | compare | explain",
  "semantic_query": "optional natural-language retrieval query",
  "filters": [
    {"field": "matter_type", "operator": "in", "value": ["foreclosure_mortgage"]},
    {"field": "feature.amount_awarded_usd", "operator": "gt", "value": 100000}
  ],
  "group_by": ["year"],
  "sort": [{"field": "feature.amount_awarded_usd", "direction": "desc"}],
  "limit": 20
}
```

## English Question Patterns

1. **Count**: "How many foreclosure cases awarded attorney fees over $50,000?"
2. **Conditional retrieval**: "Find asylum cases in which detention duration was mentioned."
3. **Distribution**: "What is the distribution of current-court dispositions in sentencing appeals?"
4. **Trend**: "How did reported damages awards in employment discrimination cases change by year?"
5. **Comparison**: "Compare median settlement amounts for product liability and medical malpractice cases."
6. **Hybrid RAG**: "In duty-to-defend cases, explain when courts found that the insurer owed a defense."

The first five patterns can use annotation filters and aggregation. The final pattern must join filtered case IDs to source opinion text and use retrieval plus generation.

## Guardrails

- Do not infer an unmentioned amount as zero.
- Do not treat a Legal Issue as a Matter Type.
- Keep requested relief, lower-court result, and current-court disposition separate.
- Preserve currency and unit; do not silently convert non-USD values.
- Exclude or separately report records marked for review when producing high-confidence statistics.
