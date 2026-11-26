# Community Video Script Skills

Reusable skill modules for the community-building video script workflow described in `req.txt`.

Each folder is a self-contained skill: a `SKILL.md` with YAML frontmatter (`name`, `description`) plus optional `references/` and `scripts/`. Agents discover them by folder — no registration step, no build.

## Skills

| Skill | Owns | Output contract |
|---|---|---|
| [`video-input-research`](video-input-research/SKILL.md) | short-input analysis: goal, audience, tone, key message, missing details | `research_summary` |
| [`video-prompt-expansion`](video-prompt-expansion/SKILL.md) | expanding the idea into a production-ready prompt without intent drift | `improved_prompt` |
| [`community-video-strategy`](community-video-strategy/SKILL.md) | objective, audience, purpose, content pillar, participation ladder | `video_brief`, `community_building_rationale` |
| [`hook-library`](hook-library/SKILL.md) | 30+ hooks across categories A–Z, top 5, psychological angles | `hook_set` |
| [`community-engagement-cta`](community-engagement-cta/SKILL.md) | engagement question, CTA styles, participation path | `engagement_plan` |
| [`video-scriptwriting`](video-scriptwriting/SKILL.md) | ready-to-record script, house scene table, caption, 11-part assembly | `video_script` |
| [`visual-direction`](visual-direction/SKILL.md) | camera, expressions, delivery, transitions, on-screen text, b-roll, music, pacing | `visual_direction` |
| [`script-quality-review`](script-quality-review/SKILL.md) | severity-tagged verdict, routing, bounded revisions | `quality_review` |

`find-skills` is also installed — it is a general discovery helper, not part of the video workflow.

## Workflow order

```
short user input (4-5 lines)
  -> video-input-research           (research summary: goal, audience, tone, message, gaps)
  -> video-prompt-expansion         (production-ready improved prompt, intent preserved)
  -> community-video-strategy       (brief, pillar, objective, ladder)
  -> hook-library                   (30+ hooks, top 5, recommended hook)
  -> community-engagement-cta       (engagement question, CTA variations)
  -> video-scriptwriting            (house scene table + caption + 11-part assembly)
  -> visual-direction               (shots, phone screens, b-roll, music, pacing)
  -> script-quality-review          (verdict + targeted revisions)
  -> deliver when verdict is pass or pass_with_notes
```

**Stage outputs.** Every stage returns its own artifact, and from research onward the orchestrator carries forward all three headline artifacts: `research_summary`, `improved_prompt`, and `video_script`. The research stage returns only the summary; the expansion stage adds the improved prompt; the scripting stage adds the final script. Never report a later artifact before its stage has produced it.

`script-quality-review` routes a `revise` verdict to the owning skill, never to a generic rewrite. Two revision rounds per script; deterministic copy fixes do not consume the budget. Intent drift routes to `video-prompt-expansion`.

**Text-only deliverables.** This system produces a script, not a video. The deliverables are `outputs/<request_id>/final/VID-YYYY-NNNN_script_vN_final.md` — containing the script, caption, and appendices with the research summary and improved prompt — and `VID-YYYY-NNNN_script_vN_final.pdf`, the print copy rendered from that exact `.md` by `tools/md_to_pdf.py`. Never generate, render, or return a video file.

## Reference material

`refernces/test Script.md` and `refernces/Videos Scripts.md` are the source of the house script format (four-column scene table, Hinglish dialogue, phone-screen beats, CTA voiceover, caption) and the mandatory hashtag set. Coin values, voucher partner, and redemption limits must match the live app and current terms — treat those as claims to verify, never as facts to invent.

## Source of truth

`req.txt` is the single source of truth for the role, six primary objectives, scriptwriting guidelines, script structure, content pillars, hook categories A–Z, output requirements, and creative standard. Skills **read** it and reference its section names instead of restating it from memory.

The goal is not views or followers. The goal is to turn viewers into participants, participants into regular members, and regular members into an active, connected community.

## Adding a skill

1. Create `.agents/skills/<kebab-case-name>/SKILL.md`.
2. Add frontmatter with `name` and a `description` that lists the trigger conditions — this is what the agent matches against.
3. Include: purpose and when to use, inputs, procedure, output contract, quality checklist, example, constraints and failure cases.
4. Put long tables in `references/`, deterministic tooling in `scripts/`.
5. Add a row to the table above.

Do not create an empty skill folder. A skill with placeholder instructions is worse than no skill, because it looks authoritative.

## Conventions

- Frontmatter `description` is a trigger list, not a summary. Write it for the agent choosing whether to load the skill.
- Output contracts return structured objects, not free-form prose.
- Every skill ends with failure cases. A skill without failure cases has not been thought through.
- Hooks must never invent a statistic, testimonial, or urgent deadline.
- Use conversational, natural language; avoid corporate language and generic motivation.

## Reference sources

These skills were adapted directly from `req.txt`. `find-skills` (`vercel-labs/skills`) is installed separately as a general discovery helper.

### Tracking

Hand-authored skills have no upstream repository, so they show as `Source: untracked` in `npx skills list` and do not appear in `skills-lock.json`. That is expected. If you want them versioned and installable by teammates, push `.agents/skills/` to a repo and use `npx skills add <owner>/<repo>`.
