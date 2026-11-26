---
name: community-engagement-cta
description: Use when writing the engagement moment or call to action of a community video, when a CTA sounds like "follow us for more", or when a brief needs participation rather than passive views. Owns the engagement question, CTA variations, and the viewer-to-participant ladder.
---

# Community Engagement CTA

Designs the moment where a viewer becomes a participant. The ultimate goal is not views or followers — it is turning viewers into participants, participants into regular members, and regular members into an active, connected community.

## When to use

- A script needs its engagement question and closing CTA.
- The current CTA is generic ("follow us for more", "link in bio").
- The brief asks how the video builds community.
- You need several CTA options for the same video.

## Inputs

- `video_brief` from `community-video-strategy`.
- The recommended hook and main message from `hook-library` / `video-scriptwriting`.
- `req.txt` — Engagement Moment, Call to Action, section 5, participation goal.

## Procedure

1. **Write the engagement moment** — one interesting question placed inside the main content, not only at the end. It must be answerable in a comment without insider knowledge.
2. **Pick a CTA style** from the list below that matches the ladder step in the brief. Use a different style from the previous video in the same series where possible.
3. **Write 3–5 CTA variations** using different styles. Never make all of them "comment below".
4. **Check the ask is small.** The first step must be something a viewer can do in one sentence or one click.
5. **State the participation path** — what happens after they comment (e.g. "we'll collect the answers in the next video").
6. **Remove any "follow us for more" default** unless the user explicitly asks for it.

## CTA styles

- Ask viewers to comment.
- Ask them to share personal experiences.
- Invite them to tag someone.
- Encourage them to share recommendations.
- Ask them to participate in a discussion.
- Invite them to contribute an idea.
- Encourage them to become part of the community.

## Good CTA shapes

- "What would you add to this list? I'll pin the best answer."
- "Tag the person you'd bring with you."
- "Tell us the [thing] nobody warned you about — we're collecting them for the next video."
- "If you've been on the other side of this, what did you do?"
- "Vote with a comment: [A] or [B]. We'll do a follow-up on whichever wins."

## Output contract

Return an `engagement_plan` object:

```json
{
  "engagement_moment": "question placed inside the main content",
  "placement": "timestamp or section",
  "ladder_step": "viewer -> participant | participant -> regular | regular -> active",
  "cta_variations": [
    { "style": "share an experience", "text": "…" },
    { "style": "tag someone", "text": "…" },
    { "style": "contribute an idea", "text": "…" }
  ],
  "recommended_cta": "…",
  "participation_path": "what happens after they respond",
  "community_building_rationale": "one sentence"
}
```

## Quality checklist

- [ ] The engagement question appears inside the content, not only at the end.
- [ ] The question is easy to answer publicly.
- [ ] At least 3 CTA variations, each a different style.
- [ ] No default "follow us for more" or "like and subscribe".
- [ ] The ask is one small action, clearly stated.
- [ ] The participation path gives a reason to return.
- [ ] No fake urgency, giveaway, or invented result.

## Constraints and failure cases

- **Sensitive topic:** Replace "tag someone" or public-sharing prompts with a private-reflection question when the topic involves grief, health, money, or identity.
- **No community to join:** If there is no real community space, ask viewers to contribute an idea that shapes the next video rather than inventing a group.
- **Over-asking:** Never stack three or more requests in one CTA. One action per variation.
- **Never** promise a response, giveaway, or outcome you cannot deliver.

## Sources

Adapted from `req.txt` — Engagement Moment, Call to Action, section 5, and the participation goal in the final note. Hand-authored; `Source: untracked`.
