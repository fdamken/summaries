preprocess:
	rm -f tmp-*.pdf tmp-*.pgf tmp-*.txt
	python genData.py
	python optimization.py
	python nonParametricModels.py
	python mixtureModels.py
	python clustering.py
	python regression.py
	python classification.py
	python pca.py
	python svm.py
	zip tmp-code.zip genData.py optimization.py nonParametricModels.py mixtureModels.py clustering.py regression.py classification.py pca.py svm.py
