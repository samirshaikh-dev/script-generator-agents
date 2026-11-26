---
name: hook-library
description: Use when generating opening hooks for a community-building video, when a brief asks for 3 hooks or a large hook library, when hooks feel repetitive or clickbaity, or when you need to select and justify the strongest openings. Owns hook generation, category coverage, top-5 selection, and psychological angles.
---

# Hook Library

Produces a wide, varied set of first-1–3-second openings for a community video, then selects and justifies the strongest five. Volume is a means to variety, not the goal.

## When to use

- A video brief is approved and openings are needed.
- The user asks for "hooks", "3 hooks", "30 hooks", or "better openings".
- Existing hooks all sound the same, too polished, or like clickbait.
- A hook must be matched to a specific psychological angle.

## Inputs

- `improved_prompt` from `video-prompt-expansion` — its `key_message`, `tone`, `audience`, and `beat_sheet[0]` are the hook's source of truth.
- `video_brief` from `community-video-strategy`.
- `req.txt` — Hook Generation, Hook Categories A–Z, Hook Quality Rules, section 3.
- `references/hook-categories.md` — the full category table with example shapes.

The hook must fit the expanded concept and the user's original words. Do not generate hooks from a topic you inferred yourself.

## Procedure

1. **Generate at least 30 hooks.** Aim for 50–100 when the topic supports that much variety. Never stop at 30 because it is the stated minimum.
2. **Cover distinct angles, not rewrites.** Spread hooks across the 26 categories in the reference. Every hook must differ in psychology or storytelling technique, not just wording.
3. **Apply the quality rules to every hook** (below). Discard any that fail.
4. **Select the top 5.** Choose for fit with the audience and objective, not for shock value alone.
5. **Explain the psychological angle** behind each of the five in one short sentence.
6. **Write one distinct opening variation** for each selected hook — the first line as it will actually be spoken.
7. **Recommend the single strongest hook** for the final script and hand it to `video-scriptwriting`.

### Internal library vs delivered script

The 30+ hooks are the internal creative engine required by `req.txt`. The house script format in `refernces/test Script.md` shows only one selected hook plus 2–3 "Other hook lines to test". Reconcile them this way:

- Keep all 30+ in `hook_set` and in the final 11-part package.
- In the scene-by-scene house script, show the selected hook at `0-3s` and put 2–3 alternates under "Other hook lines to test".
- Never trim the internal library to match the shorter script display.

## Hook quality rules

Every hook must:

- Capture attention within the first 1–3 seconds.
- Sound natural when spoken aloud.
- Be concise and easy to understand.
- Create curiosity, emotion, or relatability.
- Match the actual topic of the video.
- Avoid unnecessary clickbait.
- Avoid repetitive sentence structures.
- Be suitable for short-form video platforms.

Never fabricate a statistic, testimonial, or urgent deadline to make a hook land.

## Category coverage

Use the 26 categories A–Z in `references/hook-categories.md`:

A Curiosity · B Question · C Problem-Based · D Relatable · E Contrarian · F Storytelling · G Emotional · H Shock/Pattern-Interrupt · I Direct-Address · J Challenge · K Confession · L Comparison · M Myth-Busting · N Community-Identity · O Observation · P FOMO · Q Humour · R Data/Fact · S Scenario · T List-Based · U Negative · V Insider/Secret · W Social-Proof · X Future-Vision · Y Interactive · Z Local/Neighbourhood.

Favour these five styles often for community content:

1. **Relatable** — "Have you ever noticed that…"
2. **Curiosity** — "There's something about our neighbourhood that…"
3. **Contrarian** — "Maybe the problem isn't what you think it is…"
4. **Emotional** — "Sometimes, all we need is…"
5. **Interactive** — "Let's settle this once and for all…"

## Output contract

Return a `hook_set` object:

```json
{
  "hooks": [
    { "id": 1, "category": "D Relatable", "text": "…" }
  ],
  "top_hooks": [
    {
      "id": 7,
      "category": "G Emotional",
      "text": "…",
      "psychological_angle": "one sentence",
      "opening_variation": "first spoken line"
    }
  ],
  "recommended_hook_id": 7,
  "coverage": ["A", "B", "D", "…"],
  "discarded_count": 0
}
```

Return at least 30 `hooks` entries. Return exactly 5 `top_hooks`.

## Quality checklist

- [ ] 30+ hooks generated, 50–100 where the topic allows it.
- [ ] No two hooks are the same idea in different words.
- [ ] At least 12 distinct categories are represented.
- [ ] Every hook passes all eight quality rules.
- [ ] Exactly 5 top hooks, each with a psychological angle and opening variation.
- [ ] One recommended hook selected for the script.
- [ ] No fabricated numbers, quotes, or results.

## Example

**Topic:** the neighbourhood library.

- D Relatable: "Have you ever walked past a place every day and realised you've never actually been inside?"
- N Community-Identity: "This is the one place in our neighbourhood where nobody asks you to buy anything."
- E Contrarian: "Maybe the library isn't really about books at all."
- Y Interactive: "Let's settle this: silent reading or talking about the book afterwards?"
- O Observation: "There's a person who sits by the window every Tuesday. Nobody knows why."

## Constraints and failure cases

- **Thin topic:** If 30 genuinely different angles are impossible, say so and deliver the honest count rather than padding with near-duplicates.
- **Sensitive topic:** Drop shock, contrarian, and FOMO angles that would trivialise harm or target a vulnerable group.
- **Hook/script mismatch:** If the winning hook promises something the script cannot deliver, replace the hook — never inflate the script.
- **Never** use a hook that invents a fact, statistic, or quote.

## Sources

Adapted from `req.txt` — Hook Generation, Hook Categories A–Z, Hook Quality Rules, section 3, section 7, and the "five hook styles" recommendation. Hand-authored; `Source: untracked`.
