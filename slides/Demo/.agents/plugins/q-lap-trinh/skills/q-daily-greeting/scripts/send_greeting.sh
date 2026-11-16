#!/usr/bin/env bash
#
# Daily Greeting Script for Antigravity Agent
# This script is executed daily at 5:00 AM via crontab.
# It sends a greeting prompt to the Antigravity agent CLI (`agy`), logs the output,
# and displays a Desktop Notification if available.

set -euo pipefail

# Define variables
AGY_BIN="/home/tranquyet/.local/bin/agy"
LOG_DIR="${HOME}/.gemini/antigravity/logs"
LOG_FILE="${LOG_DIR}/daily_greeting.log"
PROMPT="Xin chào buổi sáng bạn có khỏe không, hôm nay bạn có hỗ trợ được tôi xử lý code không ?"

# Ensure log directory exists
mkdir -p "${LOG_DIR}"

# Prepare timestamp header for log
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

echo "==========================================" >> "${LOG_FILE}"
echo "[${TIMESTAMP}] Sending daily greeting to Antigravity agent..." >> "${LOG_FILE}"
echo "Prompt: ${PROMPT}" >> "${LOG_FILE}"
echo "------------------------------------------" >> "${LOG_FILE}"

# Execute agy CLI and append output to log file
if [ -x "${AGY_BIN}" ]; then
    RESPONSE=$("${AGY_BIN}" --print "${PROMPT}" 2>&1 || true)
    echo "${RESPONSE}" >> "${LOG_FILE}"
    echo "==========================================" >> "${LOG_FILE}"
    echo "" >> "${LOG_FILE}"

    # Send Desktop Notification if notify-send is available
    if command -v notify-send >/dev/null 2>&1; then
        # Truncate response for notification display if too long
        SHORT_RESPONSE=$(echo "${RESPONSE}" | head -n 5)
        notify-send -u normal -i dialog-information "Antigravity Daily Greeting" "${SHORT_RESPONSE}" || true
    fi
else
    echo "ERROR: ${AGY_BIN} not found or not executable." >> "${LOG_FILE}"
fi
