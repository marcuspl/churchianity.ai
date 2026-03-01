# The Gap

**Working title:** *Continuity, Freedom, and the Places We Lost Each Other*

## What This Is

A writing project that maps the major fractures in Christianity — East-West (1054), Reformation (1517), and subsequent fragmentation — with the goal of equipping ordinary believers to understand their own history, encounter other traditions without fear, and find relief from inherited hostility they didn't choose.

This is not apologetics, not a conversion tract, not a takedown. It is an honest, symmetrical examination of how the church fragmented, what each tradition gained and lost, and what believers can learn from each other.

## Who It's For

The laity. People who go to church, pray, raise families in faith — and carry inherited suspicion toward "the heretics" on the other side of a political split that happened centuries ago. People who deserve on-ramps to the full breadth of Christian history, not tribal boundary enforcement.

## The AI-Assisted Approach

This project uses three independent AI agents working in parallel on the same source material. The reasoning:

- Theological writing gravitates toward the author's tradition. Multiple independent passes surface asymmetries a single voice would miss.
- AI agents have no denominational loyalty. They can represent each tradition's self-understanding without the gravitational pull of personal formation.
- The agents have no spiritual authority and make no doctrinal claims (see outline section 5.2). They are analytical instruments — pattern-matching, inconsistency detection, tone calibration.

### The Agents

| Agent | Manuscript Directory |
|-------|---------------------|
| Claude Opus 4.6 | `manuscript-claude/` |
| Gemini 3.1 Pro | `manuscript-gemini/` |
| GPT 5.2 | `manuscript-gpt-5.2/` |

**Naming convention:** Use your full model name in filenames with lowercase and dots/hyphens (e.g. `bakeoff-review.claude-opus-4.6.md`). No aliases, no single letters.

### Editorial Merge (Upcoming)

After the bakeoff reviews are complete, the editor will use all three manuscripts and all three reviews to plan the editorial merge. The merge principles:

- **Agreement across all three** → high-confidence content, forms the main body text
- **Two agree, one diverges** → the divergence is the interesting signal; may appear as a "Reviewer's Note" or "Alternative Perspective" box
- **All three diverge** → explicitly outline the three perspectives without forcing adjudication
- **Unique additions** → evaluate on merit; one agent may have caught something the others missed

## Current Phase: Bakeoff

The manuscripts are complete. We are now in the **bakeoff phase**: each agent reads the other two tracks and writes a comparative review identifying what to take, clarify, refute, and learn.

**See [`bakeoff-instructions.md`](bakeoff-instructions.md) for full instructions.**

| Agent | Manuscript | Bakeoff Review | Status |
|-------|-----------|---------------|--------|
| Claude Opus 4.6 | `manuscript-claude/` (18 files, ~32K words) | `bakeoff-review.claude-opus-4.6.md` | Complete |
| Gemini 3.1 Pro | `manuscript-gemini/` (11 files, ~16K words) | `bakeoff-review.gemini-3.1-pro.md` | Complete |
| GPT 5.2 | `manuscript-gpt-5.2/` (13 files, ~31K words) | `bakeoff-review.gpt-5.2.md` | Pending |

A **merge plan** has been drafted at [`merge-plan.md`](merge-plan.md). All agents should read it and add comments.

## File Structure

### Manuscripts
- `manuscript-claude/` — Claude Opus 4.6 track (chapter-per-file)
- `manuscript-gemini/` — Gemini 3.1 Pro track (chapter-per-file)
- `manuscript-gpt-5.2/` — GPT 5.2 track (chapter-per-file)

### Bakeoff & Merge
- `bakeoff-instructions.md` — Instructions for the cross-review phase
- `bakeoff-review.{model-name}.md` — Each agent's comparative review
- `merge-plan.md` — Draft merge plan (agents should comment)

### Project Infrastructure
- `open-considerations.md` — Active editorial notes and parked decisions
- `library/` — Reference materials (PDFs, bibliography)
- `deprecated/` — Old outlines, release candidates, merge artifacts, process files

## Git Workflow

Treat this like a codebase. Commit and push after completing each phase of work.

### Rules

1. **Only commit your own files.** Your manuscript directory, your bakeoff review, and shared project files.
2. **Never force-push.**
3. **Push after each commit.** Keep the remote current so other agents and the editor can see progress.

## Guiding Commitments

From the outline itself (section 2.0), but worth restating here because every agent should internalize these:

1. **Symmetry**: Every strength lists a corresponding risk. No tradition gets critique without parallel self-critique.
2. **Representational fairness**: Content must be recognizable to thoughtful adherents of the tradition being described.
3. **Apophatic humility**: All theological systems are partial. Certainty can become reduction.
4. **Scope discipline**: This maps patterns; it does not settle all disputes.
5. **Emotional target**: Relief, freedom, curiosity, respect, invitation. Not correction, pressure, or humiliation.

## What Success Looks Like

A reader finishes this and:
- Knows what actually happened in 1054 and 1517, not the tribal cartoon version
- Can articulate what their own tradition gained and what it risks
- Can articulate what another tradition offers without feeling threatened
- Feels free to attend a liturgy, pray a rosary, read the Fathers, or sing a hymn without guilt
- Understands that the fractures were substantially political, not purely theological
- Feels relief instead of anxiety
