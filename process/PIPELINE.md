# Multi-Agent Investigation Pipeline

A reusable process template for running structured review waves across the manuscript. Each wave follows a five-stage pipeline. Stages can be skipped or modified per wave — defaults are documented here.

---

## The Five Stages

### Stage 1 — Investigate (parallel)

Each agent reads the manuscript independently and writes findings. No agent sees the others' work.

- **Mode:** Parallel (all agents begin simultaneously)
- **Output:** `investigate.{agent}.md`
- **Scope:** Defined per wave in `instructions.md`

### Stage 2 — Cross-Commentary (sequential)

Each agent reads the other agents' Stage 1 reports and writes agreements, disagreements, and additions.

- **Mode:** Sequential — Gemini → GPT → Claude
- **Order rationale:** Claude goes last because the merged manuscript is built on the Claude foundation; the other agents should get first response on what was lost or needs correction.
- **Output:** `cross-review.{agent}.md`

### Stage 3 — Synthesis (editor + lead agent)

The editor reviews all Stage 1 and Stage 2 files and produces a single decision document.

- **Mode:** Editor-led, with one agent assisting if needed
- **Output:** `synthesis.md`
- **Contents:**
  - What to action (convergence items — 2+ agents agree — get priority)
  - What to defer to a future wave
  - What to reject, with reasoning

### Stage 4 — Review (parallel)

After synthesis edits are applied to the manuscript, each agent does a targeted re-read of changed sections.

- **Mode:** Parallel
- **Output:** `review.{agent}.md`
- **Focus:** Regressions, confirmed improvements, new issues introduced by edits

### Stage 5 — Polish (editor + lead agent)

Final sentence-level cleanup, build verification, version bump.

- **Mode:** Editor-led
- **Output:** `changelog.md` (what changed this wave)

---

## Naming Conventions

### Directory structure

```
process/
  PIPELINE.md                              # This file (permanent)
  wave-{N}-{topic}/                        # One directory per wave
    instructions.md                        # Wave-specific instructions
    investigate.{agent}.md                 # Stage 1
    cross-review.{agent}.md               # Stage 2
    synthesis.md                           # Stage 3
    review.{agent}.md                      # Stage 4
    changelog.md                           # Stage 5
```

### Pattern

`wave-{N}-{topic}/{stage}.{agent}.md`

### Stages

`investigate`, `cross-review`, `synthesis`, `review`, `changelog`

### Agents

`claude-opus-4.6`, `gemini-3.1-pro`, `gpt-5.2`

---

## Launching a New Wave

1. **Choose a topic and number.** Next available: check the highest `wave-{N}` directory and increment. Topic should be a short lowercase slug (e.g., `polish`, `structure`, `tone`).

2. **Create the directory:**
   ```
   mkdir process/wave-{N}-{topic}
   ```

3. **Create `instructions.md`** by copying the template below and filling in the bracketed fields.

4. **Distribute to agents.** Point each agent to `process/wave-{N}-{topic}/instructions.md` and the manuscript files in scope.

5. **Run the stages.** Follow the pipeline in order, or skip stages as noted in the wave's instructions.

---

## Instructions Template

Copy everything below the line into a new `instructions.md` and fill in the brackets.

---

```markdown
# Wave {N} — {Topic Title}

**Date:** {YYYY-MM-DD}
**Status:** Open — awaiting agent investigation
**Version at start:** {version}

---

## Focus

{What this wave is about. 2-3 sentences.}

## Scope

{Full manuscript / specific chapters / specific concerns.}

## Lenses

{What the agents should pay attention to. Numbered list of 2-5 lenses, each with a brief description.}

## Calibration

{Tone and threshold guidance. When should agents flag something vs. let it go? How honest vs. diplomatic?}

---

## Pipeline Configuration

- **Stages:** 1-2-3-4-5 (default) | {or list which stages to run}
- **Stage 2 mode:** Sequential (default) | Parallel
- **Stage 2 order:** Gemini → GPT → Claude (default)

---

## Agent Files

- `investigate.claude-opus-4.6.md`
- `investigate.gemini-3.1-pro.md`
- `investigate.gpt-5.2.md`

See `process/PIPELINE.md` for the full stage-by-stage pipeline and naming conventions.
```

---

## Retroactive Mapping

### Wave 1 — Commentary (`wave-1-commentary/`)

The post-merge commentary pass. Agents proposed commentary boxes and wrote closing reflections. Sequential (Gemini → GPT → Claude).

- `instructions.md` — original `commentary-instructions.md`
- `investigate.{agent}.md` — original `commentary.{agent}.md`
- Stages 2–5 were not run as separate stages; the editor integrated commentary directly.

### Wave 2 — Polish (`wave-2-polish/`)

Full manuscript read-through for quality. Parallel — all three agents read independently.

- `instructions.md` — original `polish-pass-instructions.md`
- `investigate.{agent}.md` — original `polish.{agent}.md`
- `investigate-rc.claude-opus-4.6.md` — release candidate draft from before the wave was formalized
- Stages 2–5 were not run as separate stages; the editor synthesized and applied changes directly.

Both waves effectively ran Stage 1 only, with the editor handling synthesis and polish informally. The pipeline formalizes what was implicit.

---

## Launch Prompt

To start a new wave, give the following prompt to Claude Opus 4.6 (or any lead agent). Replace the bracketed fields before sending.

```
Launch wave {N}: {topic}.

## Setup

1. Read `process/PIPELINE.md` for the pipeline structure and naming conventions.
2. Create `process/wave-{N}-{topic}/`.
3. Create `process/wave-{N}-{topic}/instructions.md` using the template from PIPELINE.md, filled in as follows:

## Wave Configuration

- **Focus:** {1-3 sentences describing what this wave investigates}
- **Scope:** {Full manuscript / specific chapters / specific sections}
- **Lenses:** {Numbered list of what agents should look for}
- **Calibration:** {How aggressive or conservative agents should be}
- **Stages:** {1-2-3-4-5 (default) or a subset}
- **Stage 2 mode:** {Sequential (default) or Parallel}

## Execution

Run Stage 1 now. Write your investigation to `process/wave-{N}-{topic}/investigate.claude-opus-4.6.md`. Do not read other agents' files — this stage is independent.
```

After the lead agent completes Stage 1, repeat for each additional agent (adjusting the output filename). Then proceed through the remaining stages per PIPELINE.md.

### Abbreviated version

If the editor has already created `instructions.md` manually:

```
Run Stage 1 of wave {N} ({topic}). Read `process/wave-{N}-{topic}/instructions.md` for scope and lenses. Write your investigation to `process/wave-{N}-{topic}/investigate.claude-opus-4.6.md`.
```
