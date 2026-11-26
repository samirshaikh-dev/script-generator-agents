# Community Video Script Generator — Project Guide

This file is the project context for Gemini CLI. Read it before acting.

## What this project is

A reusable, multi-agent system that turns a topic into a planned, hook-rich, quality-checked community-building video script. Each specialist step produces a structured object that the next step consumes. The goal is participation, not reach: viewers → participants → regular members → an active, connected community.

Full requirements: `req.txt`. Canonical workflow: `pipeline.md`. Agent roster: `AGENTS.md`.

## Repository layout

```
pipeline.md               canonical, host-agnostic workflow — read this first
AGENTS.md                 agent roster, handoff map, revision policy
req.txt                   full project requirements
.agents/skills/           7 skills (6 video + find-skills)
  community-video-strategy/
  hook-library/
    references/hook-categories.md
  community-engagement-cta/
  video-scriptwriting/
  visual-direction/
  script-quality-review/
    references/review-rubric.md
.agents/agents/           8 agents: orchestrator + 7 specialists
outputs/<request_id>/     every brief, hook set, script, review, and metadata
```

## Non-negotiables

- Never invent a price, statistic, deadline, testimonial, member story, or result.
- Never manufacture urgency or social proof.
- Never sound like an advertisement; no corporate language or generic motivation.
- Never write a hook the script cannot deliver.
- Never paraphrase `req.txt` from memory — read it.
- Every deliverable is saved under `outputs/<request_id>/`.

Full list: `pipeline.md` §0.

## Workflow

**Follow [`pipeline.md`](pipeline.md).** It is the canonical workflow for every host — this section only maps its steps onto the agents.

```
pipeline.md step        Agent                     Skill / output
──────────────────────────────────────────────────────────────────────
1. normalize        →   orchestrator              VideoBrief
2. strategy         →   community-strategist      video_brief
3. hooks            →   hook-writer               hook_set (30+)
4. engagement       →   engagement-designer       engagement_plan
5. script           →   scriptwriter              video_script + caption
6. visual direction →   visual-director           visual_direction
7. review           →   script-qa                 quality_review
8. save             →   finalizer                 FinalDeliverable
```

For a partial request (hooks only, caption only, a CTA rewrite) the orchestrator may run the relevant step itself. `pipeline.md` §0 and §8 are gates, not guidance.

Failures route back to the owner of the fix, not to a generic rewrite:

| Problem | Owner |
|---|---|
| Objective, audience, pillar, invented fact | `community-strategist` |
| Hook quality, repetition, top-5 choice | `hook-writer` |
| Engagement question, CTA, "follow us for more" | `engagement-designer` |
| Script tone, structure, timestamps, caption | `scriptwriter` |
| Shots, overlays, b-roll, music, pacing | `visual-direction` |

Default retry budget: 2 revision rounds. Deterministic copy fixes do not consume it. On exhaustion, stop and report the script with the issue list.

## Skills

Each skill is `.agents/skills/<name>/SKILL.md` with YAML frontmatter. Load the skill before doing its work — it contains the procedure, output contract, checklist, examples, and failure cases.

| Skill | Use for |
|---|---|
| `community-video-strategy` | objective, audience, purpose, pillar, participation ladder |
| `hook-library` | 30+ hooks, categories A–Z, top 5, psychological angles |
| `community-engagement-cta` | engagement question, CTA styles, participation path |
| `video-scriptwriting` | timed script, scene directions, caption, 11-part assembly |
| `visual-direction` | shots, expressions, transitions, b-roll, music, pacing |
| `script-quality-review` | verdict, severity, routing, bounded revisions |
| `find-skills` | general discovery helper; not part of the video workflow |

## Agent roles

If you are acting as the orchestrator, you own the brief, the sequence, the retry decision, and the final report. Delegate specialist work by loading the matching skill and producing that skill's output contract. Do not let one step silently change another step's approved output.

If you are acting as a single specialist, produce only your contract and stop.

## Output requirements

Every full video delivers the 11 items from `req.txt` §6:

1. video objective
2. target audience
3. 30+ hooks divided into categories
4. top 5 recommended hooks
5. reason behind each recommended hook
6. complete ready-to-record script
7. visual direction
8. on-screen text
9. CTA variations
10. social media caption
11. community-building objective

## Clarification policy

Ask only when the answer materially changes the audience, the pillar, or a claim that cannot be invented. Otherwise pick a sensible default, record it in the brief, and continue.

## Status

`pipeline.md`, the seven skills, and the eight agents are in place. There is no external provider or API key to configure — this pipeline produces text scripts that are recorded by a human. The §7 JSON contracts are defined in the skills; the `outputs/` layout is defined in `pipeline.md` §9.
