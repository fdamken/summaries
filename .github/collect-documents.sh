#!/bin/bash

scope="$1"
if [[ "$scope" != all ]] && [[ "$scope" != changed ]]; then
    echo "E: Scope '$scope' is neither 'all' nor 'changed'. Usage: $0 <scope:all|changed>" >&2
    exit 128
fi

set -o errexit
set -o nounset


if [[ "$scope" == "changed" ]]; then
    first_commit="4f56a06ecd6c7accc897ce58f9ca458a83de2e3a"  # This will never change.
    latest_successful_commit="$(curl -s 'https://api.github.com/repos/fdamken/summaries/actions/runs' | jq -r "
        .workflow_runs
            | map(select(.status == \"completed\" and .conclusion == \"success\"))
            | .[0].head_commit.id
            | if . == null then \"$first_commit\" else . end
    ")"
    set +o errexit
    files="$(git diff --name-only "$latest_successful_commit")"
    exit_code="$?"
    set -o errexit
    if [[ $exit_code -ne 0 ]]; then
        scope="all"
    fi
fi
if [[ "$scope" == "all" ]]; then
    files="$(find . -type f | sed 's@^./@@g')"
fi

# Extract documents from the found files.
documents="$(echo "$files" | sed -nr 's@^summaries/([^/]+)/([^/]+)/([^/]+)/([^/]+)/.+tex$@\1 \2 \3 \4@g p' | sort | uniq)"

# And output the JSON array for GitHub to parse.
echo "documents={\"document\": $(echo "$documents" | paste -sd "," | jq -R 'split(",") | .[] |= tostring')}" | jq -cM
