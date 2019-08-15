all: vocabulary pdf

vocabulary:
	./vocabulary.sh de
	./vocabulary.sh en

pdf:
	pdflatex se0-cheatsheet.tex
	pdflatex se0-cheatsheet.tex
	pdflatex se0-cheatsheet.tex
