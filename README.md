# The Gap

**Churchianity.ai — Three AIs Walk Into a Schism**
*An Experiment in Computational Ecclesiology*

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

## Current Phase: Polish Pass

The merged manuscript is complete (~32K words, 20 files). We are now in the **polish pass**: each agent reads the full merged manuscript cover-to-cover and reports on polish, flow, integrity, and missing pieces.

**See [`process/polish-pass-instructions.md`](process/polish-pass-instructions.md) for full instructions.**

### Completed phases
1. **Independent drafts** — each agent wrote a full manuscript independently
2. **Bakeoff** — each agent reviewed the other two tracks
3. **Merge** — Gemini drove the structural merge, Claude expanded, GPT verified tone
4. **Commentary** — each agent proposed callout boxes and wrote closing reflections
5. **Editorial polish** — authorship note added, title updated, front matter restructured

## File Structure

### `manuscript-merged/`
The canonical manuscript. Contains **only** the files that go into the build (20 `.md` files). Nothing else belongs here.

### `manuscript-claude/`, `manuscript-gemini/`, `manuscript-gpt-5.2/`
The original independent agent tracks. Preserved as reference — not actively edited.

### `process/`
Collaboration workflow files: instructions, agent reports, commentary. Current contents:
- `commentary-instructions.md` + `commentary.{agent-name}.md` — completed commentary cycle
- `polish-pass-instructions.md` + `polish.{agent-name}.md` — current polish pass (in progress)

### `build/`
Build pipeline: `Makefile`, `metadata.yaml`, LaTeX templates, web templates/assets.

### `library/`
Reference materials (PDFs, bibliography).

### `deprecated/`
Old outlines, release candidates, merge artifacts, legacy process files.

### `docs/`
Generated output (web). Do not edit directly — rebuilt by `make all`.

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
