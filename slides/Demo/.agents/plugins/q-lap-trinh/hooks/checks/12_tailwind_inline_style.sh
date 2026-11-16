#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 12: Tailwind [JS-02] Inline Style Guard ===${NC}"
INLINE_STYLE_FOUND=0

for view_file in $(echo "$CHANGED_FILES" | grep '\.erb$' || true); do
  if [ -f "$view_file" ]; then
    INLINE_STYLES=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$view_file" 2>/dev/null | grep '^+' | grep -E '\bstyle=["'\''\s]*[a-zA-Z0-9_-]+:' | grep -v 'display:\s*none' || true)
    if [ -n "$INLINE_STYLES" ]; then
      echo -e "${RED}❌ INLINE STYLE VIOLATION [JS-02] in ${view_file}: Use Tailwind utility classes instead of inline 'style=\"...\"'!${NC}"
      echo -e "${RED}  Line: $(echo "$INLINE_STYLES" | head -n 1 | xargs)${NC}"
      INLINE_STYLE_FOUND=1
    fi
  fi
done

if [ "$INLINE_STYLE_FOUND" -eq 1 ]; then
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ Tailwind Inline Style Guard Passed!${NC}"
fi
