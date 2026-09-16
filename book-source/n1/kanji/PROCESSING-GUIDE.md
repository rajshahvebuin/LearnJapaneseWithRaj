# N1 Kanji (漢字) — day-by-day processing guide

Standing instructions for turning `Nihongo_SouMatome_N1-Kanji.pdf` (日本語総まとめ N1 漢字) into the site's day-by-day kanji pages. Give a week + day (e.g. "Week 1, Day 2") and this is the process to follow.

The PDF is scanned/image-only (no text layer) — render pages to PNG (e.g. with PyMuPDF/`fitz`) and read them visually.

---

## 1. Unit location & verification

- A "day" (1日目, 2日目, …) is the unit of work, not a page number. Each day is a cluster of kanji grouped by shared component (部首) and/or shared on-yomi reading (e.g. Day 1 "五・語・悟" = three kanji all read ゴ). Locate it via the table of contents (this scan **does** have one, unlike the vocabulary book), then read forward until the next N日目 heading begins.
- **PDF index = printed page number** for this scan (confirmed: PDF index 12 = printed p.12 = Week 1 Day 1's first page). No front-matter offset to account for.
- 1日2ページ (2 printed pages per day), 6 content days + 1 test day (実戦問題) per week, 8 weeks — same cadence as the grammar book. Week anchors from the TOC (printed pages): Week1 p.11 同じ部分・同じ音読みをもつ漢字を覚えよう①, Week2 p.27 同②, Week3 p.43 訓読みを覚えよう, Week4 p.59 難しい読みを覚えよう, Week5 p.75 語彙で覚えよう①, Week6 p.91 語彙で覚えよう②, Week7 p.107 いろいろな覚え方をしよう, Week8 p.123 新聞を読もう.
- **This book's answers/explanations live entirely in a separate [別冊] 解答・解説 booklet, not included in the uploaded scan** (confirmed from the TOC, p.5). Unlike grammar/vocabulary (where most answers were findable on a later in-scan page), kanji day pages should assume the key is never in-scan — work out 練習Ⅰ/Ⅱ answers from the book's own definitions on that day's spread and flag transparently that they're reasoned, not copied from an official key.

## 2. Symbols used in this book (inferred — no legend page in this scan)

| Symbol | Meaning |
|---|---|
| ❶ (numbered circle before a word) | A bonus/supplementary, lower-frequency entry (cross-referenced against the "この本の使い方" page's note that grey-printed words are low-frequency) |
| ◆ | An extended compound built from the headword shown just above it (e.g. ◆表彰状 extends 表彰) |
| * | A footnote about an alternate reading or usage (e.g. "*「もみじ」とも読む", "*主に訓読みをする") |

## 3. Delivery — a real page on the site, not a standalone file

- Build each day at `n1/kanji/week-{N}/day-{D}.html`, using `assets/css/style.css` + the shared `assets/css/day-page.css` (same file grammar/vocabulary use). Reuse `.bp-header`, `.bp-meta-grid`, `.bp-note`, `.bp-section-title`, `.bp-point`, `.bp-quiz`, `.bp-options`, `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`, plus the kanji-specific ones added for this module: `.kd-legend`, `.kd-group-head`, `.kd-kanji-table` (kanji-cluster table with a big bold `.kanji` column, `rowspan`-style repeated blank cells for a kanji's 2nd/3rd example row).
- Update `n1/kanji.html` (the week/day hub) so that day's chip flips from `day-chip soon` to a linked `day-chip ready`.
- Header block should note: week/day title, source printed-page range, the day's theme (which components/readings are being grouped), and the answer-key caveat (separate 別冊, not in scan).

## 4. Kanji Groups section format

One `.bp-point` block per shared-component cluster (Day 1 had 10). Each block: a `.kd-group-head` with the shared component in large text + its reading (+ romaji) + a `.bp-badge` naming the component, then a `.kd-kanji-table` listing every kanji in that cluster with its 1–2 example compound words (Kanji / Example JP+romaji / Reading / English / Hindi / Gujarati). Leave the Kanji cell blank on a kanji's 2nd example row (no visual rowspan needed — an empty cell reads fine). Add a `.bp-notes` callout under any cluster containing a same-reading, different-meaning trap (e.g. Day 1's せいこう＝成功／精巧).

## 5. Quiz/Exercise section format

Same shape as grammar/vocabulary, adapted for two exercise types this book actually uses:
- 練習Ⅰ (choose a/b): full sentence with blank + romaji, completed sentence + EN/HI/GU, an options table with the correct row marked `class="correct"`, and a "Why" callout.
- 練習Ⅱ (fill blank from a lettered word bank): this book gives 2 sub-blanks per numbered item, each already a partial kanji compound (e.g. 精＿＿). Present both sub-blanks in one `.bp-quiz` card with a small options/answer table (Blank / Answer / Assembled word / EN / HI / GU) and one "Why" callout covering both.

## 6. Confusion Pairs/Nuance Notes — required every day

A `.bp-confusion` table is a natural fit for kanji days since the book's whole premise (same component/reading, different kanji) **is** the confusion pairs. Pull the pairs straight from that day's exercises (e.g. Day 1: 成功 vs 精巧, 取得 vs 取材, 故障 vs 障害, 未知 vs 未定, 反響 vs 影響, 固有 vs 固定) rather than inventing new ones. Add a `.bp-callout` naming the single most testable same-reading trap of the day.

## 7. Learner level & language rules

- Same as the rest of the site: Hindi and Gujarati meanings alongside English, and **romaji under every Japanese word/reading/sentence/option** — see the site-wide romaji requirement in memory.

---

**Reference implementation:** `n1/kanji/week-1/day-1.html` is the first day built under this spec — use it as the template for structure, tone, and depth for any subsequent day.
