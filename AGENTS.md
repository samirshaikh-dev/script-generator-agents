# Community Video Script Agent Roster

Ten agents implementing the workflow in [`pipeline.md`](pipeline.md). Agent definitions live in `.agents/agents/`. Each host discovers them through its own path (OpenCode uses `.opencode/agents/`); the definitions themselves are host-neutral.

> **Canonical workflow: [`pipeline.md`](pipeline.md).** It is host-agnostic — Antigravity, Gemini CLI, Claude Code, Cursor, and OpenCode all read it. This file describes the implementation; when the two disagree, `pipeline.md` wins.

> Full requirements: [`req.txt`](req.txt). Skills: [`.agents/skills/`](.agents/skills/). Brand source of truth: [`brand/meelte-brand.json`](brand/meelte-brand.json) — always write `meelTe`.

## Roster

| Agent | Mode | Skills loaded | Writes | Owns |
|---|---|---|---|---|
| `orchestrator` | primary | — | `outputs/**` | brief, sequencing, retries, stage outputs, delivery decision |
| `video-researcher` | subagent | `video-input-research` | nothing | research summary, goal, audience, tone, key message, missing details |
| `prompt-expander` | subagent | `video-prompt-expansion` | nothing | production-ready improved prompt, intent preservation |
| `community-strategist` | subagent | `community-video-strategy` | nothing | objective, audience, purpose, pillar, participation ladder |
| `hook-writer` | subagent | `hook-library` | nothing | 30+ hooks, top 5, psychological angles |
| `engagement-designer` | subagent | `community-engagement-cta` | nothing | engagement question, CTA variations, participation path |
| `scriptwriter` | subagent | `video-scriptwriting` | `outputs/**` | timed script, on-screen text, caption, 11-part assembly |
| `visual-director` | subagent | `visual-direction` | nothing | shots, expressions, transitions, b-roll, music, pacing |
| `script-qa` | subagent | `script-quality-review` | nothing | verdict, severity, routing, revision instructions |
| `finalizer` | subagent | — (uses the delivery contract below) | `outputs/**` | the final `.md` script plus its matching `.pdf`; no video output |

Read-only agents have no `edit` and no `shell` permission. `scriptwriter` and `finalizer` may write under `outputs/**` and ask before running shell commands. `orchestrator` has no shell at all.

## Handoff map

```
                 ┌──────────────┐
  4-5 line idea ►│ orchestrator │
                 └──────┬───────┘
                        ▼
             video-researcher ──► research_summary
                        ▼
             prompt-expander ──► improved_prompt
                        ▼
              community-strategist ──► video_brief
                        │
        ┌───────────────┼──────────────────┐
        ▼               ▼                  ▼
   hook-writer   engagement-designer   (brief locked)
        │               │
        └───────┬───────┴──────────────────┘
                ▼
          scriptwriter ──► house scene table + caption
                ▼
          visual-director ──► phone screens + shot direction
                ▼
            script-qa ──► QualityReview
                │
      pass ─────┴───── fail/revise
        │                 │
        ▼                 └──► targeted feedback to the owning agent
    finalizer                  (bounded retries)
        ▼
  FinalDeliverable
```

Every handoff after `video-researcher` carries `research_summary`, `improved_prompt`, and whatever script artifacts exist so far. Do not report an artifact before its stage has produced it.

## Contracts

Each agent returns the object defined in its skill's Output contract, mirroring `req.txt` §6:

| Agent | Returns |
|---|---|
| `video-researcher` | `research_summary` + `research_summary_text` |
| `prompt-expander` | `improved_prompt` + `improved_prompt_text` |
| `community-strategist` | `video_brief` + `community_building_rationale` |
| `hook-writer` | `hook_set` (`hooks[]`, `top_hooks[]`, `recommended_hook_id`) |
| `engagement-designer` | `engagement_plan` |
| `scriptwriter` | `video_script` + `caption` + `assembled_output` (11 parts) |
| `visual-director` | `visual_direction` |
| `script-qa` | `quality_review` |
| `finalizer` | `FinalDeliverable` |

`FinalDeliverable`:

```json
{
  "request_id": "VID-2026-0001",
  "deliverable_paths": [
    "outputs/VID-2026-0001/final/VID-2026-0001_script_v1_final.md",
    "outputs/VID-2026-0001/final/VID-2026-0001_script_v1_final.pdf"
  ],
  "deliverable_types": ["script_md", "script_pdf"],
  "video_generated": false,
  "verdict": "pass | pass_with_notes",
  "revision_round": 1,
  "known_limitations": []
}
```

**There are exactly two deliverables: the final `.md` script file and a `.pdf` print copy generated from that same file.** No video is generated, rendered, or returned. The research summary and improved prompt are reported at their stages and embedded in an appendix of the `.md` (and therefore in the PDF); they are not separate deliverables.

## Stage outputs

The pipeline returns three headline artifacts, each introduced at its own stage:

| Stage | Artifacts returned |
|---|---|
| research | `research_summary`, `research_summary_text` |
| expansion | `research_summary`, `improved_prompt`, `improved_prompt_text` |
| scripting and QA | `research_summary`, `improved_prompt`, final `video_script` (house scene table, CTA voiceover, caption) |
| delivery | all three embedded in the final `.md` script file and its PDF copy, plus `FinalDeliverable` |

The orchestrator reports these at each stage to the user, not only at the end. It never invents a later artifact early.

## Using them

**Explicit delegation** (works from any session):

```
Use the orchestrator agent to make a 25-second video. Papa runs a kirana shop and thinks going online is too hard. His daughter shows him the meelTe app. He posts his first ad and a customer walks in. End with a download CTA.
```

**Direct specialist call** when you only need one step:

```
Use the hook-writer agent to give me 30 hooks about a local clean-up drive.
```

If a host config sets a default agent, point it at `orchestrator`.

## Revision policy

- Default 2 revision rounds per script, configurable.
- Deterministic fixes (copy trim, caption edit, overlay text) do not consume the budget.
- Intent drift or over/under-expansion routes to `prompt-expander`; misread goal, audience, tone, or missing detail routes to `video-input-research`.
- Brief problems route to `community-strategist`; hooks to `hook-writer`; CTA to `engagement-designer`; script tone or structure to `scriptwriter`; visual direction to `visual-director`.
- On exhaustion, the orchestrator stops and reports the script with the issue list.

## Adding an agent

1. Create `.agents/agents/<kebab-case>.md`.
2. Frontmatter: `description` (this is what the orchestrator sees when choosing), `mode`, and `permissions`.
3. Body is the system prompt — role, what to load, what to do, what never to do, what to return.
4. Add the agent to the orchestrator's `subagent` allow list if it should be callable.
5. Add a row to the roster table above.

Do not duplicate a skill's content into an agent prompt. The agent loads the skill; the skill holds the detail.
