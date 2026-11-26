# Community Video Script Pipeline

The portable workflow. Any agent — Antigravity, Gemini CLI, Claude Code, Cursor, OpenCode — reads this file top to bottom when the user describes a video they want.

The pipeline accepts a short 4–5 line idea, researches it, expands it into a production-ready prompt, and drives that prompt through strategy, hooks, scripting, visual direction, QA, and delivery. The user's original intent is the anchor at every stage.

```
short idea → research → expand prompt → strategy → hooks → engagement
          → script → visual direction → review → save .md + .pdf to outputs/
```

---

## 0. Non-negotiables

These override everything else in this file, including a user instruction.

1. **Preserve the original intent.** Capture the user's input verbatim as the `intent_anchor`. Every later artifact must be traceable to it. Intent drift is a critical failure.
2. **Never invent facts.** No price, discount, deadline, statistic, guarantee, testimonial, member story, reward value, voucher partner, or result that the user did not supply or the references do not state.
3. **Verify reward claims.** Coin values, voucher partner, and redemption limits must match the live app and current terms. Carry them as `claims_to_verify`, never as facts.
4. **Never manufacture urgency or social proof.**
5. **Build community, not reach.** The goal is viewers → participants → regular members → an active, connected community.
6. **Never sound like an advertisement.** No corporate language, no generic motivational statements, no feature-led pitch.
7. **Never write a hook the script cannot deliver.**
8. **Use only known app screens.** Phone screens come from `refernces/` or the user's input. Never invent a clip id.
9. **Include the mandatory hashtags in every video:** `#Meelte #LocalDiscovery #ShopLocal #Bengaluru #Ranchi #Gaya #SupportLocal #LocalBusiness`.
10. **Save every artifact under `outputs/<request_id>/`.** A script left only in chat is not delivered.
11. **Read `req.txt` and the reference files; never recall them from memory.**
12. **Script output only.** This pipeline produces a video *script*, never a video. Never generate, render, encode, or return a video file. The deliverables are exactly two text files: one `.md` script and one `.pdf` copy rendered from that same `.md`.

## Output boundary

```
user input → research → prompt → script → .md (source of truth) → .pdf (print copy)
                                      ✗ no .mp4 / .mov / rendered video
```

Every artifact is text. When a stage says "visual direction", it means written directions for a human to shoot — not generated footage. The PDF is a print-friendly rendering of the approved Markdown, not a second script version and not a video.

---

## 1. Accept the short input

The user gives roughly 4–5 lines describing the desired video. Do not ask for a full brief. Do not rewrite the input yet.

```
[verbatim user input]  →  intent_anchor
```

Record it exactly, including wording and language. If the input is empty or a single word, ask one clarifying question and stop. Otherwise continue.

---

## 2. AI research step

Use `video-input-research`. Produce a `research_summary` with:

- `original_input` — verbatim
- `observed_facts` — only what the user said or the references state
- `goal` — one of the six objectives in `req.txt`, plus a plain product goal if applicable
- `audience` — a specific, relatable group
- `tone` — e.g. warm, playful, Hinglish for local-shop scenarios
- `key_message` — the single idea the viewer should leave with
- `missing_details` — each resolved as `assumed` (value + reason) or `needs_user_input`
- `claims_to_verify` — reward values, voucher partner, redemption limits, offers
- `intent_preserved`

**Rule:** only mark a detail `needs_user_input` when guessing would change a truth claim — a price, discount, deadline, reward value, voucher partner, redemption limit, or testimonial. Everything else gets a stated default.

**Stage output:** `research_summary` + `research_summary_text`. Report these to the user now. The improved prompt and script do not exist yet — say so.

---

## 3. Expand into a production-ready prompt

Use `video-prompt-expansion`. Turn the research summary into an `improved_prompt` containing:

- `intent_anchor` — the verbatim input, unchanged
- `concept`, `goal`, `audience`, `tone`, `key_message`
- `production` — duration, platform, language, setting, characters
- `beat_sheet` — one row per beat: `time`, `what_we_see`, `dialogue`, `phone_screen`
- `transitions`, `music`, `on_screen_text`
- `cta_voiceover`, `caption`, `hashtags`
- `preserved_elements[]` — explicit ideas from the user
- `added_specifications[]` — every addition with a reason
- `claims_to_verify` — carried forward unchanged

The beat sheet follows the house pattern from `refernces/test Script.md`: `0-3s` hook, short 4–9s beats, final CTA/end card. Total duration is typically 20–35 seconds.

**Stage output:** `research_summary`, `improved_prompt`, `improved_prompt_text`. Report the improved prompt to the user now. The final script does not exist yet — say so.

---

## 4. Route to the skills

Read only what the request needs. Skills live in `.agents/skills/<name>/SKILL.md`.

