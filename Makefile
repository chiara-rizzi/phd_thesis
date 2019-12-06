BASIC_BUILD = pdflatex main.tex 
BUILD_GLOSSARY =  makeglossaries main
BUILD_BIBLIOGRAPHY = bibtex main
CLEAN =  rm -rf *.aux *.lof *.log *.lot *.toc *.bbl *.blg *~ *.out *.xml *blx.bib *.alg *.acr *.acn *.tex.bak *.gls *.glg *.ist *.glo


all: _base_ 
	echo "Done!"

_base_:
	@$(BASIC_BUILD) #&>/dev/null
	#@$(BUILD_BIBLIOGRAPHY)
	bibtex chap/theory
	bibtex chap/lhc
	bibtex chap/mc_simul
	bibtex chap/trig_obj 
	bibtex chap/stat
	bibtex chap/susy_general
	bibtex chap/strong_prod
	bibtex chap/ewk_prod
	bibtex chap/summary_susy
	bibtex chap/concl
	bibtex appendices/pmt_response	
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
