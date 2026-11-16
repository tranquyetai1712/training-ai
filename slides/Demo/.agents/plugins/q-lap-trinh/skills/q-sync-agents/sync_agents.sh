#!/bin/bash

# ==============================================================================
# Script: sync_agents.sh
# Description: 3-way synchronization of AI Agents / Workflows between configuration directories:
#        1. /home/tranquyet/.gemini/agents
#        2. /home/tranquyet/.copilot/agents
#        3. /home/tranquyet/.gemini/antigravity/global_workflows
# How it works:
#   - Scan all .md and .sh files in the 3 directories.
#   - Find the latest modification time (mtime) for each file.
#   - Sync to the remaining directories if the file doesn't exist or content differs.
# ==============================================================================

# Define target directories
DIR1="/home/tranquyet/.gemini/agents"
DIR2="/home/tranquyet/.copilot/agents"
DIR3="/home/tranquyet/.gemini/antigravity/global_workflows"

# Ensure target directories exist
mkdir -p "$DIR1" "$DIR2" "$DIR3"

echo "=== START AGENTS & WORKFLOWS SYNCHRONIZATION ==="
echo "[1] $DIR1"
echo "[2] $DIR2"
echo "[3] $DIR3"

# Find all unique .md and .sh files across all 3 directories
ALL_FILES=$(find "$DIR1" "$DIR2" "$DIR3" -maxdepth 1 -type f \( -name "*.md" -o -name "*.sh" \) -exec basename {} \; 2>/dev/null | sort -u)

if [ -z "$ALL_FILES" ]; then
  echo "No agent or workflow files found to synchronize."
  exit 0
fi

sync_count=0

for file in $ALL_FILES; do
  max_mtime=0
  source_file=""
  
  f1="$DIR1/$file"
  f2="$DIR2/$file"
  f3="$DIR3/$file"
  
  # Find the file with the latest mtime
  if [ -f "$f1" ]; then
    t1=$(stat -c %Y "$f1")
    if [ "$t1" -gt "$max_mtime" ]; then
      max_mtime=$t1
      source_file=$f1
    fi
  fi
  
  if [ -f "$f2" ]; then
    t2=$(stat -c %Y "$f2")
    if [ "$t2" -gt "$max_mtime" ]; then
      max_mtime=$t2
      source_file=$f2
    fi
  fi
  
  if [ -f "$f3" ]; then
    t3=$(stat -c %Y "$f3")
    if [ "$t3" -gt "$max_mtime" ]; then
      max_mtime=$t3
      source_file=$f3
    fi
  fi
  
  # If source file is not determined (should not happen if find works)
  if [ -z "$source_file" ]; then
    continue
  fi
  
  # Perform synchronization to other directories
  for target_dir in "$DIR1" "$DIR2" "$DIR3"; do
    target_file="$target_dir/$file"
    
    # Skip if destination matches source
    if [ "$source_file" = "$target_file" ]; then
      continue
    fi
    
    # Copy if destination file does not exist OR content differs
    if [ ! -f "$target_file" ] || ! cmp -s "$source_file" "$target_file"; then
      echo "  -> Syncing: $file"
      echo "     From: $source_file"
      echo "     To: $target_file"
      
      cp -p "$source_file" "$target_file"
      sync_count=$((sync_count + 1))
    fi
  done
done

echo "=== SYNCHRONIZATION COMPLETE ==="
echo "Successfully updated/copied $sync_count files."
