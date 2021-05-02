%.pdf:
	pandoc -t beamer -o $*.pdf $*.md

PDFTARGETS=presentation.pdf

WORDTARGETS=presentation.docx

# put presentation.docx into targets if necessary.

TARGETS=$(PDFTARGETS)

all: $(TARGETS)
	
clean:
	rm -rf $(TARGETS)
