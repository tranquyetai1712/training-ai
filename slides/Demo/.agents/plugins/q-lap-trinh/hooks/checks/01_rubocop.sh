#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 1: RuboCop Inspection on Changed Ruby Files ===${NC}"
EXISTING_RUBY_FILES=""
for file in $(echo "$CHANGED_FILES" | grep '\.rb$' || true); do
  if [ -f "$file" ]; then
    EXISTING_RUBY_FILES="$EXISTING_RUBY_FILES $file"
  fi
done

if [ -n "$EXISTING_RUBY_FILES" ]; then
  echo "Checking Ruby files:"
  echo "$EXISTING_RUBY_FILES"

  RC=0
  if is_web_running; then
    $DOCKER_CMD exec -T web bundle exec rubocop --force-exclusion $EXISTING_RUBY_FILES || RC=$?
  elif [ -n "$DOCKER_CMD" ] && has_docker_compose; then
    echo "Container web is not running. Executing RuboCop via ephemeral container..."
    $DOCKER_CMD run --rm --no-deps -T web bundle exec rubocop --force-exclusion $EXISTING_RUBY_FILES || RC=$?
  elif has_bundle_on_host; then
    bundle exec rubocop --force-exclusion $EXISTING_RUBY_FILES || RC=$?
  else
    echo -e "${RED}❌ ERROR: Không tìm thấy môi trường Ruby/Bundler để chạy RuboCop!${NC}"
    echo -e "${YELLOW}Nguyên nhân:${NC}"
    echo "  - Container 'web' chưa chạy trong thư mục này."
    echo "  - Máy host không cài đặt Ruby/Bundler (dự án phát triển qua Docker)."
    echo -e "${YELLOW}Giải pháp:${NC}"
    echo "  1. Khởi động Docker container: docker compose up -d"
    echo "  2. Hoặc nếu muốn bỏ qua kiểm tra pre-push: git push --no-verify"
    STOP_NOTICE
    exit 1
  fi

  if [ $RC -ne 0 ]; then
    echo -e "${RED}❌ ERROR: RuboCop detected offenses in changed files.${NC}"
    STOP_NOTICE
    exit 1
  fi
  echo -e "${GREEN}✓ RuboCop Passed!${NC}"
else
  echo "No Ruby files modified."
fi
