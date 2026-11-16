#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 10: Layered Architecture & Thin Controller Guard ===${NC}"
LAYER_VIOLATION_FOUND=0

for ctrl_file in $(echo "$CHANGED_FILES" | grep '^app/controllers/.*\.rb$' || true); do
  if [ -f "$ctrl_file" ]; then
    HTTP_DECISIONS=$(git diff "$BASE_BRANCH"...HEAD -U0 -- "$ctrl_file" 2>/dev/null | grep '^+' | grep -E 'request\.format\.(json|html)\?' || true)
    if [ -n "$HTTP_DECISIONS" ]; then
      echo -e "${RED}❌ LAYER VIOLATION in ${ctrl_file}: Business decisions must depend on domain state, not 'request.format.json?'!${NC}"
      LAYER_VIOLATION_FOUND=1
    fi

    ACTION_LENGTH_EXCEEDED=$(perl -0777 -ne 'while (/def\s+([a-z_]+)(.*?)^  end/msg) { my $name=$1; my $body=$2; my $lines = () = $body =~ /\n/g; if ($lines > 50) { print "$name:$lines\n"; } }' "$ctrl_file" 2>/dev/null || true)
    if [ -n "$ACTION_LENGTH_EXCEEDED" ]; then
      echo -e "${RED}❌ FAT CONTROLLER ACTION in ${ctrl_file}: Action exceeds 50 lines! Refactor business logic into an ActiveInteraction class.${NC}"
      echo -e "${RED}  Action: $ACTION_LENGTH_EXCEEDED${NC}"
      LAYER_VIOLATION_FOUND=1
    fi
  fi
done

if [ "$LAYER_VIOLATION_FOUND" -eq 1 ]; then
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ Layered Architecture Audit Passed!${NC}"
fi
