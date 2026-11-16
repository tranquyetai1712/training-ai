#!/usr/bin/env bash
HOOK_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$HOOK_DIR/lib/common.sh"

echo -e "${YELLOW}=== Step 5: HTML / ERB Tag Balance Verification ===${NC}"
TAG_IMBALANCE_FOUND=0
for erb_file in $(echo "$CHANGED_FILES" | grep '\.erb$' || true); do
  if [ -f "$erb_file" ]; then
    OPEN_ERB=$(grep -o '<%' "$erb_file" 2>/dev/null | wc -l | xargs)
    CLOSE_ERB=$(grep -o '%>' "$erb_file" 2>/dev/null | wc -l | xargs)
    if [ "$OPEN_ERB" -ne "$CLOSE_ERB" ]; then
      echo -e "${RED}❌ TAG IMBALANCE in ${erb_file}: Found ${OPEN_ERB} '<%' tags vs ${CLOSE_ERB} '%>' tags!${NC}"
      TAG_IMBALANCE_FOUND=1
    fi

    PERL_CHECK=$(perl -0777 -e '
      open my $fh, "<", "'"$erb_file"'" or exit 0;
      my $content = do { local $/; <$fh> };
      close $fh;

      my @tags = qw(div span form table script button a);
      for my $t (@tags) {
        my $open = () = $content =~ /<$t[\s>](?:[^>]*[^\/])?>/gi;
        my $close = () = $content =~ /<\/$t>/gi;
        if ($open != $close) {
          print "TAG_MISMATCH:$t:$open:$close\n";
        }
      }
    ' 2>/dev/null || true)

    if [ -n "$PERL_CHECK" ]; then
      while IFS= read -r line; do
        if [[ "$line" =~ ^TAG_MISMATCH:(.*):(.*):(.*)$ ]]; then
          t="${BASH_REMATCH[1]}"
          op="${BASH_REMATCH[2]}"
          cl="${BASH_REMATCH[3]}"
          echo -e "${RED}❌ TAG IMBALANCE in ${erb_file}: Found ${op} '<${t}>' vs ${cl} '</${t}>'!${NC}"
          TAG_IMBALANCE_FOUND=1
        fi
      done <<< "$PERL_CHECK"
    fi
  fi
done

if [ "$TAG_IMBALANCE_FOUND" -eq 1 ]; then
  echo -e "${RED}❌ ERROR: Unbalanced HTML/ERB tags detected in changed views.${NC}"
  STOP_NOTICE
  exit 1
else
  echo -e "${GREEN}✓ HTML / ERB Tag Balance Passed!${NC}"
fi
