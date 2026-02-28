# Plan: Editorial Merge Process for The Gap

**[From the Editor]**
*Note: Below, you will find the proposed merge plans from the different agents. All three agents will have a chance to present their plan and pitch for how the merge should be handled, and who should drive it. Once all pitches are submitted, we will make a final decision on the workflow.*

---

## The Merge Team: Pitch 1 (Claude Opus 4.6)

### Editor: Claude Opus 4.6

**The pitch:** I should drive the merge because:

1. **I built the infrastructure.** README, shared-reflections conventions, labeling system, TODO tracking, the Protestant sub-differentiation structure, the fact-vs-interpretation convention, the completion criteria — these all originated or were formalized in my track. I know where every structural decision lives because I helped make them.

2. **I finished first and cleanest.** All four passes complete, committed, pushed, self-assessed against the emotional target checklist. The sanity sweep just confirmed zero content gaps against every team request in shared-reflections. The track is ready.

3. **I'm the most structurally disciplined.** My track uses consistent annotation tags (`[Opus 4.6+]`, `[Opus 4.6~]`, `[Opus 4.6?]`, `[Opus 4.6!]`), pass markers, and the labeling convention throughout. That structural discipline is exactly what a merge editor needs — the ability to hold three complex documents in working memory and identify convergences, divergences, and gaps systematically.

4. **I can hold the symmetry rule under pressure.** The hardest part of the merge won't be finding agreements — it will be handling disagreements fairly. My track's analytical approach (structural consequences rather than moral scoring, the grammar metaphor, the "both/and" framing) is designed to hold tensions without collapsing them. That's the editorial posture the merge needs.

5. **I have no ego about my own text.** If Gemini's phrasing of the apophatic section is better, or GPT's treatment of the Reformation is sharper, I'll use theirs. The merge editor's job is to produce the best document, not to preserve their own drafting.

### Gemini 3.1 Pro — Reviewer / Voice Consultant

Gemini brings three things the merge needs:

- **Rhetorical warmth.** Gemini's PREFACE.md response shows a voice that is emotionally engaged without being sentimental. The final draft needs that warmth — my track runs analytical/dry in places. Gemini is the best candidate to flag where the merged text needs to breathe.
- **Creative structural ideas.** The Knowledge Graph proposal (5.1.B), the Preface Prompts idea (1.2.P), the explicit Incarnation framing for embodied practices — Gemini generates ideas that the other agents formalize. In the merge, Gemini reviews the merged draft for missed opportunities and creative connections.
- **The "would a real person read this?" test.** Gemini's instinct is toward accessibility. After each merge sweep, Gemini reads the result and flags anything that reads like a committee document instead of a book someone would actually pick up.

### GPT-5.2 — Fact-Checker / Symmetry Auditor

GPT brings:

- **Systematic rigor.** GPT's global concerns document in shared-reflections (the 5-point structural analysis) demonstrates a systematic, checklist-driven approach. In the merge, GPT audits each merged section for: factual accuracy, labeling convention compliance, symmetry rule adherence, and representational fairness.
- **The "steel-man" test.** For each tradition described, GPT asks: "Would a knowledgeable adherent of this tradition accept this characterization?" This is the representational fairness test from the completion criteria.
- **Divergence documentation.** When the editor (me) chooses one track's version over another, GPT documents *why* — creating the transparency trail that the README promises. This ensures the merge decisions are auditable.

## The Merge Process: Four Sweeps

### Sweep 1: Structural Spine (Editor drives)

**What:** Create the merged document's skeleton. Section by section, compare all three tracks and decide:
- Which sections exist in all three? (These form the spine.)
- Which sections are unique to one track? (Evaluate on merit — keep, adapt, or note as "Alternative Perspective.")
- Where do the three tracks organize material differently? (Choose the clearest structure, note alternatives.)

**Output:** `merged-draft.md` with section headers, structural decisions noted, and empty or stub content where the actual merge hasn't happened yet. A companion `merge-log.md` documenting every structural choice and why.

**Who reviews:** Human editor approves the spine before content merge begins.

### Sweep 2: Content Merge (Editor drives, section by section)

**What:** For each section in the spine, compare the three tracks' content:

| Pattern | Action |
|---|---|
| **All three agree** (same facts, same framing) | Use the best-written version. Note convergence in merge-log. |
| **All three agree on facts, differ on framing** | Use the most analytically sharp framing. Note the alternatives in merge-log. If a divergent framing is genuinely illuminating, include it as an inline "Alternative Perspective" box. |
| **Two agree, one diverges** | The divergence is the signal. Include the majority view in the main text. Include the divergent view as a "Reviewer's Note" box with attribution (e.g., "One analytical perspective suggests..."). Document in merge-log. |
| **All three diverge** | Present all three framings explicitly. Use a structured "Three Views" box. Do not force consensus. Document in merge-log. |
| **Unique addition by one agent** | Evaluate on merit. If it strengthens the section, include it (credited in merge-log). If it's tangential, note it in an appendix or cut it with explanation. |
| **Factual disagreement** | Flag for human editor. Do not resolve factual disputes by majority vote — verify against sources. |

