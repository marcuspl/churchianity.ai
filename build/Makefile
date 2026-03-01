SHELL := /bin/bash

# ── Paths ──
ROOT      := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))/..
SRC       := $(ROOT)/manuscript-merged
BUILD     := $(ROOT)/build
DOCS      := $(ROOT)/docs
OUTPUT    := $(ROOT)/output
WEB       := $(BUILD)/web
LATEX     := $(BUILD)/latex

# ── Metadata (parsed from metadata.yaml) ──
VERSION   := $(shell grep '^version:' $(BUILD)/metadata.yaml | sed 's/version: *"*\([^"]*\)"*/\1/')
TITLE     := $(shell grep '^title:' $(BUILD)/metadata.yaml | sed 's/title: *"*\([^"]*\)"*/\1/')

# ── Source files in publication order ──
CHAPTERS  := \
	$(SRC)/00A_Epigraph.md \
	$(SRC)/01_Chapter_1.md \
	$(SRC)/02_Chapter_2.md \
	$(SRC)/03_Chapter_3.md \
	$(SRC)/04_Chapter_4.md \
	$(SRC)/05_Chapter_5.md \
	$(SRC)/06_Chapter_6.md \
	$(SRC)/06B_The_Fracture_Pattern.md \
	$(SRC)/06C_The_Great_Stumbling_Blocks.md \
	$(SRC)/07_Chapter_7.md \
	$(SRC)/08_Chapter_8.md \
	$(SRC)/09_Chapter_9.md \
	$(SRC)/10_Chapter_10.md \
	$(SRC)/11_Chapter_11.md \
	$(SRC)/12_Chapter_12.md \
	$(SRC)/13_Chapter_13.md \
	$(SRC)/14_Back_Matter.md \
	$(SRC)/appendix-d-knowledge-graphs.md

# ── Chapter metadata for web (filename → order, title, slug) ──
define CHAPTER_META
00A_Epigraph|1|Epigraph|epigraph
01_Chapter_1|2|Chapter 1: What This Book Is|chapter-1
02_Chapter_2|3|Chapter 2: One Church Becomes Two|chapter-2
03_Chapter_3|4|Chapter 3: The Orthodox World|chapter-3
04_Chapter_4|5|Chapter 4: The Catholic West|chapter-4
05_Chapter_5|6|Chapter 5: The Reformation|chapter-5
06_Chapter_6|7|Chapter 6: After the Reformation|chapter-6
06B_The_Fracture_Pattern|8|The Fracture Pattern|the-fracture-pattern
06C_The_Great_Stumbling_Blocks|9|The Great Stumbling Blocks|the-great-stumbling-blocks
07_Chapter_7|10|Chapter 7: Scripture|chapter-7
08_Chapter_8|11|Chapter 8: Sacraments|chapter-8
09_Chapter_9|12|Chapter 9: Authority|chapter-9
10_Chapter_10|13|Chapter 10: Mary and the Saints|chapter-10
11_Chapter_11|14|Chapter 11: Worship|chapter-11
12_Chapter_12|15|Chapter 12: The Vocabulary Problem|chapter-12
13_Chapter_13|16|Chapter 13: Where Do We Go From Here|chapter-13
14_Back_Matter|17|Afterword|afterword
appendix-d-knowledge-graphs|18|Appendix: Knowledge Graphs|appendix-knowledge-graphs
endef
export CHAPTER_META

# ── Targets ──
.PHONY: all web pdf clean bump-patch bump-minor

all: web pdf

# ── Web Pipeline ──
web: $(DOCS)/index.md $(DOCS)/_config.yml $(DOCS)/assets/style.css $(DOCS)/CNAME
	@echo "Web build complete → $(DOCS)/"
	@echo "Version: $(VERSION)"

$(DOCS)/_config.yml: $(WEB)/_config.yml $(BUILD)/metadata.yaml
	@mkdir -p $(DOCS)/_layouts $(DOCS)/assets $(DOCS)/_chapters
	cp $(WEB)/_config.yml $(DOCS)/_config.yml
	@# Inject version into config
	echo "" >> $(DOCS)/_config.yml
	echo "version: \"$(VERSION)\"" >> $(DOCS)/_config.yml
	cp $(WEB)/_layouts/default.html $(DOCS)/_layouts/default.html
	cp $(WEB)/_layouts/chapter.html $(DOCS)/_layouts/chapter.html

$(DOCS)/assets/style.css: $(WEB)/assets/style.css $(WEB)/assets/lightning-qr.png
	@mkdir -p $(DOCS)/assets
	cp $(WEB)/assets/style.css $(DOCS)/assets/style.css
	cp $(WEB)/assets/lightning-qr.png $(DOCS)/assets/lightning-qr.png
	cp $(WEB)/support.md $(DOCS)/support.md

$(DOCS)/CNAME:
	@mkdir -p $(DOCS)
	echo "churchianity.ai" > $(DOCS)/CNAME

