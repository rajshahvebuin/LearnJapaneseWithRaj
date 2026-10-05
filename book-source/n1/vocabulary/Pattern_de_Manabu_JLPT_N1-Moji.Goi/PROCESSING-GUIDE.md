# パターンで学ぶ 日本語能力試験N1 文字・語彙問題集 — processing guide

Book: 増補版 パターンで学ぶ 日本語能力試験 N1文字・語彙問題集 (Learning Through Patterns: A Kanji and Vocabulary Workbook for Level N1), 岡本牧子・氏原庸子 (大阪YWCA), Jリサーチ出版, 2010.
PDF: `Pattern_de_Manabu_JLPT_N1-Moji.Goi.pdf` (162 PDF pages, same folder as this file).
Site folder: `n1/vocabulary/pattern-de-manabu/` (hub `index.html`, one HTML file per unit).
Master vocab spec: `book-source/n1/vocabulary/PROCESSING-GUIDE.md`. Reference implementation for this book: `n1/vocabulary/pattern-de-manabu/moji-i1-1.html`.

---

## 1. Scan facts (verified on rendered pages)

- **The text layer is noisy OCR.** Furigana, underlines and the boxed answer numbers come out as garbage, and the kanji are often wrong (e.g. 問題 → 間題, 漢字 → 漠字). Use it only to find pages. **Always read content from rendered images** (PyMuPDF, 150–200 dpi; crop the page in halves to read the small example phrases).
- Every PDF page has a "facebook.com/duytrieuftu" watermark at the top. Ignore it.
- **The PDF↔printed offset changes four times.** Checked against the printed page numbers at the foot of each page:

| PDF pages | Printed pages | Rule |
|---|---|---|
| 1 | cover | — |
| 2–29 | 3–30 | printed = PDF + 1 (verified: PDF 2 = p.3 目次, PDF 7 = p.8, PDF 8 = p.9, PDF 29 = p.30) |
| 30 | 2 (はじめに) | page bound out of order |
| 31–83 | 31–83 | printed = PDF (verified: PDF 31 = p.31, PDF 60 = p.60, PDF 83 = p.83) |
| — | **84–89** | **missing from the scan** (6 pages; the start of 第2章 II 形が似ているパターン) |
| 84–153 | 90–159 | printed = PDF + 6 (verified: PDF 84 = p.90, PDF 106 = p.112, PDF 132 = p.138, PDF 153 = p.159) |
| 154 | colophon (奥付) | — |
| 155–162 | 別冊 cover + 別冊 p.2–8 | 別冊 p.N = PDF 154 + N |

- Blank / title pages: PDF 5 (p.6, blank), PDF 6 (p.7, 第1章 title), PDF 58 (p.58, blank), PDF 59 (p.59, 第2章 title), PDF 104 (p.110, blank), PDF 105 (p.111, 第3章 title), PDF 130 (p.136, blank), PDF 131 (p.137, 模擬試験 title), PDF 152–153 (p.158–159, mark-sheet answer grids — not a unit).
- Front matter: p.3 目次 (PDF 2), p.4–5 「N1文字・語彙の問題パターン」 (PDF 3–4) — an overview of the four JLPT question types (問題1 漢字読み, 問題2 文脈規定, 問題3 言い換え類義, 問題4 用法). It is summarised on the hub, not built as a unit.

## 2. Answer key — 別冊〈解答・解説〉 (PDF 155–162), official, complete

| 別冊 p. | PDF | Covers |
|---|---|---|
| 2 | 156 | 第1章 p.9 – p.43 |
| 3 | 157 | 第1章 p.45 – p.57; 第2章 p.61 – p.87 |
| 4 | 158 | 第2章 p.89 – p.109 |
| 5 | 159 | 第1回 まとめ問題 (65 items) + 解説 for selected items |
| 6 | 160 | 第2回 まとめ問題 + 解説 (heading misprinted "p.113"; it is the p.120 test) |
| 7 | 161 | 第3回 まとめ問題 + 解説 (heading misprinted "p.114"; it is the p.128 test) |
| 8 | 162 | 模擬試験 第1–4回 (25 items each) + 解説 for selected items |

The key is listed by the printed page of the 問題 page (p.9, p.11, …). Chapter 1–2 keys give answer numbers only; the 解き方 / 解説 text exists only for the 例題 on each pattern's first page and for selected まとめ・模擬 items. Cite answers as "(book key, 別冊 p.N)". Write the "Why" yourself and mark anything beyond the book's 解説 as "(added, not in book)".

