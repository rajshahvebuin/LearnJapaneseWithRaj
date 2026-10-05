# 日本語能力試験 スーパー模試 N1 — processing guide

Standing instructions for turning `JLPT_Super_Moshi_N1.pdf` (JLPT Super Moshi N1, アルク, 監修 岡本能里子, 2011) into the site's unit pages under `n1/mock-tests/super-moshi/`. Pick a filename from the unit table (§4) and follow this guide.

## 1. The book and the PDF

- Three full mock exams (第1回–第3回), each in real-exam format: 言語知識（文字・語彙・文法）・読解 (110 min, items 1–71) + 聴解 (60 min, 37 questions). Front matter: はじめに, 日本語能力試験について知る, この本の使い方. Back: 聴解スクリプト for all three tests, 記録票 (score sheets). 別冊: answer sheets + 解答.
- 169 PDF pages, A5-ish scan. **The text layer is low-quality OCR** (wrong kanji, scrambled furigana, mojibake on front matter). Use it only to locate pages; **always render pages (PyMuPDF `import pymupdf`, 110–150 dpi) and read them visually** before writing anything.
- **The scan is incomplete** — 28 printed pages are missing (see §3). Offsets drift because of these gaps.
- **Answer key:** 別冊 解答 = numbers only, **no explanations** (no 解説). 第1回 PDF 166 (別冊 p.10), 第2回 PDF 167 (別冊 p.11), 第3回 PDF 168 (別冊 p.12). Every "Why" on the site is ours — mark it "(added, not in book)". For 問題6 (★ ordering) the key gives only the ★ tile; full orders are reasoned and must put the official tile at ★.
- No strategy / 解説 pages exist for individual question types. The only explanation pages are the front matter (JLPT overview + how to use the book + scoring), built as the `guide.html` unit.

## 2. Page map (verified on rendered page stamps)

| PDF range | Printed | Offset | Content | Verified on |
|---|---|---|---|---|
| 1–2 | cover, blank | — | | |
| 3–18 | 3–18 | PDF = printed | はじめに (3), 目次 (5), 日本語能力試験について知る (6–14), この本の使い方 (15–18) | PDF 5 = p.5, PDF 15 = p.15, PDF 17 = p.17 |
| 19–59 | 19–59 | PDF = printed | 第1回 title (19), 言語知識・読解 (20–47), 聴解 (48–59) | PDF 20 = p.20, PDF 29 = p.29, PDF 48 = p.48, PDF 59 = p.59 |
| 60–91 | 60–91 | PDF = printed | blank (60), 第2回 title (61), 言語知識・読解 (62–89), 聴解 (90–91) | PDF 62 = p.62, PDF 91 = p.91 |
| — | **92–93 missing** | | 第2回 聴解 問題1 5番・6番 | |
| 92–95 | 94–97 | printed = PDF + 2 | 第2回 聴解 問題2 (94–96), 問題3 (97) | PDF 92 = p.94, PDF 95 = p.97 |
| — | **98–111 missing** | | 第2回 聴解 問題4・5 (98–102), 第3回 title, 第3回 言語知識 問題1–6 (104–111) | |
| 96–99 | 112–115 | printed = PDF + 16 | 第3回 問題7 (112–113), 問題8 (1)(2) (114–115) | PDF 96 = p.112, PDF 99 = p.115 |
| — | **116–125 missing** | | 第3回 問題8 (3)(4), 問題9, 問題10 | |
| 100–118 | 126–144 | printed = PDF + 26 | 第3回 問題11–13 (126–131), 聴解 (132–143), blank (144) | PDF 100 = p.126, PDF 106 = p.132, PDF 117 = p.143 |
| 119–131 | 145–157 | printed = PDF + 26 | 聴解スクリプト 第1回 (145–156), 第2回 start (157) | PDF 119 = p.145, PDF 131 = p.157 |
| — | **158–159 missing** | | 第2回 script: 問題1 2番 (end) – 6番, 問題2 1番 (start) | |
| 132–155 | 160–183 | printed = PDF + 28 | 第2回 script (160–168), 第3回 script (169–180), 記録票 (181–183) | PDF 132 = p.160, PDF 141 = p.169, PDF 155 = p.183 |
| 156–157 | — | | colophon / authors, blank | |
| 158–168 | 別冊 cover, 3–12 | 別冊 p = PDF − 156 | 別冊 目次 (159), 解答用紙 (160–165), 解答 (166–168) | PDF 159 = 別冊 p.3, PDF 166 = 別冊 p.10, PDF 168 = 別冊 p.12 |
| 169 | — | | back cover | |

## 3. Missing pages — what each affected unit must do

