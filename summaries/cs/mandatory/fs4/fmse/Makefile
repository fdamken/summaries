clean:
	find . -type f -name 'tmp-*' -delete

all: clean code
	pdflatex fms-cheatsheet.tex
	pdflatex fms-cheatsheet.tex
	pdflatex fms-cheatsheet.tex
	pdflatex fms-cheatsheet.tex
	pdflatex fms-cheatsheet.tex


graphs:
	dot -T pdf promela-interference.dot -o tmp-promela-interference.pdf
	dot -T pdf promela-computations.dot -o tmp-promela-computations.pdf
	dot -T pdf promela-interleavings.dot -o tmp-promela-interleavings.pdf


code_clean:
	rm -f pan*
	find code -type f -name '*.out' -delete

code: code_clean
	./spin.sh code/promela/hello-world.pml
	./spin.sh code/promela/selection.pml -v
	./spin.sh code/promela/repetition.pml -p -l
	./spin.sh code/promela/jumps.pml
	./spin.sh code/promela/multiple-processes.pml
	./spin.sh code/promela/client-server.pml
