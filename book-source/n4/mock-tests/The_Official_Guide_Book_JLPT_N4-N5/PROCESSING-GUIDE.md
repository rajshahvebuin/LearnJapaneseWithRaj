# PROCESSING GUIDE — 新しい「日本語能力試験」ガイドブック 概要版と問題例集 N4, N5 (Official Guide Book for the new JLPT, N4・N5)

Site hub: `n4/mock-tests/official-guide-book/index.html` · Reference unit: `n4/mock-tests/official-guide-book/n4-moji-goi.html`

No N1/N2 official guide book course exists on the site (checked `n1/mock-tests`, `n2/mock-tests` and `book-source/n1|n2/mock-tests`), so this course mirrors `n5/mock-tests/official-workbook/` and its guide `book-source/n5/mock-tests/JLPT_Koushiki_Mondaishuu_N5/PROCESSING-GUIDE.md`. Use those finished pages as the templates (same CSS classes, same section order), with the differences listed below.

## 1. The source files

| File | Pages | What it is |
|---|---|---|
| `The_Official_Guide_Book_for_JLPT_N4.N5.pdf` | 76 | 新しい「日本語能力試験」ガイドブック 概要版と問題例集 N4, N5 (国際交流基金・日本国際教育支援協会, 凡人社, はじめに dated 2009年11月, ISBN 978-4-89358-735-0). The 2009 guide that introduced the 2010 test: an overview of the new test (概要), the question-type tables for N1–N5 (試験問題の構成), then **sample questions (問題例)** for N4 and for N5, answer sheets, answers (正解) and listening scripts. **No explanations (解説).** |
| `The_Official_Guide_Book_for_JLPT_N4.N5-AudioCD/` | 26 tracks | `01.Track 01.mp3` … `26.Track 26.mp3` (one CD, no titles in the file names). **Never publish.** |

The PDF is an image-only scan (no text layer at all). Render with PyMuPDF (`import pymupdf`), 110–150 dpi for whole pages; for look-alike kanji options render the page at 600 dpi and crop with PIL (pixel crops are more reliable than PDF clip rects on this scan). Python on this machine wants Windows paths (`C:/...`).

**Book type:** NOT a full mock test. It is a guide: each level gets a *small sample* of every question type (usually 2 items per 問題), not a timed paper. Do not call it a practice test on the pages; call it "sample questions (問題例)".

**N4 and N5 in one book.** The book is filed under N4 only. Decision: **the N5 sample questions are included in this same course as their own units, labelled "N5 level"** in the title, the `bp-week` line and the hub block. They stay under `n4/mock-tests/official-guide-book/` (one book = one course); the pages keep the n4 chrome (body class `level-page n4`, N4 level-nav) but every N5 unit says clearly at the top that its questions are N5 level. Do not create an n5 course folder and do not edit the N5 hub pages (a cross-link from the N5 mock-tests page can be added later by whoever owns the hubs).

## 2. Scan notes and page offsets (verified on the printed page stamps)

| PDF range | printed = | content | checked on |
|---|---|---|---|
| 1 | — | front cover | |
| 2 | (p.1, unstamped) | title page | |
| 3–5 | PDF + 0 | はじめに p.3, 目次 p.4–5 | PDF 3 = p.3, 4 = p.4, 5 = p.5 |
| 6–22 | PDF + 1 (p.6 not scanned) | 概要 p.7–17, 試験問題の構成 p.18–23 | PDF 7 = p.8, 9 = p.10, 16 = p.17, 22 = p.23 |
| 23–28 | PDF + 2 (p.24 not scanned) | 問題例 cover p.25, N4 文字・語彙 p.26–30 | PDF 24 = p.26, 25 = p.27, 28 = p.30 |
| 29–31 | PDF + 3 (p.31 not scanned) | N4 文法・読解 cover p.32, p.33–34 | PDF 29 = p.32, 30 = p.33, 31 = p.34 |
| 32–68 | PDF + 4 (p.35 not scanned) | rest of N4 and all N5 問題例 p.36–72 | PDF 32 = p.36, 40 = p.44, 46 = p.50, 56 = p.60, 64 = p.68, 68 = p.72 |
| 69–71 | PDF + 8 (p.73–76 not scanned) | N5 解答用紙 p.77–79 | PDF 69 = p.77, 71 = p.79 |
| 72 | PDF + 9 (p.80 not scanned) | **N5 正解 p.81** | PDF 72 = p.81 |
| 73–75 | PDF + 12 (p.82–84 not scanned) | **N5 聴解スクリプト p.85–87** | PDF 73 = p.85, 75 = p.87 |
| 76 | — | back cover | |

