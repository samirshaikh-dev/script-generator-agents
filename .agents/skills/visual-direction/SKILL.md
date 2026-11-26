---
name: visual-direction
description: Use when adding camera shots, scene choices, text overlays, facial expressions, delivery style, b-roll, music mood, or editing and pacing to a community video script. Use when a script has no scene directions or when the visual plan fights the message. Owns the visual and delivery direction.
---

# Visual Direction

Turns a written script into something a person can actually record and edit, without stealing focus from the community message.

## When to use

- A script exists and needs shot-by-shot direction.
- The user asks for camera angles, scenes, overlays, b-roll, music, or pacing.
- A script reads well but has no visual plan.
- The visuals are over-produced relative to an authentic community tone.

## Inputs

- `video_script` from `video-scriptwriting`.
- `video_brief` from `community-video-strategy`.
- `req.txt` — Visual Direction, Video Script Structure, section 4.

## Procedure

1. **Match every script block to a shot.** One shot per block is normal; two only when the idea genuinely changes.
2. **Choose the camera angle and shot size** deliberately: close-up for emotion and confession, medium for conversation, wide for place and belonging, over-shoulder for observation.
3. **Set facial expression and delivery style** per block — warm, curious, matter-of-fact, amused. Keep it human, not presenter-polished.
4. **Define scene transitions** between blocks (cut, match cut, push in, handheld walk, freeze frame). Keep transitions simple.
5. **Write the on-screen text** for each block. Short, exact, legible. No paragraph of text on screen.
6. **List b-roll** that adds information, not decoration — the place, the hands, the ordinary detail the hook mentions.
7. **Set the background music mood** in one or two words (warm, low, playful, quiet) and note where it drops so the hook and CTA land clearly.
8. **Set editing and pacing** — fast cuts in the hook, slower in the story, a clean hold on the CTA.
9. **Flag anything that cannot be filmed** with the available resources and propose a simple alternative (phone on a window ledge, natural light, one location).

## Output contract

Return a `visual_direction` object:

```json
{
  "shots": [
    {
      "time": "0-3s",
      "shot": "close-up",
      "angle": "eye level",
      "expression": "curious",
      "delivery": "direct to camera",
      "scene": "…",
      "transition": "hard cut",
      "on_screen_text": "…",
      "b_roll": ["…"],
      "notes": "…"
    }
  ],
  "music": { "mood": "warm and low", "drops_at": ["0-3s", "CTA"] },
  "editing": "fast hook cuts, slower story, clean CTA hold",
  "location": "one location, natural light",
  "unfilmable_items": []
}
```

## Quality checklist

- [ ] Every script block has a shot.
- [ ] Shot sizes vary; the video is not one static talking head.
- [ ] Expressions and delivery are described, not left to the actor.
- [ ] On-screen text is short and matches the spoken line.
- [ ] B-roll adds meaning rather than filler.
- [ ] Music mood is stated and does not cover the hook or CTA.
- [ ] Pacing changes across the structure.
- [ ] The plan is filmable with a phone and one location.
- [ ] No claim is illustrated that the script does not make.

## Example

**Hook:** "Maybe the library isn't really about books at all."

- 0–3s: close-up, eye level, direct to camera, curious expression. Hard cut on the last word. On-screen text: "Not about books?"
- 3–8s: medium shot, handheld walk through the entrance. B-roll: the door, a chair, two people talking.
- 25–35s: wide shot of the reading area, natural light. Hold two seconds on the CTA.

## Constraints and failure cases

- **No filming access:** Do not invent scenes inside a private place. Use public, accessible shots and say so.
- **Sensitive participants:** Never direct a shot at an identifiable person without consent; use hands, backs, or empty-space details instead.
- **Text overload:** If on-screen text exceeds roughly eight words per shot, cut it.
- **Never** promise a look that requires gear, crew, or location access the user has not confirmed.

## Sources

Adapted from `req.txt` — Visual Direction, section 4, Script Structure scene directions. Hand-authored; `Source: untracked`.
