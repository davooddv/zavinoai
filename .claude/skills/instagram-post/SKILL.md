---
name: instagram-post
description: Generate a complete Instagram post with caption and carousel slide breakdown for ZAVINO
---

# Instagram Post Skill

Generates a full Instagram post including caption and (if carousel) slide-by-slide content breakdown.

## Inputs
- Topic or source research file
- Format: single | carousel (3–10 slides)

## Output Structure

### Single Post
- Caption with ZAVINO formula (Hook → Proof → So What → Scale → Punch)
- 3 hashtag suggestions (placed in first comment, not caption body)

### Carousel
- Slide 1: Hook slide (headline + subtext)
- Slides 2–N: One point per slide, scannable
- Last slide: Summary + CTA ("ذخیره کن" / "برای دوستت بفرست")
- Caption: Short hook + "برای دیدن همه اسلایدها بکش →"

## Persian Standards
- Caption: conversational, colloquial verb endings
- Slide text: slightly shorter and punchier than caption
- CTA always in Persian

## Use via
`/write-post [topic] instagram carousel` or `/write-post [topic] instagram single`