**Missing from the scan — important:**
- **p.80 = N4 正解 (the N4 answer key) is not scanned.** The 目次 (p.4) lists 正解 N4 p.80, N5 p.81; only p.81 is in the PDF.
- **p.82–84 = 聴解スクリプト N4 (the N4 listening scripts) are not scanned.** 目次: scripts N4 p.82, N5 p.85.
- p.74–76 = N4 解答用紙 (answer sheets; not needed) and p.73 (probably blank verso) not scanned.
- p.6, p.24, p.31, p.35 not scanned. Each sits next to a section cover or between 問題 blocks and the item numbers run on without a gap (e.g. N4 文法 Q4 on p.34 → Q5 on p.36), so they are almost certainly blank versos. **No N4 or N5 question page is missing.**

**Upside-down pages (scanned rotated 180°):** PDF 8 (p.9) and PDF 49, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 72, 75 (most odd printed pages from p.53 on). Render them with `page.set_rotation(180)` before reading. PDF 70 (p.78 answer sheet) is printed sideways. Many pages from PDF 41 on have a dark gutter shadow and a grey top band — readable, but zoom in.

**Filler pages (grey pattern, no content, inside the 読解 sections):** PDF 35 (p.39, N4) and PDF 57 (p.61, N5). PDF 45 (p.49) is an empty page with only the 聴解 header. Not scan gaps.

## 3. Book structure

| Part | Printed pp | PDF pp | Content |
|---|---|---|---|
| はじめに・目次 | 3–5 | 3–5 | foreword, contents |
| 新しい「日本語能力試験」の概要 | 7–17 | 6–16 | 1 新しい試験について · 2 改定のポイント (p.8–9: task-based communication, 4→5 levels with the N1–N5 vs old 1–4級 table, scaled scores, Can-do list) · 3 認定の目安 (p.10, 読む／聞く per level) · 4 試験科目と試験時間 (p.11) · 5 試験の結果 (p.12–13: 得点区分 and ranges, 合否判定 with sectional pass marks, sample score report with 参考情報 A/B/C) · 6 問題の構成 (p.14, 大問 × 小問数 for N1–N5) · 7 よくある質問 Q1–Q12 (p.15–17) |
| 試験問題の構成 | 18–23 | 17–22 | intro + legend (◆ new type, ◇ changed type, ○ same as old test) on p.18; one table per level N1 p.19, N2 p.20, N3 p.21, **N4 p.22, N5 p.23** (大問, 小問数, ねらい, and for N4/N5 the page of the 問題例) |
| 問題例 N4 | 25–48 | 23–44 | 文字・語彙 p.26–30 · 文法・読解 p.32–43 · 聴解 p.44–48 |
| 問題例 N5 | 50–72 | 46–68 | 文字・語彙 p.50–53 · 文法・読解 p.54–65 · 聴解 p.66–72 |
| 解答用紙 | (N4 74–76 missing) 77–79 | 69–71 | N5 mark sheets only. Not units. |
| 正解 | (N4 80 missing) 81 | 72 | N5 only |
| 聴解スクリプト | (N4 82–84 missing) 85–87 | 73–75 | N5 only |

Instruction lines (もんだい1 「＿＿の ことばは どう よみますか…」 etc.), the 例 items in 文法 and the question stems/options are printed on the test pages and may be quoted.

## 4. Answer key status

