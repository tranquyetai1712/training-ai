#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 3: PR Description Sync Verification ===${NC}"
if command -v gh >/dev/null 2>&1; then
  PR_BODY=$(gh pr view "$BRANCH" --json body -q .body 2>/dev/null || echo "")
  if [ -n "$PR_BODY" ]; then
    # 1. Forward Check: Verify all modified files are mentioned in PR description
    UNMATCHED=""
    for file in $CHANGED_FILES; do
      base_name=$(basename "$file")
      name_no_ext="${base_name%.*}"
      if ! echo "$PR_BODY" | grep -qi "$base_name" && ! echo "$PR_BODY" | grep -qi "$name_no_ext"; then
        UNMATCHED="$UNMATCHED $file"
      fi
    done

    if [ -n "$UNMATCHED" ]; then
      echo -e "${RED}❌ ERROR: PR Description on GitHub is out of sync (Forward Check)!${NC}"
      echo -e "${RED}The following modified files are not mentioned in PR description:${NC}"
      for f in $UNMATCHED; do
        echo "  - $f"
      done
      STOP_NOTICE
      exit 1
    fi

    # 2. Reverse Check: Verify that Class/Module Names claimed in PR Body changes exist in git diff
    CHANGES_SECTION=$(echo "$PR_BODY" | sed -n '/## \(Summary\|Key Changes\|Changes\)/,/## \(How to Test\|Checklist\|Screenshots\)/p' | grep -v -E '## \(How to Test\|Checklist\|Screenshots\)')
    CLAIMED_CLASSES=$(echo "$CHANGES_SECTION" | grep -oP '\b[A-Z][a-zA-Z0-9_]+(::[A-Z][a-zA-Z0-9_]+)+\b' | sort -u || true)

    FALSE_CLAIMS=""
    for cls in $CLAIMED_CLASSES; do
      class_filename=$(echo "$cls" | awk -F'::' '{print $NF}' | sed -E 's/([a-z0-9])([A-Z])/\1_\2/g' | tr '[:upper:]' '[:lower:]' | sed 's/$/\.rb/')
      # Only consider classes that match an actual file in app/lib/spec
      existing_file=$(find app lib spec -name "$class_filename" 2>/dev/null | head -n 1 || true)
      if [ -n "$existing_file" ]; then
        if ! echo "$CHANGED_FILES" | grep -qi "$class_filename"; then
          FALSE_CLAIMS="${FALSE_CLAIMS}\n  - ${cls} (${existing_file})"
        fi
      fi
    done

    if [ -n "$FALSE_CLAIMS" ]; then
      echo -e "${RED}❌ ERROR: PR Description contains FALSE CLAIMS (Reverse Check)!${NC}"
      echo -e "${RED}The following classes are claimed in PR description changes but NOT found in git diff:${NC}"
      echo -e "${RED}${FALSE_CLAIMS}${NC}"
      STOP_NOTICE
      exit 1
    fi

    echo -e "${GREEN}✓ PR Description 2-Way Sync Verified (Forward & Reverse)!${NC}"
  else
    echo "No existing PR found on GitHub for branch '$BRANCH'. Skipping PR description sync check."
  fi
else
  echo "GitHub CLI (gh) not installed. Skipping PR description sync check."
fi
