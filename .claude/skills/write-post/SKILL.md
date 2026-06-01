---
name: write-post
description: Write a complete ZAVINO post in Persian for Instagram or Twitter using the ZAVINO voice formula
---

# Write Post Skill

Generates a publish-ready Persian social media post following ZAVINO's exact voice, structure, and formula.

## Inputs
- Topic, idea, or path to a research file
- Target platform (instagram or twitter)

## Process
1. Load `context/brand-info.md` and `.claude/rules/content/voice.md` and `reference/post-examples.md`
2. Identify the sharpest angle on the topic
3. Write using the ZAVINO Formula: Hook → Proof → So What → Scale → Closing Punch
4. Verify: max 3 emojis, all at line ends, conversational Persian verb endings
5. Save draft to `content/posts/{platform}/YYYY-MM-DD-{slug}.md`

## Use via
`/write-post [topic or file path]`
