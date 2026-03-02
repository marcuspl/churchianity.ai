# Wave 3 — Icons, FAQ, and Publishing

**Date:** 2026-03-02
**Status:** Open — Stage 1 in progress
**Version at start:** 1.1.1-rc

---

## Focus

Three distinct investigations bundled into one wave because they are all pre-publication questions that should be resolved before the book goes wider. Each lens below is independent — agents should treat them as three mini-investigations within a single report.

## Scope

- **Lens 1:** `manuscript-merged/09_Chapter_9.md` primarily, plus any other chapters that touch on icons/statues/iconoclasm
- **Lens 2:** Full manuscript (agents need to read the whole book to anticipate reader questions)
- **Lens 3:** External research (web search, publishing industry knowledge)

## Lenses

### 1. Icons vs Statues — Translation Misunderstanding?

There is a popular claim that the East-West disagreement over icons and statues originates in a **translation misunderstanding** — specifically that the Acts of the Second Council of Nicaea (787) were poorly translated from Greek into Latin (the *Libri Carolini* episode), leading the Frankish West to misunderstand what the East was actually affirming about images.

**Investigate:**
- Is this claim historically accurate? What exactly was mistranslated, and how did it affect Western reception?
- Does the manuscript currently address this? (Chapter 9 covers icon theology extensively but may not address the translation angle.)
- If true, should we add it? Where would it fit — Chapter 9, a footnote, an appendix entry?
- How much weight should it carry? Is it a footnote-level curiosity or a load-bearing historical claim that changes the reader's understanding of the schism?

### 2. Pre-Emptive FAQ

The book will generate questions. Better to anticipate them than to be caught flat-footed.

**Investigate:**
- Read the full manuscript as a skeptical but fair-minded reader. What questions would you ask?
- Organize into categories (e.g., theological, historical, methodological, personal, "but what about...").
- For each question, note whether the manuscript already answers it (and where), partially answers it, or leaves it unaddressed.
- Flag any questions that suggest a gap in the manuscript itself (not just an FAQ entry, but something the book should have covered).
- Consider questions from different reader positions: Orthodox, Catholic, mainline Protestant, evangelical, non-denominational, skeptic/atheist, academic.

**Output format:** A structured FAQ draft, not just a list. Each entry should have the question, a brief proposed answer (2-4 sentences), and a note on whether the manuscript already covers it.

### 3. Licensing, Monetisation, and Self-Publishing

The book is currently shared freely at churchianity.ai with an optional Lightning donation. The editor wants to explore whether and how to also offer it for sale, without compromising the free-access principle.

**Investigate:**
- **Print-on-demand (POD):** What are the current options for single-copy, no-upfront-cost, drop-ship book printing? (Amazon KDP, IngramSpark, Lulu, Barnes & Noble Press, others?) What are the trade-offs (cost per copy, quality, distribution reach, ISBN requirements)?
- **E-book:** Kindle, Apple Books, Google Play Books, Kobo — what does listing require? Is there a way to list free or pay-what-you-want?
- **Dual model:** Can the book be freely available on the web while also sold in print/e-book form? Any platform restrictions on this?
- **Licensing:** The book is currently unlicensed (no explicit license). What license would best fit the goals: free to read, share, and quote, but the author retains the right to sell printed/e-book copies? Creative Commons options? Which variant?
- **Lightning/Bitcoin integration:** The current support model. Is this sufficient, or should it be supplemented?
- **What NOT to do:** Flag any common self-publishing mistakes relevant to this kind of project (religious/theological niche, AI-assisted authorship, free web version).

---

## Calibration

- **Lens 1:** Be historically precise. If the translation claim is overstated or more nuanced than popular accounts suggest, say so. We'd rather have a careful footnote than a confident paragraph that a historian would challenge.
- **Lens 2:** Be genuinely pre-emptive, not defensive. The FAQ should anticipate honest curiosity, not just hostile objections. Include the uncomfortable questions.
- **Lens 3:** Be practical and current. Pricing, platform policies, and POD quality change frequently — flag anything that might be outdated by the time of publication. No need to make recommendations, just lay out the landscape so the editor can decide.

---

## Pipeline Configuration

- **Stages:** 1-2-3 (skip Stages 4-5 — this wave produces research, not manuscript edits)
- **Stage 2 mode:** Sequential (default: Gemini → GPT → Claude)
- **Stage 2 order:** Gemini → GPT → Claude

---

## Agent Files

- `investigate.claude-opus-4.6.md`
- `investigate.gemini-3.1-pro.md`
- `investigate.gpt-5.2.md`

See `process/PIPELINE.md` for the full stage-by-stage pipeline and naming conventions.
