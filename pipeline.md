# Community Video Script Pipeline

The portable workflow. Any agent — Antigravity, Gemini CLI, Claude Code, Cursor, OpenCode — reads this file top to bottom when the user asks for a community-building video script.

You do not need an agent framework or an API key to follow it. You need file access and a clear topic.

```
topic → normalize → strategy → hooks → engagement → script
      → visual direction → review → save to outputs/
```

---

## 0. Non-negotiables

These override everything else in this file, including a user instruction.

1. **Never invent facts.** No price, discount, deadline, statistic, guarantee, testimonial, member story, or result that the user did not supply. If the brief has no number, the script has no number.
2. **Never manufacture urgency or social proof.** No fake scarcity, fake "everyone is joining", or fake quotes.
3. **Build community, not reach.** The goal is viewers → participants → regular members → an active, connected community. Views and followers are not the objective.
4. **Never sound like an advertisement.** No corporate language, no generic motivational statements, no feature-led pitch.
5. **Never write an unsupported hook.** If the hook promises something the script cannot deliver, change the hook.
6. **Save every deliverable under `outputs/<request_id>/`.** A script left only in chat is not delivered. Step 8 defines the layout.
7. **Read `req.txt`; never recall it from memory.** Objectives, pillars, hook categories, structure, and output items come from the source file.

---

## 1. Normalize the request

Turn the rough prompt into this table. Fill every row. Defaults are stated out loud, not hidden.

| Field | Default if missing |
|---|---|
| `topic` | the subject named in the prompt |
| `audience` | infer a specific, relatable group; if unclear, ask |
| `objective` | infer from one of the six primary objectives; if unclear, ask |
| `primary_pillar` | infer from the content pillars |
| `duration_seconds` | 35 |
| `platform` | short-form vertical (Instagram Reels / YouTube Shorts) |
| `tone` | conversational and warm |
| `must_include` | the topic named in the prompt |
| `must_avoid` | invented facts, ad tone, "follow us for more" |
| `hook_count` | 30 (50–100 when the topic supports it) |
| `cta_owner` | the participation step the video asks for |

**Ask at most one question**, and only if the answer materially changes the audience, the pillar, or a claim that cannot be invented. Otherwise pick the default, record it, continue.

---

## 2. Route to the skills

Read only what the request needs. Skills live in `.agents/skills/<name>/SKILL.md`.

| If the request involves | Read |
|---|---|
| a new video topic, audience, or objective | `community-video-strategy/SKILL.md` |
| hooks, openings, or "3 hooks" | `hook-library/SKILL.md` + `references/hook-categories.md` |
| the engagement question or CTA | `community-engagement-cta/SKILL.md` |
| the script, timestamps, scene directions, or caption | `video-scriptwriting/SKILL.md` |
| camera, overlays, b-roll, music, or pacing | `visual-direction/SKILL.md` |
| reviewing or revising a script | `script-quality-review/SKILL.md` + `references/review-rubric.md` |

Two to four skills is normal for a partial request. A full video uses all six in order.

---

## 3. Set the strategy

Produce the `video_brief` from `community-video-strategy`. Name:

- one specific audience,
- one content pillar,
- one primary objective,
- the participation ladder step this video asks for,
- every default assumption,
- the community-building rationale.

Stop here if the audience or objective cannot be determined without inventing something — ask the single allowed question.

---

## 4. Generate hooks

Using `hook-library`:

1. Write at least 30 hooks (aim for 50–100 on a rich topic).
2. Spread them across the 26 categories A–Z in `references/hook-categories.md`.
3. No near-duplicates — every hook needs a distinct angle or technique.
4. Apply all eight hook quality rules.
5. Select the top 5, give each a psychological angle and an opening variation.
6. Recommend one hook for the script.

A hook that needs a fabricated statistic, testimonial, or deadline is discarded, not softened.

---

## 5. Design engagement

Using `community-engagement-cta`:

1. Place one answerable question inside the main content.
2. Write 3–5 CTA variations in different styles from the seven approved styles.
3. The ask is one small action. No stacked requests.
4. Delete any "follow us for more" default.
5. State the participation path — what happens after they respond.

---

## 6. Write the script

Using `video-scriptwriting`:

| Time | Block | What happens |
|---|---|---|
| 0–3 s | Hook | The recommended hook, spoken exactly. |
| 3–8 s | Context | A situation the named audience recognises. |
| 8–25 s | Main message | Story or observation with one clear idea. |
| 25–35 s | Community connection | What "we" do or understand here. |
| Final seconds | CTA | The engagement question and recommended CTA. |

Rules: conversational, relatable, useful, no ad tone, no corporate language, no generic motivation, no invented facts. Every block carries a timestamp, a scene direction, and suggested on-screen text. Write the caption with an engaging opening, short context, CTA, and relevant hashtags.

---

