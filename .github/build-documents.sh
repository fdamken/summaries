#!/bin/bash

set -o errexit
set -o nounset


# Extract the root repository directory from the location of this script.
root="$(dirname $(dirname $(readlink -f $0)))"

first_commit="4f56a06ecd6c7accc897ce58f9ca458a83de2e3a"  # This will never change.
latest_successful_commit="$(curl -s 'https://api.github.com/repos/fdamken/summaries/actions/runs' | jq -r "
    .workflow_runs
        | map(select(.status == \"completed\" and .conclusion == \"success\"))
        | .[0].head_commit.id
        | if . == null then \"$first_commit\" else . end
")"

echo "Searching documents changed since commit $latest_successful_commit."

#files="$(find . -type f | sed 's@^./@@g')"
files="$(git diff --name-only "$latest_successful_commit")"
documents="$(echo "$files" | sed -nr 's@^summaries/([^/]+)/([^/]+)/([^/]+)/([^/]+)/.+$@\1 \2 \3 \4@g p' | sort | uniq)"
if [[ "$documents" == "" ]]; then
    echo "No changed documents found."
    exit 0
fi

echo "Found $(echo "$documents" | wc -l) changed documents."

while IFS= read -r line; do
    department="$(echo "$line" | awk '{ print $1 }')"
    type="$(echo "$line" | awk '{ print $2 }')"
    category="$(echo "$line" | awk '{ print $3 }')"
    subject="$(echo "$line" | awk '{ print $4 }')"

    document_id="$department/$type/$category/$subject"
    document_dir="$root/summaries/$document_id"
    document_tex="$document_dir/$subject-summary.tex"

    echo "Building $document_id"

    echo "Checking if TeX file exists."
    if [[ -f "$document_tex" ]]; then
        echo "Starting build."
        cd "$document_dir"
        echo "Copying fdsummary class and tuda_logo."
        cp -r "$root/sys/tuda_logo.pdf" "$root/pkg/"* .
        "$root/bin/compile-summary"
        cd -
    else
        echo "W: Cannot find TeX file for $document_id. Skipping." >&2
    fi
done <<<"$documents"