| Unit | Missing | What to do |
|---|---|---|
| test-2-choukai | p.92–93 (問題1 5番・6番 options); p.98–102 (問題4, 問題5 pages — only 問題5 3番 has printed options); script p.158–159 (問題1 2番 end – 6番, 問題2 1番 start) | 問題1 3番・4番: options survive, script missing. 問題1 5番・6番: **no options and no script** — give the key number only, marked "question page and script missing from the scan". 問題4 / 問題5 1–2番 print nothing anyway (options are spoken) — use the scripts (p.160–168 survive). 問題5 3番: options are reconstructed from the script if it states them; otherwise say so. |
| test-3-gengo | p.104–111 (問題1–6, items 1–40) | Build only 問題7 (items 41–45, PDF 96–97). List items 1–40 as "question pages missing from the scan" with the key numbers from 別冊 p.12 (PDF 168), nothing invented. |
| test-3-dokkai | p.116–125 (問題8 (3)(4), 問題9, 問題10 = items 48–62) | Build 問題8 (1)(2) (items 46–47), 問題11–13 (63–71). Items 48–62: key numbers only, marked missing. |

## 4. Unit definition and full unit table

A unit = one paper of one 回: 言語知識（文字・語彙・文法） (問題1–7, items 1–45), 読解 (問題8–13, items 46–71), 聴解 (問題1–5, 37 questions) — plus one `guide.html` unit for the book's explanation pages. 10 units.

| # | Filename | Title | Printed pp | PDF pp | Answer key PDF | Audio |
|---|---|---|---|---|---|---|
| 1 | guide.html | はじめに・日本語能力試験について知る・この本の使い方・記録票 | 3, 5–18, 181–183 | 3, 5–18, 153–155 | — | — |
| 2 | test-1-gengo.html | 第1回 言語知識（文字・語彙・文法） 問題1–7 (1–45) | 20–29 | 20–29 | 166 (別冊 p.10) | — |
| 3 | test-1-dokkai.html | 第1回 読解 問題8–13 (46–71) | 30–47 | 30–47 | 166 | — |
| 4 | test-1-choukai.html | 第1回 聴解 問題1–5 + script | 48–59; script 145–156 | 48–59; 119–130 | 166 | CD1 T1–41 |
| 5 | test-2-gengo.html | 第2回 言語知識（文字・語彙・文法） 問題1–7 (1–45) | 62–71 | 62–71 | 167 (別冊 p.11) | — |
| 6 | test-2-dokkai.html | 第2回 読解 問題8–13 (46–71) | 72–89 | 72–89 | 167 | — |
| 7 | test-2-choukai.html | 第2回 聴解 問題1–5 + script | 90–103 (92–93, 98–103 missing); script 157–168 (158–159 missing) | 90–95; 131–140 | 167 | CD2 T1–41 |
| 8 | test-3-gengo.html | 第3回 言語知識（文字・語彙・文法） — only 問題7 (41–45) survives | 104–113 (104–111 missing) | 96–97 | 168 (別冊 p.12) | — |
| 9 | test-3-dokkai.html | 第3回 読解 — 問題8 (1)(2), 問題11–13 survive | 114–131 (116–125 missing) | 98–105 | 168 | — |
| 10 | test-3-choukai.html | 第3回 聴解 問題1–5 + script | 132–143; script 169–180 | 106–117; 141–152 | 168 | CD3 T1–41 |

Paper layout inside each 回 (same for all three; item numbers continue across 言語知識 and 読解 as in the real exam):

- 言語知識: 問題1 漢字読み 1–6 · 問題2 文脈規定 7–13 · 問題3 言い換え類義 14–19 · 問題4 用法 20–25 · 問題5 文法形式の判断 26–35 · 問題6 文の組み立て★ 36–40 · 問題7 文章の文法 41–45.
- 読解: 問題8 内容理解（短文）46–49 (4 passages) · 問題9 内容理解（中文）50–58 (3 passages × 3) · 問題10 内容理解（長文）59–62 · 問題11 統合理解 63–65 (A/B) · 問題12 主張理解（長文）66–69 · 問題13 情報検索 70–71.
- 聴解: 問題1 課題理解 1–6番 · 問題2 ポイント理解 1–7番 · 問題3 概要理解 1–6番 · 問題4 即時応答 1–14番 · 問題5 統合理解 1番, 2番, 3番 (質問1・2) = 37 questions.

## 5. Audio — track map (CDs listed next to the PDF; never publish them)

Three CDs, one per 回: `JLPT_Super_Moshi_N1-AudioCD1/` = 第1回, `CD2` = 第2回, `CD3` = 第3回. Each holds 41 tracks named `NN Track N.wma`. The book's CD badges ("CD-1 ⑤") were checked on PDF 48–59 (CD1), 91–95 (CD2) and 106–117 (CD3); the layout is identical on all three CDs:

| Track | Content |
|---|---|
| 1 | 問題1 instructions |
| 2–7 | 問題1 1番–6番 |
| 8 | 問題2 instructions |
| 9–15 | 問題2 1番–7番 |
| 16 | 問題3 instructions |
| 17–22 | 問題3 1番–6番 |
| 23 | 問題4 instructions |
| 24–37 | 問題4 1番–14番 |
| 38 | 問題5 instructions |
| 39, 40, 41 | 問題5 1番, 2番, 3番 (質問1・2) |

