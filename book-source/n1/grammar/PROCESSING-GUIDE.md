# N1 Grammar (文法) — day-by-day processing guide

Standing instructions for turning `Nihongo_Soumatome_N1-Bunpou.pdf` (日本語総まとめ N1 文法) into the site's day-by-day grammar pages. Give a week + day (e.g. "Week 1, Day 2") and this is the process to follow.

The PDF is scanned/image-only (no text layer) — render pages to PNG (e.g. with PyMuPDF/`fitz`) and read them visually.

---

## 1. Unit location & verification

- A "day" (1日目, 2日目, …) is the unit of work, not a page number. Locate the day's starting page via the table of contents, then read forward until the next 日目/実戦問題 heading begins — include every page in between, even if content or drill answers spill across a page break.
- Verify against the printed page number visible in the scan itself. For this book: **PDF page index = printed page number + 2** (front-matter pages push the offset). This was re-verified during Week 8 processing by rendering a candidate page and reading the stamped printed-page number visible on the image itself (PDF page 128 showed stamp "126"), not assumed from an older, incorrect "+1" note — always cross-check the same way before trusting either offset on a new scan.
- Drill answers for a day often print at the bottom of a *later* page — this book prints them at the bottom of the following day's second page. Fetch that page too and cite the confirmed answer rather than guessing.
- 実戦問題 (day 7 test) answers may live in a separate answer booklet ([別冊]) not included in the uploaded PDF. If so, work out the answer using N1-level knowledge and flag transparently that it isn't from an official key.
- 1日2ページ (2 printed pages per day), 7 days per week (days 1–6 = content, day 7 = 実戦問題 test), 8 weeks total.

**Week map** (printed page the week starts on, and its title, from the table of contents):

| Week | Starts at | Title |
|---|---|---|
| 1 | p.13 | 努力してこそ合格できる |
| 2 | p.29 | 私なりに努力している |
| 3 | p.45 | 言うまでもなく、努力している |
| 4 | p.61 | 努力なくして合格はない |
| 5 | p.77 | 努力せずにはすまない |
| 6 | p.93 | 以前にも増して努力している |
| 7 | p.109 | 努力に努力を重ねている |
| 8 | p.125 | 結果はどうあれ、努力しよう |

---

## 2. Delivery — a real page on the site, not a standalone file

- Build each day at `n1/grammar/week-{N}/day-{D}.html`, using the site's shared header/nav/footer/breadcrumb (`assets/css/style.css`) plus the dedicated `assets/css/day-page.css` stylesheet. Reuse its existing classes rather than inventing new ones: `.bp-header`, `.bp-point`, `.bp-table`, `.bp-formation-table`, `.bp-examples-table`, `.bp-quiz`, `.bp-options`, `.bp-confusion`, `.bp-order-chain`, `.bp-assembled`, `.bp-day-nav`, `.bp-callout`.
- Update `n1/grammar.html` (the week/day hub) so that day's chip flips from `day-chip soon` to a linked `day-chip ready`.
- Always include all three sections below every time, even if one is empty (write "*(None on this page.)*").
- Start with a header block noting: week/day title, source file + printed page range used, grammar points covered, and notes (answer key location, register warnings, exam traps).

## 3. Grammar Point section format

For each grammar point, a `.bp-point` block with:
- **【N】 〜form〜** subheading + a register badge (`.bp-badge`, or `.bp-badge.formal` for 硬)
- Field table: Reading / Meaning (EN) / Meaning (Hindi) / Meaning (Gujarati) / Connection (接続) / Register / Typical use
- Formation-breakdown table for verb / い-adj / な-adj / noun — fill in plausible forms for anything the book doesn't show, marking those cells "(added, not in book)"
- Examples table (every example from the book): Japanese / English / Hindi / Gujarati
- 2–4 sentences of learner-friendly notes in English

## 4. Quiz/Exercise section format

For every question that day (warm-up, 練習Ⅰ, 練習Ⅱ, …):
- Full Japanese sentence with blank + English/Hindi/Gujarati translation of the completed sentence
- Options table (Option / Japanese / English / Hindi / Gujarati) — mark the correct row `class="correct"` (CSS renders the ✅ automatically)
- A "Why" callout: why the correct answer fits, why each wrong option is ruled out
- Sentence-ordering (並べ替え) questions: show the assembled sentence, an order chain (`.bp-order-chain`, e.g. `3 → 2 → 1 → 4`), and flag if the source doesn't mark a ★ blank (this book uses plain numbered underscores instead of the official JLPT ★ format)

## 5. Confusion Pairs/Nuance Notes — required every day

A `.bp-confusion` comparison table (Form / Meaning / Connection / Key difference / Use when) across that day's grammar points — near-synonyms, same-form-different-meaning traps, connection traps, register traps, positive/negative pairing traps. Add a `.bp-callout` for any trap N1 habitually tests.

## 6. Learner level & language rules

- Intermediate learner preparing for JLPT N1. Native languages are Hindi and Gujarati — always give meanings/examples in both, plus simple, concise English grammar explanations.
- **Add romaji** under every Japanese line (sentences, quiz options, formation examples) — a standing site-wide requirement, not specific to grammar.

## 7. Optional add-on

If asked to "drill me" after a day, generate 5 fresh practice questions using that day's grammar points in the same Q-format, with answers/explanations at the bottom rather than inline.

---

**Reference implementation:** [`n1/grammar/week-1/day-1.html`](../../../n1/grammar/week-1/day-1.html) is the first day built under this spec — use it as the template for structure, tone, and depth for any subsequent day.
