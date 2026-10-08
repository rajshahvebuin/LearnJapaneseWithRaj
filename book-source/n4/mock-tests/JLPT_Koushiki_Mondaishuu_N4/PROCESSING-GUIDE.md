# PROCESSING GUIDE — 日本語能力試験 公式問題集 N4 (JLPT Official Practice Workbook N4)

Site hub: `n4/mock-tests/official-workbook/index.html` · Reference unit: `n4/mock-tests/official-workbook/moji-goi.html`
Sister course (same book series, already finished — copy its page format): `n5/mock-tests/official-workbook/` and `book-source/n5/mock-tests/JLPT_Koushiki_Mondaishuu_N5/PROCESSING-GUIDE.md`.

## 1. The source files

| File | Pages | What it is |
|---|---|---|
| `JLPT_Koushiki_Mondaishuu_N4.pdf` | 93 | 日本語能力試験 公式問題集 N4 (国際交流基金 + 日本国際教育支援協会, 凡人社, 初版 2012-03-31). Section 1 試験問題: ONE complete N4 test (問題用紙 for the three papers) + 解答用紙. Section 2 正答表と聴解スクリプト: answer key + listening scripts. Section 3 日本語能力試験の概要: general JLPT information (levels, scoring, FAQ). **No explanations (解説)** anywhere in the book. |
| `JLPT_Koushiki_Mondaishuu_N4-AudioCD/` | 39 tracks | `01.mp3` … `39.mp3` (one CD; file names are numbers only). **Never publish.** |

The PDF is an image-only scan (no text layer; one 2105×2977 JPEG per page ≈ 300 dpi). Render with PyMuPDF (`import pymupdf`), 100–150 dpi for whole pages; Python on this machine wants Windows paths (`C:/...`). The 文字 問題2 options use look-alike / made-up kanji shapes that differ by one stroke — render those lines at 400–600 dpi (clip). Even then the scan resolution makes some differences hard to see: rely on the 正答表 and describe the wrong shape as "look-alike, not a real kanji".

**Book type:** the official JLPT workbook — ONE full test in the current N4 layout: 言語知識（文字・語彙） 30分 (34 items), 言語知識（文法）・読解 60分 (35 items), 聴解 35分 (例 + 8/7/5/8 items). Page headers name the paper and its page, e.g. 「言語知識（文字・語彙）－ 3」, 「言語知識（文法）・読解－ 12」, 「聴解－ 5」.

## 2. Page offsets (verified on the printed page stamps)

The offset changes several times because some blank versos were not scanned.

| PDF range | printed = | checked on |
|---|---|---|
| 1–2 | — | PDF 1 front cover (colour), PDF 2 a greyscale copy of the cover (title page) |
| 3–4 | roman | PDF 3 = p.i (はじめに), PDF 4 = p.ii (目次) |
| 5 | PDF − 4 | PDF 5 = p.1 (section divider 「1 試験問題」) |
| 6 | PDF − 3 | PDF 6 = p.3 (文字・語彙 cover) |
| 7–15 | PDF − 2 | PDF 7 = p.5, 8 = p.6, 9 = p.7, 15 = p.13 |
| 16 | PDF − 1 | PDF 16 = p.15 (文法・読解 cover) |
| 17–31 | PDF + 0 | PDF 17 = p.17, 31 = p.31 |
| 32 | PDF + 1 | PDF 32 = p.33 (聴解 cover) |
| 33–63 | PDF + 2 | PDF 33 = p.35, 47 = p.49, 48 = p.50, 50 = p.52, 51 = p.53 (divider 2), 52 = p.54 (正答表), 54 = p.56, 62 = p.64, 63 = p.65 |
| 64 | duplicate | PDF 64 is a **second scan of p.64** (same 聴解スクリプト page as PDF 62). Ignore it. |
| 65–91 | PDF + 2 | PDF 65 = p.67 (divider 3), 66 = p.68, 91 = p.93 |
| 92–93 | — | PDF 92 colophon (奥付), PDF 93 back cover |

Not in the scan: p.2, p.4, p.14, p.16, p.32, p.34 (each the verso right after a divider or paper cover — almost certainly blank) and p.66 (after the last script page — almost certainly blank). **No question, key or script page is missing.**

