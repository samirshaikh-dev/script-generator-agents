---
name: video-input-research
description: Use when the user supplies a short 4-5 line video idea, when a brief is vague or feature-led, or before any hook or script is written. Analyzes the raw input for goal, audience, tone, key message, and missing details, and returns a research summary with intent anchors and claims to verify.
---

# Video Input Research

The first stage of the pipeline. It reads a short user idea and produces a research summary — without rewriting or improving it yet. Improvement is the next stage (`video-prompt-expansion`).

## When to use

- The user gives a rough 4–5 line description of the video they want.
- A request is too thin to script directly.
- You need to separate what the user actually said from what you are assuming.
- A request involves app rewards, prices, offers, or other claims that must be verified.

## Inputs

- The user's raw input, captured verbatim.
- `refernces/test Script.md` — house script format example.
- `refernces/Videos Scripts.md` — script library and claim-verification warning.
- `req.txt` — primary objectives and content pillars.

## Procedure

1. **Capture the raw input verbatim.** This is the `intent_anchor`. Never paraphrase it away.
2. **Read the reference files.** They carry the house format and the product facts you are allowed to use. Do not invent app screens, features, reward values, or offer numbers that are not in the references or the user's input.
3. **Extract observed facts** — only what the user actually said or what the references state.
4. **Identify the goal.** Prefer one of the six objectives in `req.txt`. If the request is an app-feature video, state the product goal in plain words as well.
5. **Identify the audience** as a specific, relatable group. If absent, mark it as an assumption.
6. **Identify the tone** from the user's words and the reference house style (warm, conversational, Hinglish for local-shop scenarios). Mark it as an assumption if inferred.
7. **Identify the key message** — the single idea the viewer should leave with.
8. **List missing details** that affect production: duration, platform, language, characters, setting, app screen or feature shown, offer numbers, city/location, CTA, caption.
9. **Resolve each missing detail** as `assumed` (with value and reason) or `needs_user_input`. Only mark `needs_user_input` when guessing would change a truth claim — a price, discount, deadline, reward value, voucher partner, redemption limit, or testimonial.
10. **Flag claims to verify.** Coin values, voucher partner, and redemption limits must match the live app and current terms. Carry this as a verification requirement for any reward-related video.
11. **Set `intent_preserved: true`** only when every explicit element of the raw input is still represented.

## Output contract

Return a `research_summary` object:

```json
{
  "original_input": "verbatim",
  "observed_facts": ["…"],
  "goal": "…",
  "audience": "…",
  "tone": "…",
  "key_message": "…",
  "missing_details": [
    { "field": "duration", "status": "assumed", "value": "25s", "reason": "house default in reference scripts" },
    { "field": "discount", "status": "needs_user_input", "value": null, "reason": "price claim cannot be invented" }
  ],
  "reference_sources": ["refernces/test Script.md", "refernces/Videos Scripts.md"],
  "claims_to_verify": ["…"],
  "intent_preserved": true
}
```

Also return a short `research_summary_text` (5–8 lines) suitable for showing the user at this stage.

## Stage output

At this stage, return: `research_summary` + `research_summary_text`. The improved prompt and final script do not exist yet — say so explicitly rather than inventing them.

## Quality checklist

- [ ] `original_input` is verbatim.
- [ ] Goal, audience, tone, and key message are each stated once, clearly.
- [ ] Every missing detail is either assumed with a reason or marked `needs_user_input`.
- [ ] No price, discount, reward value, or deadline was assumed.
- [ ] Reward-related requests carry the verification warning.
- [ ] Reference files are named as sources.
- [ ] `intent_preserved` reflects an honest check.

## Constraints and failure cases

- **Empty or one-word input:** Ask one clarifying question; do not research a topic that does not exist.
- **Contradictory input:** Report the contradiction in `missing_details` with `needs_user_input` rather than silently choosing one.
- **Reward/offer video:** Stop at this stage if the reward value, voucher partner, or redemption limit is required and not supplied or verifiable.
- **Reference mismatch:** If the user asks for a screen or feature that is not in the references, mark it `needs_user_input`; do not invent a screen name or clip id.

## Sources

Adapted from `refernces/test Script.md`, `refernces/Videos Scripts.md`, and `req.txt`. Hand-authored; `Source: untracked`.
