#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 4: Dead Code Audit & Broken Binding Check (Stimulus Controllers & Views) ===${NC}"
DEAD_CODE_FOUND=0

for js_file in $(echo "$CHANGED_FILES" | grep '^app/javascript/controllers/.*\.js$' || true); do
  if [ -f "$js_file" ]; then
    controller_basename=$(basename "$js_file" .js)
    controller_name=$(echo "$controller_basename" | sed 's/_controller$//' | tr '_' '-')
    
    TARGETS=$(grep -oP 'static targets = \[\K[^\]]+' "$js_file" 2>/dev/null | tr -d '\r"'"'" | tr ',' ' ' || true)
    for target in $TARGETS; do
      target=$(echo "$target" | xargs)
      [ -z "$target" ] && continue
      REF_COUNT=$(grep -rnP "(#${target}\b|data-${controller_name}-target=[\"']${target}[\"']|${target}Target\b)" app/views/ app/javascript/ 2>/dev/null | wc -l | xargs)
      if [ "$REF_COUNT" -eq 0 ]; then
        echo -e "${RED}❌ DEAD CODE: Target '${target}' in ${js_file} is unused anywhere in views or JS!${NC}"
        DEAD_CODE_FOUND=1
      fi
    done

    IMPORTED_FUNCS=$(grep -oP 'import\s+\{([^}]+)\}' "$js_file" 2>/dev/null | sed -E 's/import\s*\{([^}]+)\}.*/\1/' | tr ',' '\n' | xargs -n1 2>/dev/null | grep -oP '^[a-zA-Z0-9_]+' || true)
    IMPORTED_DEFAULT=$(grep -oP 'import\s+([a-zA-Z0-9_]+)\s+from' "$js_file" 2>/dev/null | awk '{print $2}' || true)
    ALL_IMPORTS="$IMPORTED_FUNCS $IMPORTED_DEFAULT"

    METHODS=$(grep -oP '^\s*(async\s+|static\s+|get\s+|set\s+|#)?\s*([a-zA-Z0-9_]+)\s*\([^)]*\)\s*\{' "$js_file" 2>/dev/null | grep -oP '[a-zA-Z0-9_]+\s*\([^)]*\)\s*\{' | cut -d'(' -f1 | xargs -n1 | sort -u || true)
    for method in $METHODS; do
      case "$method" in
        connect|disconnect|initialize|constructor|if|for|while|switch|catch|render|clearTimeout|setTimeout|setInterval|clearInterval|fetch|addEventListener|removeEventListener|cloneNode|appendChild|replaceChildren|append|alert|confirm|prompt|requestAnimationFrame|cancelAnimationFrame|console|parseInt|parseFloat|encodeURIComponent|decodeURIComponent|structuredClone|queueMicrotask|requestIdleCallback|cancelIdleCallback) continue ;;
      esac
      if echo "$ALL_IMPORTS" | grep -qw "$method" 2>/dev/null; then
        continue
      fi
      VIEW_REFS=$(grep -rnP "#${method}\b" app/views/ 2>/dev/null | wc -l | xargs)
      JS_REFS=$(grep -rnP "(this\.${method}\b|#${method}\b)" app/javascript/ 2>/dev/null | wc -l | xargs)
      TOTAL_REFS=$((VIEW_REFS + JS_REFS))
      if [ "$TOTAL_REFS" -eq 0 ]; then
        echo -e "${RED}❌ DEAD CODE: Method '${method}' in ${js_file} is unreferenced anywhere in app/views/ or app/javascript/!${NC}"
        DEAD_CODE_FOUND=1
      fi
    done
  fi
done

for erb_file in $(echo "$CHANGED_FILES" | grep '\.erb$' || true); do
  if [ -f "$erb_file" ]; then
    ACTIONS=$(grep -oP '[a-zA-Z0-9_-]+#[a-zA-Z0-9_]+' "$erb_file" 2>/dev/null || true)
    for action in $ACTIONS; do
      c_name=$(echo "$action" | cut -d'#' -f1)
      m_name=$(echo "$action" | cut -d'#' -f2)
      c_js_file="app/javascript/controllers/$(echo "$c_name" | tr '-' '_')_controller.js"
      
      if [ -f "$c_js_file" ]; then
        HAS_METHOD=$(grep -cE "^\s*(async\s+)?${m_name}\s*\(" "$c_js_file" 2>/dev/null || echo "0")
        HAS_METHOD=$(echo "$HAS_METHOD" | tail -n 1 | xargs)
        [ -z "$HAS_METHOD" ] && HAS_METHOD=0
        if [ "$HAS_METHOD" -eq 0 ]; then
          echo -e "${RED}❌ BROKEN ACTION BINDING: ${erb_file} references '${action}', but method '${m_name}' is missing in ${c_js_file}!${NC}"
          DEAD_CODE_FOUND=1
        fi
      fi
    done
  fi
done

if [ "$DEAD_CODE_FOUND" -eq 1 ]; then
  echo -e "${RED}❌ ERROR: Dead code or broken Stimulus controller bindings detected.${NC}"
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ Dead Code & Action Binding Audit Passed!${NC}"
fi
