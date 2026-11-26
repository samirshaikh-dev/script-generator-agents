---
name: video-scriptwriting
description: Use when writing or revising a ready-to-record community video script, when a script needs timestamps and scene directions, when a caption with hashtags is required, or when a draft reads like an advertisement. Owns the complete script, on-screen text, caption, and final output assembly.
---

# Video Scriptwriting

Writes the complete, ready-to-record short-form script from an approved brief, hook, and engagement plan.

## When to use

- A `video_brief`, hook, and engagement plan are ready and the script must be written.
- The user asks for a "complete script", "ready-to-record script", or "caption".
- A draft needs rewriting to sound conversational rather than promotional.
- The final 11-part output must be assembled.

## Inputs

- `improved_prompt` — `video-prompt-expansion`. Its `beat_sheet`, `language`, `production`, `cta_voiceover`, `caption`, and `hashtags` drive the script.
- `video_brief` — `community-video-strategy`.
- `hook_set` with `recommended_hook_id` — `hook-library`.
- `engagement_plan` — `community-engagement-cta`.
- `visual_direction` — `visual-direction` (merge before final delivery).
- `references/script-format.md` — the house scene-table format from `refernces/`.
- `req.txt` — Scriptwriting Guidelines, Video Script Structure, Output Requirements, section 6.

## Script structure

| Time | Block | What happens |
|---|---|---|
| 0–3 s | Hook | The recommended hook, spoken exactly as written. |
| 3–8 s | Context | Introduce the situation or problem; make it relatable. |
| 8–25 s | Main message | Storytelling, useful information, or a new perspective. |
| 25–35 s | Community connection | Connect the message to the community and its purpose. |
| Final seconds | CTA | The engagement moment / call to action. |

Adjust the durations to the topic; a 20-second script may compress the middle blocks, never the hook. The exact block boundaries come from the improved prompt's `beat_sheet`, which follows the house pattern in `references/script-format.md` (0–3s hook, 4–9s beats, final CTA/end card).

## House scene table

Deliver the scene-by-scene script as a four-column table, exactly as in `refernces/test Script.md`:

| Time | What we see | Dialogue | Phone screen |
| --- | --- | --- | --- |
| 0-3s | … | Speaker: "…" | None or app screen |

- Use the speaker names and language from the improved prompt (Hinglish for local-shop scenarios).
- The `Phone screen` column names a screen from `refernces/` or describes it in words. Never invent a clip id.
- After the table, add the CTA voiceover over the end card, the caption with mandatory hashtags, and 2–3 alternate hook lines.

Mandatory hashtags in every video — the union of the mandatory set in `refernces/Videos Scripts.md` and the caption in `refernces/test Script.md`:

`#Meelte #LocalDiscovery #ShopLocal #Bengaluru #Ranchi #Gaya #SupportLocal #LocalBusiness`

## Writing rules

- Conversational, natural, human language. Read it aloud before finalising.
- Address real audience problems, interests, emotions, and experiences.
- Avoid sounding like an advertisement.
- Focus on storytelling, relatable situations, and practical value.
- Include the engagement question inside the content.
- Create curiosity and emotional connection.
- End with the natural CTA from `engagement_plan`.
- Avoid generic motivational statements and unnecessary corporate language.
- No invented price, statistic, testimonial, deadline, guarantee, or result.
- This skill produces a text script only. No video is generated, rendered, or returned.

## Procedure

1. Open with the exact recommended hook. Do not "warm up" before it.
2. Build context from a concrete, everyday situation the named audience recognises.
3. Deliver the main message as a short story or observation with one clear idea.
4. Connect to the community in one or two sentences — what "we" do here, what "we" understand.
5. Place the engagement question at the natural pivot, then close with the recommended CTA.
6. Build the house scene table: one row per beat from the improved prompt's `beat_sheet`, with `Time`, `What we see`, `Dialogue`, `Phone screen`.
7. Add transitions and suggested on-screen text per block from the improved prompt and visual direction.
8. Write the CTA voiceover over the end card, using `cta_voiceover` from the improved prompt and the recommended CTA from `engagement_plan`.
9. Write the caption: an engaging opening line, 2–4 short lines of context, the CTA, and the mandatory hashtag set. Do not trim or reorder the mandatory hashtags.
10. Add 2–3 alternate hook lines under "Other hook lines to test".
11. Assemble the final 11-part output (below).

## Output contract

Return a `video_script` object:

```json
{
  "script": [
    {
      "time": "0-3s",
      "block": "Hook",
      "spoken": "…",
      "scene_direction": "…",
      "on_screen_text": "…"
    }
  ],
  "caption": "…\n\n#Meelte #LocalDiscovery #ShopLocal #Bengaluru #Ranchi #Gaya #SupportLocal #LocalBusiness",
  "scene_table": "| Time | What we see | Dialogue | Phone screen |…",
  "cta_voiceover": "…",
  "alternate_hooks": ["…", "…"],
  "duration_seconds": 35,
  "assembled_output": {
    "video_objective": "…",
    "target_audience": "…",
    "hooks": "30+ hooks from hook-library",
    "top_5_hooks": "…",
    "reasons": "…",
    "ready_to_record_script": "…",
    "visual_direction": "…",
    "on_screen_text": "…",
    "cta_variations": "…",
    "social_media_caption": "…",
    "community_building_objective": "…"
  }
}
```

The `assembled_output` mirrors `req.txt` §6 and must contain all 11 items before delivery. The `scene_table` is the same script in house format for recording.

## Stage output

At this stage, return `research_summary`, `improved_prompt`, and the complete `video_script`. This is the final video script stage — the improved prompt and research summary are carried forward, not regenerated. The deliverable is a `.md` script file, never a video file.

## Quality checklist

- [ ] Hook is verbatim from the hook library and lands in the first 3 seconds.
- [ ] Every block has a timestamp, scene direction, and on-screen text suggestion.
- [ ] Language sounds spoken, not written.
- [ ] No advertisement tone, corporate language, or generic motivation.
- [ ] The engagement question appears inside the content.
- [ ] CTA is the recommended one from `engagement_plan`.
- [ ] Caption contains the full mandatory hashtag set, unchanged.
- [ ] Scene table has four columns, contiguous timings, and a named speaker per dialogue line.
- [ ] Phone screen column uses a known screen from `refernces/` or a plain description — no invented clip id.
- [ ] CTA voiceover and 2–3 alternate hooks are present after the table.
- [ ] All 11 output items are present.
- [ ] No invented facts, prices, statistics, quotes, or results.

## Example

**Topic:** neighbourhood library, hook = "Maybe the library isn't really about books at all."

- 0–3s: hook, close-up of a library door opening.
- 3–8s: "You walk in for a book and leave having talked to three people." Medium shot, shelves.
- 8–25s: "Last week I watched someone ask for a recommendation and end up discussing football for twenty minutes." Two-shot, warm light.
- 25–35s: "That's the bit we forget — a community needs a place to bump into each other."
- Final: engagement question and CTA from the engagement plan.

## Constraints and failure cases

- **No approved hook:** Stop and get one from `hook-library`; never invent a hook here.
- **Script drifts from brief:** Send it back to `community-video-strategy` rather than patching the message silently.
- **Caption-only request:** Produce only the caption; do not regenerate the script.
- **Fact risk:** If a line needs a number or quote the user did not supply, replace it with a specific but non-numeric observation.

## Sources

Adapted from `req.txt` — Scriptwriting Guidelines, Video Script Structure, Output Requirements, section 3, section 6. Hand-authored; `Source: untracked`.
