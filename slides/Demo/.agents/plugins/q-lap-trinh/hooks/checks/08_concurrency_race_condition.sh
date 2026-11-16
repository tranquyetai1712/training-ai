#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 8: Concurrency, Busy-Wait & Race Condition Audit ===${NC}"
CONCURRENCY_ERROR=0

for rb_file in $(echo "$CHANGED_FILES" | grep '^app/\(controllers\|interactions\)/.*\.rb$' || true); do
  if [ -f "$rb_file" ]; then
    BUSY_WAITS=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$rb_file" 2>/dev/null | grep '^+' | grep -E '\bsleep\(\d+\)|\bThread\.sleep' || true)
    if [ -n "$BUSY_WAITS" ]; then
      echo -e "${RED}❌ BUSY-WAIT DETECTED in ${rb_file}: Found 'sleep' inside Controller/Interaction which blocks Puma worker threads! Use Async Jobs or ActionCable instead.${NC}"
      CONCURRENCY_ERROR=1
    fi
  fi
done

for rb_file in $(echo "$CHANGED_FILES" | grep '^app/.*\.rb$' || true); do
  if [ -f "$rb_file" ]; then
    RACE_CREATES=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$rb_file" 2>/dev/null | grep '^+' | grep -E 'find_by\(.*\)\s*\|\|\s*create' || true)
    if [ -n "$RACE_CREATES" ]; then
      echo -e "${RED}❌ NON-ATOMIC RACE CONDITION in ${rb_file}: Found 'find_by || create'. Use 'find_or_create_by' with DB unique index.${NC}"
      CONCURRENCY_ERROR=1
    fi
  fi
done

if [ "$CONCURRENCY_ERROR" -eq 1 ]; then
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ Concurrency & Race Condition Audit Passed!${NC}"
fi
