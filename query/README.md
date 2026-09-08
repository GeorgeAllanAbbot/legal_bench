# Legal Bench Query Data

`descriptive_query/` contains 120 English descriptive legal-analytics questions for comparing
BM25, dense, hybrid, reranking, and other RAG methods. Queries join the database through `case_id`
and `document_id`; public prompts are separated from private answers and qrels.

- 40 count, 40 proportion, and 40 comparison questions.
- 36 exhaustive structured SQL questions and 84 structured-plus-semantic Hybrid questions.

Question design follows real judicial-statistics dimensions documented by the
[U.S. Courts](https://www.uscourts.gov/statistics-reports/caseload-statistics-data-tables),
[Federal Judicial Center](https://www.fjc.gov/research/federal-court-cases-fjc-integrated-database-1979-present),
[National Center for State Courts](https://www.courtstatistics.org/__data/assets/pdf_file/0031/88735/State-Court-Guide-to-Statistical-Reporting.pdf),
and [Bureau of Justice Statistics](https://bjs.ojp.gov/data-collection/state-court-processing-statistics-scps-and-national-pretrial-reporting-program-nprp).
These references establish research value; benchmark answers come only from the frozen database
and project qrels.

Use `queries_public.json` as model input and keep `qrels_private.json` hidden until evaluation.
Unjudged pooled cases are not negatives. See the bilingual documentation inside
`descriptive_query/` for fields, qrel semantics, metrics, and limitations.
