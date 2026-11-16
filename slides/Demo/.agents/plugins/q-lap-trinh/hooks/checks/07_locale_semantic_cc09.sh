#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 7: UI Feature Removal & Locale Semantic Consistency Check [CC-09] ===${NC}"
LOCALE_SEMANTIC_MISMATCH=0

for view_file in $(echo "$CHANGED_FILES" | grep '\.erb$' || true); do
  if [ -f "$view_file" ]; then
    REMOVED_UI_KEYWORDS=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$view_file" 2>/dev/null | grep '^-[^-]' | grep -iE 'search|filter|delete|export|remove' | grep -oP '\b(search|filter|delete|export|remove)\b' | sort -u || true)
    
    for kw in $REMOVED_UI_KEYWORDS; do
      kw_lower=$(echo "$kw" | tr '[:upper:]' '[:lower:]')
      view_dir=$(dirname "$view_file" | sed 's|^app/views/||')
      locale_files=$(find config/locales/ -path "*${view_dir}*.yml" 2>/dev/null || true)
      
      for loc_file in $locale_files; do
        if [ -f "$loc_file" ]; then
          case "$kw_lower" in
            search) MATCHES=$(grep -iE '(_tip_|_help_|_description|_instructions).*:\s*.*(search|tìm kiếm|検索)' "$loc_file" 2>/dev/null || true) ;;
            delete|remove) MATCHES=$(grep -iE '(_tip_|_help_|_description|_instructions).*:\s*.*(delete|remove|xóa|削除)' "$loc_file" 2>/dev/null || true) ;;
            export) MATCHES=$(grep -iE '(_tip_|_help_|_description|_instructions).*:\s*.*(export|xuất|エクスポート)' "$loc_file" 2>/dev/null || true) ;;
            *) MATCHES="" ;;
          esac
          
          if [ -n "$MATCHES" ]; then
            echo -e "${RED}⚠️ SEMANTIC DESYNCHRONIZATION [CC-09]: UI feature '${kw}' was removed from ${view_file}, but locale file ${loc_file} still contains description text referencing it!${NC}"
            echo -e "${RED}  Matching line: $(echo "$MATCHES" | xargs)${NC}"
            LOCALE_SEMANTIC_MISMATCH=1
          fi
        fi
      done
    done
  fi
done

if [ "$LOCALE_SEMANTIC_MISMATCH" -eq 1 ]; then
  echo -e "${RED}❌ ERROR: Outdated locale tip/help descriptions detected [CC-09]. Please update locale YAML files.${NC}"
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ UI & Locale Semantic Consistency Passed [CC-09]!${NC}"
fi
