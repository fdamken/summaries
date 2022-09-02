all: clean preprocess collect compile


preprocess:
	for dir in $$(find . -mindepth 2 -type d -exec test -e {}/Makefile \; -print); do \
		cd "$$dir"; \
		make preprocess; \
		cd -; \
	done

collect:
	./collect.sh >tmp-collected.tex

compile:
	pdflatex all.tex
	pdflatex all.tex
	pdflatex all.tex
	pdflatex all.tex
	pdflatex all.tex

clean:
	# Clean aux files.
	find elective -name content.aux -delete
	find mandatory -name content.aux -delete
