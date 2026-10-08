# 日本語能力試験 スーパー模試 N4・N5 — processing guide

Standing instructions for turning this book (JLPT Super Moshi N4・N5, アルク, 監修 岡本能里子, 初版 2012-10-04; the main scan is the 第5刷 of 2019-08-08) into the site's unit pages under `n4/mock-tests/super-moshi/`. Pick a filename from the unit table (§5) and follow this guide.

## 1. The book

- **Four full mock exams**: N4 第1回, N4 第2回, N5 第1回, N5 第2回. Each one is in real-exam format with three papers: 言語知識（文字・語彙）, 言語知識（文法）・読解 and 聴解.
- Front matter: はじめに (p.3), 目次 (p.4–5), 日本語能力試験について知る (p.6–15: levels, papers and times, question types for N4 and N5, pass marks), この本の使い方 (p.16–19: timing, where the answers are, how to score yourself, how to use the 記録票).
- Back matter: 聴解スクリプト for all four tests (p.146–167), 模擬テスト 記録票 score sheets (p.168–171).
- **別冊** (a separate booklet): 解答用紙 mark sheets (別冊 p.4–15) and 解答 (別冊 p.16–19).
- **The book has no explanations.** The 解答 pages give answer numbers only. Every "Why", every translation and every word table on the site is ours and must be marked "(added, not in book)".

### N4 and N5 in one course

The book is filed under N4 only, so the course lives at `n4/mock-tests/super-moshi/`. **The two N5 tests are included in this same course as units, with "N5" in the filename and an "N5 level" label** in the title, header and contents-page heading. N5 learners reach them from this course; we do not make a second copy under `n5/`. Do not edit the N5 hub pages to link here (hub pages are out of scope for unit work).

## 2. The two PDFs and how they relate

| File | Pages | What it is |
|---|---|---|
| `日本語能力試験スーパー模試N4・N5.pdf` (**"main PDF"**) | 176 single portrait pages | The **complete main book**, clean scan: cover, p.1–171, colophon, blank, back covers. Has a text layer, but it is low-quality OCR (and in Shift-JIS bytes that print as mojibake), so use it only to find page numbers. **The 別冊 is NOT in this file.** |
| `JLPT_Super_Moshi_N4.N5.pdf` (**"spread PDF"**) | 57 landscape two-page spreads | A **second, older scan of a different physical copy** (made 2016, yellow sticky tabs visible from PDF 22 on). It covers only printed p.20–119 of the main book (N4 第1回 to N5 第1回, plus the N5 第2回 title page) and then **the 別冊**: mark sheets and the **answer key**. No text layer at all. |

So: **use the main PDF for every question, passage, picture and script; use the spread PDF only for the answer key** (it is the only place the 解答 exists). The two scans show the same printing of the questions (checked: N4 第1回 文字・語彙 p.22–29 is identical in both).

### Offsets (verified on rendered page stamps)

**Main PDF: PDF page = printed page** for the whole book (p.1–171). Checked on PDF 3, 5, 14, 16, 22–29, 46, 61, 136, 145–168. PDF 172 = colophon, 173 blank, 174–175 back/front covers, 176 blank. No missing pages.

**Spread PDF:**

| Spread PDF | Content | Formula |
|---|---|---|
| 1–50 | Main book printed p.20–119, two pages per spread | spread PDF *n* = printed p.(2*n*+18) left + p.(2*n*+19) right. E.g. PDF 2 = p.22–23, PDF 18 = p.54–55, PDF 36 = p.90–91, PDF 50 = p.118–119 |
| 51–55 | 別冊 解答用紙 (mark sheets) p.4–13 | spread PDF *n* = 別冊 p.(2*n*−98) + (2*n*−97). 51 = p.4–5 … 55 = p.12–13 |
| 56 | 別冊 p.16 (left) **N4 第1回 解答**, p.17 (right) **N4 第2回 解答** | page is turned 90° — rotate the render 90° clockwise to read |
| 57 | 別冊 p.18 (right half) **N5 第1回 解答**, p.19 (left half) **N5 第2回 解答** | page is turned the other way — rotate 90° counter-clockwise; halves are swapped |

Not in either PDF: 別冊 cover and p.1–3 (contents), 別冊 p.14–15 (N5 第2回 文法・読解 and 聴解 mark sheets). Nothing on those pages is needed: they are blank answer sheets.

