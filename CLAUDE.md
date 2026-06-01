# ZAVINO Workspace

## What is ZAVINO?
ZAVINO is a Persian-language social media community covering AI, marketing, and technology.
- **ZAV** = growth, movement, forward momentum
- **INO** = Innovation
- **Tagline:** "تکامل نوآوری" (Evolution of Innovation)

**Tone:** Casual, friendly, direct — like a knowledgeable friend, not a professor.
**Language:** All audience-facing content is in **Persian (Farsi)** — colloquial, not formal.
**Platforms:** Instagram, Twitter/X (primary), with newsletter and threads.

---

## Content Engine — How It Works

This workspace is a Claude + Obsidian-style persistent content engine. Every session builds on the last.

### The Flow
```
Research → Backlog → Write → Draft → Output → Publish
```

1. `/research [topic]` — Find a topic, extract angles, save to `research/`, add to backlog
2. `/morning` — Daily startup: review backlog, surface what to write today
3. `/write-post [topic]` — Write a complete post using ZAVINO voice formula
4. `/repurpose [file]` — Adapt a post to another platform
5. `/weekly` — End-of-week review + next week planning
6. `/create-plan` — Plan a campaign or content series
7. `/implement` — Execute a plan

---

## Context Files (read before any content work)

| File | Purpose |
|---|---|
| @context/brand-info.md | ZAVINO identity, voice, positioning |
| @context/voice-dna.md | Deep tone guide — sentence patterns, what to avoid |
| @context/audience.md | Who we're talking to |
| @context/strategy.md | Current priorities and content mix |
| @context/current-data.md | Live metrics and trending topics |
| @context/backlog.md | Ideas pipeline — hot / queue / someday |

---

## Workspace Structure

### Content Pipeline
| Folder | Stage | Purpose |
|---|---|---|
| `research/inbox/` | 0 — Raw | Unprocessed research to turn into posts |
| `research/ai-tools/` | 0 — Raw | AI tool research |
| `research/trends/` | 0 — Raw | Trend tracking |
| `research/competitors/` | 0 — Raw | Competitor analysis |
| `content/backlog/` | 1 — Ideas | Idea files waiting to be written |
| `content/posts/instagram/` | 2 — Draft | Instagram drafts in progress |
| `content/posts/twitter/` | 2 — Draft | Twitter drafts in progress |
| `content/threads/` | 2 — Draft | Thread drafts |
| `content/newsletters/` | 2 — Draft | Newsletter drafts |
| `content/reels/` | 2 — Draft | Reel scripts |
| `outputs/instagram/` | 3 — Ready | Finalized, ready to publish |
| `outputs/twitter/` | 3 — Ready | Finalized, ready to publish |
| `outputs/campaigns/` | 3 — Ready | Full campaigns |

### Support
| Folder | Purpose |
|---|---|
| `assets/templates/` | Reusable post templates |
| `assets/brand/` | Logo, colors, fonts |
| `assets/images/` | Graphics and visuals |
| `plans/` | Campaign and series plans |
| `reference/` | Swipe files, inspiration, saved articles |
| `context/daily/` | Daily session notes (YYYY-MM-DD.md) |

---

## Commands Reference

| Command | When to use |
|---|---|
| `/prime` | Start of a new project session — loads all context |
| `/morning` | Start of every content session — reviews pipeline |
| `/research [topic]` | Research a topic and add angles to backlog |
| `/write-post [topic]` | Write a complete post from a topic or research file |
| `/repurpose [file → platform]` | Adapt existing content to another format |
| `/weekly` | End of week — review + plan next week |
| `/create-plan [request]` | Plan a campaign, series, or workspace change |
| `/implement [plan file]` | Execute a plan step-by-step |

---

## Content Standards

- **Hook first** — most surprising or bold claim in line 1, always `<b>bold</b>`
- **RTL rule** — every paragraph must start with a Persian word (شرکت / ابزار / مدل / اپ / پلتفرم / سرویس before English brand names)
- **Specific numbers** — "۲۵۰ هزار" beats "خیلی زیاد"
- **Max 2–3 emojis** per post, only at line ends, never mid-sentence
- **Short paragraphs** — max 2–3 lines, blank line between each
- **Colloquial Persian** — می‌تونه، داره، بودن (not می‌تواند، دارد)
- **No dashes (—)** — never use as list markers or separators
- **Introduce unknown brands** — first mention: "شرکت Intuit، شرکتی که نرم‌افزارهای مالی می‌سازه،..."
- **Never:** formal openings, walls of text, empty hype, mid-sentence emojis
- **Footer — every post, no exceptions:**
  ```
  زاوینو | دنیای AI و تکنولوژی
  ⚡️ @zavinoai
  ```

See @context/voice-dna.md for the full sentence-level guide.

---

## YAML Frontmatter Standard

Every content file should start with:

```yaml
---
date: YYYY-MM-DD
type: post | research | plan | daily
platform: instagram | twitter | newsletter | thread
status: draft | ready | published
topic: [topic tag]
pillar: ai | marketing | tech
image_url: https://...   # optional — direct image URL for Telegram sendPhoto
---
```

`image_url` is optional. When present, the publish script sends the post as a photo with caption instead of plain text.
