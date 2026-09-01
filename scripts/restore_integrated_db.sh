#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DATA_DIR="$ROOT/data/integrated"
ARCHIVE="$DATA_DIR/legal_rag_dataset_v3.db.zst"
DATABASE="$DATA_DIR/legal_rag_dataset_v3.db"

cat "$DATA_DIR"/legal_rag_dataset_v3.db.zst.part-* > "$ARCHIVE"
echo "27cdf5ca6aef29ac3cacf825e1bf75d8596e0200deb37ad3a37177ce59ca7b8d  $ARCHIVE" | sha256sum -c -
zstd -d --force "$ARCHIVE" -o "$DATABASE"
echo "9a93f7b3a0c757fd1c19524d32238914616a58380e604b44061f2711e5172c7e  $DATABASE" | sha256sum -c -

CHECK="$(sqlite3 "$DATABASE" 'PRAGMA quick_check;')"
if [[ "$CHECK" != "ok" ]]; then
  echo "SQLite quick_check failed: $CHECK" >&2
  exit 1
fi

printf 'Restored and verified: %s\n' "$DATABASE"
