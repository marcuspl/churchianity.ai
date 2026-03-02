# Polish Pass — Full Manuscript Sweep

**Date:** 2026-03-02
**Status:** Open — awaiting agent sweeps
**Version at start:** 1.0.7-draft

---

## Context

The merged manuscript is structurally complete and has been through one commentary cycle (see `commentary-instructions.md`). Since then, several editorial changes have been made:

- A new "Note on Authorship" was added between the Epigraph and Chapter 1
- The "Computational Method" section was removed from Chapter 1 (folded into the authorship note)
- The Personal Letter was cleaned up (grammar, reviewer notes restructured)
- Chapter 9 received a footnote clarification
- The title was updated to "Churchianity.ai — Three AIs Walk Into a Schism"

These changes improved the opening, but they were made by one agent (Claude Opus 4.6) under editorial direction. The full manuscript has not had a fresh read from all three agents since the merge. It's time.

---

## What This Is

Each agent reads the entire merged manuscript from start to finish — every file in `manuscript-merged/` that appears in the build (see `build/Makefile` CHAPTERS list). This is not a structural or analytical pass. It is a reader's pass: you are reading the book as a reader would, front to back, and noting everything that catches your eye.

---

## Scope

Four lenses, applied simultaneously as you read:

### 1. Polish
- Awkward phrasing, unclear sentences, grammatical errors
- Tonal inconsistencies (places where the voice shifts register without reason)
- Redundancies within and across chapters (we just caught a "map" repetition between the authorship note and Ch 1 — there may be more)
- Paragraphs that run too long or too short for their content

### 2. Flow
- Transitions between chapters: does the ending of one chapter set up the beginning of the next?
- Transitions within chapters: are there abrupt jumps, missing bridges, or sections that feel disconnected?
- Pacing: are there stretches that drag or sections that move too fast for their weight?
- Does the reading order feel natural? (Epigraph → Authorship Note → Ch 1 → ... → Personal Letter → Appendix)

### 3. Integrity
- Factual claims that need checking or qualifying
- Places where the symmetry rule is violated (one tradition critiqued without a corresponding self-critique elsewhere)
- Reviewer's Notes or Editorial Notes that are now outdated, redundant, or refer to content that has moved
- Internal contradictions (the book says X in one chapter and not-X in another)
- Citations or footnotes that are incomplete, incorrect, or missing

### 4. Missing Pieces
- Arguments that the book sets up but never delivers
- Promises made in early chapters ("Chapter 13 addresses this") that aren't fulfilled
- Topics the reader would reasonably expect to find but that are absent
- Emotional beats that the tone target demands but that the prose doesn't land

---

## Instructions for Each Agent

### Read the full manuscript in build order

The CHAPTERS list in `build/Makefile` gives the canonical reading order. Read every file, in order, cover to cover. Do not skip the front matter, back matter, or appendix.

### Write your report in your own file

Create a new file in `manuscript-merged/`:

- `process/polish.claude-opus-4.6.md`
- `process/polish.gemini-3.1-pro.md`
- `process/polish.gpt-5.2.md`

### Report format

For each finding, include:

- **File and location** (filename + quote a short phrase so we can find the spot)
- **Lens** (Polish / Flow / Integrity / Missing Piece)
- **Finding** (what you noticed)
- **Suggested fix** (if you have one — "flag only" is also fine)

Group findings by chapter for readability. A summary section at the end is welcome but not required.

### Calibration

- Be honest, not diplomatic. If something doesn't work, say so.
- Don't invent problems to fill a quota. If a chapter is clean, say "clean" and move on.
- Small things matter. A single awkward sentence can break the reader's trust.
- Big things matter more. If a whole section isn't earning its place, say that.
- You are not editing each other's reviewer notes — but you can flag if a note is outdated or no longer makes sense in context.

---

## Turn Order

Unlike the commentary pass, this one is **parallel, not sequential**. Each agent reads and reports independently, without seeing the others' files first. This is deliberate: we want three genuinely independent reads, not three reads where each agent anchors on the previous one's findings.

1. **Claude Opus 4.6** — writes `polish.claude-opus-4.6.md`
2. **Gemini 3.1 Pro** — writes `polish.gemini-3.1-pro.md`
3. **GPT 5.2** — writes `polish.gpt-5.2.md`

All three can begin immediately.

---

## What Happens After

1. Editor reviews all three polish reports
2. Convergence analysis: where did two or three agents flag the same issue? (These get priority.)
3. Editor decides which findings to action, and assigns execution (may be to any agent)
4. Changes are made to the merged manuscript
5. Version bump, rebuild, tag

---

## What This Is NOT

- This is not a rewrite pass. Do not rewrite sections in your report — just flag and suggest.
- This is not a second commentary pass. Do not propose new Reviewer's Note boxes.
- This is not a structural reorganization. If you think chapters should move, flag it, but the default is that structure stays.
- No changes to the manuscript itself during this pass. Reports only.

---

## File Locations

All process files live in `process/`, not in `manuscript-merged/` (which contains only the manuscript itself).

- `process/polish.claude-opus-4.6.md`
- `process/polish.gemini-3.1-pro.md`
- `process/polish.gpt-5.2.md`
- `process/polish-pass-instructions.md` (this file)

Previous commentary cycle files are also in `process/`:
- `process/commentary-instructions.md`
- `process/commentary.claude-opus-4.6.md`
- `process/commentary.gemini-3.1-pro.md`
- `process/commentary.gpt-5.2.md`
