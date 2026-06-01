# Create Plan

Create a detailed implementation plan for a ZAVINO content project, campaign, research task, or workspace change. Plans are thorough documents that capture full context, rationale, and step-by-step tasks needed to execute with complete clarity.

## Variables

request: $ARGUMENTS (describe what you want to plan — content series, campaign, platform strategy, new command, structural change, etc.)

---

## Instructions

- **IMPORTANT:** You are creating a PLAN, not implementing changes. Research thoroughly, think deeply, then output a comprehensive plan document.
- Use your reasoning to think hard about the request, ZAVINO's content strategy, and the best approach.
- Research the workspace to understand existing patterns, conventions, and how this fits.
- Create the plan in the `plans/` directory with filename: `YYYY-MM-DD-{descriptive-name}.md`
  - Use today's date
  - Replace `{descriptive-name}` with a short, kebab-case name
  - Examples: `2026-05-26-ai-tools-series.md`, `2026-05-26-weekly-newsletter-launch.md`, `2026-05-26-competitor-analysis.md`
- Fill out every section of the Plan Format below. Replace all `<placeholders>` with specific, actionable content.
- Be thorough — this plan will be executed by `/implement` and needs enough detail to execute without ambiguity.
- Always factor in ZAVINO's voice (casual, Persian, no fluff) and the target audience when making recommendations.

---

## Research Phase

Before writing the plan, investigate:

1. **Read core context files:**
   - `CLAUDE.md` — workspace overview and ZAVINO identity
   - `context/brand-info.md` — voice, pillars, and positioning
   - `context/strategy.md` — current priorities
   - `context/current-data.md` — live metrics and trending topics

2. **Explore relevant areas:**
   - If creating a content series: check `content/` and `outputs/` for existing patterns
   - If building a campaign: check `plans/` for past campaign structures
   - If adding a command: read existing commands in `.claude/commands/`
   - If doing research: check `research/` for existing work on the topic

3. **Understand connections:**
   - How does this connect to ZAVINO's current strategic priorities?
   - Which platform(s) is this for — Instagram, Twitter/X, newsletter?
   - What content format works best (post, carousel, thread, reel)?
   - What audience segment is this targeting?

---

## Plan Format

Write the plan using this exact structure:

```markdown
# Plan: <descriptive title>

**Created:** <YYYY-MM-DD>
**Status:** Draft
**Request:** <one-line summary of what was requested>

---

## Overview

### What This Plan Accomplishes

<2-3 sentences describing the end result and why it matters for ZAVINO>

### Why This Matters

<Connect this to ZAVINO's goals — audience growth, engagement, brand voice, content consistency, etc.>

---

## Current State

### Relevant Existing Structure

<List files, folders, or patterns that exist and relate to this work>

### Gaps or Problems Being Addressed

<What's missing, inconsistent, or suboptimal that this plan fixes?>

---

## Proposed Changes

### Summary of Changes

<Bulleted list of all changes or deliverables at a high level>

### New Files to Create

| File Path         | Purpose                            |
| ----------------- | ---------------------------------- |
| `path/to/file.md` | Description of what this file does |

### Files to Modify

| File Path         | Changes                      |
| ----------------- | ---------------------------- |
| `path/to/file.md` | Description of modifications |

### Files to Delete (if any)

<List any files being removed and why>

---

## Content Details (if applicable)

### Platform
<Instagram / Twitter/X / Newsletter / Multi-platform>

### Format
<Post / Carousel / Thread / Reel script / Newsletter>

### Tone & Style Notes
<Any specific voice guidance beyond the default ZAVINO casual Persian style>

### Persian Copy Notes
<Any specific language, expressions, or cultural nuances to apply>

---

## Design Decisions

### Key Decisions Made

1. **<Decision>**: <Rationale>
2. **<Decision>**: <Rationale>

### Alternatives Considered

<What other approaches were considered and why they were rejected?>

### Open Questions (if any)

<List any decisions that need input before implementation>

---

## Step-by-Step Tasks

Execute these tasks in order during implementation.

### Step 1: <Task Title>

<Detailed description of what to do>

**Actions:**
- <Specific action>
- <Specific action>

**Files affected:**
- `path/to/file.md`

---

### Step 2: <Task Title>

<Detailed description of what to do>

**Actions:**
- <Specific action>
- <Specific action>

**Files affected:**
- `path/to/file.md`

---

<Continue with as many steps as needed. Include:>
<- Creating content files with full Persian copy>
<- Modifying existing files with specific edits>
<- Updating context files and cross-references>
<- Validation steps>

---

## Connections & Dependencies

### Files That Reference This Area
<List any files that link to or depend on areas being changed>

### Updates Needed for Consistency
<List any context, strategy, or reference files that need updating>

### Impact on Existing Workflows
<Describe how this affects existing commands, outputs, or content series>

---

## Validation Checklist

- [ ] <e.g., "Content saved to correct folder with right filename">
- [ ] <e.g., "Persian copy reviewed for natural tone — not stiff or translated-sounding">
- [ ] <e.g., "CLAUDE.md updated if workspace structure changed">
- [ ] <e.g., "current-data.md updated with any new metrics or trending topics">

---

## Success Criteria

The implementation is complete when:

1. <Specific, measurable criterion>
2. <Specific, measurable criterion>
3. <Specific, measurable criterion>

---

## Notes

<Any additional context, platform-specific considerations, future content ideas, or related opportunities>
```

---

## Quality Standards

- **Completeness:** Every section filled out — no generic placeholders left
- **Actionability:** Steps are detailed enough that `/implement` can execute without asking questions
- **ZAVINO-aligned:** All recommendations reflect ZAVINO's casual Persian voice and content pillars (AI, marketing, tech)
- **Consistency:** Follows existing workspace patterns and naming conventions
- **Clarity:** Someone unfamiliar with the project could understand and execute the plan

---

## Report

After creating the plan:

1. Provide a brief summary of what the plan covers
2. List any open questions that need input before implementation
3. Provide the full path: `plans/YYYY-MM-DD-{name}.md`
4. Remind to run `/implement plans/YYYY-MM-DD-{name}.md` to execute
