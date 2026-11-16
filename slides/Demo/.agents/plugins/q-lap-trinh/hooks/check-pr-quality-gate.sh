#!/usr/bin/env bash
set -e

HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$HOOK_DIR/lib/common.sh"

# Skip on main/master branch or detached state
if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ] || [ -z "$BRANCH" ]; then
  echo -e "${GREEN}[Quality Gate] Main/master branch or detached state detected. Skipping checks.${NC}"
  exit 0
fi

if [ -z "$CHANGED_FILES" ]; then
  echo -e "${GREEN}[Quality Gate] No changed files detected.${NC}"
  exit 0
fi

# Execute all active check modules in sorted order
for check_script in $(ls "$HOOK_DIR/checks/"*.sh 2>/dev/null | sort); do
  if [ -x "$check_script" ]; then
    bash "$check_script" || exit 1
  fi
done

echo -e "${GREEN}🎉 All Quality Gates Passed Successfully!${NC}"
exit 0
