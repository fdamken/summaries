#!/bin/bash

set -o errexit
set -o nounset


echo "\\newcommand{\lstbasepath}{unset}"
for content_tex in $(find mandatory elective -name 'content.tex' | sed 's/mandatory/1-mandatory/' | sed 's/elective/2-elective/' | sort); do
    content_tex="$(sed -r 's/(1-|2-)//' <<<"$content_tex")"
    dir="$(dirname "$content_tex")"
    metadata="$dir/metadata.txt"
    author="$(head -n 1 "$metadata" | tail -n 1)"
    title="$(head -n 2 "$metadata" | tail -n 1)"
    language="$(head -n 3 "$metadata" | tail -n 1 | sed -e 's/english/USenglish/' -e 's/german/ngerman/')"
    module="$(basename $(dirname "$content_tex"))"
    category="$(basename "$(dirname "$(dirname "$content_tex")" )" )"
    uber_category="$(basename "$(dirname "$(dirname "$(dirname "$content_tex")" )" )" )"
    content="$(echo "$content_tex" | sed 's/.tex//g')"

    echo "\\selectlanguage{$language}"
    echo "\\part{$title}"
    echo "\\graphicspath{{./$dir/}}"
    echo "\\renewcommand{\lstbasepath}{./$dir}"
    echo "\\include{$content}"
done
