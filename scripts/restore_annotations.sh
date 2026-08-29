#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
mkdir -p "$ROOT/restored"
xz -dc "$ROOT/data/taxonomy/case_taxonomy_v3.jsonl.xz" > "$ROOT/restored/case_taxonomy_v3.jsonl"
xz -dc "$ROOT/data/features/matter_type_features_v1_1.jsonl.xz" > "$ROOT/restored/matter_type_features_v1_1.jsonl"
printf 'Restored annotation JSONL files under %s/restored
' "$ROOT"