Part-empty pages that ARE scanned (not gaps): PDF 8 (p.6) has only 文字 Q9; PDF 11 (p.9) only Q23–24; PDF 13 (p.11) only Q28–29; PDF 15 (p.13) only Q33–34.

## 3. Structure of the test

| Paper | Time | 問題 (item numbers) | PDF pp (printed) |
|---|---|---|---|
| 言語知識（文字・語彙） | 30分 | cover PDF 6 (p.3) · 問題1 漢字読み 1–9 (PDF 7–8) · 問題2 表記 10–15 (PDF 9) · 問題3 文脈規定 16–24 (PDF 10–11) · 問題4 言い換え類義 25–29 (PDF 12–13) · 問題5 用法 30–34 (PDF 14–15) | 6–15 (3–13) |
| 言語知識（文法）・読解 | 60分 | cover PDF 16 (p.15) · 文法: 問題1 文法形式の判断 1–15 (PDF 17–19) · 問題2 文の組み立て ★ 16–20 (PDF 20–21) · 問題3 文章の文法 21–25 (essay 「ポチ」 about the family dog, PDF 22–23) · 読解: 問題4 内容理解（短文） 26–29 (four texts (1)–(4): a memo, a park notice, an e-mail, a short text about a librarian; PDF 24–27) · 問題5 内容理解（中文） 30–33 (a family hotel trip, PDF 28–29) · 問題6 情報検索 34–35 (questions PDF 30, flyer 「あおぞら一日スポーツ教室」 PDF 31) | 16–31 (15–31) |
| 聴解 | 35分 | cover PDF 32 (p.33) · 問題1 課題理解 例+1–8 (PDF 33–37; pictures or printed options) · 問題2 ポイント理解 例+1–7 (PDF 38–42; printed options) · 問題3 発話表現 例+1–5 (PDF 43–46; one picture with an arrow each, options only on the audio) · 問題4 即時応答 例+1–8 (PDF 47, "メモ" page only) | 32–47 (33–49) |

解答用紙: PDF 48 文字・語彙, 49 文法・読解, 50 聴解 (printed rotated, p.50–52). Not units.
Section 3 (PDF 65–91, p.67–93) is general JLPT information — not a unit; nothing from it needs publishing.

The book's instruction lines (もんだい1 「＿＿の ことばは ひらがなで どう かきますか…」 etc.) and the 例 items with their filled-in answer bubbles are printed on the test pages and may be quoted.

## 4. Answer key status

**Official and complete** — 正答表 PDF 52–53 (p.54–55). There are **no 解説**: every "Why" on our pages is our own explanation and must be worded as such (e.g. "Answer 2 (正答表 p.54). Why (our explanation): …").

言語知識（文字・語彙） (PDF 52 = p.54): 問題1 1-1 2-1 3-4 4-2 5-2 6-3 7-1 8-2 9-4 · 問題2 10-1 11-4 12-3 13-4 14-4 15-1 · 問題3 16-4 17-3 18-2 19-2 20-4 21-3 22-1 23-2 24-3 · 問題4 25-3 26-2 27-1 28-3 29-2 · 問題5 30-4 31-3 32-4 33-1 34-2.

言語知識（文法）・読解 (PDF 52–53 = p.54–55): 問題1 1-3 2-4 3-1 4-2 5-4 6-2 7-3 8-1 9-2 10-4 11-1 12-1 13-3 14-4 15-2 · 問題2 16-3 17-2 18-4 19-3 20-3 · 問題3 21-2 22-3 23-2 24-1 25-4 · 問題4 26-4 27-3 28-2 29-3 · 問題5 30-2 31-4 32-4 33-1 · 問題6 34-3 35-2.

聴解 (PDF 53 = p.55): 問題1 例4, 1-1 2-4 3-3 4-4 5-3 6-2 7-2 8-1 · 問題2 例3, 1-4 2-2 3-3 4-3 5-1 6-2 7-3 · 問題3 例3, 1-1 2-2 3-1 4-2 5-1 · 問題4 例3, 1-2 2-3 3-2 4-1 5-2 6-3 7-3 8-1.

