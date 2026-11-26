# Script Review Rubric

Run every line against the 11 output items in `req.txt` §6. Tag each failure critical, major, or minor.

## Severity definitions

- **Critical** — breaks the community-first premise or the creative standard. Must fix before delivery.
- **Major** — materially weakens the video or the participation goal. Fix before delivery.
- **Minor** — polish issue. Deliver and list it.

## Rubric

| # | Item | Check | Severity if failed |
|---|---|---|---|
| 1 | Video objective | One clear objective from the six; behaviour-focused, not reach-focused | Major |
| 2 | Target audience | Specific human group named; not "everyone" | Major |
| 3 | 30+ hooks | At least 30 hooks, no near-duplicates, 12+ categories, all eight quality rules pass | Major if count/duplicates; Minor if coverage short |
| 4 | Top 5 hooks | Exactly 5 selected, each with a psychological angle and an opening variation | Major |
| 5 | Reasons | Each top hook has a one-sentence reason tied to audience/objective | Minor |
| 6 | Ready-to-record script | Hook verbatim; 0–3/3–8/8–25/25–35/final structure; timestamps; spoken lines; natural spoken language; no ad tone | Critical if ad tone or hook missing; Major otherwise |
| 7 | Visual direction | Shot per block, angle, expression, delivery, transitions, b-roll, music, pacing, filmable | Major if missing; Minor if thin |
| 8 | On-screen text | Short, exact, legible, matches spoken line | Minor |
| 9 | CTA variations | 3+ distinct styles, one small action, no "follow us for more" default | Major |
| 10 | Social caption | Engaging opening, short context, CTA, relevant hashtags; not a tag wall | Minor |
| 11 | Community-building objective | Explicit explanation of how viewers become participants | Major |

## Cross-cutting critical failures

Any of these is critical regardless of which item it appears in:

- The final script drops, replaces, or contradicts an explicit element of the verbatim original user input.
- `research_summary`, `improved_prompt`, or `video_script` is missing at the final stage.
- The deliverable is a video file, or the prompt requests video generation/rendering instead of a written script.
- Invented price, statistic, testimonial, deadline, guarantee, reward value, voucher partner, or result.
- Mandatory hashtag set from `refernces/Videos Scripts.md` is missing or reordered.

## Major failures specific to the house format

- Scene table is not four columns (`Time`, `What we see`, `Dialogue`, `Phone screen`).
- Timings are not contiguous, or no speaker is named in a dialogue line.
- A clip id is invented instead of naming a known screen or describing it in words.
- No CTA voiceover over the end card, or no 2–3 alternate hook lines.
- Fabricated urgency, scarcity, or social proof.
- Advertisement tone, corporate language, or generic motivational statements.
- Hook promises something the script does not deliver.
- Humour, shock, contrarian, or tag-a-friend framing on grief, health, money, or identity.
- A participant shown or named without consent implied by the direction.
- One of the 11 output items is entirely absent.

## Verdict rule

- Any critical → `revise`.
- No critical, two or more major → `revise`.
- No critical, zero or one major → `pass_with_notes` if minors exist, otherwise `pass`.
- Max two revision rounds per script; on exhaustion stop and report remaining issues.
