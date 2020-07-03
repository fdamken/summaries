#!/bin/sed -rnf

# This script converts structures in Markdown to TeX structures (can be useful
# to blueprint a structure before writing TeX).
# The Markdown file has to be a list with [*+-] at the beginning indented with
# 4 spaces per level. Every file with {} at the end will be interpeted as a
# section. The content between { and } will be added as a comment after the
# section command. Hint: Putting a '&' at the end of any line will force that
# line to be added to the TeX document.
# A \todo{Content} will be placed in every section.

s/^( *)[\*+-] (.+) \{(.+)\}$/\1{\2} % \3\&/
s/^( {16,16})\{/\1\\paragraph\{/
s/^( {12,12})\{/\1\\subsubsection\{/
s/^( {8,8})\{/\1\\subsection\{/
s/^( {4,4})\{/\1\\section\{/
s/^\{/\\chapter\{/
s/^( *)(.+)\&$/\1\2\n\1    \\todo{Content}\n/p
