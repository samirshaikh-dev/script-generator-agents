# Community Video Script Generator — Project Guide

This file is the project context for Gemini CLI. Read it before acting.

## What this project is

A reusable, multi-agent system that takes a short 4–5 line video idea, researches it, expands it into a production-ready prompt, and produces a ready-to-record community-building video script. Each specialist step produces a structured object that the next step consumes.

The goal is participation, not reach: viewers → participants → regular members → an active, connected community. The user's original words are the intent anchor at every stage.

Full requirements: `req.txt`. Canonical workflow: `pipeline.md`. Agent roster: `AGENTS.md`. House scripts: `refernces/`.

## Repository layout

```
pipeline.md               canonical, host-agnostic workflow — read this first
AGENTS.md                 agent roster, handoff map, stage outputs, revision policy
req.txt                   full project requirements
refernces/
  test Script.md          house scene table example
  Videos Scripts.md       script library, mandatory hashtags, claim warning
.agents/skills/           9 skills (8 video + find-skills)
  video-input-research/
  video-prompt-expansion/
  community-video-strategy/
  hook-library/
    references/hook-categories.md
  community-engagement-cta/
  video-scriptwriting/
    references/script-format.md
  visual-direction/
  script-quality-review/
    references/review-rubric.md
.agents/agents/           10 agents: orchestrator + 9 specialists
outputs/<request_id>/     input, drafts, reviews, final .md script + matching .pdf copy
tools/md_to_pdf.py        renders the final .md into its .pdf copy
```

## Non-negotiables

- Capture the user's 4–5 line input verbatim as `intent_anchor`. Never paraphrase it away.
- Research before expanding; expand before scripting.
- Never invent a price, discount, deadline, statistic, testimonial, member story, reward value, voucher partner, or result.
- `refernces/Videos Scripts.md` warns that coin values, voucher partner, and redemption limits must match the live app and current terms — treat them as claims to verify.
- Never name a clip id or app screen that is not in `refernces/` or the user's input.
- Include the mandatory hashtag set in every video, with the brand spelled `meelTe` — never `Meelte`, `meelte`, or `MELTE`. `brand/meelte-brand.json` is the source of truth.
- Never sound like an advertisement; no corporate language or generic motivation.
- Save every artifact under `outputs/<request_id>/`.
- **Script output only:** produce a video *script*, never a video. Never generate, render, encode, or return a video file. The deliverables are one `.md` script file and one `.pdf` copy rendered from it.

Full list: `pipeline.md` §0.

## Workflow

**Follow [`pipeline.md`](pipeline.md).** It is the canonical workflow for every host — this section only maps its steps onto the agents.

```
pipeline.md step        Agent                  Skill / output
──────────────────────────────────────────────────────────────────────
1. accept input     →   orchestrator           intent_anchor (verbatim)
2. research         →   video-researcher       research_summary
3. expand prompt    →   prompt-expander        improved_prompt
4/5. strategy       →   community-strategist   video_brief
6. hooks            →   hook-writer            hook_set (30+)
7. engagement       →   engagement-designer    engagement_plan
8. script           →   scriptwriter           house scene table + caption
9. visual           →   visual-director        visual_direction
10. review          →   script-qa              quality_review
11. save            →   finalizer              FinalDeliverable
```

For a partial request (hooks only, caption only, CTA rewrite) the orchestrator may enter at the matching stage, but still carries the intent anchor.

Failures route back to the owner of the fix:

| Problem | Owner |
|---|---|
| Intent changed, prompt over/under-expanded | `prompt-expander` |
| Goal, audience, tone, or missing detail misread | `video-input-research` |
| Objective, audience, pillar, invented fact | `community-strategist` |
| Hook quality, repetition, top-5 choice | `hook-writer` |
| Engagement question, CTA, "follow us for more" | `engagement-designer` |
| Script tone, structure, caption, missing output item | `scriptwriter` |
| Shots, phone screens, overlays, music, pacing | `visual-director` |

