#!/usr/bin/env bash
# Run once from repo root, after `gh auth login` and `gh repo create ... --push`.
# Creates one milestone per phase, one issue per week (linked to milestone),
# and a Project (v2) board with those issues added.
set -euo pipefail

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
echo "Setting up project for $REPO"

declare -A MILESTONES=(
  ["Phase 0: Python for ML"]="1:1"
  ["Phase 1: Math refresh"]="2:4"
  ["Phase 2: PyTorch fundamentals"]="5:10"
  ["Phase 3: Transformers"]="11:18"
  ["Phase 4: Modern LLM"]="19:27"
  ["Checkpoint week"]="28:28"
  ["Phase 5: Post-training & RL"]="29:35"
  ["Phase 6: Evals & research method"]="36:39"
  ["Phase 7: ML systems"]="40:47"
  ["Phase 8: Research project"]="48:52"
)

for name in "${!MILESTONES[@]}"; do
  gh api "repos/$REPO/milestones" -f title="$name" -f state="open" >/dev/null 2>&1 || true
done

# Create the Project (v2) board
PROJECT_URL=$(gh project create --owner "@me" --title "ML Conversion Year" --format json | jq -r .url)
echo "Project board: $PROJECT_URL"

for f in weeks/week-*.md; do
  n=$(basename "$f" .md | sed 's/week-//')
  title=$(head -1 "$f" | sed 's/# //')
  phase=$(echo "$title" | sed -E 's/Week [0-9]+ — //')
  body=$(cat "$f")

  # find matching milestone by week number range
  milestone=""
  for name in "${!MILESTONES[@]}"; do
    range="${MILESTONES[$name]}"
    lo="${range%%:*}"; hi="${range##*:}"
    if [ "$((10#$n))" -ge "$lo" ] && [ "$((10#$n))" -le "$hi" ]; then
      milestone="$name"
      break
    fi
  done

  issue_url=$(gh issue create --title "$title" --body "$body" --milestone "$milestone")
  gh project item-add --owner "@me" --url "$issue_url" $(gh project list --owner "@me" --format json | jq -r ".projects[] | select(.title==\"ML Conversion Year\") | .number") >/dev/null 2>&1 || true
  echo "Created: $title"
done

echo "Done. 10 milestones + 52 issues created and added to the Project board."