**N5 — official and complete:** 正解 p.81 = PDF 72 (page is upside down). Cite it as "(正解 p.81)".
- 言語知識（文字・語彙）: 1-1 2-4 3-4 4-2 5-1 6-3 7-3 8-2
- 言語知識（文法）・読解: 1-4 2-3 3-2 4-1 5-4 6-3 7-2 8-1 9-3 10-4 11-2 12-1 13-1
- 聴解: 問題1 1-3 2-4 · 問題2 1-3 2-4 · 問題3 1-3 2-2 · 問題4 1-2 2-1

**N4 — NO answer key in the scan** (p.80 not scanned). Every N4 answer on the site is ours and must be marked on every item: `<b>Our answer: 2</b> (our answer, not in book — the N4 正解 page p.80 is missing from the scan)`; the header's "Answer key" row must say so once in full. Work answers out carefully; where an item is genuinely uncertain, say so instead of guessing.
- N4 文字・語彙 (worked out for unit 1): 1-2 2-2 3-4 4-1 5-2 6-3 7-1 8-4 9-3 10-3.

**N4 聴解 — no key, no script.** The N4 listening questions cannot be answered from the book: the answer page and the script pages are both missing, and the audio is not transcribed here. For each N4 聴解 item give the printed options / picture description, the question type and the strategy, and write "Answer: not available — the book's N4 answer page (p.80) and script (p.82–84) are missing from our scan" — unless someone has listened to the track and can give a worked answer, which must then be labelled "(our answer from the audio, not in book)" with only a 1–2 sentence summary of what is heard.

文法 もんだい2 (★): even for N5 the key gives only the ★ number; the full order is ours — "(order worked out by us; the book gives only the ★ answer)".

## 5. Audio — track map (by number only; never publish or embed)

The test pages carry no track numbers and the file names carry no titles. By file size the CD splits cleanly into N4 = tracks 01–13 and N5 = tracks 14–26 (tracks 01 and 14 are both ~210 KB, i.e. the level openings). **Probable** map, inferred from file sizes (short = instruction track, long = item) — confirm by listening before relying on it, and say "probable" on the page if not confirmed:

| Level | Opening | 問題1 | 問題2 | 問題3 | 問題4 |
|---|---|---|---|---|---|
| N4 | 01 | 02 instr · 03 1ばん · 04 2ばん | 05 instr · 06 1ばん · 07 2ばん | 08 instr · 09 1ばん · 10 2ばん | 11 instr · 12 1ばん · 13 2ばん |
| N5 | 14 | 15 instr · 16 1ばん · 17 2ばん | 18 instr · 19 1ばん · 20 2ばん | 21 instr · 22 1ばん · 23 2ばん | 24 instr · 25 1ばん · 26 2ばん |

On pages use the badge `<span class="ld-track">CD · Track 16</span>`. **No `<audio>` elements, no file names or paths.**

## 6. Unit definition and table

One unit = one paper section per level (文法・読解 split at the 文法／読解 boundary, as in the N5 workbook course), plus one unit for the book's overview chapters. **9 units.** Question units come first (they are the core of the course); the overview unit is last.

