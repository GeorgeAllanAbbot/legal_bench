# Methodology, Sources, and Provenance

The database was built from the CourtListener `2026-06-30` bulk exports maintained by the Free Law
Project: Opinion Clusters populate cases, Opinions provide document text/type/authorship, Courts
provide jurisdiction metadata, and Dockets provide case linkage. Source documentation:

- https://www.courtlistener.com/help/api/bulk-data/
- https://free.law/projects/courtlistener/
- https://www.courtlistener.com/help/api/rest/

The deterministic sample contains 20,000 Opinion Clusters from 1970–2025, with a controlled
pre-2000 tail and a 21st-century majority. It is not a probability sample of all U.S. filings.
`decision_year` means opinion/cluster decision year, not filing year.

The builder selects and normalizes `preferred_text` from available HTML/plain-text variants while
retaining source fields. Cases remain clusters and opinions remain separate documents. Retrieval
chunks are approximately 800 tokens with 120-token overlap, primarily from majority-like/unknown
opinion groups.

Court normalization combines CourtListener IDs, jurisdiction codes, names, and metadata. Taxonomy
uses four distinct layers: broad Practice Area, concrete Matter Type, adjudicated Legal Issue, and
Matter Type-specific analytical Features. The local closed registries were informed by
[U.S. Courts Nature of Suit terminology](https://www.uscourts.gov/forms-rules/forms/civil-cover-sheet)
and [SALI LMSS](https://github.com/sali-legal/LMSS), but neither is copied as the project taxonomy.

Annotations are model-assisted Silver data. Most feature jobs were initially extracted with
`gpt-5.4-mini`; targeted reviews used gpt-5.4/5.5/5.6 variants and a small number of human decisions.
Deterministic validation covers JSON schema, evidence scope, closed enums, units, actor/polarity,
and cross-layer contradictions. Confidence is workflow metadata, not calibrated gold accuracy.

Known limits include empty `citations_json`, 91.03% Practice Area coverage, 59.32% retained Legal
Issue coverage, selective Feature extraction, source/OCR noise, and partial pooled qrels for Hybrid
queries. Root and nested manifests provide SHA256 lineage; database tables
`annotation_registry_snapshot` and `annotation_release` freeze annotation versions.