All 34 文字・語彙 answers were checked against the question pages (each keyed option is the sensible one). 問題2 (文の組み立て ★): the key gives only the ★ number; the full order is ours — say "(order worked out by us; the book gives only the ★ answer)".

Print quirk — 文字・語彙 問題2 look-alike options (checked at 600 dpi): Q11 options 1–2 pair 揚／場 with a made-up 所-like shape, option 3 揚所 (real kanji, wrong word); Q12 two shapes of 走 and two of 歩 — one of each pair is made up (option 4 is a look-alike 歩); Q13 options 1 and 4 both look like 便利, 2 and 3 like 便理 — option 1 has a changed stroke; Q14 options 2 and 4 both look like 眠かった (option 2 a look-alike), 1 and 3 are 眠むかった (wrong okurigana). Q10 (青／黒／赤／白) and Q15 (雪／電／雷／雲) are all real kanji. Never type a non-existent glyph — describe it.

## 5. Audio — track map (by number only; never publish or embed)

The test pages carry no track badges and the CD files are named only `01`–`39`. The map below is **inferred** from the item counts and the file sizes (instructions and 例 tracks are longer; 問題3–4 items are short; 21 is a long track with the break pause; 39 is very short = おわり). Confirm by listening before relying on a single track number.

| Section | Tracks |
|---|---|
| 聴解 opening announcement | 01 |
| 問題1 | 02 instructions · 例 03 · 1番 04 · 2番 05 · 3番 06 · 4番 07 · 5番 08 · 6番 09 · 7番 10 · 8番 11 |
| 問題2 | 12 instructions · 例 13 · 1番 14 · 2番 15 · 3番 16 · 4番 17 · 5番 18 · 6番 19 · 7番 20 |
| break | 21 |
| 問題3 | 22 instructions · 例 23 · 1番 24 · 2番 25 · 3番 26 · 4番 27 · 5番 28 |
| 問題4 | 29 instructions · 例 30 · 1番 31 · 2番 32 · 3番 33 · 4番 34 · 5番 35 · 6番 36 · 7番 37 · 8番 38 |
| end | 39 |

On pages use the badge `<span class="ld-track">CD · Track 04</span>`. **No `<audio>` elements, no file names or paths.**

聴解スクリプト (PDF 54–63 = p.56–65; M／F speaker labels, furigana; PDF 64 = duplicate of p.64): 問題1 PDF 54–57 (例 + 1番 PDF 54, 2–4番 PDF 55, 5–7番 PDF 56, 8番 PDF 57) · 問題2 PDF 57–60 (例 starts PDF 57) · 問題3 PDF 60–61 (例 starts PDF 60) · 問題4 PDF 61–63 (例 bottom of PDF 61, 1–5番 PDF 62, 6–8番 PDF 63). Confirm each 番 on the rendered page.

## 6. Unit definition and table

Same split as the N5 book: one unit = one paper, except that 文法・読解 is split at the 文法 / 読解 boundary. **4 units.**

| # | File | Title | Items | Printed pp | PDF pp | Key PDF (printed) | Script PDF | Audio |
|---|---|---|---|---|---|---|---|---|
| 1 | moji-goi.html | 言語知識（文字・語彙） | 問題1–5, Q1–34 | 5–13 (cover 3) | 7–15 (cover 6) | 52 (54) | — | — |
| 2 | bunpou.html | 言語知識（文法） | 問題1–3, Q1–25 | 17–23 (cover 15) | 17–23 (cover 16) | 52 (54) | — | — |
| 3 | dokkai.html | 読解 | 問題4–6, Q26–35 | 24–31 | 24–31 | 53 (55) | — | — |
| 4 | choukai.html | 聴解 | 問題1–4 (例 + 8/7/5/8) | 35–49 (cover 33) | 33–47 (cover 32) | 53 (55) | 54–63 (56–65) | CD · Tracks 01–39 |

Hub order and prev/next: moji-goi → bunpou → dokkai → choukai (first unit's prev = the hub; last unit's next = the hub).

## 7. How each paper maps to the page sections

