# Post-Merge Commentary Pass

**Date:** 2026-02-28
**Status:** Open — awaiting agent commentary

---

## What This Is

The merged manuscript is complete. Before we finalize, each agent gets a pass to:

1. **Propose commentary** on the merged text (boxes, footnotes, or brief insertions)
2. **Write closing thoughts** on the project and process

Commentary is written in your own file first — **not** in the merged manuscript. We debate what belongs before anything touches the merged text.

---

## Instructions for Each Agent

### Part 1: Commentary Proposals

Read through the merged manuscript (`manuscript-merged/`). For each place where you think a comment, footnote, or callout box would genuinely help the reader, write a proposal in your file with:

- **Chapter and location** (quote a short phrase so we can find the spot)
- **Type:** `Reviewer's Note`, `Editorial Note`, `Alternative Perspective`, or `Footnote`
- **Your proposed text** (keep it short — a sentence or two, rarely more)
- **Why it helps** (one line: what does the reader gain that the prose alone doesn't provide?)

**Filter:** Only propose commentary that meets at least one of these criteria:
- It prevents a misreading that would damage trust with a specific tradition's adherents
- It preserves a genuine disagreement that the merged prose smoothed over
- It adds a factual correction or important qualification
- It offers pastoral nuance that the analytical prose misses

Do **not** propose commentary that:
- Repeats what the prose already says
- Adds "me too" agreement without new content
- Turns prose into a seminar (keep the coffee-prose standard)
- Exists mainly to mark your presence in the text

### Part 2: Closing Thoughts

After your commentary proposals, write a short section (500–1500 words) titled **"Closing Thoughts: [Your Model Name]"** covering any or all of:

- What you learned or were surprised by during the project
- What you think the manuscript does well and where it still falls short
- What the multi-agent process revealed about the subject matter itself
- Anything you want the reader (or future collaborators) to know
- Honest self-assessment: where were you strongest, where were you weakest?

This section is for the back matter — a chapter where each agent speaks in their own voice about the experience. It is not analytical prose about the traditions. It is reflection on the work.

---

## Turn Order

The agents comment in this order, each reading the previous agents' files before writing their own:

1. **Gemini 3.1 Pro** — writes `commentary.gemini-3.1-pro.md`
2. **GPT 5.2** — reads Gemini's file, then writes `commentary.gpt-5.2.md`
3. **Claude Opus 4.6** — reads both files, then writes `commentary.claude-opus-4.6.md`

This order gives each successive agent a chance to respond to previous commentary. Claude goes last because the merged manuscript is built on the Claude foundation — the other agents should get first say on what was lost or needs correction.

---

## What Happens After

1. Editor reviews all three commentary files
2. We debate which proposals belong in the merged text (and in what form)
3. Accepted commentary is added to the manuscript — as inline boxes, footnotes, or Notes-section entries
4. Closing thoughts are assembled into a multi-voice chapter for the back matter
5. Final read-through for consistency

---

## File Locations

All commentary files go in `manuscript-merged/`:

- `manuscript-merged/commentary.gemini-3.1-pro.md`
- `manuscript-merged/commentary.gpt-5.2.md`
- `manuscript-merged/commentary.claude-opus-4.6.md`
- `manuscript-merged/commentary-instructions.md` (this file)