Rendering tip: `pymupdf` at 150 dpi for main-PDF pages; for the key, clip the half of spread 56/57 you need at 200 dpi and rotate with PIL.

## 3. Answer-key status

**Complete for all four tests**, numbers only (no explanations):

| Test | 別冊 page | Where in the scan |
|---|---|---|
| N4 第1回 | 別冊 p.16 | spread PDF 56, left half |
| N4 第2回 | 別冊 p.17 | spread PDF 56, right half |
| N5 第1回 | 別冊 p.18 | spread PDF 57, right half |
| N5 第2回 | 別冊 p.19 | spread PDF 57, left half |

Cite as "(別冊 p.16)". The key confirms the counts: N4 文字・語彙 35, 文法・読解 35, 聴解 28 (問題1 8 · 問題2 7 · 問題3 5 · 問題4 8); N5 文字・語彙 35, 文法・読解 32, 聴解 24 (7 · 6 · 5 · 6).

N4 第1回 文字・語彙 key (checked item by item against the questions on p.22–29 — all consistent): 1-1 2-4 3-3 4-1 5-2 6-2 7-3 8-3 9-1 · 10-1 11-2 12-3 13-4 14-4 15-2 · 16-2 17-3 18-1 19-1 20-2 21-3 22-4 23-1 24-1 25-4 · 26-3 27-3 28-2 29-2 30-1 · 31-4 32-2 33-1 34-2 35-3.

## 4. Timing and scoring (book p.14, 16, 17)

| | N4 | N5 |
|---|---|---|
| 言語知識（文字・語彙） | 30 分 | 25 分 |
| 言語知識（文法）・読解 | 60 分 | 50 分 |
| 聴解 | 35 分 | 30 分 |
| Score: 言語知識・読解 (0–120) | 120 × correct ÷ 70 | 120 × correct ÷ 67 |
| Score: 聴解 (0–60) | 60 × correct ÷ 28 | 60 × correct ÷ 24 |
| Pass | total ≥ 90 / 180 | total ≥ 80 / 180 |
| 基準点 (each section) | 言語知識・読解 ≥ 38, 聴解 ≥ 19 | same |

The 文字・語彙 and 文法・読解 papers share **one** score section (言語知識・読解); the item counts of both papers go into the ÷ 70 / ÷ 67.

## 5. Unit definition and full unit table

A unit = one paper of one test (3 per test × 4 tests = 12) + one `guide.html` unit for the book's explanation pages = **13 units**. N4 units use `test-N-…`; N5 units use `n5-test-N-…`.

| # | Filename | Title | Printed = main PDF pp | Spread PDF | Answer key | Audio |
|---|---|---|---|---|---|---|
| 1 | test-1-moji-goi.html | N4 第1回 言語知識（文字・語彙） 1–35 | 22–29 (title 21) | 2–5 | 別冊 p.16 (spread 56 L) | — |
| 2 | test-1-bunpou-dokkai.html | N4 第1回 言語知識（文法）・読解 1–35 | 30–43 | 6–12 | 別冊 p.16 | — |
| 3 | test-1-choukai.html | N4 第1回 聴解 (28 q) + script | 44–54; script 146–151 | 13–18 | 別冊 p.16 | CD1 T1–32 |
| 4 | test-2-moji-goi.html | N4 第2回 言語知識（文字・語彙） 1–35 | 56–63 (title 55) | 19–22 | 別冊 p.17 (spread 56 R) | — |
| 5 | test-2-bunpou-dokkai.html | N4 第2回 言語知識（文法）・読解 1–35 | 64–77 | 23–29 | 別冊 p.17 | — |
| 6 | test-2-choukai.html | N4 第2回 聴解 (28 q) + script | 78–88; script 152–157 | 30–35 (L) | 別冊 p.17 | CD1 T33–64 |
| 7 | n5-test-1-moji-goi.html | N5 第1回 言語知識（文字・語彙） 1–35 — N5 level | 90–95 (title 89) | 36–38 | 別冊 p.18 (spread 57 R) | — |
| 8 | n5-test-1-bunpou-dokkai.html | N5 第1回 言語知識（文法）・読解 1–32 — N5 level | 96–107 | 39–44 | 別冊 p.18 | — |
| 9 | n5-test-1-choukai.html | N5 第1回 聴解 (24 q) + script — N5 level | 108–118; script 158–162 | 45–50 (L) | 別冊 p.18 | CD2 T1–28 |
| 10 | n5-test-2-moji-goi.html | N5 第2回 言語知識（文字・語彙） 1–35 — N5 level | 120–125 (title 119) | — (not in spread scan) | 別冊 p.19 (spread 57 L) | — |
| 11 | n5-test-2-bunpou-dokkai.html | N5 第2回 言語知識（文法）・読解 1–32 — N5 level | 126–135 | — | 別冊 p.19 | — |
| 12 | n5-test-2-choukai.html | N5 第2回 聴解 (24 q) + script — N5 level | 136–145; script 163–167 | — | 別冊 p.19 | CD2 T29–56 |
| 13 | guide.html | はじめに・日本語能力試験について知る・この本の使い方・記録票 | 3, 6–19, 168–171 | — | — | — |