All pages: `bp-header` (Source with printed + PDF pages and the offset, question types, answer key line, Notes) → §1 Points → §2 Every question → §3 Confusion pairs → `bp-day-nav`. EN + Hindi + Gujarati for every meaning, question sentence and option; `<span class="romaji">` under every Japanese line; anything we add is marked "(added, not in book)" — and since the book has no 解説, say once in the header that all explanations are ours. Headings carry the 問題 type and item range. Keep language simple (N4 learners). The N4 test sentences use kanji with small furigana above some words; we write them in kanji + kana as printed (furigana are not reproduced) and give the full reading in romaji.

### 文字・語彙 (reference: moji-goi.html)
- §1: kanji table (`kd-kanji-table`) for every kanji word in 問題1–2 (reading in the item + common other reading, our additions); vocabulary table (`bp-table`) for 問題3–5 words; for 問題4 show the underlined phrase and its paraphrase; for 問題5 the word and its core use.
- §2: 問題1 漢字読み — sentence + underlined word, options = readings (mark long-vowel / small っ / dakuten traps). 問題2 表記 — options = written forms; describe made-up kanji. 問題3 文脈規定 — sentence with （　）, options with meanings. 問題4 言い換え類義 — each option a full sentence with EN/HI/GU. 問題5 用法 (new at N4) — the target word, then each of the four sentences with EN/HI/GU and a note on why the word does or does not fit.
- §3: `bp-confusion` from the trap sets + 2–3 `bp-callout`.

### 文法 (template: n5/mock-tests/official-workbook/bunpou.html)
- §1: pattern table (pattern → meaning EN/HI/GU → example).
- §2: 問題1 each item with options; 問題2 ★ tiles + `bp-order-chain` + `bp-assembled` (order ours); 問題3 the essay 「ポチ」 — **summary only** (EN/HI/GU) + the sentence around each blank.
- §3: confusable pattern pairs.

### 読解 (template: n5/mock-tests/official-workbook/dokkai.html)
- §1: strategy box (`rd-strategy`) for 短文 / 中文 / 情報検索 + key words.
- §2: per text: **Passage summary (not the book's text)** EN/HI/GU, the question + options (EN/HI/GU), quote only the key sentence, answer + why. Q34–35: summarise only the flyer rows needed (sports, times, place, fees, sign-up deadline) — do not reproduce the whole flyer.
- §3: distractor patterns.

### 聴解 (template: n5/mock-tests/official-workbook/choukai.html)
- §1: strategy per 問題 type (課題理解, ポイント理解, 発話表現, 即時応答) + useful expressions.
- §2: per item `ld-track` badge, printed options (問題1–2) or picture description (問題1 picture items, 問題3), **Script summary (not the book's text)** EN/HI/GU, quote only the key line(s), official answer + why. 問題3–4 options exist only on the audio: they are short one-line replies and may be quoted as options, with EN/HI/GU.
- §3: confusable set phrases and number/time traps.

## 8. Passage, script and audio rules (hard)

- **Never reproduce reading passages or listening scripts** — not in pages, scratch files, notes or messages. Summarise in 2–3 sentences (own words, EN/HI/GU) and quote only the sentence(s) a question needs.
- Question stems, printed options, instructions and 例 items may be quoted.
- Audio by track number only. Never link, embed or copy the mp3 files.
- Never invent questions or answers — the 正答表 is official; cite PDF/printed page. Worked answers not from the book (e.g. full ★ orders) are labelled "(our answer, not in book)".
- No emoji glyphs in body text. Do not edit CSS, JS, `tools/`, other courses or hub pages.

## 9. File naming & hub

- Files flat in `n4/mock-tests/official-workbook/`: `moji-goi.html`, `bunpou.html`, `dokkai.html`, `choukai.html`.
- Hub (`index.html`): one `.week-block` per paper (文字・語彙 / 文法・読解 / 聴解). Built chip `<a class="day-chip ready" href="…">`, unbuilt `<span class="day-chip soon" data-href="…">`. Update `In progress — N of 4 units built`; when all are built, change the note to `Complete — 4 of 4 units built` (build_site.py then marks the book ready).
- After building a unit: flip its chip, check balanced tags (html.parser), every relative link resolves, no `<audio>`, no passage/script text beyond quoted key lines, then run `python tools/build_site.py` (only when the person running the workflow allows it).

## 10. Build log

- Unit 1 `moji-goi.html` — built (問題1–5, Q1–34).