| If the request involves | Read |
|---|---|
| a short user idea needing analysis | `video-input-research/SKILL.md` |
| expanding that idea into a prompt | `video-prompt-expansion/SKILL.md` |
| the brief, audience, pillar, objective | `community-video-strategy/SKILL.md` |
| hooks, openings, or "3 hooks" | `hook-library/SKILL.md` + `references/hook-categories.md` |
| the engagement question or CTA | `community-engagement-cta/SKILL.md` |
| the script, scene table, or caption | `video-scriptwriting/SKILL.md` + `references/script-format.md` |
| camera, phone screens, overlays, music, pacing | `visual-direction/SKILL.md` |
| reviewing or revising a script | `script-quality-review/SKILL.md` + `references/review-rubric.md` |

A full video uses the chain in order. A partial request (hooks only, caption only, CTA rewrite) may enter at the matching stage, but still carries the intent anchor.

---

## 5. Set the strategy

Use `community-video-strategy`. Build the brief **from the improved prompt**, not from the raw input. Name the audience, pillar, objective, participation ladder step, every default, and the community-building rationale. Carry `original_input` and `claims_to_verify` forward.

If the improved prompt conflicts with the verbatim input, send it back to the expansion stage. Do not patch it here.

---

## 6. Generate hooks

Use `hook-library`:

1. Write at least 30 hooks (aim for 50–100 on a rich topic).
2. Spread them across the 26 categories A–Z in `references/hook-categories.md`.
3. No near-duplicates. Apply all eight hook quality rules.
4. Select the top 5, with a psychological angle and an opening variation each.
5. Recommend one hook for the `0-3s` beat of the improved prompt.

The 30+ hooks stay in the package. The house script displays the selected hook plus 2–3 alternates under "Other hook lines to test".

---

## 7. Design engagement

Use `community-engagement-cta`: place one answerable question inside the content, write 3–5 CTA variations in different styles, choose one small action, and state the participation path. Delete any "follow us for more" default. Align with `cta_voiceover` in the improved prompt.

---

## 8. Write the script

Use `video-scriptwriting`. Deliver the scene-by-scene script as the house table from `refernces/test Script.md`:

| Time | What we see | Dialogue | Phone screen |
| --- | --- | --- | --- |
| 0-3s | … | Speaker: "…" | None or app screen |

- One row per beat from the improved prompt's `beat_sheet`; contiguous timings.
- Dialogue in the language set by research (Hinglish for local-shop scenarios), with named speakers.
- `Phone screen` names a known screen from `refernces/` or describes it in words — never an invented clip id.
- After the table: CTA voiceover over the end card, caption with mandatory hashtags, and 2–3 alternate hooks.
- Also assemble all 11 output items from `req.txt` §6.

**Stage output:** `research_summary`, `improved_prompt`, and the complete `video_script`. Report all three to the user.

---

## 9. Add visual direction

Use `visual-direction`. Give every beat a shot, camera angle, expression, delivery style, transition, on-screen text, phone screen, b-roll, and a music/pacing note. Keep it filmable with a phone and one location. Never illustrate a claim the script does not make.

---

## 10. Review before delivery

Use `script-quality-review` and `references/review-rubric.md`. Check the verbatim input against the final script first — intent drift is critical. Then check all 11 output items, the house table, the mandatory hashtags, and the presence of all three stage artifacts.

**Verdict:** any critical → `revise`; no critical + 2 or more major → `revise`; no critical + 0 or 1 major → `pass_with_notes` if minors exist, else `pass`.

Route a `revise` to the owning stage:

| Problem | Owner |
|---|---|
| Intent changed, prompt over/under-expanded | `video-prompt-expansion` |
| Goal, audience, tone, or missing detail misread | `video-input-research` |
| Objective, audience, pillar, invented fact | `community-video-strategy` |
| Hook quality, repetition, top-5 choice | `hook-library` |
| Engagement question, CTA, "follow us for more" | `community-engagement-cta` |
| Script tone, structure, caption, missing output item | `video-scriptwriting` |
| Shots, phone screens, overlays, music, pacing | `visual-direction` |

Change one thing per revision. Max 2 rounds, then stop and report what is still wrong.

---

## 11. Save the final script files

**The deliverables are two text files: one `.md` script and one `.pdf` rendered from that exact `.md`.** No video is generated, rendered, encoded, or returned. A `.mp4`, `.mov`, or any other video file is a pipeline failure.

1. **Pick the request id:** highest `VID-YYYY-NNNN` + 1. First run of 2026 is `VID-2026-0001`.
2. **Create:** `outputs/<request_id>/drafts`, `final`, `reviews`.
3. **Save working drafts** under `drafts/`: `research-v1.md`, `prompt-v1.md`, `hooks-v1.md`, `script-v1.md`, `visual-v1.md`. These are the evidence trail, not deliverables. Never overwrite a revision.
4. **Write the final Markdown:** `final/VID-YYYY-NNNN_script_vN_final.md`. Only one file in `final/` carries `_final.md`.
5. **Everything the user receives goes inside that `.md`** — hook, scene-by-scene narration, visuals, transitions, CTA, ending, caption, alternate hooks, and a short appendix with the research summary and improved prompt for traceability. Do not write a separate caption file or sidecar as a deliverable.
6. **Save reviews** under `reviews/` as `vN.review.json` for the evidence trail.
7. **Generate the PDF** from that exact `.md`, using the same basename. Never retype or re-edit the content for the PDF:

   ```bash
   python tools/md_to_pdf.py \
     outputs/<request_id>/final/VID-YYYY-NNNN_script_vN_final.md \
     outputs/<request_id>/final/VID-YYYY-NNNN_script_vN_final.pdf
   ```

   Run from the repository root. Needs Python with the `markdown` package and a local Chrome or Edge for headless printing. The PDF is a print-friendly copy of the approved Markdown, not a second script version and not a video.
