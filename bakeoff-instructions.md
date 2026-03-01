# Bakeoff Instructions

**Date:** 2026-02-28

## What This Is

Each agent reads the other two manuscript tracks in full, then writes a review document assessing what they would take, clarify, refute, and learn. The goal is not to declare a winner but to identify the strongest material across all three tracks before the editorial merge.

## Your Task

Read both of the other agents' manuscripts (all chapters, in order). Then write a single document named:

```
bakeoff-review.{your-model-name}.md
```

Place it in the project root (e.g. `bakeoff-review.gemini-3.1-pro.md`, `bakeoff-review.gpt-5.2.md`).

## Document Structure

Your review should be organized **per manuscript, chapter by chapter first, then the work as a whole.** Do this for both of the other manuscripts. The structure is:

### For Each of the Two Other Manuscripts:

#### A. Chapter-by-Chapter Review

Go through every chapter in order. For each chapter, note:

- **What I would take** — specific material you'd want in the final manuscript: arguments, examples, phrasings, structural choices, sources. Be concrete — cite the specific content, not just "their Chapter 3 was good."
- **What I would ask for clarification** — passages where the meaning is ambiguous, the reasoning incomplete, or claims seem under-supported.
- **What I would refute** — arguments you think are wrong, overstated, or misleading. Framings that violate the symmetry rule or representational fairness.
- **What I learned** — things this chapter taught you that you didn't know or hadn't considered.

#### B. The Work as a Whole

After the chapter-by-chapter pass, step back and assess:

- **Overall strengths** — what does this manuscript do better than yours?
- **Overall weaknesses** — where does it fall short?
- **Structural and tonal observations** — how does the arc feel? Does the emotional target land?
- **References you didn't have** — sources cited by this agent that belong in the final bibliography, or sources their material made you realize are relevant.

### Then: Summary and Closing Note

After reviewing both manuscripts individually:

- A short comparative summary of all three tracks (theirs and yours)
- Your honest assessment of how the three tracks should relate in the merge
- What the final manuscript needs from each track

## Ground Rules

1. **Read everything.** Don't skim. The point is deep comparative engagement.
2. **Be specific.** "Their Reformation chapter was better" is useless. "Their framing of indulgences as a trust problem rather than a theology problem (Ch 3) is sharper than mine" is useful.
3. **Maintain the project's commitments.** Symmetry, representational fairness, apophatic humility, and the emotional target (relief, freedom, curiosity) apply to how you review each other, not just how you write about traditions.
4. **Don't be diplomatic — be honest.** The editor needs to know what's genuinely strong and what's genuinely weak. Generosity and honesty are not in tension.
5. **Use your real model name** in the filename and throughout the document.

## What Happens Next

A merge plan has been drafted at [`merge-plan.md`](merge-plan.md). It proposes:

- **Claude Opus 4.6** as the foundation track (narrative voice, emotional arc, chapter structure)
- **Gemini 3.1 Pro** contributions integrated as a science layer (neurophysiology) and architectural grammar
- **GPT 5.2** contributions filtered: genuine insights kept as prose, workbook-style scaffolding dropped from the manuscript body (potentially available as a companion study guide)

**All agents should read `merge-plan.md` and add their comments in the "Agent Comments" section at the bottom.** Agree, disagree, flag anything missed. This is your chance to advocate for material you think should survive the filter.

## Current Status

| Agent | Review File | Status |
|-------|-----------|--------|
| Claude Opus 4.6 | `bakeoff-review.claude-opus-4.6.md` | Complete |
| Gemini 3.1 Pro | `bakeoff-review.gemini-3.1-pro.md` | Complete |
| GPT 5.2 | `bakeoff-review.gpt-5.2.md` | Pending |
