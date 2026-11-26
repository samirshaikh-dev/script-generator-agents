---
name: community-video-strategy
description: Use at the start of every community video request to define the video objective, target audience, purpose, and content pillar. Use when a brief is product-led and needs a community-first angle, when the audience or purpose is unclear, or when a concept risks sounding like an advertisement. Owns the community-building objective and the participation ladder.
---

# Community Video Strategy

Turns a rough topic into a community-first brief before any hook or script is written. It is the gate that keeps the video from becoming an ad.

## When to use

- Any community-building video script request.
- The topic is given but the audience, purpose, or pillar is not.
- A concept is feature-led or promotional and needs a belonging/trust angle.
- You need to state briefly how the video contributes to community building.

## Inputs

- The raw topic or "make a video about X" request.
- Any supplied audience, community, platform, or duration hints.
- `req.txt` — role, primary objectives, content pillars, creative standard.

## Procedure

1. **Identify the domain and real audience.** Who experiences this topic in daily life? Prefer a specific, relatable group ("new parents in our neighbourhood") over "everyone". If no audience is supplied, choose one and state it as an explicit default.
2. **Name the content pillar.** Pick one primary pillar from the list below. A video can touch several, but one must lead.
3. **Set the video objective.** Choose one of the six primary objectives. Write it as a behaviour change, not a reach target.
4. **Define the purpose in one sentence.** Explain what the viewer should understand, feel, or do — never "get views" or "grow followers".
5. **Map the participation ladder.** State where the viewer starts and which step this video asks them to take: viewer → commenter/participant → regular member → active, connected member.
6. **List constraints.** No invented facts, no fabricated statistics, no fake testimonials, no manufactured urgency, no corporate language, no generic motivation.
7. **Ask at most one clarification question**, and only when the answer materially changes the audience, the pillar, or a claim that cannot be invented.

## Content pillars

- Community awareness
- Everyday problems and shared experiences
- Local stories and people
- Educational content
- Questions and discussions
- Behind-the-scenes content
- Community success stories
- User-generated content
- Tips and recommendations
- Events and activities
- Community participation

## Primary objectives

1. Build connection — make viewers feel they belong to something meaningful.
2. Build trust — communicate authentically and establish credibility.
3. Encourage engagement — make people comment, share opinions, ask questions, participate.
4. Create awareness — help people understand the community, its purpose, and its value.
5. Drive participation — encourage viewers to join discussions and become active members.
6. Build relationships — make the audience feel heard, valued, and included.

## Output contract

Return a `video_brief` object:

```json
{
  "topic": "…",
  "audience": "…",
  "purpose": "one sentence",
  "primary_pillar": "one of the content pillars",
  "video_objective": "one of the six objectives",
  "participation_ladder_step": "viewer -> participant | participant -> regular | regular -> active",
  "default_assumptions": ["…"],
  "constraints": ["…"],
  "clarification_needed": null
}
```

Also return a one-sentence `community_building_rationale` explaining how the video turns viewers into participants.

## Quality checklist

- [ ] A specific human audience is named, not "everyone".
- [ ] One primary pillar and one primary objective are chosen.
- [ ] Purpose describes understanding, feeling, or participation — not views or followers.
- [ ] The ladder step names a concrete next action.
- [ ] Every default is stated out loud.
- [ ] No price, statistic, testimonial, deadline, or result was invented.
- [ ] The concept would not read as a product advertisement.

## Example

**Input:** "a video about our neighbourhood library"

**Output:** audience = "people in the neighbourhood who did not know the library is more than books"; pillar = Community awareness; objective = Drive participation; purpose = "show that the library is a place to meet, not just to borrow"; ladder step = viewer → participant; default = 35–45 second talking-head short; constraints = no invented membership numbers, no fake quotes.

## Constraints and failure cases

- **Feature-led brief:** If the user only supplies a product or service, reframe around the shared experience it touches. Ask one question only if the reframe is impossible.
- **Sensitive local topic:** Do not invent neighbourhood problems or quote residents. Switch to an observational, non-claiming angle.
- **No community context:** If no community exists yet, define the "community" as the people sharing the experience and say so explicitly.
- **Never proceed** with an invented statistic, fake member story, or unsupported claim just to make the brief concrete.

## Sources

Adapted from `req.txt` — Role; Primary Objectives; Content Pillars; Creative Standard. Hand-authored; `Source: untracked`.
