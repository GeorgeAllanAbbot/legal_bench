# Legal Bench v3.1

Legal Bench v3.1 is an English U.S. case-law research dataset for retrieval, RAG, and descriptive
legal analytics. The clean release has two primary entry points:

- `data/`: integrated SQLite corpus, opinion text, annotations, registries, and dataset docs.
- `query/descriptive_query/`: 120 descriptive questions, hidden answers/qrels, and benchmark docs.

## Dataset

The restored SQLite database contains 20,000 CourtListener Opinion Cluster cases, 21,261 nonempty
opinion texts, 440 courts, 94,314 retrieval chunks, full Matter Type projection coverage, and
Matter Type analytical features. Restore four Zstandard parts with:

```bash
./scripts/restore_integrated_db.sh
```

See [data/README.md](data/README.md) for source provenance, schema, field meanings, relationships,
coverage, construction, limitations, and SQL/Python use.

## Descriptive benchmark

The benchmark contains 40 count, 40 proportion, and 40 comparison questions: 36 structured SQL
queries and 84 structured-plus-semantic Hybrid queries. Splits are frozen at 60 development, 30
validation, and 30 test queries. Keep `qrels_private.json` hidden from evaluated systems.

See [query/README.md](query/README.md) for task and evaluation semantics.

## Source and references

Cases and opinions come from the CourtListener `2026-06-30` bulk snapshot maintained by the Free
Law Project: [Bulk Legal Data](https://www.courtlistener.com/help/api/bulk-data/) and
[CourtListener project](https://free.law/projects/courtlistener/).

The local taxonomy was informed, but not defined, by U.S. Courts Nature of Suit terminology and
SALI LMSS compatibility concepts. Benchmark research dimensions were informed by U.S. Courts,
Federal Judicial Center, National Center for State Courts, and Bureau of Justice Statistics
reporting practices. External references do not supply benchmark answers.

This is model-assisted Silver research data, not human-gold legal annotation or legal advice.
Run `python3 scripts/verify_release.py` before use.
