#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATA_DIR="$ROOT/data/courtlistener_legal_20k/analytics_v1/v3_0_release/data"
XZ="$DATA_DIR/legal_issue_feature_full_v1_16k_final_merged.json.xz"
OUT="$DATA_DIR/legal_issue_feature_full_v1_16k_final_merged.json"
if [[ ! -f "$XZ" ]]; then
  echo "Missing compressed annotation file: $XZ" >&2
  exit 1
fi
xz -dkf "$XZ"
echo "Restored $OUT"