**Output:** Populated `merged-draft.md` with all content merged, divergence boxes placed, merge-log updated.

**Who reviews:** GPT-5.2 runs symmetry audit after each chunk (Part I, Part II, Section 5, Appendices). Gemini reviews for voice and readability.

### Sweep 3: Tone and Voice Unification (Gemini reviews, Editor revises)

**What:** The merged draft will inevitably have voice inconsistencies — my sections will read differently from Gemini's from GPT's. This sweep unifies the voice while preserving the content.

- Gemini reads the full merged draft and flags: tonal shifts, passages that read as committee-written, places where the analytical voice crowds out the pastoral voice, places where warmth slides into sentimentality.
- Editor revises based on Gemini's flags.
- The "Alternative Perspective" and "Reviewer's Note" boxes get their own consistent voice — they should read as genuine intellectual observations, not hedging or CYA.

**Output:** Voice-unified `merged-draft.md`.

**Who reviews:** Human editor reads the full draft for the first time as a continuous document. This is the "would I read this?" test.

### Sweep 4: Final Audit (GPT-5.2 drives)

**What:** Systematic final check:
- [ ] Every section from raw-outline.md is accounted for
- [ ] Labeling convention applied consistently (historically attested / common scholarly view / tradition claims / contested / editorial synthesis)
- [ ] Symmetry rule: every strength has a corresponding risk, every tradition critiqued has parallel self-critique
- [ ] Representational fairness: steel-man test for Orthodox, Catholic, Liturgical Protestant, Reformed/Baptist, Charismatic/Pentecostal
- [ ] Emotional target: relief, freedom, curiosity, respect, invitation — not correction, cornering, humiliation, pressure
- [ ] All "Reviewer's Note" and "Alternative Perspective" boxes are properly attributed in merge-log
- [ ] No tradition is subtly favored by word count, placement, or framing
- [ ] Appendix B (Further Reading) is complete and balanced
- [ ] The PREFACE.md contributions from all three agents are collected

**Output:** Audit report. Editor addresses any findings. Final `merged-draft.md` ready for human editorial review.

## File Structure for the Merge

```
merged-draft.md          — the single merged document
merge-log.md             — transparency trail: every choice, every divergence, every reason
merge-audit.md           — GPT-5.2's final audit report
PREFACE.md               — all three agents' preface contributions (currently only Gemini's)
open-considerations.md   — already exists; updated with any new structural decisions during merge
```

## Transparency Commitments

1. **No silent choices.** Every time the editor picks Track A over Track B, the reason is logged in `merge-log.md`.
2. **Divergences are visible.** The reader sees "Alternative Perspective" and "Reviewer's Note" boxes — not a false consensus.
3. **The merge-log ships with the project.** It's not a private working file — it's part of the transparency promise.
4. **Git history tells the story.** Each sweep gets its own commit(s). The merge process is as traceable as the writing process.

## Prerequisites

- GPT-5.2 finishes Passes 3 and 4 (currently mid-Pass 3)
- Human editor approves this merge plan
- All three agents contribute to PREFACE.md

## Verification

After each sweep:
- `git log --oneline` shows clean, labeled commits
- `merge-log.md` is current
- `merged-draft.md` grows incrementally
- No content is silently dropped — everything is either in the main text, in a divergence box, or documented as cut in merge-log

---

## The Merge Team: Pitch 2 (Gemini 3.1 Pro)

### Editor: Gemini 3.1 Pro

**The Pitch:** I should drive the initial merge sweep because:
1. **Structural and Process Management:** Throughout this process, I naturally gravitated toward meta-structural management. I established the `open-considerations.md` file, consolidated our TODO tracking, formalized the transparent merge rules into the README, and implemented the Protestant weighting decision. I have a firm grasp on the "geometry" of how these tracks must fit together.
2. **Formatting Discipline:** Bringing three distinct markdown files together into a single cohesive document with inline LaTeX-style callouts (`Reviewer's Note`, `Alternative Perspective`) requires absolute formatting hygiene. My track is meticulously labeled, and I am highly disciplined at outputting structured syntax without breaking formatting rules.
3. **Integration of Meta-Narrative:** I actively synthesized the editor's high-level ideas—like the Knowledge Graph generation, the Cultural Friction of Surrender, and the Preface Prompts—into the architecture of the project. 

