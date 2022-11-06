#!/bin/bash

scope="$1"
if [[ "$scope" != all ]] && [[ "$scope" != changed ]]; then
    echo "E: Scope '$scope' is neither 'all' nor 'changed'. Usage: $0 <scope:all|changed>" >&2
    exit 128
fi

set -o errexit
set -o nounset


if [[ "$scope" == "changed" ]]; then
    echo "Collecting changed documents."
    first_commit="4f56a06ecd6c7accc897ce58f9ca458a83de2e3a"  # This will never change.
    latest_successful_commit="$(curl -s 'https://api.github.com/repos/fdamken/summaries/actions/runs' | jq -r "
        .workflow_runs
            | map(select(.status == \"completed\" and .conclusion == \"success\"))
            | .[0].head_commit.id
            | if . == null then \"$first_commit\" else . end
    ")"
    echo "Searching documents that changed since commit $latest_successful_commit."
    set +o errexit
    files="$(git diff --name-only "$latest_successful_commit")"
    exit_code="$?"
    set -o errexit
    if [[ $exit_code -ne 0 ]]; then
        echo "Collecting changed documents failed. Falling back to collecting all documents."
        scope="all"
    fi
fi
if [[ "$scope" == "all" ]]; then
    echo "Collecting all documents."
    files="$(find . -type f | sed 's@^./@@g')"
fi

# Extract documents from the found files.
documents="$(echo "$files" | sed -nr 's@^summaries/([^/]+)/([^/]+)/([^/]+)/([^/]+)/.+tex$@\1 \2 \3 \4@g p' | sort | uniq | head -n 2)"

# And output the JSON array for GitHub to parse.
echo "documents=$(echo "$documents" | paste -sd "," | jq -R 'split(",") | .[] |= tostring' | jq -cM)" >>$GITHUB_OUTPUT