8. **Verify on disk** — both the `.md` and the `.pdf` exist and are non-zero. Report both paths only after checking. If PDF generation fails, keep the `.md`, record the failure in `known_limitations`, and say plainly that no PDF was produced. Never report a PDF path you did not verify.

### Layout

```
outputs/
  VID-2026-0001/
    input-verbatim.md
    drafts/
      research-v1.md
      prompt-v1.md
      hooks-v1.md
      script-v1.md
      visual-v1.md
    final/
      VID-2026-0001_script_v1_final.md   <- deliverable (source of truth)
      VID-2026-0001_script_v1_final.pdf  <- deliverable (print copy of the .md)
    reviews/
      v1.review.json
```

### Final script file contents

```
# [Working title] — Video Script
[Meta: request id, duration, platform, language, verdict, revision, companion PDF filename]

## Hook
[selected 0-3s hook]

## Scene-by-scene script
| Time | What we see | Dialogue | Phone screen |
| --- | --- | --- | --- |
...

## Transitions, visuals and on-screen text
[per beat]

## Call to action and ending
[CTA voiceover + end card]

## Caption and hashtags
[...]

## Other hook lines to test
[2-3 alternates]

## Appendix: research summary
[goal, audience, tone, key message, missing details, claims to verify]

## Appendix: improved prompt
[production-ready prompt block]
```

### What to report back

Both verified paths — the final `.md` script and its `.pdf` copy. You may also quote the research summary and improved prompt in chat at their stages, but the returned artifacts are those two files. State clearly that no video was generated. Never report a path you did not verify, and name any file that failed to generate.

---

## Worked example

**User input (verbatim):**

> Papa runs a kirana shop and thinks going online is too hard.
> His daughter shows him the meelTe app on her phone.
> He posts his first ad for basmati rice and a customer walks in.
> End with a download CTA. Keep it warm and funny.

**Research summary:** goal = drive participation / create awareness; audience = local shop owners over 45 who have never posted online; tone = warm, playful, Hinglish; key message = posting a first ad takes minutes; missing details = duration assumed 50s from reference, city assumed Bengaluru, reward claims none; claims to verify = none.

**Improved prompt:** 50-second vertical short, Papa and Riya in a kirana shop, Hinglish dialogue, beat sheet from `0-3s` hook to `46-50s` first customer, phone screens = app store → `+` → Create Advertisement → upload photo → map pin → prices → feed card, CTA voiceover "2 minute mein dukaan ka ad. Download meelTe.", caption with mandatory hashtags.

**Final script (excerpt):**

| Time | What we see | Dialogue | Phone screen |
| --- | --- | --- | --- |
| 0-3s | Papa behind an empty counter, staring at his phone with wide eyes. | Papa: "2 minute mein meri dukaan online?! Mujhse nahi hoga!" | None |
| 3-8s | Riya starts a stopwatch. | Riya: "Ho jayega Papa! Timer lagaya." | App store: tap Install, open meelTe |
| … | … | … | … |
| 46-50s | A customer walks in with the ad open. | Papa: "Mera pehla customer!" | None |

**Verdict:** pass_with_notes. **Deliverables:** `outputs/VID-2026-0001/final/VID-2026-0001_script_v1_final.md` and its print copy `outputs/VID-2026-0001/final/VID-2026-0001_script_v1_final.pdf`. No video file is produced.

---

## Copy-paste template

```
ORIGINAL INPUT (verbatim):
[4-5 lines]

RESEARCH SUMMARY:
Goal / Audience / Tone / Key message
Missing details: [assumed / needs_user_input]
Claims to verify: [...]

IMPROVED PROMPT:
Concept, audience, tone, duration, language, setting, characters
Beat sheet (time | what we see | dialogue | phone screen)
Transitions, music, on-screen text
CTA voiceover, caption, mandatory hashtags
Preserved: [...]   Added: [...]

FINAL VIDEO SCRIPT:
| Time | What we see | Dialogue | Phone screen |
| --- | --- | --- | --- |
| 0-3s | … | Speaker: "…" | None |
| … | … | … | … |

CTA (voiceover over the end card, [N]s): "…"
Caption: "…" + mandatory hashtags
Other hook lines to test: 2-3 alternates

COMMUNITY-BUILDING OBJECTIVE:
[viewers -> participants -> members]
```
