# Implement

Execute an implementation plan created by `/create-plan`. Read the plan thoroughly, execute each step in order, and report on the completed work.

## Variables

plan_path: $ARGUMENTS (path to the plan file, e.g., `plans/2026-05-26-ai-tools-series.md`)

---

## Instructions

### Phase 1: Understand the Plan

1. **Read the plan file completely.** Do not skim — understand every section.
2. **Verify prerequisites:**
   - Are there open questions that need answers before proceeding?
   - Are there dependencies on external resources or decisions?
   - If blockers exist, stop and ask before proceeding.
3. **Confirm the plan is ready:**
   - Status should be "Draft" or "Ready"
   - All sections should be filled out (no placeholder text remaining)

---

### Phase 2: Execute the Plan

1. **Follow the Step-by-Step Tasks in exact order.**
   - Complete each step fully before moving to the next
   - If a step involves creating a content file, write the complete content — not a stub
   - If a step involves modifying a file, read it first, then apply changes precisely

2. **For each task:**
   - Read any files that will be affected
   - Make the changes specified
   - Verify the change is correct before proceeding

3. **Handle issues gracefully:**
   - If a step can't be completed as written, note the issue and adapt if the intent is clear
   - If you're unsure how to proceed, ask rather than guessing
   - Document any deviations from the plan

4. **ZAVINO content standards:**
   - All audience-facing copy must be in natural, conversational Persian (Farsi)
   - Tone must match ZAVINO's voice: casual, clear, no fluff, like a knowledgeable friend
   - Finalized, publish-ready content goes to `outputs/` in the correct platform subfolder
   - Drafts and work-in-progress stay in `content/`

---

### Phase 3: Validate

1. **Run through the Validation Checklist** from the plan
   - Check off each item
   - Note any that fail

2. **Verify Success Criteria** are met
   - Confirm each criterion is satisfied
   - Note any gaps

3. **Check cross-references and consistency:**
   - Ensure new files are referenced where they should be
   - Verify `CLAUDE.md` is updated if workspace structure changed
   - Confirm naming conventions are followed
   - Update `context/current-data.md` if new metrics, tools, or trending topics were surfaced

---

### Phase 4: Update Plan Status

After implementation, update the plan file:

1. Change `**Status:** Draft` to `**Status:** Implemented`
2. Add an Implementation Notes section at the end:

```markdown
---

## Implementation Notes

**Implemented:** <YYYY-MM-DD>

### Summary
<Brief summary of what was done>

### Deviations from Plan
<List any changes made during implementation, or "None">

### Issues Encountered
<List any problems hit and how they were resolved, or "None">
```

---

## Quality Standards

- **Thoroughness:** Every step in the plan is executed, not skipped
- **Precision:** Changes match what the plan specifies
- **Completeness:** Content files are fully written, not stubbed out
- **ZAVINO-aligned:** All outputs reflect ZAVINO's Persian voice, audience, and content pillars
- **Traceability:** Deviations are documented

---

## Report

After implementation, provide:

1. **Summary:** Bulleted list of work completed
2. **Files changed:** List all files created, modified, or deleted
3. **Validation results:** Status of each checklist item
4. **Deviations:** Any changes from the original plan
5. **Next steps:** Any follow-up actions (scheduling, publishing, repurposing, etc.)

Format:

```
## Implementation Complete

### Summary
- <What was done>

### Files Changed
**Created:**
- `path/to/new-file.md`

**Modified:**
- `path/to/modified-file.md`

**Deleted:**
- (none)

### Validation
- [x] <Passed check>
- [ ] <Failed check — reason>

### Deviations from Plan
<None, or list deviations>

### Plan Status
Updated `plans/YYYY-MM-DD-{name}.md` → "Implemented"
```
