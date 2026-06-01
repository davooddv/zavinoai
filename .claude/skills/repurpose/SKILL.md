---
name: repurpose
description: Adapt existing ZAVINO content from one platform/format to another
---

# Repurpose Skill

Takes a finished post and adapts it for a different platform or format — Instagram → Thread, Thread → Reel script, etc.

## Inputs
- Source file path
- Target platform/format

## Supported Conversions
- Instagram post → Twitter/X thread
- Twitter thread → Instagram carousel
- Post → Reel script (spoken word)
- Post → Newsletter section

## Process
1. Read source file and voice rules
2. Identify core message and hook
3. Restructure for target format
4. Save to `outputs/{platform}/YYYY-MM-DD-{slug}-{platform}.md`

## Use via
`/repurpose [source file] → [target format]`
