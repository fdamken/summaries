#!/bin/bash

documents="$1"
if [[ "$documents" == "" ]]; then
    echo "E: Documents not passed. Usage: $0 <documents>" >&2
    exit 128
fi

set -o errexit
set -o nounset


# Extract the root repository directory from the location of this script.
root="$(dirname $(dirname $(readlink -f $0)))"


IFS="\n"
for line in $(echo "$documents" | jq -r '.[]'); do
    echo "Processing '$line'."

    department="$(echo "$line" | awk '{ print $1 }')"
    type="$(echo "$line" | awk '{ print $2 }')"
    category="$(echo "$line" | awk '{ print $3 }')"
    subject="$(echo "$line" | awk '{ print $4 }')"

    artifact_dir="$department $type $category $subject"
    artifact_pdf="$artifact_dir/$subject-summary.pdf"
    document_id="$department/$type/$category/$subject"
    document_dir="$root/summaries/$document_id"
    document_pdf="$document_dir/$subject-summary.pdf"

    if [[ ! -f "$artifact_pdf" ]]; then
        echo "E: Cannot find artifact file for $document_id. Something failed while downloading the artifacts!" >&2
        exit 128
    fi

    mv -v "$artifact_pdf" "$document_pdf"
    rm -rf "$artifact_dir"
done
