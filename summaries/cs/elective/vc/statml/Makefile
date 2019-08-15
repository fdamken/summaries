all:
	rm -f tmp-*.pdf tmp-*.pgf tmp-*.txt
	python3 genData.py
	python3 optimization.py
	python3 nonParametricModels.py
	python3 mixtureModels.py
	python3 clustering.py
	python3 regression.py
	python3 classification.py
	python3 pca.py
	python3 svm.py
	zip tmp-code.zip genData.py optimization.py nonParametricModels.py mixtureModels.py clustering.py regression.py classification.py pca.py svm.py
	pdflatex -shell-escape sml-cheatsheet.tex
	pdflatex -shell-escape sml-cheatsheet.tex
	pdflatex -shell-escape sml-cheatsheet.tex
	pdflatex -shell-escape sml-cheatsheet.tex
	pdflatex -shell-escape sml-cheatsheet.tex
