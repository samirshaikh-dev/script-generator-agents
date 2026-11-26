---
name: script-quality-review
description: Use before delivering any community video script, when a script must be checked against the brief and brand of authenticity, when hooks feel repetitive or clickbaity, or when a revision needs routing to the right owner. Owns the pass/fail verdict, severity tags, and targeted revision instructions.
---

# Script Quality Review

Final gate. Reviews a complete script package against the brief and the community-building standard, then returns a verdict with severity-tagged issues and targeted revision instructions.

## When to use

- A script package is assembled and about to be delivered.
- A draft needs a pass/fail decision before recording.
- A revision request arrives and you must decide which agent owns the fix.
- A series is drifting into advertisement tone or repetitive hooks.

## Inputs

- `original_input`, `research_summary`, `improved_prompt`, `video_brief`, `hook_set`, `engagement_plan`, `video_script`, `visual_direction`.
- `refernces/test Script.md` and `refernces/Videos Scripts.md` — house format and mandatory hashtags.
- `req.txt` — Scriptwriting Guidelines, Hook Quality Rules, Final Output Format, Creative Standard.
- `references/review-rubric.md` — the full checklist with severity tags.

## Procedure

1. **Read the verbatim original input first**, then the research summary and improved prompt. Check that every explicit element of the user's idea survived. Intent drift is a critical failure.
2. **Read the brief.** Judge against the stated objective, audience, pillar, and ladder step — not against personal taste.
3. **Run the rubric in `references/review-rubric.md`** across all 11 output items.
4. **Tag each issue** critical, major, or minor.
5. **Return a verdict:**
   - `pass` — no critical or major issues.
   - `pass_with_notes` — only minor issues, listed.
   - `revise` — any critical issue, or two or more major issues.
6. **Route each issue to its owner**, never to a generic "rewrite":

   | Issue type | Route to |
   |---|---|
   | Original intent changed, over/under-expanded prompt | `video-prompt-expansion` |
   | Goal, audience, tone, or missing detail misread | `video-input-research` |
   | Objective, audience, pillar, invented fact in brief | `community-video-strategy` |
   | Hook quality, repetition, category gap, top-5 choice | `hook-library` |
   | Engagement question, CTA, "follow us for more" | `community-engagement-cta` |
   | Script tone, structure, timestamps, caption, missing output item | `video-scriptwriting` |
   | Shots, overlays, b-roll, music, pacing, filmability | `visual-direction` |

7. **Write one targeted instruction per issue** — name the block and the single change required.
8. **Cap revisions** at two rounds per script. On exhaustion, stop and report the remaining issues honestly.

## Output contract

Return a `quality_review` object:

```json
{
  "verdict": "pass | pass_with_notes | revise",
  "issues": [
    {
      "severity": "critical | major | minor",
      "category": "script tone",
      "location": "8-25s block",
      "description": "…",
      "route_to": "video-scriptwriting",
      "instruction": "one specific change"
    }
  ],
  "checked_items": ["all 11 output items"],
  "intent_preserved": true,
  "stage_outputs_present": ["research_summary", "improved_prompt", "video_script"],
  "revision_round": 1,
  "max_revision_rounds": 2,
  "summary": "one honest sentence"
}
```

## Stage output

At this stage, return `research_summary`, `improved_prompt`, and the final `video_script` alongside the `quality_review`. This is the last stage before delivery, so all three artifacts must be present.

## Quality checklist for the reviewer

- [ ] The verbatim original input was compared with the final script; intent is preserved.
- [ ] Research summary, improved prompt, and final script are all present.
- [ ] Mandatory hashtag set is present in the caption, unchanged.
- [ ] Scene table has four columns, contiguous timings, and a named speaker per line.
- [ ] All 11 output items were checked, not sampled.
- [ ] Every issue has a severity, a location, an owner, and a one-change instruction.
- [ ] No issue was fixed silently by the reviewer.
- [ ] Verdict follows the rule above, exactly.
- [ ] Revision round is incremented and capped.
- [ ] The summary does not claim success when the verdict is `revise`.

## Example

**Issue:** "Follow us for more" as the only CTA.

```json
{
  "severity": "major",
  "category": "CTA",
  "location": "final seconds",
  "description": "Generic follow request; no participation ask.",
  "route_to": "community-engagement-cta",
  "instruction": "Replace with one style-matched CTA that asks viewers to contribute an idea."
}
```

## Constraints and failure cases

- **Missing input:** If the brief is missing, stop — do not review a script in a vacuum.
- **Subjective preference:** "I would have written it differently" is not an issue. Require a rubric line.
- **Sensitive topic:** An otherwise good humour or tag-a-friend CTA on grief, health, money, or identity is a major issue.
- **Never** deliver a `revise` script as if it passed, and never bump the revision cap without user approval.

## Sources

Adapted from `req.txt` — Scriptwriting Guidelines, Hook Quality Rules, section 5, section 6, section 7, Creative Standard. Hand-authored; `Source: untracked`.
