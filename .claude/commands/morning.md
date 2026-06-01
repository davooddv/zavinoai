# Morning — Daily Content Session Startup

> Run this at the start of every content session. Loads context, reviews the pipeline, and actively finds what to work on today — including searching for fresh topics if the pipeline is empty.

---

## Phase 1: Load Context

Read these files in order:

1. `CLAUDE.md`
2. `context/brand-info.md`
3. `context/strategy.md`
4. `context/current-data.md`
5. `context/backlog.md`

Check today's daily note — if it exists read it:
- `context/daily/YYYY-MM-DD.md` (use today's actual date)

If today's daily note does NOT exist, create it using the Daily Note Template below.

---

## Phase 2: Pipeline Scan

Scan and count files in each stage:

| Folder | Stage |
|---|---|
| `research/inbox/` | Unprocessed research |
| `content/backlog/` | Ideas waiting to be written |
| `content/posts/instagram/` | Instagram drafts |
| `content/posts/twitter/` | Twitter drafts |
| `outputs/instagram/` | Ready to publish |
| `outputs/twitter/` | Ready to publish |

---

## Phase 3: Active Intelligence (THE IMPORTANT PART)

Based on pipeline state, take action — don't just report:

### If backlog has hot ideas → surface the top 3
Pick the 3 best ideas from `context/backlog.md` based on:
- Timeliness (trending topics first)
- Pillar balance (what pillar hasn't been covered recently?)
- Format variety (mix posts, threads, carousels)

### If backlog is empty OR has fewer than 3 ideas → use zavino-researcher NOW
**Do not just say "backlog is empty." Act.**

Use the `zavino-researcher` agent to find 3 trending topics RIGHT NOW by searching:
- Latest AI tool releases or updates
- Trending tech/marketing news in the past 48 hours
- What's being talked about in Persian tech communities

For each topic found, extract the best post angle and add it to `context/backlog.md`.

### If there are drafts in `content/posts/` → flag them
List any drafts older than 1 day that are still unfinished. These are stuck — either finish them or archive.

### If there is unprocessed research in `research/inbox/` → highlight it
These are ready to be turned into posts. Flag them as the fastest path to output today.

---

## Phase 4: Briefing

After taking action above, deliver a briefing covering:

1. **Today's date**
2. **Pipeline status** — count per stage
3. **Top 3 to work on today** — with specific recommended action for each
4. **One clear next command** — tell exactly what to type next

Format: tight, direct, like a smart colleague — not a formal report.

---

## Daily Note Template

```markdown
---
date: YYYY-MM-DD
type: daily
---

# YYYY-MM-DD

## Today's Focus
<!-- What's the one thing to accomplish today? -->

## Ideas Captured
<!-- Drop any content ideas here as they come -->

## Decisions Made
<!-- Any content/strategy decisions worth remembering -->

## Notes
<!-- Anything else worth capturing -->
```