The questions for p.85, p.87 and p.89 are **not in the scan** (only their answer numbers are in the key). Do not rebuild those questions from the key. Their units stay as "soon" chips on the hub, labelled as missing from the scan.

## 3. Unit definition

- **第1章・第2章: one unit = one two-page spread** (even page = 例題 box (first spread of a pattern only) + word/kanji list; odd page = 問題). Every odd page from p.9 to p.109 is a 問題 page, and that is how the 別冊 key is organised.
- **第3章: one unit = one whole まとめ問題 (8 pages, 65 items) or one 模擬試験 (5 pages, 25 items).**
- 57 units in total: 25 in 第1章, 25 in 第2章 (3 of them missing from the scan), 7 in 第3章.

## 4. Unit table

File names: `moji-<pattern>-<n>.html` for 第1章, `goi-<pattern>-<n>.html` for 第2章, `matome-<n>.html` / `mogi-<n>.html` for 第3章.

| File | Title | Printed pp | PDF pp | Key (別冊 p / PDF) | Items |
|---|---|---|---|---|---|
| moji-i1-1.html | I-1 読み方が同じもの ① (あいかん〜かいそう) | 8–9 | 7–8 | 2 / 156 | I 8 + II 5 |
| moji-i1-2.html | I-1 読み方が同じもの ② (かいそく〜きさい) | 10–11 | 9–10 | 2 / 156 | I 8 + II 5 |
| moji-i1-3.html | I-1 読み方が同じもの ③ | 12–13 | 11–12 | 2 / 156 | I 8 + II 5 |
| moji-i1-4.html | I-1 読み方が同じもの ④ | 14–15 | 13–14 | 2 / 156 | I 8 + II 5 |
| moji-i1-5.html | I-1 読み方が同じもの ⑤ | 16–17 | 15–16 | 2 / 156 | I 8 + II 5 |
| moji-i1-6.html | I-1 読み方が同じもの ⑥ | 18–19 | 17–18 | 2 / 156 | I 8 + II 5 |
| moji-i2-1.html | I-2 訓読みが複数あるもの ① | 20–21 | 19–20 | 2 / 156 | I 8 + II 5 |
| moji-i2-2.html | I-2 訓読みが複数あるもの ② | 22–23 | 21–22 | 2 / 156 | I 8 + II 6 |
| moji-i2-3.html | I-2 訓読みが複数あるもの ③ | 24–25 | 23–24 | 2 / 156 | I 8 + II 6 |
| moji-i2-4.html | I-2 訓読みが複数あるもの ④ | 26–27 | 25–26 | 2 / 156 | I 8 + II 6 (II numbered 1–6) |
| moji-ii1-1.html | II-1 形が似ていて読み方が同じもの ① | 28–29 | 27–28 | 2 / 156 | 6 |
| moji-ii1-2.html | II-1 形が似ていて読み方が同じもの ② | 30–31 | 29, 31 (PDF 30 = はじめに, out of order) | 2 / 156 | 6 |
| moji-ii1-3.html | II-1 形が似ていて読み方が同じもの ③ | 32–33 | 32–33 | 2 / 156 | 6 |
| moji-ii1-4.html | II-1 形が似ていて読み方が同じもの ④ | 34–35 | 34–35 | 2 / 156 | 6 |
| moji-ii2-1.html | II-2 形が似ていて読み方が違うもの | 36–37 | 36–37 | 2 / 156 | 10 |
| moji-iii1-1.html | III-1 一字で言葉になるもの ① | 38–39 | 38–39 | 2 / 156 | 10 |
| moji-iii1-2.html | III-1 一字で言葉になるもの ② | 40–41 | 40–41 | 2 / 156 | 10 |
| moji-iii2-1.html | III-2 特別な読み方 | 42–43 | 42–43 | 2 / 156 | 16 |
| moji-iv1-1.html | IV-1 小さい「っ」になるもの ① | 44–45 | 44–45 | 3 / 157 | 17 |
| moji-iv1-2.html | IV-1 小さい「っ」になるもの ② | 46–47 | 46–47 | 3 / 157 | 17 |
| moji-iv2-1.html | IV-2 音が「゛」や「゜」に変わるもの ① | 48–49 | 48–49 | 3 / 157 | 10 |
| moji-iv2-2.html | IV-2 音が「゛」や「゜」に変わるもの ② | 50–51 | 50–51 | 3 / 157 | 10 |
| moji-iv3-1.html | IV-3 長い音と短い音 ① | 52–53 | 52–53 | 3 / 157 | I 8 + II 7 |
| moji-iv3-2.html | IV-3 長い音と短い音 ② | 54–55 | 54–55 | 3 / 157 | I 8 + II 6 |
| moji-iv4-1.html | IV-4 同じ音・似ている音が続くもの | 56–57 | 56–57 | 3 / 157 | I 8 + II 8 |
| goi-i-01.html | I 意味がたくさんあるパターン ① | 60–61 | 60–61 | 3 / 157 | 5 |
| goi-i-02.html | I 意味がたくさんあるパターン ② | 62–63 | 62–63 | 3 / 157 | 5 |
| goi-i-03.html | I 意味がたくさんあるパターン ③ | 64–65 | 64–65 | 3 / 157 | 5 |
| goi-i-04.html | I 意味がたくさんあるパターン ④ | 66–67 | 66–67 | 3 / 157 | 5 |
| goi-i-05.html | I 意味がたくさんあるパターン ⑤ | 68–69 | 68–69 | 3 / 157 | 5 |
| goi-i-06.html | I 意味がたくさんあるパターン ⑥ | 70–71 | 70–71 | 3 / 157 | 5 |
| goi-i-07.html | I 意味がたくさんあるパターン ⑦ | 72–73 | 72–73 | 3 / 157 | 5 |
| goi-i-08.html | I 意味がたくさんあるパターン ⑧ | 74–75 | 74–75 | 3 / 157 | 5 |
| goi-i-09.html | I 意味がたくさんあるパターン ⑨ | 76–77 | 76–77 | 3 / 157 | 5 |
| goi-i-10.html | I 意味がたくさんあるパターン ⑩ | 78–79 | 78–79 | 3 / 157 | 5 |
| goi-i-11.html | I 意味がたくさんあるパターン ⑪ | 80–81 | 80–81 | 3 / 157 | 5 |
| goi-i-12.html | I 意味がたくさんあるパターン ⑫ | 82–83 | 82–83 | 3 / 157 | 5 |
| goi-ii-1.html | II 形が似ているパターン ① — **not in scan** | 84–85 | — | 3 / 157 (answers only) | 10 |
| goi-ii-2.html | II 形が似ているパターン ② — **not in scan** | 86–87 | — | 3 / 157 (answers only) | 10 |
| goi-ii-3.html | II 形が似ているパターン ③ — **not in scan** | 88–89 | — | 4 / 158 (answers only) | 10 |
| goi-ii-4.html | II 形が似ているパターン ④ | 90–91 | 84–85 | 4 / 158 | I 7 + II 3 |
| goi-ii-5.html | II 形が似ているパターン ⑤ | 92–93 | 86–87 | 4 / 158 | I 7 + II 3 |
| goi-iii-1.html | III 意味が似ているパターン ① | 94–95 | 88–89 | 4 / 158 | I 7 + II 3 |
| goi-iii-2.html | III 意味が似ているパターン ② | 96–97 | 90–91 | 4 / 158 | I 7 + II 3 |
| goi-iii-3.html | III 意味が似ているパターン ③ | 98–99 | 92–93 | 4 / 158 | I 7 + II 3 |
| goi-iv-1.html | IV 決まり言葉のパターン ① | 100–101 | 94–95 | 4 / 158 | 11 |
| goi-iv-2.html | IV 決まり言葉のパターン ② | 102–103 | 96–97 | 4 / 158 | 11 |
| goi-iv-3.html | IV 決まり言葉のパターン ③ | 104–105 | 98–99 | 4 / 158 | I 5 + II 3 |
| goi-v-1.html | V 二つの部分からなるパターン | 106–107 | 100–101 | 4 / 158 | 11 |
| goi-vi-1.html | VI 「たとえ」のパターン | 108–109 | 102–103 | 4 / 158 | I 5 + II 3 |
| matome-1.html | 第1回 まとめ問題 | 112–119 | 106–113 | 5 / 159 | 65 (問題I–VII) |
| matome-2.html | 第2回 まとめ問題 | 120–127 | 114–121 | 6 / 160 | 65 |
| matome-3.html | 第3回 まとめ問題 | 128–135 | 122–129 | 7 / 161 | 65 |
| mogi-1.html | 第1回 模擬試験 | 138–142 | 132–136 | 8 / 162 | 25 (問題1–4) |
| mogi-2.html | 第2回 模擬試験 | 143–147 | 137–141 | 8 / 162 | 25 |
| mogi-3.html | 第3回 模擬試験 | 148–152 | 142–146 | 8 / 162 | 25 |
| mogi-4.html | 第4回 模擬試験 | 153–157 | 147–151 | 8 / 162 | 25 |

