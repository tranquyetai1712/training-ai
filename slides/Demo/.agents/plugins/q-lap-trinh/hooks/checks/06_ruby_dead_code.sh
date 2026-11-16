#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 6: Ruby / Rails Dead Code & Cleanliness Audit ===${NC}"
RUBY_DEAD_CODE_FOUND=0

for rb_file in $(echo "$CHANGED_FILES" | grep '^app/.*\.rb$' || true); do
  if [ -f "$rb_file" ]; then
    METHODS=$(grep -oP '^\s*def\s+(self\.)?\K[a-zA-Z0-9_?!=]+' "$rb_file" 2>/dev/null || true)
    for method in $METHODS; do
      case "$method" in
        index|show|new|create|edit|update|destroy|execute|initialize|call|perform|change|up|down|setup|teardown|to_s|inspect|==|===|hash|eql?) continue ;;
      esac
      
      CLEAN_METHOD=$(echo "$method" | sed -E 's/[!?=]$//')
      REFS=$(grep -rnP "\b${CLEAN_METHOD}[!?=]?" app/ config/ lib/ spec/ test/ 2>/dev/null | wc -l | xargs)
      if [ "$REFS" -le 1 ]; then
        echo -e "${RED}❌ DEAD RUBY METHOD: Method 'def ${method}' in ${rb_file} is unreferenced across app/, config/, lib/, spec/, test/!${NC}"
        RUBY_DEAD_CODE_FOUND=1
      fi
    done

    if [[ "$rb_file" =~ ^app/interactions/(.*)\.rb$ ]]; then
      CLASS_NAME=$(grep -oP '^\s*class\s+\K[A-Za-z0-9_:]+' "$rb_file" 2>/dev/null | tail -n 1 || true)
      if [ -n "$CLASS_NAME" ]; then
        SHORT_NAME=$(echo "$CLASS_NAME" | awk -F'::' '{print $NF}')
        CLASS_REFS=$(grep -rnP "\b(${CLASS_NAME}|${SHORT_NAME})\b" app/ config/ lib/ spec/ test/ 2>/dev/null | grep -v "$rb_file:" | wc -l | xargs)
        if [ "$CLASS_REFS" -eq 0 ]; then
          echo -e "${RED}❌ UNUSED INTERACTION CLASS: Interaction '${CLASS_NAME}' in ${rb_file} is never called!${NC}"
          RUBY_DEAD_CODE_FOUND=1
        fi
      fi
    fi
  fi
done

if [ "$RUBY_DEAD_CODE_FOUND" -eq 1 ]; then
  echo -e "${RED}❌ ERROR: Dead Ruby methods or unused Interactions detected.${NC}"
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ Ruby / Rails Dead Code Audit Passed!${NC}"
fi
