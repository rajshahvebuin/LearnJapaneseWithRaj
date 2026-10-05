# 日本語パワードリル N1 文法 — unit-by-unit processing guide

Standing instructions for turning `Nihongo_Power_Drill_N1-Bunpou.pdf` (日本語パワードリル N1 文法, Nihongo Power Drill N1 Bunpou, アスク出版, 2011) into the site's grammar pages. Give a unit (e.g. "第7回" or "集中トレーニング③") and this is the process to follow.

This guide adapts the master spec [`../PROCESSING-GUIDE.md`](../PROCESSING-GUIDE.md) (日本語総まとめ). Everything in the master spec still applies (shared header/nav/footer, `day-page.css` `bp-*` classes, three required sections, EN + Hindi + Gujarati, romaji under every Japanese line) unless overridden below.

---

## 1. The PDF

- 86 PDF pages, scanned image-only (no text layer). Render with PyMuPDF (`import pymupdf`; `page.get_pixmap(dpi=130–150)`) and read visually.
- **Every page carries `/Rotate 180`.** `get_pixmap()` honours it (images come out upright). `Page.show_pdf_page()` (used for contact sheets/montages) does **not** — montages come out upside down. Use plain `get_pixmap()` for reading content.
- Layout: PDF 1 cover · PDF 2 はじめに (p.3) · PDF 3–4 目次 (p.4–5) · PDF 5–6 学習スケジュール表 (p.6–7) · PDF 7–75 drills (p.8–77) · PDF 76 「問題2の解答の仕方」 (p.78) · PDF 77 colophon · PDF 78 back cover · **PDF 79–86 別冊 解答 (answer booklet, scanned in after the back cover).**

### Verified page offset (read from the stamped page numbers on the images)

| Printed pages | PDF page index | Checked at |
|---|---|---|
| p.3 – p.15 | **PDF = printed − 1** | PDF 2 = はじめに (TOC says p.3); PDF 5 stamp "6"; PDF 7 stamp "8" (第1回); PDF 8 stamp "9"; PDF 14 stamp "15" |
| p.16 | **missing from the scan** | PDF 14 = p.15 and PDF 15 = p.17 are both right-hand (odd) pages; p.16 never appears |
| p.17 – p.78 | **PDF = printed − 2** | PDF 15 stamp "17"; PDF 16 stamp "18" (集中①); PDF 42 stamp "44" (第16回); PDF 43 stamp "45"; PDF 74 stamp "76" (第30回); PDF 76 stamp "78" |

**Consequence:** 第5回's first page (p.16 — its whole 問題1, Q1–10) is not in the PDF. Only its p.17 (問題2 + 問題3) can be built from the book. The answer key for 第5回 問題1 is still in the 別冊 (PDF 80), but the questions themselves are missing — say so in the page header and build 問題1 as "*(Page missing from the source scan — questions not available.)*". Do not invent replacement questions as if they were the book's.

### Answer key — present (別冊, PDF 79–86)

The 別冊 解答 is included at the end of the PDF. It gives, per unit: 問題1 answer numbers, 問題2 ★ answer **plus the full order chain** in brackets (e.g. `3 (4→2→3→1)`), 問題3 answer numbers; for 集中トレーニング, a/b for each of the 10 items. Always cite the key; never guess. (Only fall back to the master rule — work it out at N1 level and flag it as not from an official key — if an entry is illegible.)

---

## 2. Unit definition

A **unit** is one heading in the TOC: either a round (第N回) or one 集中トレーニング page. 40 units total.

- **第1回 – 第15回**: 2 printed pages, 目標解答時間 10分, 20 points, **17 questions**: 問題1 文の文法1 (文法形式の判断) ×10 · 問題2 文の文法2 (文の組み立て, ★) ×4 · 問題3 文章の文法 (passage) ×3.
- **第16回 – 第30回**: 2 printed pages, 10分, 20 points, **15 questions**: 問題1 ×7 · 問題2 ×3 · 問題3 ×5 (2点×5).
- **集中トレーニング①–⑩**: 1 printed page, 3分, 10 points: 10 sentences, each with a two-way choice `（ a ○○  b ○○ ）` — "（ ）の中のaとbのうち、文に合うほうを選びましょう".
- 問題2 uses the official JLPT ★ format (four blanks, one marked ★); the book's p.78 explains it. The 別冊 gives both the ★ answer and the full order.

### Full unit table

