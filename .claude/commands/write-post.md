# Write Post

Generate a complete, publish-ready ZAVINO post from a topic or idea.

## Variables

request: $ARGUMENTS (topic, idea, or path to a research file — e.g. "Claude 4 release", "research/ai-tools/gemini-ultra.md", "no-code app builders")

---

## Instructions

### Step 1: Load Voice & Context

Read these before writing anything:
- `context/brand-info.md`
- `.claude/rules/content/voice.md`
- `reference/post-examples.md`

### Step 2: Understand the Topic

- If $ARGUMENTS is a file path → read that file for source material
- If $ARGUMENTS is a topic → use your knowledge + check `research/` for relevant files
- Identify the most surprising, useful, or impactful angle

### Step 3: Choose the Format

Based on the topic, decide:

| Format | When to use |
|---|---|
| **Single post** | One punchy insight, quick news, a stat |
| **Carousel (3–7 slides)** | How-to, listicle, comparison |
| **Twitter thread** | Deep explanation, story, step-by-step |
| **Reel script** | Trending topic, visual demo |

Ask if unsure — don't guess.

### Step 4: Write Using the ZAVINO Formula

Follow this structure (from `reference/post-examples.md`):

1. **Hook Line** — 1 line, bold claim, 1–2 emojis at the end
2. **The Proof** — specific stat or fact that backs up the hook
3. **The So What** — "هر کسی می‌تونه..." / "حالا دیگه..." — make it personal
4. **The Scale** — big number or context (optional but powerful)
5. **Closing Punch** — before/after framing, ends with 1 emoji

Rules:
- All copy in conversational Persian — colloquial verb endings
- Max 2–3 lines per paragraph, blank line between each
- Max 2–3 emojis total, only at line ends
- Never start with generic: "هوش مصنوعی داره همه چیز رو تغییر میده"

### Step 5: Save the Draft

Save to:
- `content/posts/instagram/YYYY-MM-DD-{slug}.md` for Instagram
- `content/posts/twitter/YYYY-MM-DD-{slug}.md` for Twitter
- `content/threads/YYYY-MM-DD-{slug}.md` for threads

Use the Content File Template below.

### Step 6: Report

After writing:
1. Show the full post
2. State which format was chosen and why
3. Highlight the hook — confirm it passes the "would I stop scrolling?" test
4. Provide the file path

---

## Content File Template

```markdown
---
date: YYYY-MM-DD
type: post
platform: instagram | twitter | thread
status: draft
topic: [topic tag]
pillar: ai | marketing | tech
---

# [Post Title / Slug]

[Full post content here]

---

## Notes
<!-- Source, inspiration, or context for this post -->
```
