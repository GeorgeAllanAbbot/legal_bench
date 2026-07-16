#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PHASE1_DIR="$ROOT/data/courtlistener_legal_20k/phase1"
OUTPUT="$PHASE1_DIR/legal_cases.db"
EXPECTED_SHA256="88ab3946bc4feee745f04940b5a867525413ee771aa69c3c39bad7cbe7445665"

command -v xz >/dev/null || { echo "xz is required to restore the database." >&2; exit 1; }

parts=("$PHASE1_DIR"/legal_cases.db.xz.part-*)
if [[ ! -e "${parts[0]}" ]]; then
  echo "Database parts are missing. Run: git lfs pull" >&2
  exit 1
fi

temp_output="$OUTPUT.tmp"
cat "${parts[@]}" | xz -dc > "$temp_output"
actual_sha256="$(sha256sum "$temp_output" | awk '{print $1}')"
if [[ "$actual_sha256" != "$EXPECTED_SHA256" ]]; then
  rm -f "$temp_output"
  echo "SHA-256 verification failed: $actual_sha256" >&2
  exit 1
fi

mv "$temp_output" "$OUTPUT"
echo "Restored $OUTPUT"
