#!/bin/bash

set -o errexit
set -o nounset

lang="$1"

content="$(tail -n +2 vocabulary.csv)"
if [[ "$lang" == "de" ]]; then
  content="$(echo "$content" | awk -F '|' '{ print $2" & "$1" \\\\" }')"
elif [[ "$lang" == "en" ]]; then
  content="$(echo "$content" | awk -F '|' '{ print $1" & "$2" \\\\" }')"
else
  echo "Unknown language: <$lang>." >&2
fi
content="$(echo "$content" | sort)"
echo "$content" >"tmp-vocabulary-$lang.tex"
