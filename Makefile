# Author: Emiliano Carlos de Moraes Firmino @ 10/2012
SHELL=/bin/sh
THESIS=main

.SUFFIXES:
.SUFFIXES: .bib .pdf .tex
.PHONY: clean

run: $(THESIS).pdf

$(THESIS).pdf: $(THESIS).bbl $(THESIS).tex
	pdflatex $(THESIS).tex 

$(THESIS).bbl: $(THESIS).aux
	pdflatex $(THESIS).tex -draftmode	
	bibtex $(THESIS)

$(THESIS).aux: $(THESIS).bib
	pdflatex $(THESIS).tex -draftmode
	pdflatex $(THESIS).tex 

clean_pdf:
	rm -rf *.aux *.lof *.log *.lot *.toc *.bbl *.blg *pdf

clean:
	rm -rf *.aux *.lof *.log *.lot *.toc *.bbl *.blg *~ *.out *.xml *blx.bib