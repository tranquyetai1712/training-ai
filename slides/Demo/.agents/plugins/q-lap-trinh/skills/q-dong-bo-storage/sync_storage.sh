#!/bin/bash

# ==============================================================================
# Script: sync_storage.sh
# Description: Synchronize storage folder across projects with the same prefix.
# Supports --delete / -d flag to delete destination files not present in source.
# ==============================================================================

CURRENT_DIR=$(pwd)
PROJECT_NAME=$(basename "$CURRENT_DIR")

# Extract prefix before _ or - character
PREFIX=$(echo "$PROJECT_NAME" | cut -d'_' -f1 | cut -d'-' -f1)

if [ -z "$PREFIX" ]; then
  echo "Could not determine the prefix of the current project ($PROJECT_NAME)."
  exit 1
fi

echo "Current project: $PROJECT_NAME (Prefix: $PREFIX)"

# Source storage directory
SRC_STORAGE_DIR="$CURRENT_DIR/storage"
if [ ! -d "$SRC_STORAGE_DIR" ]; then
  echo "Source directory storage does not exist."
  exit 1
fi

# Default behavior: do not delete destination files
DELETE_DEST=false

# Parse arguments
for arg in "$@"; do
  if [ "$arg" = "--delete" ] || [ "$arg" = "-d" ]; then
    DELETE_DEST=true
  fi
done

# Find other projects with the same prefix in /var/www/html
HTML_DIR="/var/www/html"
TARGET_PROJECTS=()

# Search all subdirectories in HTML_DIR and level 2 subdirectories
# containing storage or .git, and having project name prefix matching PREFIX
for dir in "$HTML_DIR"/* "$HTML_DIR"/*/*; do
  if [ -d "$dir" ]; then
    # Skip the current project
    REAL_DIR=$(realpath "$dir" 2>/dev/null)
    REAL_CURRENT=$(realpath "$CURRENT_DIR" 2>/dev/null)
    if [ "$REAL_DIR" = "$REAL_CURRENT" ]; then
      continue
    fi
    
    # Check if storage or .git exists
    if [ -d "$dir/storage" ] || [ -d "$dir/.git" ]; then
      DIR_NAME=$(basename "$dir")
      DIR_PREFIX=$(echo "$DIR_NAME" | cut -d'_' -f1 | cut -d'-' -f1)
      
      if [ "$DIR_PREFIX" = "$PREFIX" ]; then
        TARGET_PROJECTS+=("$REAL_DIR")
      fi
    fi
  fi
done

if [ ${#TARGET_PROJECTS[@]} -eq 0 ]; then
  echo "No other projects with prefix '$PREFIX' found for synchronization."
  exit 0
fi

# Remove duplicate elements if any
TARGET_PROJECTS=($(echo "${TARGET_PROJECTS[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))

echo "Target projects to be synchronized: ${TARGET_PROJECTS[*]}"

# Proceed to copy storage files
for target_proj in "${TARGET_PROJECTS[@]}"; do
  TARGET_STORAGE_DIR="$target_proj/storage"
  mkdir -p "$TARGET_STORAGE_DIR"
  
  # Recursively copy storage directory to target (excluding events directory)
  if command -v rsync >/dev/null 2>&1; then
    if [ "$DELETE_DEST" = true ]; then
      echo "Synchronizing with deletion (rsync --delete) to: $target_proj"
      rsync -av --delete --exclude="events" "$SRC_STORAGE_DIR/" "$TARGET_STORAGE_DIR/" >/dev/null
    else
      echo "Synchronizing without deletion (rsync) to: $target_proj"
      rsync -av --exclude="events" "$SRC_STORAGE_DIR/" "$TARGET_STORAGE_DIR/" >/dev/null
    fi
  else
    if [ "$DELETE_DEST" = true ]; then
      echo "Synchronizing with deletion (rm + cp) to: $target_proj"
      rm -rf "${TARGET_STORAGE_DIR:?}"/* 2>/dev/null
    else
      echo "Synchronizing without deletion (cp) to: $target_proj"
    fi
    # Copy items except 'events' directory
    for item in "$SRC_STORAGE_DIR"/*; do
      item_name=$(basename "$item")
      if [ "$item_name" != "events" ]; then
        cp -R "$item" "$TARGET_STORAGE_DIR/" 2>/dev/null
      fi
    done
  fi
  echo "Synchronized to: $target_proj"
done

echo "Synchronization complete!"
