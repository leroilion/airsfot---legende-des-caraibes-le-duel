all: rules.pdf

rules.pdf: rules.tex pirategame.cls repartition.py
	python3 repartition.py
	pdflatex rules.tex
	rm rules.pdf
	pdflatex rules.tex

clean :
	rm -f *.aux *.log *.pdf *.toc *.out

.PHONY: all clean