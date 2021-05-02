%.pdf:
	pdflatex $*.tex

paper.pdf:
	rm -rf ./pythontex-files-paper
	pdflatex -interaction=nonstopmode paper.tex
	./build.sh ./paper.tex
	pdflatex -interaction=nonstopmode paper.tex

images:
	../analysis/analyze.py 1 True
	../analysis/analyze.py 2 True
	../analysis/analyze.py 5 True

.PHONY: images

%.docx:
	pandoc -o $*.docx $*.tex

PDFTARGETS=paper.pdf

WORDTARGETS=paper.docx

TARGETS=$(PDFTARGETS)

pdf: $(PDFTARGETS) junk

docx: $(WORDTARGETS)

all: $(TARGETS)

clean: junk
	rm -rf $(TARGETS)
	rm -rf paper.pytxcode
	rm -rf ./pythontex-files-paper

junk:
	rm -rf *.aux *.log *.out
	
.PHONY: pdf docx all clean junk
