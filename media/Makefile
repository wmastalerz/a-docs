# Define variables
SPHINXOPTS    := -W
SPHINXBUILD   := sphinx-build
SOURCEDIR     := source
BUILDDIR      := build

# Define pattern rule for building HTML files
$(BUILDDIR)/docx/%.html: $(SOURCEDIR)/%.rst
	$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)/html" $(SPHINXOPTS)

# Define pattern rule for building PDF files
$(BUILDDIR)/docx/%.pdf: $(SOURCEDIR)/%.rst
	$(SPHINXBUILD) -M latex "$(SOURCEDIR)" "$(BUILDDIR)/latex" $(SPHINXOPTS)
	cd $(BUILDDIR)/latex && make

# Define targets
.PHONY: all clean html pdf

all: html pdf

html: $(patsubst $(SOURCEDIR)/%.rst,$(BUILDDIR)/html/%.html,$(wildcard $(SOURCEDIR)/*.rst))

pdf: $(patsubst $(SOURCEDIR)/%.rst,$(BUILDDIR)/latex/%.pdf,$(wildcard $(SOURCEDIR)/*.rst))

clean:
	rm -rf $(BUILDDIR)/*