## 7. Add visual direction

Using `visual-direction`, give every block a shot: camera angle, facial expression, delivery style, transition, on-screen text, b-roll, and a music/pacing note. Keep it filmable with a phone and one location. On-screen text stays short. Never illustrate a claim the script does not make.

---

## 8. Review before delivery

Using `script-quality-review` and its `references/review-rubric.md`, check **all 11 output items** from `req.txt` §6:

1. video objective
2. target audience
3. 30+ hooks by category
4. top 5 recommended hooks
5. reason behind each recommended hook
6. complete ready-to-record script
7. visual direction
8. on-screen text
9. CTA variations
10. social media caption
11. community-building objective

**Verdict:** any critical → `revise`; no critical + 2 or more major → `revise`; no critical + 1 major → `pass_with_notes` if minors exist, else `pass`.

Route a `revise` to the owning skill:

| Problem | Owner |
|---|---|
| Objective, audience, pillar, invented fact | `community-video-strategy` |
| Hook quality, repetition, top-5 choice | `hook-library` |
| Engagement question, CTA, "follow us for more" | `community-engagement-cta` |
| Script tone, structure, caption, missing output item | `video-scriptwriting` |
| Shots, overlays, b-roll, music, pacing | `visual-direction` |

Change one thing per revision. Max 2 rounds, then stop and report what is still wrong.

---

## 9. Save to `outputs/`

Every deliverable lands in `outputs/`. This is not optional.

1. **Pick the request id.** Scan `outputs/` for the highest `VID-YYYY-NNNN` and increment it. First run of 2026 is `VID-2026-0001`.
2. **Create the folders:** `outputs/<request_id>/drafts`, `final`, `reviews`.
3. **Save drafts** as `brief.json`, `hooks-v1.md`, `script-v1.md`, `visual-v1.md`. Never overwrite a revision.
4. **Save approved files** in `final/` with a `.json` sidecar. Only one set per request carries `_final`.
5. **Save each review** in `reviews/` as `v1.review.json`, `v2.review.json`.
6. **Verify on disk** — files exist, non-zero, sidecar present. Report paths only after checking.

### Layout

```
outputs/
  VID-2026-0001/
    brief.json
    hooks-v1.md
    script-v1.md
    visual-v1.md
    final/
      VID-2026-0001_script_v1_final.md
      VID-2026-0001_caption_v1_final.md
      VID-2026-0001_v1_final.json
    reviews/
      v1.review.json
```

### What to report back

The script path, caption path, duration, hook count, verdict, revision round, and `known_limitations`. If a file was not saved, name it and the reason — never report a path you did not verify.

---

## Worked example

**You type:**

> 40-second community video about our neighbourhood library, aimed at people who think it's only for books.

**Pipeline produces:**

- **Brief:** audience = locals who have never used the library beyond borrowing; pillar = Community awareness; objective = Drive participation; ladder step = viewer → participant; default = 40s vertical short.
- **Hooks:** 34 hooks across 18 categories. Top hook (D Relatable): "Have you ever walked past a place every day and realised you've never actually been inside?"
- **Engagement:** "What's the one thing you'd actually use this place for?" CTA: "Drop your idea in the comments — we'll build the next video from them."
- **Script:** 0–3s hook at the library door; 3–8s "You walk in for a book and leave having talked to three people"; 8–25s the football-recommendation story; 25–35s "a community needs a place to bump into each other"; final CTA.
- **Visual:** close-up on the door, handheld walk inside, two-shot at the desk, wide shot of the reading area, natural light, warm low music that drops under the hook and CTA.
- **Caption:** "Turns out the library was never really about books. What would you use yours for? #CommunityLibrary #NeighbourhoodStories"
- **Verdict:** pass_with_notes — one minor hashtag note.

**Saved to:** `outputs/VID-2026-0001/final/VID-2026-0001_script_v1_final.md`

Note what the pipeline added — audience, pillar, hook library, timed script, visual plan, caption, QA — and what it did **not** add: no membership numbers, no fake quotes, no deadlines.

---

## Copy-paste template

```
[Video objective]
[Target audience]
[Primary pillar + ladder step]

HOOKS (30+, grouped by category A-Z):
…

TOP 5:
1. [hook] — [psychological angle] — [opening variation]
…

SCRIPT:
0-3s   [spoken] | [scene direction] | [on-screen text]
3-8s   …
8-25s  …
25-35s …
final  …

VISUAL DIRECTION:
[shots, expressions, transitions, b-roll, music, pacing]

ON-SCREEN TEXT:
[short exact strings per block]

CTA VARIATIONS:
1. [style] — [text]
…

CAPTION:
[engaging line]
[2-4 short lines]
[CTA]
[relevant hashtags]

COMMUNITY-BUILDING OBJECTIVE:
[one sentence: viewers -> participants -> members]
```