$(DOCS)/index.md: $(BUILD)/metadata.yaml $(CHAPTERS)
	@mkdir -p $(DOCS)/_chapters
	@# Generate landing page
	@echo '---' > $(DOCS)/index.md
	@echo 'layout: default' >> $(DOCS)/index.md
	@echo 'title: Home' >> $(DOCS)/index.md
	@echo '---' >> $(DOCS)/index.md
	@echo '' >> $(DOCS)/index.md
	@echo '# Churchianity.ai' >> $(DOCS)/index.md
	@echo '' >> $(DOCS)/index.md
	@echo '*Continuity, Freedom, and the Places We Lost Each Other*' >> $(DOCS)/index.md
	@echo '' >> $(DOCS)/index.md
	@echo 'A map of Christian fractures, written by three AI agents under human editorial direction.' >> $(DOCS)/index.md
	@echo '' >> $(DOCS)/index.md
	@echo '---' >> $(DOCS)/index.md
	@echo '' >> $(DOCS)/index.md
	@echo '## Contents' >> $(DOCS)/index.md
	@echo '' >> $(DOCS)/index.md
	@# Generate chapter files with YAML front matter
	@echo "$$CHAPTER_META" | while IFS='|' read -r file order title slug; do \
		[ -z "$$file" ] && continue; \
		src="$(SRC)/$${file}.md"; \
		dest="$(DOCS)/_chapters/$${slug}.md"; \
		echo "  Processing: $$title"; \
		echo '---' > "$$dest"; \
		echo "title: \"$$title\"" >> "$$dest"; \
		echo "nav_title: \"$$title\"" >> "$$dest"; \
		echo "order: $$order" >> "$$dest"; \
		echo "slug: $$slug" >> "$$dest"; \
		echo '---' >> "$$dest"; \
		echo '' >> "$$dest"; \
		cat "$$src" >> "$$dest"; \
		echo "$$order. [$$title](/$$slug/)" >> $(DOCS)/index.md; \
	done
	@echo '' >> $(DOCS)/index.md
	@echo '---' >> $(DOCS)/index.md
	@echo '' >> $(DOCS)/index.md
	@echo "*Version $(VERSION)*" >> $(DOCS)/index.md

# ── PDF Pipeline ──
pdf: $(OUTPUT)/churchianity-ai-v$(VERSION).pdf
	@echo "PDF build complete → $<"

$(OUTPUT)/churchianity-ai-v$(VERSION).pdf: $(CHAPTERS) $(LATEX)/template.tex $(LATEX)/preamble.tex $(LATEX)/front-matter.tex $(BUILD)/metadata.yaml
	@mkdir -p $(OUTPUT)
	@# Write version file for LaTeX \input
	echo "$(VERSION)" > $(LATEX)/version.tex
	@# Concatenate all chapters, prefixing footnotes to avoid collisions
	@> /tmp/churchianity-combined.md
	@first=true; \
	for f in $(CHAPTERS); do \
		prefix=$$(basename "$$f" .md | tr -cd 'a-zA-Z0-9'); \
		if [ "$$first" = true ]; then \
			first=false; \
		else \
			echo -e '\n\\newpage\n' >> /tmp/churchianity-combined.md; \
		fi; \
		sed -e "s/\[\^\([^]]*\)\]/[^$${prefix}_\1]/g" "$$f" >> /tmp/churchianity-combined.md; \
		echo '' >> /tmp/churchianity-combined.md; \
	done
	@# Run pandoc → LaTeX → PDF
	cd $(LATEX) && pandoc \
		/tmp/churchianity-combined.md \
		--from=markdown+footnotes+pipe_tables+smart \
		--to=latex \
		--template=template.tex \
		--pdf-engine=lualatex \
		--top-level-division=chapter \
		-o $(OUTPUT)/churchianity-ai-v$(VERSION).pdf
	@rm -f /tmp/churchianity-combined.md
	@echo "Generated: churchianity-ai-v$(VERSION).pdf"

# ── Version Bumping ──
bump-patch:
	@current=$(VERSION); \
	major=$$(echo $$current | cut -d. -f1); \
	minor=$$(echo $$current | cut -d. -f2); \
	patch=$$(echo $$current | cut -d. -f3); \
	new="$$major.$$minor.$$((patch + 1))"; \
	sed -i "s/version: \"$$current\"/version: \"$$new\"/" $(BUILD)/metadata.yaml; \
	echo "Version bumped: $$current → $$new"

bump-minor:
	@current=$(VERSION); \
	major=$$(echo $$current | cut -d. -f1); \
	minor=$$(echo $$current | cut -d. -f2); \
	new="$$major.$$((minor + 1)).0"; \
	sed -i "s/version: \"$$current\"/version: \"$$new\"/" $(BUILD)/metadata.yaml; \
	echo "Version bumped: $$current → $$new"

# ── Clean ──
clean:
	rm -rf $(DOCS)
	rm -rf $(OUTPUT)
	rm -f $(LATEX)/version.tex
	@echo "Cleaned generated files."
