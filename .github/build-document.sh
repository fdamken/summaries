#!/bin/bash

department="$1"
type="$2"
category="$3"
subject="$4"
if [[ "$department" == "" ]] || [[ "$type" == "" ]] || [[ "$category" == "" ]] || [[ "$subject" == "" ]]; then
    echo "E: Invalid arguments. Usage: $0 <department> <type> <category> <subject>" >&2
    exit 128
fi

set -o errexit
set -o nounset


# Extract the root repository directory from the location of this script.
root="$(dirname $(dirname $(readlink -f $0)))"


document_id="$department/$type/$category/$subject"
document_dir="$root/summaries/$document_id"
document_tex="$document_dir/$subject-summary.tex"
document_pdf="$document_dir/$subject-summary.pdf"

echo "Building $document_id"

echo "Checking if TeX file exists."
if [[ ! -f "$document_tex" ]]; then
    echo "E: Cannot find TeX file for $document_id. Skipping." >&2
    exit 128
fi

echo "Starting build."
cd "$document_dir"
echo "Copying fdsummary class and tuda_logo."
cp -r "$root/sys/tuda_logo.pdf" "$root/pkg/"* .
"$root/bin/compile-summary"

if [[ ! -f "$document_pdf" ]]; then
    echo "E: Cannot find PDF file for $document_id. Something failed during compilation!" >&2
    exit 128
fi
echo "artifact_path=$document_pdf" >>$GITHUB_OUTPUT