Note: the TOC prints the 第2章 numbers one line out of step with their labels. The page numbers above come from the section header bars on the pages themselves (II p.84, III p.94, IV p.100, V p.106, VI p.108). Item counts come from the 別冊 key; check them against the page when you build.

## 5. What each pattern's pages look like → page sections

Every unit page uses the master vocab layout: `bp-header` (Source with printed + PDF pp, Pattern, Answer key, Notes) → §1 → §2 → §3 → `bp-day-nav`. Breadcrumb: Home / JLPT N1 / Vocabulary (`../../vocabulary.html`) / パターンで学ぶ N1 文字・語彙 (`index.html`) / unit.

**§1 Points**
- First spread of a pattern: the 例題 box becomes a worked example (`bp-point`), with each 例題 as a mini-quiz giving the book's answer. Give the ヒント and 解き方 as EN/HI/GU paraphrases (labelled "summary, not the book's text"). Later spreads of the same pattern repeat the ヒント in one line and link back to the first spread.
- The list page becomes a `vd-wordlist` table in the book's order. Columns: Japanese (word + kana reading + romaji) / English / Hindi / Gujarati / Book's example (the book's phrase + romaji + EN gloss).
  - 第1章 I-1, II-1 (same reading): group the rows by reading. Put a reading header row (e.g. いし <span class="romaji">ishi</span>) before each group, because the same-reading contrast is what the drill tests.
  - I-2 (several 訓読み), III-1 (one-kanji words), III-2 (special readings), IV (sound changes): one row per word. Add a Note column for the sound rule (e.g. 発＋行 → はっこう).
  - II-1 / II-2 (look-alike kanji): one row per kanji/word. Note what part the look-alike shares (e.g. 衰 vs 哀).
  - 第2章 I (多義語): one row per **sense**, with the headword repeated. The book lists 3–6 example phrases per word and each one is a different sense.
  - 第2章 II–VI: one row per word or expression. For IV (collocations) put the whole fixed phrase in the Japanese cell (やきもちを焼く). For VI (たとえ) give the literal and the figurative meaning.
- 第3章 units have no list page. §1 becomes a short guide to the test's 問題 types and links to the patterns they draw on.

**§2 Every exercise** — every item of 問題I / 問題II (and III–VII in まとめ). Use the `bp-quiz` format: the sentence with the target underlined in `<u>` (or the blank shown as （　）), romaji, the full/correct sentence, EN/HI/GU, a 4-row `bp-options` table with the correct row marked `class="correct"`, and `bp-why` starting "**Answer N** (book key, 別冊 p.X)".
- 漢字 questions (choose the kanji, or the word with the same reading): give each option's reading so learners see why the distractors fail. Some distractors are not real words (e.g. 懐顧, 開掃) — say so.
- 用法 / 多義 questions (第2章 I, まとめ VI–VII): the four options are full sentences. Translate each one and say which sense it uses.
- The 問題文 instruction line is given once per 問題 block in a `bp-notes` paragraph (JP + romaji + EN/HI/GU).

**§3 Confusion pairs** — a `bp-confusion` table of the same-reading or look-alike sets from the unit's list (usually the very sets the drill tests), plus a `bp-callout` for each exam trap (fake-word distractors, kanji that also have another reading, and so on).

**第3章 (まとめ・模擬)** — no long passages are involved (the tests are sentence-level only), so every item is reproduced in full. まとめ: 問題I 読み, II 同じ漢字, III 漢字選択, IV 漢字書き, V 文脈規定, VI 多義, VII 用法 (check the headings on the page). 模擬: 問題1 漢字読み, 問題2 文脈規定, 問題3 言い換え類義, 問題4 用法, in the real JLPT N1 format. Quote the 別冊's 解説 lines paraphrased where it gives them.

## 6. Content rules (site-wide)

- EN + Hindi + Gujarati for every meaning, example and question sentence. Romaji (`<span class="romaji">`) under every Japanese line, option and word.
- Anything not in the book (extra notes, readings of distractors, the "Why" reasoning) is marked "(added, not in book)" when it goes beyond the book's own 解き方/解説.
- No passages or audio are involved in this book. If any longer text ever turns up, give a 2–3 sentence summary in your own words, never the text.
- Never invent questions. The p.84–89 gap stays marked as missing.

## 7. Hub

`n1/vocabulary/pattern-de-manabu/index.html`: one `.week-block` per pattern (第1章 I–IV, 第2章 I–VI, 第3章 まとめ / 模擬). Built chips are `<a class="day-chip ready" href="…">`; unbuilt ones are `<span class="day-chip soon" data-href="…">`. The note keeps the exact text `In progress — N of 57 units built`. The three "not in scan" units count toward the 57 but can never be built from this scan.