| # | File | Title | Items | Printed pp | PDF pp | Answer page | Script | Audio |
|---|---|---|---|---|---|---|---|---|
| 1 | n4-moji-goi.html | N4 言語知識（文字・語彙） | もんだい1–5, Q1–10 | 27–30 (cover 26; 問題例 cover 25) | 25–28 (cover 24; 問題例 cover 23) | none (p.80 missing) — ours | — | — |
| 2 | n4-bunpou.html | N4 言語知識（文法） | もんだい1–3, Q1–9 | 33–37 (cover 32) | 30–33 (cover 29) | none — ours | — | — |
| 3 | n4-dokkai.html | N4 読解 | もんだい4–6, Q10–16 | 38–43 (39 filler) | 34–39 (35 filler) | none — ours | — | — |
| 4 | n4-choukai.html | N4 聴解 | 問題1–4, 2 items each | 45–48 (cover 44) | 41–44 (cover 40) | none | none (p.82–84 missing) | probable 01–13 |
| 5 | n5-moji-goi.html | N5 言語知識（文字・語彙） — N5 level | もんだい1–4, Q1–8 | 51–53 (cover 50) | 47–49 (cover 46) | p.81 = PDF 72 | — | — |
| 6 | n5-bunpou.html | N5 言語知識（文法） — N5 level | もんだい1–3, Q1–9 | 55–59 (cover 54) | 51–55 (cover 50) | p.81 = PDF 72 | — | — |
| 7 | n5-dokkai.html | N5 読解 — N5 level | もんだい4–6, Q10–13 | 60–65 (61 filler) | 56–61 (57 filler) | p.81 = PDF 72 | — | — |
| 8 | n5-choukai.html | N5 聴解 — N5 level | 問題1–4, 2 items each | 67–72 (cover 66) | 63–68 (cover 62) | p.81 = PDF 72 | p.85–87 = PDF 73–75 | probable 14–26 |
| 9 | gaiyou.html | 新しい「日本語能力試験」の概要・試験問題の構成 | overview + question-type tables | 7–23 | 6–22 | — | — | — |

Hub order and prev/next: n4-moji-goi → n4-bunpou → n4-dokkai → n4-choukai → n5-moji-goi → n5-bunpou → n5-dokkai → n5-choukai → gaiyou (first unit's prev = the hub; last unit's next = the hub). While the next unit is unbuilt, a page's Next link points to `index.html` (labelled "coming soon"); when you build a unit, update the previous unit's Next link to it.

## 7. Unit contents (page by page)

**1 N4 文字・語彙** — p.25 = PDF 23 is the general 問題例 cover; p.26 = PDF 24 is the 「問題例 N4 言語知識（文字・語彙）」 cover. p.27: もんだい1 漢字読み Q1 通って, Q2 医学; もんだい2 表記 Q3 おくります (近／逆／辺／送), Q4 おんがく (options are 音楽／音楽／音薬／音薬 where options 2 and 4 use a **made-up 音 with 口 instead of 日** — describe, do not type). p.28: もんだい3 文脈規定 Q5 レシート, Q6 えんりょ. p.29: もんだい4 言い換え類義 Q7, Q8. p.30: もんだい5 用法 Q9 けんぶつ, Q10 じゅうしょ (each option a full sentence). No 例 items.

**2 N4 文法** — p.33: もんだい1 文法形式の判断 例 + Q1 (おちています), Q2 (病院で; 飲まなくても いいですか). p.34: もんだい2 文の組み立て 問題例 + 答え方 + Q3, Q4. p.36: もんだい3 文章の文法 — Ali's letter to 田中さん about moving (blanks 5–9; summary only); p.37: options for Q5–9.

**3 N4 読解** — p.38: もんだい4 短文 — 中野コーヒー notice, Q10 (price calculation). p.39 filler. p.40: もんだい5 中文 — text on 引っ越しのあいさつ, Q11; p.41: Q12–14. p.42: もんだい6 情報検索 Q15–16; p.43: A 「アパートのみなさんへ」 (rubbish rules, four bins A–D) + B calendar.

**4 N4 聴解** — p.44 cover; p.45 問題1 課題理解 1ばん (printed options: ぎゅうにゅう / チーズ), 2ばん (4 pictures); p.46 問題2 ポイント理解 1ばん, 2ばん (printed options); p.47 問題3 発話表現 1ばん, 2ばん (one picture each, arrow marks the speaker); p.48 問題4 即時応答 (メモ page only). No key, no script (see §4).

**5 N5 文字・語彙** — p.51: もんだい1 Q1 新しい, Q2 電気; もんだい2 Q3 そと, Q4 ほてる. p.52: もんだい3 Q5 (タクシーに), Q6 (picture: noisy guitar). p.53 (upside down): もんだい4 Q7, Q8.

**6 N5 文法** — p.55: もんだい1 例 + Q1, Q2. p.56: もんだい2 例 + Q3. p.57 (upside down): Q4. p.58: もんだい3 two self-introductions by ジョン and ヤン (blanks 5–9; summary only); p.59 (upside down): options 5–9.

