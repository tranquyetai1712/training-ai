#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 9: Hardcoded UI Text & Missing I18n Audit ===${NC}"
HARDCODED_I18N_FOUND=0

for view_file in $(echo "$CHANGED_FILES" | grep '\.erb$' || true); do
  if [ -f "$view_file" ]; then
    HARDCODED_LINES=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$view_file" 2>/dev/null | grep '^+' | grep -v '^+++' | grep -E '>[^<>{}\n]*(Tìm kiếm|Xóa|Sửa|Thêm|Tải|検索|削除|編集|Save|Submit|Delete)[^<>{}\n]*<' | grep -v 't(' || true)
    if [ -n "$HARDCODED_LINES" ]; then
      echo -e "${RED}❌ HARDCODED UI TEXT in ${view_file}: Extract text strings to config/locales/*.yml using t('key')!${NC}"
      echo -e "${RED}  Line: $(echo "$HARDCODED_LINES" | head -n 2 | xargs)${NC}"
      HARDCODED_I18N_FOUND=1
    fi
  fi
done

if [ "$HARDCODED_I18N_FOUND" -eq 1 ]; then
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ Hardcoded UI Text & I18n Check Passed!${NC}"
fi
