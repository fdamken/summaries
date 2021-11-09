#!/bin/bash

set -o errexit
set -o nounset

# Extract the root repository directory from the location of this script.
root="$(dirname $(dirname $(readlink -f $0)))"

publish_repo_dir="$root/gh-pages"
if [[ -e "$publish_repo_dir" ]]; then
    echo "E: Directory for gh-pages repo exists!" >&2
    exit 126
fi
mkdir "$publish_repo_dir"
git clone "https://$gh_user:$gh_token@github.com/fdamken/fdamken.github.io.git" "$publish_repo_dir"

echo "Copying index files."
cd "$root"
find summaries -name '_index.md' -exec cp --parents {} "$publish_repo_dir/content" \;
cd - >/dev/null

echo "Copying document files."
mkdir -p "$publish_repo_dir/static/summaries-docs"
cd "$root"
documents="$(find summaries -name '*-summary.pdf' -print -exec cp --parents {} "$publish_repo_dir/static" \; | sed -nr 's@^summaries/([^/]+)/([^/]+)/([^/]+)/([^/]+)/.+$@\1 \2 \3 \4@g p')"
cd - >/dev/null
echo "Copied $(echo "$documents" | wc -l) documents."

while IFS= read -r line; do
    department="$(echo "$line" | awk '{ print $1 }')"
    type="$(echo "$line" | awk '{ print $2 }')"
    category="$(echo "$line" | awk '{ print $3 }')"
    subject="$(echo "$line" | awk '{ print $4 }')"

    document_id="$department/$type/$category/$subject"
    document_dir="$root/summaries/$document_id"
    document_meta="$document_dir/metadata.txt"

    if [[ -f "$document_meta" ]]; then
        meta_author="$(cat "$document_meta" | head -n 1 | tail -n 1)"
        meta_title="$(cat "$document_meta" | head -n 2 | tail -n 1)"
        meta_lang="$(cat "$document_meta" | head -n 3 | tail -n 1 | sed 's/german/deutsch/')"
        meta_by="$(echo "$meta_lang" | sed -e 's/deutsch/von/' -e 's/english/by/')"

        echo "Publishing $document_id."
        cat >"$publish_repo_dir/content/summaries/$document_id.md" <<EOF
---
title: "$meta_title $meta_by $meta_author ($meta_lang)"
draft: false
---

[Download]($subject-summary.pdf)

[![Buy Me a Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20Me%20a%20Coffee&emoji=&slug=fdamken&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://www.buymeacoffee.com/fdamken)

## Recent Changes
$(git log --pretty=tformat:'%as %s' "$document_dir" | sed -r 's/^([^ ]+)/- `\1`/g')
EOF
    else
        echo "W: Cannot find metadata file for $document_id. Skipping." >&2
    fi
done <<<"$documents"

cd "$publish_repo_dir"
git push
cd -
