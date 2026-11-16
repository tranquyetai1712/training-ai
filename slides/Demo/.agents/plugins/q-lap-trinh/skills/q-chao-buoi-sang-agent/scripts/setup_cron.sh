#!/usr/bin/env bash
#
# Setup script to register the 5:00 AM daily greeting cron job in user's crontab.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEND_GREETING_SCRIPT="${SCRIPT_DIR}/send_greeting.sh"

# Grant execution permissions
chmod +x "${SEND_GREETING_SCRIPT}"
chmod +x "${SCRIPT_DIR}/setup_cron.sh"
chmod +x "${SCRIPT_DIR}/remove_cron.sh"

CRON_CMD="0 5 * * * ${SEND_GREETING_SCRIPT}"

# Check if entry already exists in crontab
CURRENT_CRONTAB=$(crontab -l 2>/dev/null || true)

if echo "${CURRENT_CRONTAB}" | grep -Fq "${SEND_GREETING_SCRIPT}"; then
    echo "[INFO] Daily greeting cron job already exists in crontab."
else
    # Append cron entry
    (echo "${CURRENT_CRONTAB}"; echo "${CRON_CMD}") | crontab -
    echo "[SUCCESS] Added daily greeting cron job (0 5 * * *) to crontab:"
    echo "  ${CRON_CMD}"
fi
