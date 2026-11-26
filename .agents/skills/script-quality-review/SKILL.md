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

- `video_brief`, `hook_set`, `engagement_plan`, `video_script`, `visual_direction`.
- `req.txt` — Scriptwriting Guidelines, Hook Quality Rules, Final Output Format, Creative Standard.
- `references/review-rubric.md` — the full checklist with severity tags.

## Procedure

1. **Read the brief first.** Judge against the stated objective, audience, pillar, and ladder step — not against personal taste.
2. **Run the rubric in `references/review-rubric.md`** across all 11 output items.
3. **Tag each issue** critical, major, or minor.
4. **Return a verdict:**
   - `pass` — no critical or major issues.
   - `pass_with_notes` — only minor issues, listed.
   - `revise` — any critical issue, or two or more major issues.
5. **Route each issue to its owner**, never to a generic "rewrite":

   | Issue type | Route to |
   |---|---|
   | Objective, audience, pillar, invented fact in brief | `community-video-strategy` |
   | Hook quality, repetition, category gap, top-5 choice | `hook-library` |
   | Engagement question, CTA, "follow us for more" | `community-engagement-cta` |
   | Script tone, structure, timestamps, caption, missing output item | `video-scriptwriting` |
   | Shots, overlays, b-roll, music, pacing, filmability | `visual-direction` |

6. **Write one targeted instruction per issue** — name the block and the single change required.
7. **Cap revisions** at two rounds per script. On exhaustion, stop and report the remaining issues honestly.

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
  "revision_round": 1,
  "max_revision_rounds": 2,
  "summary": "one honest sentence"
}
```

## Quality checklist for the reviewer

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
