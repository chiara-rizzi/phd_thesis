BASIC_BUILD = pdflatex main.tex 
BUILD_GLOSSARY =  makeglossaries main
BUILD_BIBLIOGRAPHY = bibtex main
CLEAN =  rm -rf *.aux *.lof *.log *.lot *.toc *.bbl *.blg *~ *.out *.xml *blx.bib *.alg *.acr *.acn *.tex.bak *.gls *.glg *.ist *.glo


all: _base_ 
	echo "Done!"

_base_:
	@$(BASIC_BUILD) #&>/dev/null
	@$(BUILD_BIBLIOGRAPHY)
	@$(BUILD_GLOSSARY)
	@$(BASIC_BUILD) #&>/dev/null
	@$(BASIC_BUILD) #&>/dev/null
	@$(CLEAN)

clean:
	@$(CLEAN)

clean_pdf: clean
	rm *.pdf