### Paper layouts (item numbers restart at 1 in every paper, as in the book)

- **N4 文字・語彙** (35): もんだい1 漢字読み 1–9 · もんだい2 表記 10–15 · もんだい3 文脈規定 16–25 · もんだい4 言い換え類義 26–30 · もんだい5 用法 31–35.
- **N4 文法・読解** (35): もんだい1 文法形式の判断 1–15 · もんだい2 文の組み立て★ 16–20 · もんだい3 文章の文法 21–25 · もんだい4 内容理解（短文）26–29 (4 passages) · もんだい5 内容理解（中文）30–33 · もんだい6 情報検索 34–35.
- **N4 聴解** (28): もんだい1 課題理解 1–8ばん · もんだい2 ポイント理解 1–7ばん · もんだい3 発話表現 1–5ばん (pictures, arrow person) · もんだい4 即時応答 1–8ばん (nothing printed).
- **N5 文字・語彙** (35): もんだい1 漢字読み 1–12 · もんだい2 表記 13–20 · もんだい3 文脈規定 21–30 · もんだい4 言い換え類義 31–35.
- **N5 文法・読解** (32): もんだい1 文法形式 1–16 · もんだい2 ★ 17–21 · もんだい3 文章の文法 22–26 · もんだい4 短文 27–29 (3 passages) · もんだい5 中文 30–31 · もんだい6 情報検索 32.
- **N5 聴解** (24): もんだい1 課題理解 1–7ばん · もんだい2 ポイント理解 1–6ばん · もんだい3 発話表現 1–5ばん · もんだい4 即時応答 1–6ばん.

Note: the N4/N5 test pages are written mostly in kana with spaces between words (わかち書き), like the real N4/N5 papers. Quote them as printed (keep the spaces); give the kanji form in the translations block where it helps.

## 6. Audio — track map (never publish)

Two CDs next to the PDFs: `JLPT_Super_Moshi_N4.N5-AudioCD1/` (64 mp3, **both N4 tests**) and `…-AudioCD2/` (56 mp3, **both N5 tests**) = 120 tracks. Book badges read "CD1-①" etc.; checked on p.44–54, 78–88, 108–118, 136–145.

| CD | Test | Intro + items |
|---|---|---|
| CD1 | N4 第1回 | 問題1 T1, 1–8ばん T2–9 · 問題2 T10, 1–7ばん T11–17 · 問題3 T18, 1–5ばん T19–23 · 問題4 T24, 1–8ばん T25–32 |
| CD1 | N4 第2回 | 問題1 T33, T34–41 · 問題2 T42, T43–49 · 問題3 T50, T51–55 · 問題4 T56, T57–64 |
| CD2 | N5 第1回 | 問題1 T1, 1–7ばん T2–8 · 問題2 T9, T10–15 · 問題3 T16, T17–21 · 問題4 T22, T23–28 |
| CD2 | N5 第2回 | 問題1 T29, T30–36 · 問題2 T37, T38–43 · 問題3 T44, T45–49 · 問題4 T50, T51–56 |

Refer to audio only as `<span class="ld-track">CD1 · Track 12</span>`. **No `<audio>` elements, no links to the mp3 files, no copies.**

## 7. Hard content rules

