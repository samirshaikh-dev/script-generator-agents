---
name: video-prompt-expansion
description: Use after video-input-research, when a short idea must become a clear, detailed, production-ready video prompt. Expands goal, audience, tone, key message, scenes, dialogue, phone screens, transitions, CTA, and caption while preserving the user's original intent word for word.
---

# Video Prompt Expansion

Turns the research summary into the production-ready prompt that drives every later stage. This is where a thin idea becomes specific — without changing what the user asked for. The prompt describes a script to be written and recorded by a human; it never requests video generation or rendering.

## When to use

- A `research_summary` exists from `video-input-research`.
- A user idea needs to be expanded before scripting.
- A draft prompt has drifted from the original request.
- You need a single prompt that strategy, hooks, scripting, and QA all consume.

## Inputs

- The verbatim `original_input` and `research_summary`.
- `refernces/test Script.md` — the house scene table and dialogue pattern.
- `refernces/Videos Scripts.md` — house format, app feature names, CTA and hashtag conventions.
- `req.txt` — script structure and output requirements.

## Procedure

1. **Start with the intent anchor.** Quote the user's original input at the top of the prompt. Every later section must be traceable to it or marked as an added specification.
2. **Fill the fixed fields:** goal, audience, tone, key message, duration, platform, language, setting, characters. Use research values; do not re-decide them.
3. **Write a one-line concept** a producer could understand without reading anything else.
4. **Build a scene beat sheet** from the house structure:

   | Time | What we see | Dialogue | Phone screen |
   |---|---|---|---|
   | 0–3s | Hook visual | Spoken hook, verbatim from the winning hook once selected | None or app screen |

   Beat lengths follow the reference pattern: 0–3s hook, then short beats of 4–9 seconds, resolving in a final CTA/end card. Total duration comes from research.
5. **Set the dialogue language and speaker style.** Match the reference house voice (Hinglish for local-shop and neighbourhood scenarios). Name speakers, not generic "voiceover", unless the reference uses voiceover.
6. **Specify phone screens** using only screens named in `refernces/` or the user's input. If a clip id from the reference library applies, name it; otherwise describe the screen in words. **Never invent a clip id.**
7. **Add transitions, music, and on-screen text** per beat. Keep transitions simple and on-screen text short.
8. **Write the CTA voiceover line** and the end card. Add the caption with the mandatory hashtag set from `refernces/` — the union of the mandatory set in `Videos Scripts.md` and the caption in `test Script.md`:

   `#meelTe #LocalDiscovery #ShopLocal #Bengaluru #Ranchi #Gaya #SupportLocal #LocalBusiness`

9. **List `preserved_elements[]`** — explicit ideas from the user's input carried into the prompt.
10. **List `added_specifications[]`** — everything you added, each with a reason.
11. **Carry forward `claims_to_verify`** from research. Never turn a claim into a fact.

## Output contract

Return an `improved_prompt` object:

```json
{
  "intent_anchor": "verbatim user input",
  "concept": "one line",
  "goal": "…",
  "audience": "…",
  "tone": "…",
  "key_message": "…",
  "production": {
    "duration_seconds": 25,
    "platform": "short-form vertical",
    "language": "Hinglish",
    "setting": "…",
    "characters": ["…"]
  },
  "beat_sheet": [
    { "time": "0-3s", "what_we_see": "…", "dialogue": "Speaker: …", "phone_screen": "None" }
  ],
  "transitions": ["…"],
  "music": "…",
  "on_screen_text": ["…"],
  "cta_voiceover": "…",
  "caption": "…",
  "hashtags": ["#meelTe", "…"],
  "preserved_elements": ["…"],
  "added_specifications": [{ "detail": "…", "reason": "…" }],
  "claims_to_verify": ["…"]
}
```

Also return `improved_prompt_text` — the full prompt as a single readable block, suitable for showing the user at this stage.

## Stage output

At this stage, return: `research_summary`, `improved_prompt`, and `improved_prompt_text`. The final script does not exist yet — say so explicitly.

## Quality checklist

- [ ] `intent_anchor` is verbatim.
- [ ] Every explicit element of the input appears in `preserved_elements`.
- [ ] Every addition is listed with a reason.
- [ ] No invented price, discount, deadline, reward value, testimonial, or clip id.
- [ ] Phone screens come only from references or the user's input.
- [ ] Beat sheet covers the full duration and ends with a CTA/end card.
- [ ] Mandatory hashtags are present in the caption.
- [ ] `claims_to_verify` carried forward unchanged.
- [ ] The prompt is specific enough to record from, without further questions.

## meelTe App Promotion Rule Override

When expanding a prompt for a **meelTe app promotion video**:
- **Duration & Platform:** Exactly 25 seconds, 9:16 vertical short.
- **Fixed Beat Sheet Structure:**
  - `0–3s`: Hook (loud, relatable problem in Hinglish, <= 8 words, unsold good stock).
  - `3–7s`: Friend suggests meelTe; shopkeeper asks what it is ("meelTe" spoken first by 7s).
  - `7–11s`: One plain line explaining the app: nearby people see local offers.
  - `11–16s`: Real app recording: set price, start date, end date. (No start/end times or countdown clock).
  - `16–20s`: A customer arrives and says they saw the offer on meelTe.
  - `20–25s`: End card and download voiceover.
- **Brand Mentions:** Ensure "meelTe" is spoken 3 to 4 times across dialogue and CTA VO.
- **Closing CTA:** Must be exact: *"Download the meelTe app. Now available on Play Store and App Store."*
- **Word Budget:** Dialogue across beats must stay around ~55 words or fewer.
- **Brief Override:** These requirements replace user-supplied hooks or CTAs that violate promo rules; record changes in `added_specifications`.
- **Product Constraints:** Never include countdowns, start/end times, payment processing, or footfall promises. Carry dates only (12:00 AM to 11:59 PM).

## Constraints and failure cases

- **Intent drift:** If a later stage changes the goal, audience, or key message, route it back here — do not patch it downstream.
- **Missing truth claim:** If research marked a field `needs_user_input`, leave a placeholder in the prompt and stop; do not fill it with a guess.
- **Screen not in references:** Describe the screen in words and flag it as unverified rather than naming a clip id.
- **Over-specification:** Do not add a scene, character, or offer that the user did not imply. Specificity means concrete details, not new ideas.

## Sources

Adapted from `refernces/test Script.md`, `refernces/Videos Scripts.md`, and `req.txt`. Hand-authored; `Source: untracked`.
