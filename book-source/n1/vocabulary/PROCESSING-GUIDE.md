# N1 Vocabulary (語彙) — day-by-day processing guide

Standing instructions for turning `Nihongo_SouMatome_N1-Goi.pdf` (日本語総まとめ N1 語彙) into the site's day-by-day vocabulary pages. Give a week + day (e.g. "Week 1, Day 2") and this is the process to follow.

The PDF is scanned/image-only (no text layer) — render pages to PNG (e.g. with PyMuPDF/`fitz`) and read them visually.

---

## 1. Unit location & verification

- A "day" (1日目, 2日目, …) is the unit of work, not a page number. Each day is a themed word list (e.g. "どんな人？" = words for describing a person) — locate it by its `第N週 / N日目` header bar and read forward until the next 日目 heading begins, including every page in between.
- **This scan has no table of contents or front matter** — content starts almost immediately (PDF page index 1 = printed page 12, i.e. **printed page = PDF index + 11**). Since there's no TOC to pre-read week titles/page anchors from, locate each week/day by paging forward from wherever the previous day left off, and record the week title the first time its `第N週 タイトル` header is seen.
- 1日2ページ (2 printed pages per day) — same cadence as the grammar book, but weekly test-day / count structure has not been confirmed yet for this book (don't assume 7-day weeks or a day-7 test day the way the grammar book has; verify as each week is reached).
- Drill answers for a day print at the bottom of a *later* page (confirmed pattern: Day 1's answers, for the p.13 exercises, print at the bottom of p.15). Fetch that later page and cite the confirmed answer rather than guessing.

## 2. Symbols used in this book

No legend page was included in this scan, so these meanings are inferred from context — flag transparently if a new symbol turns up that doesn't match this list:

| Symbol | Meaning |
|---|---|
| ※ (next to が) | 「が」can be swapped for 「の」 (e.g. 愛想がいい ＝ 愛想のいい), the の form being more common in writing |
| → | A related word follows, usually the verb form of a ある/がいる-type phrase (e.g. 思いやりがある → 思いやる) |
| ⇔ | Antonym pair (e.g. 大柄な ⇔ 小柄な) |
| ・ | A common example phrase using the headword, not a separate vocabulary entry (e.g. ・いさぎよく罪を認める under いさぎよい) |

## 3. Delivery — a real page on the site, not a standalone file

- Build each day at `n1/vocabulary/week-{N}/day-{D}.html`, using the site's shared header/nav/footer/breadcrumb (`assets/css/style.css`) plus the shared `assets/css/day-page.css` stylesheet — the same file the grammar day pages use. Reuse its existing classes: `.bp-header`, `.bp-meta-grid`, `.bp-note`, `.bp-section-title`, `.bp-quiz`, `.bp-options`, `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`, plus the vocab-specific ones: `.vd-legend`, `.vd-warmup`, `.vd-wordlist` (word-list table).
- Update `n1/vocabulary.html` (the week/day hub) so that day's chip flips from `day-chip soon` to a linked `day-chip ready`. The first time a week's real title is discovered, replace that week's `(title TBD)` with the real Japanese title (+ romaji).
- Header block should note: week/day title, source file + printed page range used (and PDF page range, since there's no reliable TOC to cross-check against), the day's theme, and notes (answer key location).

## 4. Vocabulary List section format

One `.vd-wordlist` table for the day's full word list (do not split it into thematic sub-groups the book doesn't itself use — Day 1's ~50 words were one continuous list spanning both pages). Columns: **Japanese** (headword + romaji) / **English** / **Hindi** / **Gujarati** / **Note** (for ※, →, ⇔, ・ annotations — put the related word/antonym/example phrase in this column, itself with its own romaji + a short gloss).

## 5. Warm-up section

If the day opens with a "Q. 何と言う？..." riddle-style prompt (as Day 1 did), reproduce it as a `.vd-warmup` block: the Japanese prompt + romaji + a bracketed English paraphrase, then the revealed answer word.

## 6. Quiz/Exercise section format

Same format as the grammar guide: for every 練習Ⅰ/Ⅱ/… item —
- Full Japanese sentence with blank + romaji, then the completed sentence + English/Hindi/Gujarati translation
- An options table (Option / Japanese / English / Hindi / Gujarati), correct row marked `class="correct"`
- A "Why" callout explaining why the right answer collocates/fits and why the wrong option doesn't

## 7. Confusion Pairs/Nuance Notes — required every day

A `.bp-confusion` table grouping near-synonyms from that day's word list that an English (or Hindi/Gujarati) gloss would wrongly flatten into "the same word" — e.g. Day 1's 愛想がいい／気さくな／気立てがいい (all "friendly" in English, different in Japanese), or まめな／勤勉な／誠実な. Add a `.bp-callout` for any fixed-idiom trap where a word can't be swapped for a near-synonym even though the kanji/meaning looks close (e.g. 金遣いが荒い vs 荒っぽい).

## 8. Learner level & language rules

- Same as the rest of the site: Hindi and Gujarati meanings alongside English, and **romaji under every Japanese word/sentence/option** — see the site-wide romaji requirement in memory.

---

**Reference implementation:** `n1/vocabulary/week-1/day-1.html` is the first day built under this spec — use it as the template for structure, tone, and depth for any subsequent day.