Default retry budget: 2 revision rounds. Deterministic copy fixes do not consume it. On exhaustion, stop and report the script with the issue list.

## Stage outputs

Return artifacts at their own stages, not only at the end:

| Stage | Artifacts returned |
|---|---|
| research | `research_summary`, `research_summary_text` |
| expansion | `research_summary`, `improved_prompt`, `improved_prompt_text` |
| scripting / QA | `research_summary`, `improved_prompt`, final `video_script` |
| delivery | all three plus `FinalDeliverable` |

Never report a later artifact before its stage has produced it.

## Skills

Each skill is `.agents/skills/<name>/SKILL.md` with YAML frontmatter. Load the skill before doing its work — it contains the procedure, output contract, checklist, examples, and failure cases.

| Skill | Use for |
|---|---|
| `video-input-research` | short-input analysis: goal, audience, tone, key message, gaps |
| `video-prompt-expansion` | production-ready prompt without intent drift |
| `community-video-strategy` | objective, audience, purpose, pillar, participation ladder |
| `hook-library` | 30+ hooks, categories A–Z, top 5, psychological angles |
| `community-engagement-cta` | engagement question, CTA styles, participation path |
| `video-scriptwriting` | house scene table, caption, 11-part assembly |
| `visual-direction` | shots, phone screens, b-roll, music, pacing |
| `script-quality-review` | verdict, severity, routing, bounded revisions |
| `find-skills` | general discovery helper; not part of the video workflow |

## House script format

From `refernces/test Script.md`, the final scene-by-scene script is a four-column table:

| Time | What we see | Dialogue | Phone screen |
| --- | --- | --- | --- |
| 0-3s | … | Speaker: "…" | None or app screen |

After the table: CTA voiceover over the end card, caption with mandatory hashtags, and 2–3 alternate hooks. Dialogue uses the language set by research (Hinglish for local-shop scenarios). The 30+ hook library stays in the full package; the script displays the chosen hook plus a few alternates.

Mandatory hashtags in every video:

`#meelTe #LocalDiscovery #ShopLocal #Bengaluru #Ranchi #Gaya #SupportLocal #LocalBusiness`

## Agent roles

If you are acting as the orchestrator, you own the verbatim input, the sequence, the stage outputs, the retry decision, and the final report. Delegate specialist work by loading the matching skill and producing that skill's output contract. Do not let one step silently change another step's approved output.

If you are acting as a single specialist, produce only your contract and stop.

## Output requirements

Every full video delivers the 11 items from `req.txt` §6, including the house script table, on-screen text, CTA variations, caption, and community-building objective.

## Clarification policy

Ask only when the answer changes a truth claim that cannot be invented: price, discount, deadline, reward value, voucher partner, redemption limit, or testimonial. Otherwise pick a sensible default, record it in the brief, and continue.

## Deliverable boundary

The user receives exactly two files: `outputs/<request_id>/final/VID-YYYY-NNNN_script_vN_final.md` and `VID-YYYY-NNNN_script_vN_final.pdf`. The `.md` contains the hook, scene-by-scene narration, visuals, transitions, CTA, ending, caption, alternate hooks, and appendices with the research summary and improved prompt. The `.pdf` is that same `.md` rendered by `tools/md_to_pdf.py` — never a separately edited script version. Working drafts and reviews stay under `drafts/` and `reviews/` as the evidence trail. No `.mp4`, `.mov`, or other video file is produced. Verify both files are non-zero before reporting their paths; if PDF generation fails, keep the `.md`, record the failure in `known_limitations`, and say so plainly.

## Status

`pipeline.md`, the nine skills, the reference format, and the ten agents are in place. There is no video generator, render step, provider, or API key to configure — the script is recorded by a human. The only rendering step is `tools/md_to_pdf.py`, which prints the final `.md` to a `.pdf` using Python-Markdown and headless Chrome/Edge. The `outputs/` layout is defined in `pipeline.md`.