| # | File | Unit | Topic | Printed pp | PDF pp | Answer PDF p |
|---|---|---|---|---|---|---|
| 1 | kai-01.html | 第1回 | — | 8–9 | 7–8 | 79 |
| 2 | kai-02.html | 第2回 | — | 10–11 | 9–10 | 79 |
| 3 | kai-03.html | 第3回 | — | 12–13 | 11–12 | 79 |
| 4 | kai-04.html | 第4回 | — | 14–15 | 13–14 | 80 |
| 5 | kai-05.html | 第5回 | — | 16–17 | **p.16 missing**, 15 | 80 |
| 6 | training-01.html | 集中トレーニング① | 助詞 (1) | 18 | 16 | 80 |
| 7 | training-02.html | 集中トレーニング② | 助詞 (2) | 19 | 17 | 80 |
| 8 | kai-06.html | 第6回 | — | 20–21 | 18–19 | 80 |
| 9 | kai-07.html | 第7回 | — | 22–23 | 20–21 | 81 |
| 10 | kai-08.html | 第8回 | — | 24–25 | 22–23 | 81 |
| 11 | kai-09.html | 第9回 | — | 26–27 | 24–25 | 81 |
| 12 | kai-10.html | 第10回 | — | 28–29 | 26–27 | 81 |
| 13 | training-03.html | 集中トレーニング③ | 助詞 (3) | 30 | 28 | 82 |
| 14 | training-04.html | 集中トレーニング④ | 「こと」と「もの」 | 31 | 29 | 82 |
| 15 | kai-11.html | 第11回 | — | 32–33 | 30–31 | 82 |
| 16 | kai-12.html | 第12回 | — | 34–35 | 32–33 | 82 |
| 17 | kai-13.html | 第13回 | — | 36–37 | 34–35 | 82 |
| 18 | kai-14.html | 第14回 | — | 38–39 | 36–37 | 83 |
| 19 | kai-15.html | 第15回 | — | 40–41 | 38–39 | 83 |
| 20 | training-05.html | 集中トレーニング⑤ | 副詞 (1) | 42 | 40 | 83 |
| 21 | training-06.html | 集中トレーニング⑥ | 副詞 (2) | 43 | 41 | 83 |
| 22 | kai-16.html | 第16回 | — | 44–45 | 42–43 | 83 |
| 23 | kai-17.html | 第17回 | — | 46–47 | 44–45 | 83 |
| 24 | kai-18.html | 第18回 | — | 48–49 | 46–47 | 84 |
| 25 | kai-19.html | 第19回 | — | 50–51 | 48–49 | 84 |
| 26 | kai-20.html | 第20回 | — | 52–53 | 50–51 | 84 |
| 27 | training-07.html | 集中トレーニング⑦ | 似ている表現 (1) | 54 | 52 | 84 |
| 28 | training-08.html | 集中トレーニング⑧ | 似ている表現 (2) | 55 | 53 | 84 |
| 29 | kai-21.html | 第21回 | — | 56–57 | 54–55 | 84 |
| 30 | kai-22.html | 第22回 | — | 58–59 | 56–57 | 85 |
| 31 | kai-23.html | 第23回 | — | 60–61 | 58–59 | 85 |
| 32 | kai-24.html | 第24回 | — | 62–63 | 60–61 | 85 |
| 33 | kai-25.html | 第25回 | — | 64–65 | 62–63 | 85 |
| 34 | training-09.html | 集中トレーニング⑨ | 使役・受身 | 66 | 64 | 85 |
| 35 | training-10.html | 集中トレーニング⑩ | くり返しの文型 | 67 | 65 | 85 |
| 36 | kai-26.html | 第26回 | — | 68–69 | 66–67 | 86 |
| 37 | kai-27.html | 第27回 | — | 70–71 | 68–69 | 86 |
| 38 | kai-28.html | 第28回 | — | 72–73 | 70–71 | 86 |
| 39 | kai-29.html | 第29回 | — | 74–75 | 72–73 | 86 |
| 40 | kai-30.html | 第30回 | — | 76–77 | 74–75 | 86 |

Answer-booklet page contents (verified): PDF 79 = 第1–3回 · PDF 80 = 第4回, 第5回, 集中①②, 第6回 · PDF 81 = 第7–10回 · PDF 82 = 集中③④, 第11–13回 · PDF 83 = 第14–15回, 集中⑤⑥, 第16–17回 · PDF 84 = 第18–20回, 集中⑦⑧, 第21回 · PDF 85 = 第22–25回, 集中⑨⑩ · PDF 86 = 第26–30回. Each entry is headed with its printed page range (e.g. 「第1回 (p.8–p.9)」) — use that heading to confirm you are reading the right unit.

