#!/bin/bash

# Get the contributor name from the argument or default to the git config user.name
CONTRIBUTOR_NAME="${1:-$(git config --get user.name)}"

# Check if the contributor name is empty (i.e., no git config set)
if [ -z "$CONTRIBUTOR_NAME" ]; then
  echo "Error: Contributor name is not specified and no user.name is configured in Git."
  exit 1
fi

# Get commits by the contributor and format the output
git log --author="$CONTRIBUTOR_NAME" --pretty=format:"%h %s %ad" --date=short | while read commit; do 
  # Extract the commit date
  commit_date=$(echo $commit | sed -E 's/.* ([0-9]{4}-[0-9]{2}-[0-9]{2})$/\1/')
  
  # Get the "week starting" date in DD/MM/YYYY format
  week_start=$(date -d "$commit_date" +'%d/%m/%Y')
  
  # Output the commit hash, message, and week starting date
  echo "$commit week starting $week_start"
done
