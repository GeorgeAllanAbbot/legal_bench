#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATA_DIR="$ROOT/data/dataset"
ARCHIVE="$DATA_DIR/legal_rag_dataset_v3.db.zst"
DATABASE="$DATA_DIR/legal_rag_dataset_v3.db"

cat "$DATA_DIR"/legal_rag_dataset_v3.db.zst.part-* > "$ARCHIVE"
echo "cb73fc1167aef5167dc0113373c692e52ce5413f31e864b694fd9243f4baaff0  $ARCHIVE" | sha256sum -c -
zstd -d --force "$ARCHIVE" -o "$DATABASE"
echo "29025e4ef4c0510643d0e3a0143419f87f34d9384eebdf2a60bf1aac2dad0386  $DATABASE" | sha256sum -c -

CHECK="$(sqlite3 "$DATABASE" 'PRAGMA quick_check;')"
if [[ "$CHECK" != "ok" ]]; then
  echo "SQLite quick_check failed: $CHECK" >&2
  exit 1
fi

printf 'Restored and verified: %s\n' "$DATABASE"
