# Legal Bench v3.1 Dataset

This directory contains the complete CourtListener-derived English case corpus, normalized
annotations, frozen registries, and quality reports. The core artifact under `dataset/` is a SQLite
database containing case metadata, 21,261 opinion texts, retrieval chunks, Matter Types, and
analytical features.

## Layout

| Path | Contents |
|---|---|
| `dataset/` | SQLite archive parts, schema, field catalog, and coverage report |
| `registry/` | Frozen Practice Area, Matter Type, Legal Issue, and Feature registries |
| `docs/` | Annotation semantics and Matter Type-to-Feature membership |

## Hierarchy

```text
Court -> Case/Opinion Cluster -> Opinion -> Retrieval chunk
                              -> Practice Area
                              -> Matter Type -> Matter occurrence -> Feature values
                              -> Legal Issue
```

Practice Area is broad. Matter Type identifies the concrete kind of matter and selects a Feature
Pack. Legal Issue is a narrower question adjudicated by the court and is not a case-type label.
Feature values are evidence-backed facts, amounts, dates, actors, and outcomes extracted under a
Matter Type.

## Coverage

- 20,000 cases; 21,261 nonempty opinions; 21,189 usable opinions; 94,314 retrieval chunks.
- Case name, court, decision date, and Matter Type: 100% case coverage.
- Practice Area: 18,206 cases (91.03%).
- Retained Legal Issue: 11,864 cases (59.32%).
- Accepted Matter Type Feature job: 12,712 cases (63.56%).

See `dataset/COVERAGE_REPORT.json` for complete distributions. Coverage is not human-gold accuracy.

## Source and construction references

The corpus was built from the CourtListener `2026-06-30` bulk snapshot: Opinion Clusters, Opinions,
Courts, and Dockets. Primary sources are [CourtListener Bulk Legal Data](https://www.courtlistener.com/help/api/bulk-data/),
the [Free Law Project CourtListener project](https://free.law/projects/courtlistener/), and the
[CourtListener REST API documentation](https://www.courtlistener.com/help/api/rest/).

The local taxonomy is an application-oriented closed registry. The
[U.S. Courts Civil Cover Sheet and Nature of Suit](https://www.uscourts.gov/forms-rules/forms/civil-cover-sheet)
and [SALI LMSS](https://github.com/sali-legal/LMSS) informed terminology and compatibility planning;
they are not copied labels and do not define ordinary query behavior.

Sampling covers 1970–2025 with a controlled pre-2000 tail. Cases are Opinion Clusters; opinions
remain separate documents. Search chunks are approximately 800 tokens with 120-token overlap.
Taxonomy and features are model-assisted Silver annotations with deterministic validation and
targeted review.

## Use

Restore the database with `./scripts/restore_integrated_db.sh`, then open it read-only:

```python
import sqlite3
db = sqlite3.connect("file:data/dataset/legal_rag_dataset_v3.db?mode=ro", uri=True)
```

See `dataset/FIELD_DICTIONARY_en.md` for every table and field, and
`docs/MATTER_TYPE_FEATURE_REFERENCE_en.md` for Feature definitions, units, coverage, and membership.

Important limitations: `citations_json` is empty in this snapshot; `not_mentioned` means unknown,
not zero or false; opinion text may retain source formatting/OCR noise; annotations are research
data and not legal advice.
