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
index_files="$(find summaries -name '_index.md' -exec cp --parents {} "$publish_repo_dir/content" \;)"
cd - >/dev/null
echo "Copied $(echo "$index_files" | wc -l) index files."

echo "Copying document files."
mkdir -p "$publish_repo_dir/static/summaries-docs"
cd "$root"
documents="$(find summaries \( -name '*-summary.pdf' -o -name '*-summary-dark.pdf' \) -print -exec cp --parents {} "$publish_repo_dir/static" \; | sed -nr 's@^summaries/([^/]+)/([^/]+)/([^/]+)/([^/]+)/.+summary\.pdf$@\1 \2 \3 \4@g p')"
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
        meta_lang_code="$(echo "$meta_lang" | sed -r 's/^(..).*$/\1/')"

        if [[ -f "$document_dir/$subject-summary-dark.pdf" ]]; then
            text_dark="[![Download (Dark Mode)](/download-dark.png)]($subject-summary-dark.pdf)"
        else
            text_dark=""
        fi

        echo "Publishing $document_id."
        cat >"$publish_repo_dir/content/summaries/$document_id.md" <<EOF
---
title: "$meta_title"
draft: false
author: "$meta_author"
date: $(git log --pretty=tformat:'%as %s' | tail -n 1 | sed -r 's/^([^ ]+).*$/\1/g')
pdf: https://fabian.damken.net/summaries/$department/$type/$category/$subject/$subject-summary.pdf
language: $meta_lang_code
---

[![Download (Light Mode)](/download.png)]($subject-summary.pdf)
$text_dark

[![Buy Me a Coffee](/kofi.png)](https://ko-fi.com/fdamken)

## Recent Changes
$(git log --pretty=tformat:'%as %s' "$document_dir" | sed -r 's/^([^ ]+)/- `\1`/g')
EOF
    else
        echo "W: Cannot find metadata file for $document_id. Skipping." >&2
    fi
done <<<"$documents"

echo "Showing diff, committing changes, and pushing."
cd "$publish_repo_dir"
git diff
git add -A
git config user.name "Summary Auto-Publishing Action"
git config user.email "actions@github"
if git status | grep "nothing to commit" &>/dev/null; then
    echo "Nothing to commit; skipping commit."
else
    git commit -m "Automated summary publishing."
fi
git push
