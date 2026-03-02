# Wave 4 — Synthesis

**Date:** 2026-03-02
**Editor decisions on:** FAQ (placement + content), Cover (deferred to commissioning)

---

## Decision 1: FAQ — Written and Placed

All three agents converged on structure, placement, and core questions. The FAQ is now written in two forms.

### What was created

1. **Web FAQ** (`build/web/faq.md`) — 34 entries across 8 categories. Full version, linkable, updatable as reader questions come in. Added to site footer alongside Support link. Available at churchianity.ai/faq.

2. **Print appendix** (`manuscript-merged/appendix-f-faq.md`) — 15 entries, condensed. Points readers to the web FAQ for the full list. Added to the build pipeline as Appendix F (order 22, after Editorial Process Notes).

### Category structure (adopted from GPT, confirmed by all three)

A. What is this book doing? (framing & intent)
B. What happened historically? (macro story)
C. Theological questions
D. Stumbling blocks (visceral reactions)
E. Safety, trauma, and coercion
F. Method and AI
G. "But what about...?" (scope limitations)
H. Practical questions

### Design principles

- Answers are 2-4 sentences, in the book's voice (relief, not defensiveness)
- Chapter cross-references throughout (readers can go deeper)
- Scope limitations acknowledged honestly, not defended
- Practical visitor guidance (Q31) fills a gap the on-ramps chapter didn't cover
- Web FAQ includes entries the print version omits for space (PSA, editor's role, colonialism, Anglicanism)

### Build changes

- `build/Makefile`: added `appendix-f-faq.md` to CHAPTERS list and CHAPTER_META (order 22)
- `build/Makefile`: added `faq.md` copy step to web build
- `build/web/_layouts/default.html`: added FAQ link to site footer
- `build/web/faq.md`: new web page

---

## Decision 2: Cover — Research Complete, Commissioning Deferred

All three agents produced cover concepts and specs. The research is complete and a designer brief is ready.

### Convergence

- **Specs:** 6" x 9" trim, ~200pp cream paper, spine ~0.50", CMYK, 300 DPI, single wraparound PDF
- **Genre positioning:** must signal "serious theology" and "computational experiment" simultaneously
- **Two traps to avoid** (Gemini's framing): Too Academic (seminary textbook) vs Too Christian Living (devotional paperback)
- **Budget:** $200-500. Fiverr Pro or Behance direct hire recommended.

### Recommended concepts (for the designer brief)

**Primary — "The Terminal and the Cathedral" (Claude):** Typography-only. Title in monospace/terminal font, subtitle in traditional serif. Dark background (near-black or deep navy), title in warm gold or cream. No imagery. Cheapest, fastest, most distinctive at thumbnail size.

**Alternative — "Council Minutes / Code Diff" (GPT):** Layered typographic textures — faint council-like marginalia with subtle diff marks. Serif + monospace accent. Parchment/near-black palette. More original but needs the right designer.

### What was deferred

- Commissioning the designer (editor to choose service and concept)
- Back cover copy (needs to be written)
- Final page count confirmation (affects spine width calculation)
- ISBN (required before barcode placement)

### Designer brief location

Full ready-to-send brief is in `process/wave-4-faq-cover/investigate.claude-opus-4.6.md` (Lens 2 section).

---

## Manuscript gaps flagged (deferred to future wave)

All three agents independently flagged these as gaps the FAQ surfaces but cannot solve:

1. **Palamism / essence-energies distinction** — needs a dedicated paragraph (Chapter 6 or 9)
2. **Vatican II** — needs a short section on its significance for modern Catholic life
3. **Penal substitutionary atonement** — unnamed in the forensic/therapeutic section; a parenthetical would help
4. **Oriental Orthodox continuity** — one or two later mentions would reduce the "they vanish" feeling
5. **Anglican via media** — a short "mixed grammar" callout would prevent avoidable reader frustration
6. **Global South / colonial modernity** — at minimum, a more explicit "this map is Western-structured" note

---

## Build Verification

Clean rebuild required to pick up all changes.
