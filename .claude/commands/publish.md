# Publish

Send a finalized post to the ZAVINO Telegram channel.

## Variables

file: $ARGUMENTS (path to the output file — e.g. `outputs/telegram/2026-05-27-post.md`)

---

## Instructions

### Step 1: Verify the file is ready

Read the file at $ARGUMENTS and check:
- Status in frontmatter is `ready` (not `draft`)
- Content is complete — no placeholder text
- Persian copy looks correct

If status is still `draft` → stop and say: "این پست هنوز draft هست. اول ببرش توی outputs/ و status رو ready کن."

### Step 2: Check .env exists

Verify `F:\Test\.env` exists and contains `TELEGRAM_BOT_TOKEN` and `TELEGRAM_CHANNEL_ID`.

If `.env` doesn't exist:
- Tell the user to create it from `.env.example`
- Stop

### Step 3: Run the publish script

Run:
```
python scripts/telegram-publish.py $ARGUMENTS
```

### Step 4: Report

If successful:
- Confirm the post was sent
- Update the file's frontmatter: change `status: ready` → `status: published`
- Add `published_at: YYYY-MM-DD` to the frontmatter

If failed:
- Show the error message clearly
- Suggest the fix

---

## Quick Publish Flow

```
/write-post [topic]   →  draft saved to content/posts/
                      →  review it
                      →  move to outputs/telegram/
/publish outputs/telegram/YYYY-MM-DD-post.md
```
