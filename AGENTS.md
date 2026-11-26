# Community Video Script Agent Roster

Eight agents implementing the workflow in [`pipeline.md`](pipeline.md). Agent definitions live in `.agents/agents/`. Each host discovers them through its own path (OpenCode uses `.opencode/agents/`); the definitions themselves are host-neutral.

> **Canonical workflow: [`pipeline.md`](pipeline.md).** It is host-agnostic — Antigravity, Gemini CLI, Claude Code, Cursor, and OpenCode all read it. This file describes the implementation; when the two disagree, `pipeline.md` wins.

> Full requirements: [`req.txt`](req.txt). Skills: [`.agents/skills/`](.agents/skills/).

## Roster

| Agent | Mode | Skills loaded | Writes | Owns |
|---|---|---|---|---|
| `orchestrator` | primary | — | `outputs/**` | brief, sequencing, retries, delivery decision |
| `community-strategist` | subagent | `community-video-strategy` | nothing | objective, audience, purpose, pillar, participation ladder |
| `hook-writer` | subagent | `hook-library` | nothing | 30+ hooks, top 5, psychological angles |
| `engagement-designer` | subagent | `community-engagement-cta` | nothing | engagement question, CTA variations, participation path |
| `scriptwriter` | subagent | `video-scriptwriting` | `outputs/**` | timed script, on-screen text, caption, 11-part assembly |
| `visual-director` | subagent | `visual-direction` | nothing | shots, expressions, transitions, b-roll, music, pacing |
| `script-qa` | subagent | `script-quality-review` | nothing | verdict, severity, routing, revision instructions |
| `finalizer` | subagent | — (uses the delivery contract below) | `outputs/**` | final package, `outputs/` layout, metadata sidecar |

Read-only agents have no `edit` and no `shell` permission. `scriptwriter` and `finalizer` may write under `outputs/**` and ask before running shell commands. `orchestrator` has no shell at all.

## Handoff map

```
                 ┌──────────────┐
   topic ───────►│ orchestrator │
                 └──────┬───────┘
                        │ VideoBrief
        ┌───────────────┼──────────────────┐
        ▼               ▼                  ▼
 community-strategist  hook-writer   engagement-designer
        │               │                  │
        └───────┬───────┴──────────────────┘
                ▼
          scriptwriter ──► timed script + caption
                ▼
          visual-director ──► shot-by-shot direction
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

## Contracts

Each agent returns the object defined in its skill's Output contract, mirroring `req.txt` §6:

| Agent | Returns |
|---|---|
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
  "script_path": "outputs/VID-2026-0001/final/VID-2026-0001_script_v1_final.md",
  "caption_path": "outputs/VID-2026-0001/final/VID-2026-0001_caption_v1_final.md",
  "metadata_path": "outputs/VID-2026-0001/final/VID-2026-0001_v1_final.json",
  "verdict": "pass | pass_with_notes",
  "revision_round": 1,
  "known_limitations": []
}
```

## Using them

**Explicit delegation** (works from any session):

```
Use the orchestrator agent to create a 45-second community video about our neighbourhood library.
```

**Direct specialist call** when you only need one step:

```
Use the hook-writer agent to give me 30 hooks about a local clean-up drive.
```

If a host config sets a default agent, point it at `orchestrator`.

## Revision policy

- Default 2 revision rounds per script, configurable.
- Deterministic fixes (copy trim, caption edit, overlay text) do not consume the budget.
- Brief problems route to `community-strategist`; hooks to `hook-writer`; CTA to `engagement-designer`; script tone or structure to `scriptwriter`; visual direction to `visual-director`.
- On exhaustion, the orchestrator stops and reports the script with the issue list.

## Adding an agent

1. Create `.agents/agents/<kebab-case>.md`.
2. Frontmatter: `description` (this is what the orchestrator sees when choosing), `mode`, and `permissions`.
3. Body is the system prompt — role, what to load, what to do, what never to do, what to return.
4. Add the agent to the orchestrator's `subagent` allow list if it should be callable.
5. Add a row to the roster table above.

Do not duplicate a skill's content into an agent prompt. The agent loads the skill; the skill holds the detail.
