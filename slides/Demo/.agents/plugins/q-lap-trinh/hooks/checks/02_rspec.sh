#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 2: RSpec Execution for Affected Specs ===${NC}"
SPEC_FILES=""
for file in $CHANGED_FILES; do
  if [[ "$file" =~ ^spec/.*_spec\.rb$ ]] && [ -f "$file" ]; then
    SPEC_FILES="$SPEC_FILES $file"
  elif [[ "$file" =~ ^app/(.*)\.rb$ ]]; then
    possible_spec="spec/${BASH_REMATCH[1]}_spec.rb"
    if [ -f "$possible_spec" ]; then
      SPEC_FILES="$SPEC_FILES $possible_spec"
    fi
  fi
done

SPEC_FILES=$(echo "$SPEC_FILES" | tr ' ' '\n' | grep -v '^$' | sort -u | tr '\n' ' ')

if [ -n "$SPEC_FILES" ]; then
  echo "Running specs: $SPEC_FILES"

  RC=0
  if is_web_running; then
    $DOCKER_CMD exec -T web bundle exec rspec $SPEC_FILES || RC=$?
  elif has_bundle_on_host; then
    bundle exec rspec $SPEC_FILES || RC=$?
  else
    echo -e "${RED}❌ ERROR: Không thể chạy RSpec do thiếu môi trường thực thi (Database/Container)!${NC}"
    echo -e "${YELLOW}Nguyên nhân:${NC}"
    echo "  - Container 'web' của project này chưa chạy (hoặc Docker đang chạy ở thư mục khác)."
    echo "  - Máy host không có sẵn lệnh 'bundle' để chạy test trực tiếp."
    echo -e "${YELLOW}Giải pháp:${NC}"
    echo "  1. Khởi động Docker cho dự án này: docker compose up -d"
    echo "  2. Hoặc nếu bạn đã verify test trước đó và muốn push: git push --no-verify"
    STOP_NOTICE
    exit 1
  fi

  if [ $RC -ne 0 ]; then
    echo -e "${RED}❌ ERROR: RSpec tests failed.${NC}"
    STOP_NOTICE
    exit 1
  fi
  echo -e "${GREEN}✓ RSpec Passed!${NC}"
else
  echo "No matching spec files found for modified code."
fi
