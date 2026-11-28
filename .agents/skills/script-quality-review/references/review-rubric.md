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
- Mandatory hashtag set from `refernces/` is missing or reordered.

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

## Special Gate: meelTe App Promotion Videos

For meelTe app promotion videos, the following are **Critical Failures** (verdict must be `revise`):
1. **Hook failure:** First spoken line not meeting hook rules (must be a loud, relatable problem in everyday Hinglish, 8 words or fewer, no greeting or logo intro).
2. **Brand mention count/timing:** "meelTe" not spoken 3 to 4 times, or first mention not by 7s.
3. **Missing core value prop:** New viewer cannot tell what meelTe does (nearby people see local offers).
4. **Incorrect ending CTA:** Closing VO does not match exact line: *"Download the meelTe app. Now available on Play Store and App Store."* or missing badges on end card.
5. **Duration / word count drift:** Video not exactly 25s, or spoken dialogue exceeds ~55 words.
6. **False product claims:** Showing start/end times or countdowns (dates only: 12:00 AM to 11:59 PM), claiming payment processing, promising footfall/sales numbers, or claiming self-serve merchant onboarding.
7. **Testimonial misrepresentation:** Presenting acted customer as a real testimonial.
8. **Missing AI prompts / bad prompts:** Missing AI video prompts or prompts containing AI text/logos/app screens.
9. **Hook count mismatch:** Hook library header count does not match the list count.
10. **Repetitive boilerplate cloning:** Dialogue or scene directions in beats 3–7s or 7–11s copied verbatim from previous scripts rather than crafted for the specific shop scenario.