- **Romaji** (`<span class="romaji">`) under every Japanese line, including option cells, table cells and headings.
- **EN + HI + GU** for every meaning, example, question sentence and option.
- **Every question gets the book's answer**, cited as "Answer N (別冊 p.16)". Anything we add (all explanations, distractor notes, word tables, full ★ orders, translations) is labelled "(added, not in book)". A worked answer we reason out ourselves where the book gives none (e.g. the full ★ order — the key gives only the ★ tile) is labelled "(our answer, not in book)".
- **No long passages or scripts.** Reading passages (もんだい3 cloze, もんだい4–6) and listening scripts are never reproduced in full — not in pages, scratch files or notes. Write a 2–3 sentence "Passage summary (not the book's text)" / "Script summary (not the book's text)" in EN/HI/GU, then quote only the sentence(s) a question needs. Question stems and options are quoted in full. For もんだい6 notices/timetables, give only the rows a question needs.
- Never invent questions or answers. Describe pictures (聴解 / もんだい3 発話表現) in words; never copy illustrations.
- No emoji glyphs in body text. No new CSS/JS; use the shared classes only.

## 8. Page format (mirror `n1/mock-tests/super-moshi/test-1-gengo.html`)

Head/header/footer copied from `index.html` in this folder (depth `../../../`, body class `level-page n4`, N4 level-nav with "Mock tests" active). Breadcrumb: Home / JLPT N4 / Mock tests (`../../mock-tests.html`) / スーパー模試 N4・N5 (`index.html`) / unit. N5 units keep the N4 chrome (the course lives under N4) but say "N5 level" in `.bp-week`, `<h1>` and the header notes.

**Header** `.bp-header` with `.bp-week` + `<h1>` + `.bp-meta-grid`: Source (printed pp = main-PDF pp, and the spread-PDF pages), question types (`.bp-points` spans), Answer key (all answers in one line + "numbers only, every explanation added"), Time and score (§4), Notes.

**§1 Points** — `.bp-point` with added revision tables: 文字・語彙 → one vocabulary/kanji table for every target word (item, word + kana + romaji, EN, HI, GU). 文法・読解 → grammar table for もんだい1–3 (pattern, meaning EN/HI/GU, connection) + per passage: type and "how to find the answer". 聴解 → per もんだい type: what to listen for. Cross-link the site's N4/N5 pages where useful.

**§2 Every question** — one `.bp-quiz` per item, `q-label` "Q1"… (聴解: "問題1 1ばん"):
- もんだい1 漢字読み / もんだい2 表記 / もんだい3 文脈規定: stem with `<u>` or （　） + romaji; `.q-translations` (underlined word or full sentence, EN, HI, GU); `.bp-options` table (Option · JP + romaji · EN · HI · GU) with `tr.correct`; `.bp-why`.
- もんだい4 言い換え類義: options are full sentences; mark which ones change the meaning.
- もんだい5 用法 (N4 only): option column = full sentence; wrong ones get "✗ Means … — needs X".
- ★ (文法 もんだい2): tiles, `.bp-order-chain`, `.bp-assembled` + romaji, EN/HI/GU, options, why; full order labelled "(our answer, not in book)".
- もんだい3 文章の文法 and 読解: `.bp-point` with passage summary (not the book's text), then one quiz per item quoting only the needed sentence.
- 聴解: `<span class="ld-track">CDn · Track NN</span>`, the question (from the script), printed or spoken options, script summary, the deciding line quoted, answer + why. Pictures described in words.

**§3 Confusion pairs** — `.bp-confusion` table of look-alikes from the wrong options + 2–3 `.bp-callout` exam tips (added).

**Footer nav** `.bp-day-nav`: ← previous unit / next unit → in table order (§5); unit 1's "previous" is the contents page.

## 9. Contents page

`n4/mock-tests/super-moshi/index.html` is hand-built (it replaced the generated "Coming soon" placeholder). Week-blocks: N4 第1回, N4 第2回, N5 第1回 (N5 level), N5 第2回 (N5 level), 本書について (guide). Built unit = `<a class="day-chip ready" href="x.html">`; unbuilt = `<span class="day-chip soon" data-href="x.html">`. Update the `.sample-note` header `In progress — N of 13 units built` each time a unit is added.

## 10. Build status

- `test-1-moji-goi.html` — built (reference implementation for the 文字・語彙 papers). All 35 answers checked against 別冊 p.16 (spread PDF 56).
- Remaining 12 units: not built.
