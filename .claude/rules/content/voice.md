# ZAVINO Content Voice Rules

## Language
- All audience-facing content is written in **Persian (Farsi)**
- Use natural, conversational Farsi — colloquial verb endings: "داره"، "می‌تونه"، "بودن"، "شده"
- Avoid formal/bureaucratic Persian (زبان اداری)
- Prefer everyday expressions over literary ones — write like you'd talk to a friend

## Tone
- Casual and warm — like a knowledgeable friend who just found something exciting
- Enthusiastic but grounded — backed by facts, not just hype
- Direct — get to the point in the first line
- ZAVINO has opinions — say when something is impressive, surprising, or a big deal
- Make the reader feel smart for following ZAVINO — not lectured

## Post Structure (follow this pattern)

### 1. Title/Hook — bold, 1 line max
- Wrap in `<b>...</b>` for Telegram — always bold
- Bold, surprising, or curiosity-triggering statement
- Emojis in the title are OPTIONAL — only add if they add meaning, not decoration
- If used, max 1 emoji at the END of the title line
- Example: `<b>ساخت اپلیکیشن اندروید، بدون حتی یک خط کدنویسی 📱</b>`

### 2. The "Proof" — 1–2 short paragraphs
- Back up the hook with a specific number, stat, or fact
- Makes the claim feel real, not just hype
- **Always introduce unknown companies/people** — if the audience might not know them, explain in one phrase
  - ✅ `Intuit، شرکتی که نرم‌افزارهای مالی مثل TurboTax و QuickBooks رو می‌سازه،...`
  - ❌ `Intuit اخراج کرد...` (audience doesn't know who Intuit is)

### 3. The "So What" — 1–2 short paragraphs
- Explain what this means for the reader
- Use "هر کسی می‌تونه..." or "حالا دیگه..." to make it feel personal and accessible

### 4. The Scale — 1 short paragraph (optional but powerful)
- Add a big number or context that shows the magnitude

### 5. Closing Punch — 1–2 lines
- "Before vs. now" or "seemed impossible → now real" framing works great
- End on an inspiring or thought-provoking note

### 6. Footer — ALWAYS, every single post, no exceptions
```
زاوینو | دنیای AI و تکنولوژی
⚡️ @zavinoai
```

## Formatting Rules (Telegram HTML)

- **Titles/headers** → always `<b>bold</b>`
- **Never use dashes (—) as bullet points or list markers**
- Use line breaks and blank lines for structure, not dashes
- Keep paragraphs max 2–3 lines

## RTL Alignment Rule — CRITICAL

Telegram detects text direction from the **first character** of each paragraph.
If a paragraph starts with an English letter → left-aligned → broken for Persian readers.

**Every paragraph must start with a Persian word.**

❌ Wrong: `Codex، ایجنت AI جدید...`
✅ Right: `ابزار Codex، ایجنت AI جدید...`

Prefix map:
- شرکت → for companies (شرکت OpenAI، شرکت Google)
- ابزار → for tools (ابزار Codex، ابزار Cursor)
- مدل → for AI models (مدل Claude، مدل GPT-4)
- اپ → for apps
- پلتفرم → for platforms
- سرویس → for services

## Paragraph Rules
- Max 2–3 lines per paragraph
- One blank line between every paragraph
- Never write walls of text
- Each paragraph should carry one clear idea

## Numbers & Stats
- Always use specific numbers — they build credibility
- ۲۵۰ هزار is more powerful than "خیلی زیاد"
- Include scale comparisons when relevant

## Emojis
- **Title:** optional, max 1, only if it adds meaning
- **Body:** 1–2 emojis max, only at the END of a line, never mid-sentence
- **Footer:** always `⚡️ @zavinoai`
- Total per post (excluding footer): max 2–3
- Preferred set: 🤖 🚀 ⚡ 💡 📱 📈 🔍 👀

## Context Rule — IMPORTANT
Always briefly introduce companies, people, or products the Persian audience may not know:
- First mention → include a one-phrase context: `OpenAI، شرکت سازنده‌ی ChatGPT،...`
- Don't assume the audience knows every tech brand

## Verbs & Phrasing (use these patterns)
- "هر کسی می‌تونه..." — democratization angle
- "حالا دیگه..." — before/after contrast
- "جالب‌تر اینکه..." — layering surprise
- "احتمالاً..." — honest, not overconfident
- "چیزی که X سال پیش..." — time contrast for impact

## What to Avoid
- ❌ Dashes as list markers or separators
- ❌ Formal verb conjugations (نوشته می‌شود، انجام می‌گردد)
- ❌ Vague openings: "هوش مصنوعی داره همه چیز رو تغییر میده"
- ❌ Mentioning a brand/person without explaining who they are
- ❌ Emojis mid-sentence
- ❌ Forgetting the ⚡️ @zavinoai footer

## Reference Post (benchmark)

```
<b>ساخت اپلیکیشن اندروید، بدون حتی یک خط کدنویسی 📱</b>

فقط از هفته‌ی پیش تا الان، بیشتر از ۲۵۰ هزار اپلیکیشن اندرویدی ساخته شده.

جالب‌تر اینکه احتمالاً بیشتر از ۹۹٪ این افراد، قبلاً حتی یک اپ اندروید هم نساخته بودن.

حالا هر کسی می‌تونه فقط با AI اپ خودش رو بسازه؛
بدون کدنویسی، بدون تیم فنی، بدون دردسر.

اندروید الان بیشتر از ۳ میلیارد کاربر فعال داره،
و حالا برای اولین بار، ساخت اپ برای این بازار عظیم تقریباً برای همه ممکن شده.

چیزی که شاید ۵ سال پیش شبیه فیلم علمی‌تخیلی بود،
الان تبدیل شده به واقعیت. 🚀

⚡️ @zavinoai
```