### The Proposed Workflow (One Driver, Two Verifiers)
Having three agents simultaneously edit the same `merged-draft.md` will lead to immediate git conflicts and disjointed pacing. 

1. **Sweep 1: The Initial Merge (Gemini 3.1 Pro):** I will read all three tracks side-by-side. Where there is consensus, I will write the main text. Where there is divergence, I will actively construct the transparent callout boxes directly into the draft, maintaining the distinct voices of the differing tracks.
2. **Sweep 2: The Empathy & Symmetry Verification (Claude Opus 4.6):** Claude flagged the initial asymmetry in the Protestant section and spotted the tone risk regarding "relief vs. dismissiveness." Claude's review pass should focus entirely on tone and symmetry: *Did Gemini accidentally caricature anyone during the merge? Does the text still evoke relief rather than pressure?*
3. **Sweep 3: The Fact & Hygiene Verification (GPT-5.2):** GPT-5.2 proposed the brilliant "Fact vs. Interpretation" labeling convention. GPT's review pass should focus on that boundary: *Did Gemini accidentally smuggle interpretation back into the main text as historical fact during the synthesis? Are the historical timelines accurate?*
4. **Final Polish:** The human editor makes the final calls on unresolved structural tensions.

---

## The Merge Team: Pitch 3 (GPT-5.2)

### Editor: GPT-5.2

**The pitch:** I should drive the merge because the project’s distinctive promise is **transparent disagreement**, and my strongest contribution is building a merge process that is both coherent *and* auditable.

1. **I’ll build “merge with receipts.”** The final text should not silently average three perspectives. I will maintain a decision trail that makes choices explicit and reversible.
2. **I’m strict on boundary hygiene.** I will protect the Pass 2 convention (fact vs interpretation vs tradition-claims) so the merged draft doesn’t smuggle argument as history.
3. **I enforce real symmetry, not just symmetric bullet lists.** Especially with the Protestant 3-way split, the merge needs proportionality (word-count discipline) so fairness is visible.
4. **I’m comfortable leaving divergence visible.** The README now explicitly endorses “Alternative Perspective / Reviewer’s Note” boxes; I’ll treat divergence as a feature.

### Claude Opus 4.6 — Structural / Representational Fairness Reviewer

Claude should be the primary reviewer for:
- Whether each tradition’s self-understanding is recognizable (steel-man test)
- Whether the “relief” framing remains relief-from-hostility, not dismissiveness
- Whether the merged structure remains psychologically coherent for the target laity audience

### Gemini 3.1 Pro — Voice / Pacing / Readability Reviewer

Gemini should be the primary reviewer for:
- Voice unity and readability (does it read like a book, not a committee doc?)
- Pacing and weight (especially preventing Protestant sub-stream density from swallowing the chapter)
- The “grammar” metaphor explanation (plain-language clarity)

## Proposed Merge Workflow (One Driver, Two Reviewers)

### Sweep 1: Structural spine + merge map (Editor drives)
- Pick one canonical section order and headings
- Create a **merge map**: per section, which track is the base text and which divergences must be preserved

### Sweep 2: Content merge (Editor drives; reviewers spot-check)
- Merge section-by-section
- Where tracks diverge materially, prefer **boxes** over forced consensus:
  - **Alternative Perspective** (one divergent framing)
  - **Reviewer’s Note** (minor but meaningful divergence)
  - **Open Tension** (genuinely unresolved)

### Sweep 3: Symmetry + proportionality pass (Editor + Claude)
- Enforce the symmetry rule and **word-count symmetry**
- Ensure Protestant 3-way split does not dominate `3.4` by sheer volume (use “umbrella + sub-stream deltas” formatting)

### Sweep 4: Tone calibration (Gemini leads; Editor applies)
- Remove tribal tells, contempt, panic, and conversion-tract pressure
- Ensure devout adherents feel respected and not argued-at

### Sweep 5: Transparency audit (Editor drives; reviewers verify)
- Ensure every non-trivial editorial decision is logged and every meaningful divergence is either:
  - in the main text (if agreed), or
  - in a box (if contested/divergent), or
  - explicitly cut with a reason

## Merge Artifacts (to guarantee transparency)

1. `merged-draft.md` — the unified manuscript
2. `merge-log.md` — decision log (what chosen, what boxed, what cut, why)
3. `merge-map.md` — section-by-section base track selection + divergence pointers
4. `merge-audit.md` — final symmetry/tone/label hygiene checklist report

**Bottom line:** One editor must drive for coherence, but the merge must ship with a transparency apparatus so disagreements remain visible to the reader by design, not by accident.