**7 N5 読解** — p.60: もんだい4 note from the teacher to アンナさん, Q10. p.61 filler. p.62: もんだい5 ヤンさん's neighbourhood, Q11; p.63 (upside down): Q12. p.64: もんだい6 train vs bus timetables to いちご山, Q13; p.65 (upside down): the two timetables.

**8 N5 聴解** — p.66 cover; p.67 (upside down) 問題1 1ばん (four textbook-page pictures); p.68 2ばん (four pictures); p.69 (upside down) 問題2 1ばん (picture of four people); p.70 2ばん (four pictures); p.71 (upside down) 問題3 1ばん, 2ばん; p.72 問題4 (メモ only). Scripts p.85–87 (M／F labels, furigana; p.87 upside down).

**9 概要** — see §3. Summarise; the level descriptions (認定の目安), the timetable, score sections/ranges and the 問題の構成 count tables are facts and may be given as tables. Note on the page that the book dates from 2009 and some details (e.g. item counts, FAQ about "the new test") have since changed — check jlpt.jp for current figures. Q&A section: summarise each Q in one line.

## 8. Page format (mirror n5/mock-tests/official-workbook)

All pages: n4 chrome (paths `../../../`, body class `level-page n4`, N4 level-nav with "Mock tests" active, breadcrumb Home / JLPT N4 / Mock tests / 公式ガイドブック N4・N5 / unit). `bp-header` (`bp-week` line with "unit X of 9" and, for N5 units, "N5-level questions"; Source with printed + PDF pages and the offset; Question types; Answer key line; Notes) → §1 Points → §2 Every question → §3 Confusion pairs → `bp-day-nav`.

- `bp-quiz` per item: `q-label`, `q-jp` (+ romaji), `q-translations` EN/HI/GU, `bp-options` table (Option / Japanese / English / Hindi / Gujarati, `tr.correct` on the answer), `bp-why`.
- N5 answer line: `<b>Answer 2</b> (正解 p.81). Why (our explanation): …`
- N4 answer line: `<b>Our answer: 2</b> (our answer, not in book). Why: …`
- Templates: 文字・語彙 = n5/mock-tests/official-workbook/moji-goi.html (plus a 用法 block for N4 もんだい5: each option a full sentence with EN/HI/GU, and a note on which use is wrong and why); 文法 = …/bunpou.html; 読解 = …/dokkai.html; 聴解 = …/choukai.html.
- 概要 unit: `bp-point` blocks with `bp-table` tables; no quiz blocks.

## 9. Hard rules

- Romaji (`<span class="romaji">`) under every Japanese line; EN + Hindi + Gujarati for every meaning, example, question sentence and option.
- Every question with its answer: N5 = official, cite 正解 p.81; N4 = "(our answer, not in book)" on every item; N4 聴解 = "not available" unless worked from the audio and labelled.
- Anything we add (tables, extra readings, explanations) is ours — say once in the header that the book has no explanations.
- **Never reproduce reading passages or listening scripts** — not on pages, scratch files or messages. Summarise in 2–3 sentences (own words, EN/HI/GU) and quote only the sentence(s) a question needs.
- Audio by track number only. No `<audio>`, no mp3 links, no file names.
- Made-up look-alike kanji in 表記 options: describe them in words, never type a different real kanji in their place.
- No emoji glyphs in body text. Do not edit CSS, JS, `tools/`, other courses or hub pages.
- Files flat in `n4/mock-tests/official-guide-book/`. Hub (`index.html`) is hand-built: built chip `<a class="day-chip ready" href="…">`, unbuilt `<span class="day-chip soon" data-href="…">`; update the `.sample-note` count `In progress — N of 9 units built`; when all are built change it to `Complete — 9 of 9 units built`.
- After building a unit: flip its chip, check balanced tags (html.parser), every relative link resolves, no `<audio>`, no passage/script text beyond quoted key lines, then (the site owner) runs `python tools/build_site.py`.
