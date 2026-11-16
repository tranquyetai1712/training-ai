#!/usr/bin/env bash
#
# Script to remove the 5:00 AM daily greeting cron job from user's crontab.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SEND_GREETING_SCRIPT="${SCRIPT_DIR}/send_greeting.sh"

CURRENT_CRONTAB=$(crontab -l 2>/dev/null || true)

if echo "${CURRENT_CRONTAB}" | grep -Fq "${SEND_GREETING_SCRIPT}"; then
    # Remove lines containing send_greeting.sh
    NEW_CRONTAB=$(echo "${CURRENT_CRONTAB}" | grep -Fv "${SEND_GREETING_SCRIPT}" || true)
    echo "${NEW_CRONTAB}" | crontab -
    echo "[SUCCESS] Removed daily greeting cron job from crontab."
else
    echo "[INFO] No daily greeting cron job found in crontab."
fi
