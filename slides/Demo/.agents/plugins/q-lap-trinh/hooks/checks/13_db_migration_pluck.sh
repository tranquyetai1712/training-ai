#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 13: DB Migration Safety & Pluck Optimization Guard ===${NC}"
DB_OPTIMIZATION_ERROR=0

for migration_file in $(echo "$CHANGED_FILES" | grep '^db/migrate/.*\.rb$' || true); do
  if [ -f "$migration_file" ]; then
    MISSING_DEFAULTS=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$migration_file" 2>/dev/null | grep '^+' | grep -E 'add_column.*:string' | grep -v 'default:' || true)
    if [ -n "$MISSING_DEFAULTS" ]; then
      echo -e "${RED}❌ MISSING DEFAULT VALUE in ${migration_file}: String columns should have default: '' in DB migration!${NC}"
      DB_OPTIMIZATION_ERROR=1
    fi
  fi
done

for rb_file in $(echo "$CHANGED_FILES" | grep '^app/.*\.rb$' || true); do
  if [ -f "$rb_file" ]; then
    MAP_ID_USAGE=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$rb_file" 2>/dev/null | grep '^+' | grep -E '\.map\(&:id\)' || true)
    if [ -n "$MAP_ID_USAGE" ]; then
      echo -e "${RED}❌ UNOPTIMIZED QUERY in ${rb_file}: Use '.pluck(:id)' instead of '.map(&:id)' to avoid loading full ActiveRecord objects!${NC}"
      DB_OPTIMIZATION_ERROR=1
    fi
  fi
done

if [ "$DB_OPTIMIZATION_ERROR" -eq 1 ]; then
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ DB Migration & Pluck Optimization Guard Passed!${NC}"
fi