Always re-verify a unit's start page by reading the stamped page number and the 第N回 / 集中トレーニング heading on the rendered image before building.

---

## 3. Delivery

- Files live in `n1/grammar/power-drill/` (`kai-01.html` … `kai-30.html`, `training-01.html` … `training-10.html`). Page depth is three levels: assets `../../../assets/...`, site home `../../../index.html`, N1 home `../../index.html`, grammar hub `../../grammar.html`, book hub `index.html`.
- Same `<head>` as the master reference (`auth.js` first, favicon, Noto Sans JP, `style.css` + `day-page.css`), same site header/nav/footer, `main.js` at the end.
- Breadcrumb: `Home / JLPT N1 / Grammar / 日本語パワードリル N1 文法 (index.html) / <unit>`.
- `bp-day-nav` at the bottom: previous unit / next unit **in book order** (the unit table above). First unit's "previous" links to the hub (`index.html`); last unit's "next" links back to the hub.
- **Hub update rule:** after building a unit, edit `n1/grammar/power-drill/index.html` and flip that unit's chip from `<span class="day-chip soon">…</span>` to `<a class="day-chip ready" href="<file>">…</a>`. Also update the `sample-note` progress line. Do not touch `n1/grammar.html` (it already links the hub).
- Reference implementation: [`n1/grammar/power-drill/kai-01.html`](../../../../n1/grammar/power-drill/kai-01.html).

## 4. Header block (`.bp-header`)

- `.bp-week`: `JLPT N1 · Grammar · 日本語パワードリル N1 文法` (+ romaji).
- `h1`: unit title (`第1回 — 文法形式の判断・文の組み立て・文章の文法`, or `集中トレーニング① — 助詞 (1)`).
- Source: book name + printed pp + PDF pp.
- Grammar points covered: the patterns tested by the **correct** answers.
- Answer key: "別冊 解答, PDF page N — confirmed, not guessed."
- Notes must say: **this is a drill-only book with no explanation pages — every Grammar Point explanation, formation table and example (other than the book's own question sentences) is added for this site and marked "(added, not in book)"**. Plus 目標解答時間, scoring, any missing page, any exam traps.

## 5. The three required sections, adapted

### §1 Grammar Points
One `.bp-point` per pattern that a correct answer tests (問題1 correct options, the pattern the assembled 問題2 sentence hinges on, 問題3 correct options). Same structure as the master: 【N】 heading + register badge, field table (Reading / Meaning EN / HI / GU / Connection / Register / Typical use), formation table (verb / い-adj / な-adj / noun — mark every cell the book doesn't show as `class="added"` "(added, not in book)"; since the book shows no formation tables, that is all of them except what the question sentence itself demonstrates), examples table, 2–4 sentences of notes.
- Examples: first row = the book's own question sentence (completed), labelled "(book: 問題1 Q3)". Every other example is labelled **(added, not in book)**.
- For 集中トレーニング pages, the "points" are the particle / adverb / near-synonym contrasts drilled (e.g. に即して vs を…), grouped sensibly rather than one block per item.

### §2 Quiz / Exercise Section
- **問題1**: full sentence with （　）, romaji, completed sentence + EN/HI/GU, options table with all four options (Option / Japanese+romaji / English / Hindi / Gujarati), correct row `class="correct"`, `.bp-why` explaining the right answer and ruling out each wrong option.
- **問題2**: sentence with the four blanks and ★ shown in place, tiles with romaji, `.bp-order-chain` in the 別冊's order with the ★ slot marked (`★ 3 やせようと`), `.bp-assembled` sentence + romaji, EN/HI/GU, and a Why line that states "★ = 3rd slot → answer 3" and the grammar the chain hinges on. This book *does* use the official ★ format.
- **問題3**: the passage in full (blanks as **［1］［2］［3］**), romaji for the passage, full EN/HI/GU translation of the completed passage, the source credit line, then one `.bp-quiz` per blank with the options table and Why.
- **集中トレーニング**: each item as a `.bp-quiz` with a two-row options table (a / b), correct row marked, translations of the completed sentence, Why.

### §3 Confusion Pairs / Nuance Notes
`.bp-confusion` table (Form / Meaning / Connection / Key difference / Use when) built mainly from the **distractors the book actually used** against each correct answer (e.g. ところで vs ところが vs としたら vs とはいえ), plus `.bp-callout` exam-trap notes.

## 6. Language rules
Same as master §6: EN + Hindi + Gujarati for every meaning, example and quiz sentence; romaji `<span class="romaji">` under every Japanese line (sentences, options, tiles, formation examples, passage).