Refer to audio only as e.g. `<span class="ld-track">CD1 · Track 12</span>`. **No `<audio>` elements, no links to the .wma files, no copies.**

## 6. Hard content rules (from the site brief)

- **No long passages or transcripts.** Reading passages (問題7 cloze, 問題8–13) and listening scripts are never reproduced verbatim — not in pages, scratch files or notes. For each passage/script write a 2–3 sentence "Passage summary (not the book's text)" / "Script summary (not the book's text)" in EN, HI and GU in your own words, then quote **only** the sentence(s) a question needs (for 問題7: the sentence containing each blank; for reading: the key sentence; for listening: the deciding line). Question stems and options are quoted in full. If an output is blocked by the content filter, leave that part out and report it — do not work around it.
- Never invent questions or answers. Missing pages are marked as missing (§3).
- EN + HI + GU for every meaning / example / question sentence; `<span class="romaji">` under every Japanese line; "(added, not in book)" on anything we add (all explanations, distractor notes, word tables beyond what the book prints).

## 7. Page sections

Shared CSS only (bp-*, kd-*, vd-*, rd-*, ld-track, day chips); no new CSS/JS. Head/header/footer copied from `index.html` in this folder (depth `../../../`). Breadcrumb: Home / JLPT N1 / Mock tests (`../../mock-tests.html`) / スーパー模試 N1 (`index.html`) / unit.

**Header** `.bp-header`: 回 + paper, printed pp + PDF pp, item range, key status ("from 別冊 解答 p.N (PDF M), numbers only"), scoring formula for that paper (book p.16: 60 × correct ÷ 45 / 26 / 37; pass = total ≥ 100 of 180 and every section above 19 — the book says 19点以下は不合格), the time (110 min shared by 言語知識・読解; 60 min 聴解), and any missing pages.

**§1 Points** — what the paper tests, as revision tables (all added): 言語知識 → a vocabulary table (every target word of 問題1–4 with reading, EN/HI/GU) + a grammar table (pattern tested by each 問題5–6 item, meaning EN/HI/GU, connection). 読解 → per passage: source line, question type, "how to find the answer" note. 聴解 → per 問題 type: what to listen for. Cross-link earlier site pages where useful (e.g. `../../grammar/shin-kanzen-master/…`).

**§2 Every question** — one `.bp-quiz` per item, numbered as in the book (Q1…Q45 / Q46…Q71 / 問題1 1番…):
- 問題1–3, 5: stem (with （　） or <u>underline</u>) + romaji, full sentence, EN/HI/GU; `.bp-options` table (option · JP + romaji · EN · HI · GU), `tr.correct` on the key answer; `.bp-why` with "Answer N (別冊 key)" + why the others fail (added). Reference: `n1/multi-skill/pattern-betsu-tettei-drill/moji-kanji-yomi-1.html`, `n1/grammar/shin-kanzen-master/mock-test-1.html`.
- 問題4 用法: option column = the full sentence; wrong options get "✗ Means … — needs X" (ref. `pattern-betsu-tettei-drill/moji-youhou-doushi.html`).
- 問題6 ★: tiles line, `.bp-order-chain`, `.bp-assembled` + romaji, EN/HI/GU, options table, why (★ tile from key; order reasoned).
- 問題7: one `.bp-point` with the source line and a 2–3 sentence passage summary (EN/HI/GU, not the book's text), then one quiz per blank quoting only the sentence with the blank.
- 読解: per passage `.bp-point` with source + summary, then each question: stem + options (quoted) with EN/HI/GU, the key sentence(s) quoted, why (added). Reference: `n1/multi-skill/drill-and-drill/r-choubun-01.html`.
- 聴解: per question `<span class="ld-track">CDn · Track NN</span>`, the question (spoken questions taken from the script), printed options (or spoken options from the script for 問題3–5), script summary, the deciding line quoted, answer + why. Reference: `n1/multi-skill/drill-and-drill/l-kadai-01.html`.

**§3 Confusion pairs / traps** — `.bp-confusion` table of look-alike words / readings / patterns from the wrong options, plus 2–3 `.bp-callout` exam tips (added).

**Footer nav** `.bp-day-nav`: ← previous unit / next unit → in table order (§4).

## 8. File naming

`guide.html`, `test-{1,2,3}-{gengo,dokkai,choukai}.html` in `n1/mock-tests/super-moshi/`. The hub `index.html` lists all 10; a built unit is `<a class="day-chip ready" href="…">`, an unbuilt one `<span class="day-chip soon" data-href="…">`, and the `.sample-note` reads `In progress — N of 10 units built`.

## 9. Build status

- `test-1-gengo.html` — built (reference implementation for the 言語知識 papers). All 45 answers checked against 別冊 p.10 (PDF 166).
- Remaining 9 units: not built.
