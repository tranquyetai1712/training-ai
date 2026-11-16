#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 11: Dangerous Rescue & Raw Error Leak Audit ===${NC}"
SECURITY_RESCUE_FOUND=0

for rb_file in $(echo "$CHANGED_FILES" | grep '^app/.*\.rb$' || true); do
  if [ -f "$rb_file" ]; then
    BROAD_RESCUES=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$rb_file" 2>/dev/null | grep '^+' | grep -E 'rescue\s+Exception\b' || true)
    if [ -n "$BROAD_RESCUES" ]; then
      echo -e "${RED}❌ DANGEROUS RESCUE in ${rb_file}: Never 'rescue Exception'! Rescue specific errors or StandardError.${NC}"
      SECURITY_RESCUE_FOUND=1
    fi

    RAW_ERROR_LEAKS=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$rb_file" 2>/dev/null | grep '^+' | grep -E 'render\s+json:.*(e\.message|error\.message|exception\.message)' || true)
    if [ -n "$RAW_ERROR_LEAKS" ]; then
      echo -e "${RED}❌ ERROR INFORMATION LEAK in ${rb_file}: Avoid leaking raw 'e.message' (AWS/Server trace) to UI. Sanitize error messages first.${NC}"
      SECURITY_RESCUE_FOUND=1
    fi
  fi
done

if [ "$SECURITY_RESCUE_FOUND" -eq 1 ]; then
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ Broad Rescue & Security Audit Passed!${NC}"
fi
