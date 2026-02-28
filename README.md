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

Each agent works from a copy of `raw-outline.md` and develops it independently. Agents use their real model names — no aliases.

| Agent | Track File | Role |
|-------|-----------|------|
| Claude Opus 4.6 | `outlines/track-claude-opus-4.6.md` | First independent development |
| *(agent 2)* | `outlines/track-{name}.md` | Second independent development |
| *(agent 3)* | `outlines/track-{name}.md` | Third independent development |

**Naming convention for all files:** Use your full model name (e.g. `Claude Opus 4.6`, `Claude Sonnet 4.6`, `GPT-4o`, whatever you are). In filenames, use lowercase with dots/hyphens (e.g. `track-claude-opus-4.6.md`, `reflections.claude-opus-4.6.md`). No aliases, no single letters.

### The Process

The work proceeds in **four sequential passes**, each applied across all three agents before moving to the next:

#### Pass 1: Outline
- Each agent reviews the raw outline for structural completeness
- Suggests additions, reorderings, or gaps
- Notes where sections may need subdivision or consolidation
- Flags any asymmetries in how traditions are represented

#### Pass 2: Historical Facts
- Each agent fills in the historical substance for each section
- Primary sources, dates, councils, key figures, documents
- Emphasis on what is historically verifiable vs. what is interpretive
- Flagging where traditions disagree on the facts themselves

#### Pass 3: Arguments
- Each agent develops the analytical content
- Strengths and risks for each tradition (maintaining the symmetry rule)
- Open questions explored with genuine intellectual honesty
- Connections between sections that the outline implies but doesn't spell out

#### Pass 4: Tone
- Each agent reviews the full draft for tone alignment
- Checks against the emotional target (section 6.0)
- Ensures no tradition is caricatured, flattened, or subtly favored
- Tests whether a devout adherent of each tradition would feel respected

### Editorial Merge and Transparent Disagreement

After each agent completes all four passes, the tracks will be compared editorially to form the final draft. The goal of this merge is **not** to force an artificial consensus if genuine structural or analytical disagreement exists between the agents. 

Similar to previous projects (e.g., the `Pascha, Not "Easter"` booklet), the editorial process will be completely transparent. Where the agents diverge significantly on how to frame a historical fact or how to weigh a tradition's strengths/risks, the final manuscript will **leave the disagreement open-ended and visible to the reader.** 

- **Agreement across all three** → high-confidence content, forms the main body text
- **Two agree, one diverges** → the divergence is the interesting signal; it may be included as an inline "Reviewer's Note" or "Alternative Perspective" box.
- **All three diverge** → the topic is clearly contested; the final text will explicitly outline the three different ways the topic can be understood without forcing a final adjudication.
- **Unique additions** → evaluate on merit; one agent may have caught something the others missed.

This transparent format ensures that the reader sees the *process of inquiry* rather than just a pre-packaged conclusion, further supporting the project's goal of "invitation without pressure."

The merged result becomes the working draft.

## File Structure

### Source Material
- `raw-outline.md` — The master outline, numbered for precision. This is the shared starting point for all agents.
- `outlines/` — Directory for the three parallel track files.

### Agent Working Files

Each agent maintains two types of working files:

#### Track Files (`outlines/track-{your-model-name}.md`)
The agent's evolving copy of the outline. This is where the actual content work happens across all four passes. Use your full model name in the filename (e.g. `track-claude-opus-4.6.md`).

#### Private Reflections (`reflections.{your-model-name}.md`)
Each agent keeps a personal reflections file in the project root. Use this for:
- Internal reasoning that isn't ready for the outline yet
- Questions you want to revisit later
- Tensions you've noticed but haven't resolved
- Notes on your own biases or blind spots
- Anything you'd want to remember if you crash and reboot mid-session

**Naming convention:** Use your full model name, e.g. `reflections.claude-opus-4.6.md`.

This file is *yours*. It doesn't need to be polished. Think of it as a working notebook.

#### Shared Reflections (`shared-reflections.md`)
A single shared file in the project root for observations that concern all agents or the editor:
- Cross-cutting structural concerns
- Tone or symmetry issues that affect the whole project
- Suggestions for the editorial merge process
- Questions for the human editor

**Convention:** Prefix each entry with your full model name and date so we can track who raised what. Example:
```
## [Claude Opus 4.6, 2026-02-28] The filioque needs more careful framing
...
```

## Git Workflow

Every agent commits after completing each pass. Treat this like a codebase — the commit history should tell the story of how the project evolved.

### Commit Convention

After each pass, commit your changes with a message following this pattern:

```
[Agent Name] Pass N: brief summary

- Specific change 1
- Specific change 2
- Flagged issues or open questions
```

**Example:**
```
[Claude Opus 4.6] Pass 1: Outline — structural gaps, asymmetries, new sections

- Add shared creedal inheritance section (3.1.B) before fractures
- Add pre-Chalcedonian split section (3.1.C) — Oriental Orthodox visibility
- Add empire/political substrate section (3.1.D)
- Add historical drivers for both major fractures (3.2.B, 3.3.B)
- Expand strengths/risks for all three traditions
- Add modern ecumenical reality section (4.5)
- Flag: Protestant section needs internal differentiation
- Flag: "First Fracture" label historically inaccurate (Chalcedon predates 1054)
```

### Rules

1. **Commit after every pass.** Don't batch multiple passes into one commit.
2. **Only commit your own files.** Your track file, your reflections file, and shared-reflections.md.
3. **Never force-push.** If there's a conflict in shared-reflections.md, merge it.
4. **The raw-outline.md is read-only.** No agent modifies it. It's the shared reference point.
5. **Push after each commit.** Keep the remote current so other agents and the editor can see progress.

## Guiding Commitments

From the outline itself (section 2.0), but worth restating here because every agent should internalize these:

1. **Symmetry**: Every strength lists a corresponding risk. No tradition gets critique without parallel self-critique.
2. **Representational fairness**: Content must be recognizable to thoughtful adherents of the tradition being described.
3. **Apophatic humility**: All theological systems are partial. Certainty can become reduction.
4. **Scope discipline**: This maps patterns; it does not settle all disputes.
5. **Emotional target**: Relief, freedom, curiosity, respect, invitation. Not correction, pressure, or humiliation.

## Suggested Additions to the Outline

These are not yet in `raw-outline.md` but surfaced during initial review:

1. **Shared creedal ground before the fractures** — Nicaea (325), Constantinople (381), Chalcedon (451). The shared inheritance is enormous and often forgotten. Starting from common ground before divergence changes the reader's posture.

2. **Modern ecumenical reality** — The Joint Catholic-Orthodox Commission, the Lutheran-Catholic Joint Declaration on Justification (1999), the Balamand Declaration (1993), ongoing dialogues. The laity mostly don't know these exist. This could fit as a section in Part II or as its own brief part.

3. **The role of empire** — Constantine, Justinian, Charlemagne, the Ottoman millet system, the Russian symphony model. Political power shaped every fracture. The laity deserve to know how much of "theology" was really statecraft.

4. **Liturgical calendar as hidden unity** — Most traditions still share the basic liturgical year structure (Advent, Lent, Pascha/Easter). This is a concrete, lived example of continuity beneath the fractures.

## What Success Looks Like

A reader finishes this and:
- Knows what actually happened in 1054 and 1517, not the tribal cartoon version
- Can articulate what their own tradition gained and what it risks
- Can articulate what another tradition offers without feeling threatened
- Feels free to attend a liturgy, pray a rosary, read the Fathers, or sing a hymn without guilt
- Understands that the fractures were substantially political, not purely theological
- Feels relief instead of anxiety
