# Release Maintenance

## Frozen Layers

Every published annotation release must freeze the taxonomy registries, feature registry, data artifacts, reports, and manifest together. Do not update a registry without either regenerating affected annotations or recording an explicit compatibility migration.

## Required Checks

1. Parse every JSONL record.
2. Verify unique `case_id` or `job_id` constraints for the relevant artifact.
3. Recompute record counts, compressed sizes, and SHA-256 values in `manifest.json`.
4. Recompute per-feature non-`not_mentioned` counts.
5. Record missing jobs and review lineage; never silently drop them.
6. Validate that every emitted canonical ID exists in the frozen Registry.
7. Run contradiction and assertion-scope validators before publication.

## Version Policy

- Major: incompatible schema or taxonomy-layer meaning changes.
- Minor: new canonical IDs or features with backward-compatible fields.
- Patch: documentation, count, or metadata corrections that do not alter annotations.

Query templates and field catalogs are interfaces, not benchmark gold questions. A later benchmark release should separately version questions, expected case IDs, executable query plans, and answer provenance.
