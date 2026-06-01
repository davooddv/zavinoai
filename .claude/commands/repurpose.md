# Repurpose

Take existing content and adapt it for a different platform or format. One piece of content → multiple outputs.

## Variables

request: $ARGUMENTS (path to existing content + target platform — e.g. "outputs/instagram/2026-05-26-android-apps.md → twitter thread")

---

## Instructions

### Step 1: Load Source Content

Read:
- The source file specified in $ARGUMENTS
- `context/brand-info.md`
- `.claude/rules/content/voice.md`

### Step 2: Understand What You Have

Identify:
- Original platform and format
- Core message and hook
- Key stats/facts used
- What worked about it

### Step 3: Adapt for Target Platform

**Instagram → Twitter thread:**
- Break into 5–10 tweets
- Each tweet = one idea, self-contained
- Tweet 1 = hook (same energy as Instagram hook)
- Last tweet = summary + CTA

**Twitter → Instagram:**
- Compress into single post or carousel
- Rework into tighter paragraphs
- Add visual slide suggestions if carousel

**Post → Reel script:**
- Write as spoken word (conversational Persian)
- Add visual cue notes: `[show screen recording]`, `[cut to text overlay]`
- Hook = first 3 seconds (most important)
- Total duration: 30–60 seconds

**Post → Newsletter section:**
- Expand with more context and detail
- Add a "what to do with this" section
- More formal than social — but still ZAVINO voice

### Step 4: Save Output

Save to correct `outputs/` subfolder:
- `outputs/instagram/YYYY-MM-DD-{slug}-ig.md`
- `outputs/twitter/YYYY-MM-DD-{slug}-tw.md`

### Step 5: Report

1. Show the repurposed content
2. Note any key adaptations made
3. File path saved
