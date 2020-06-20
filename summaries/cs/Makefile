all: clean collect compile


collect:
	./collect.sh >tmp-collected.tex


compile:
	lualatex all.tex
	lualatex all.tex
	lualatex all.tex
	lualatex all.tex
	lualatex all.tex


clean:
	# Clean aux files.
	find elective -name content.aux -delete
	find mandatory -name content.aux -delete
