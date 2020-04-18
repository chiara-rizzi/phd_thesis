BASIC_BUILD = pdflatex main.tex 
BUILD_GLOSSARY =  makeglossaries main
BUILD_BIBLIOGRAPHY = bibtex main
CLEAN =  rm -rf *.aux *.lof *.log *.lot *.toc *.bbl *.blg *~ *.out *.xml *blx.bib *.alg *.acr *.acn *.tex.bak *.gls *.glg *.ist *.glo */*.aux */*.lof */*.log */*.lot */*.toc */*.bbl */*.blg */*~ */*.out */*.xml */*blx.bib */*.alg */*.acr */*.acn */*.tex.bak */*.gls */*.glg */*.ist */*.glo


all: _base_ 
	echo "Done!"

_base_:
	@$(BASIC_BUILD) #&>/dev/null
	#@$(BUILD_BIBLIOGRAPHY)
	bibtex chap/Rizzi-Chap2
	bibtex chap/Rizzi-Chap3
	bibtex chap/Rizzi-Chap4
	bibtex chap/Rizzi-Chap5
	bibtex chap/Rizzi-Chap6
	bibtex chap/Rizzi-Chap7
	bibtex chap/Rizzi-Chap8
	bibtex chap/Rizzi-Chap9
	bibtex chap/Rizzi-Chap10
	bibtex chap/Rizzi-Chap11
	bibtex appendices/Rizzi-App4
	@$(BUILD_GLOSSARY)
	@$(BASIC_BUILD) #&>/dev/null
	@$(BASIC_BUILD) #&>/dev/null
	@$(CLEAN)

clean:
	@$(CLEAN)

clean_pdf: clean
	rm *.pdf

two:
	pdflatex two_page_summary.tex
	bibtex two_page_summary
	pdflatex two_page_summary.tex
	pdflatex two_page_summary.tex
