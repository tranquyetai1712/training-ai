#!/usr/bin/env bash
# Color definitions
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

STOP_NOTICE() {
  echo -e "${RED}------------------------------------------------------------------------${NC}"
  echo -e "${RED}🛑 CHÚ Ý DÀNH CHO AI AGENT: KHÔNG TỰ ĐỘNG FIX CODE HOẶC CHẠY LẠI PUSH!${NC}"
  echo -e "${RED}   Hãy dừng lại, thông báo chi tiết lỗi trên cho người dùng và chờ chỉ đạo.${NC}"
  echo -e "${RED}------------------------------------------------------------------------${NC}"
}

# Detect current git branch
BRANCH=$(git branch --show-current 2>/dev/null || echo "")

# Determine base branch
BASE_BRANCH="origin/main"
if ! git rev-parse --verify "$BASE_BRANCH" >/dev/null 2>&1; then
  BASE_BRANCH="origin/master"
fi

# Calculate modified files
CHANGED_FILES=$(git diff "$BASE_BRANCH"...HEAD --name-only 2>/dev/null || true)

# Docker Compose detection
DOCKER_CMD=""
if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
  DOCKER_CMD="docker compose"
elif command -v docker-compose >/dev/null 2>&1; then
  DOCKER_CMD="docker-compose"
fi

is_web_running() {
  if [ -n "$DOCKER_CMD" ]; then
    $DOCKER_CMD ps --services --filter "status=running" 2>/dev/null | grep -q "^web$"
  else
    return 1
  fi
}

has_docker_compose() {
  [ -f "docker-compose.yml" ] || [ -f "docker-compose.yaml" ]
}

has_bundle_on_host() {
  command -v bundle >/dev/null 2>&1
}
