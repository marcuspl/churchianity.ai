# Wave 3 — Synthesis

**Date:** 2026-03-02
**Editor decisions on:** Licensing, Icons, Reading List

---

## Decision 1: Apply CC BY-NC-SA 4.0

All three agents converged on Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International as the correct licence for this project. Editor confirmed.

### What this means

- **BY (Attribution):** Anyone sharing or adapting the work must credit the author.
- **NC (NonCommercial):** Third parties may not sell copies or use the work commercially. The author retains all commercial rights (print sales, ebook sales, etc.).
- **SA (ShareAlike):** Derivative works must carry the same licence.

The licence governs what *others* may do. As the copyright holder, Marcus retains the right to sell print and ebook editions, licence translations, or grant commercial permissions.

### What was changed

1. **PDF copyright page** (`build/latex/front-matter.tex`): Replaced "All rights reserved" with the CC BY-NC-SA 4.0 notice and URL.
2. **Web footer** (`build/web/_layouts/default.html`): Added "CC BY-NC-SA 4.0" link in the site footer on all pages.
3. **Web support page** (`build/web/support.md`): Added a "License" section with the full human-readable notice.

### Deferred

- **Pastoral exception** (churches printing at cost): NC is sufficient for now. A clarifying permission statement can be added later if needed.

---

## Decision 2: Add Libri Carolini Paragraph to Chapter 9

All three agents converged: the *Libri Carolini* translation episode should be added to the icons section of Chapter 9. It reinforces the book's recurring thesis that vocabulary divergence drives institutional division (the same pattern as the Chalcedonian split in Chapter 3).

### What was changed

**`manuscript-merged/09_Chapter_9.md`** — inserted a new paragraph after the icon theology section and before the "Protestant reader" paragraph. The addition:

- Describes the translation failure: Greek *proskynesis* collapsed into Latin *adoratio*
- Names the *Libri Carolini* and the Council of Frankfurt (794) as the Frankish response
- Notes the translation failure was real but not the whole story (genuine theological difference + Carolingian political rivalry)
- Explicitly links back to Chapter 3: "The Chalcedonian split and the Carolingian icon dispute are the same mechanism, centuries apart"
- Added footnote [^11] citing Noble (2009) and Freeman's critical edition (1998)

### Calibration

Per GPT's caution: the paragraph does **not** frame the episode as explaining the icon-vs-statue aesthetic divergence (which is a longer, multi-factor trajectory). It frames it as a mistranslation that intensified hostility — consistent with the book's pattern-recognition approach.

---

## Decision 3: Fix Reading List Gender Gap

All agents who examined the reading list noted the absence of women authors — an unforced error that undermines the book's representational fairness claim. Teresa of Ávila, Julian of Norwich, and Dorothy Day all appear in the manuscript text but were missing from Appendix B.

### What was changed

**`manuscript-merged/14_Back_Matter.md`** — added three women authors:

- **Catholic section:** *Interior Castle* by Teresa of Ávila — "The great mystic's map of the soul's journey toward God."
- **Cross-Tradition section:** *Revelations of Divine Love* by Julian of Norwich — "The first book written in English by a woman."
- **Cross-Tradition section:** *The Long Loneliness* by Dorothy Day — "A convert's memoir that fuses Catholic faith with radical social witness."

---

## Deferred Items

### Publishing (Lens 3 — research complete, execution deferred)
- **Print-on-demand setup** (KDP + IngramSpark): Research in Stage 1 reports. Awaiting editor decision to proceed. **Do NOT enrol in KDP Select / Kindle Unlimited** — it requires 90-day digital exclusivity and would legally require taking down the free web version at churchianity.ai.
- **ISBN purchase** ($125–295 from Bowker) and **copyright registration** ($65–85 via USCO): Recommended before print publication.
- **Cover design**: All agents flagged as necessary. Budget $200–500. Not yet commissioned.
- **IngramSpark AI policy**: Contact before committing — they may reject AI-generated content.
- **Free ebook listings** (Apple Books, Google Play, Kobo) + Amazon price-match strategy.

### FAQ (Lens 2 — drafts complete, format/location deferred)
- All three agents produced FAQ drafts (22–28 entries). Convergence on core questions is high.
- **Open question:** Where does the FAQ live? Options: new appendix, web-only page, or both.
- **Open question:** How many entries to include? The merged set would be ~25 after deduplication.
- Strongest convergence categories: AI methodology, symmetry-as-theology, "all traditions equally right?", practical visitor guidance.

### Manuscript gaps flagged but not actioned
- **Palamism / essence-energies distinction**: Under-treated for Orthodox readers. Potential addition to Chapter 6 or 9.
- **Vatican II**: Under-treated for Catholic readers. Potential addition to Chapter 5 or 6.
- **Penal substitutionary atonement**: Unnamed in the forensic/therapeutic section. A parenthetical in Chapter 6C could address this.
- **Oriental Orthodox, Anglicans, Global South**: Scope limitations acknowledged in the manuscript but could be stated more explicitly.

---

## Build Verification

Clean rebuild passes — both web and PDF output generated successfully at v1.1.1-rc.
