# PROCESSING GUIDE — ゼッタイ合格！日本語能力試験 完全模試 N1 (Jリサーチ出版)

Site hub: `n1/mock-tests/kanzen-moshi/index.html` · Reference unit: `n1/mock-tests/kanzen-moshi/r1-gengo.html`

## 1. The source files

| File | Pages | What it is |
|---|---|---|
| `JLPT_Kanzen_Moshi_N1-Main.pdf` | 119 | Main book: はじめに, 使い方, N1 overview, 問題パターン (p.7–12), **解答・解説** for 第1–3回 (正答一覧 + explanations + full 聴解 scripts), 採点表 (p.92–93), 付録「試験に出る重要語句・文型リスト」(p.94–118), colophon (p.119) |
| `JLPT_Kanzen_Moshi_N1-Tests.pdf` | 129 | 別冊 test booklet: the three tests' question papers + 解答用紙 (answer sheets, PDF 124–129) |
| `JLPT_Kanzen_Moshi_N1-AudioCD1/2/3/` | 3 × 48 tracks | `Track01.mp3`…`Track48.mp3` per CD. **Never publish.** |

Both PDFs are image-only scans (no text layer). Render with PyMuPDF (`import pymupdf`, 120–160 dpi; the 解説 pages are 2-column with small furigana — render each column separately at ~160 dpi).

## 2. Page offsets (verified on page stamps)

**Main PDF: printed = PDF everywhere** (checked PDF 3, 13, 14, 19, 26, 36, 39, 65).

**Tests PDF: the offset drifts**, because the blank verso before each 聴解 cover and before 第2回/第3回 language papers was not scanned:

| Tests PDF range | printed = | checked on |
|---|---|---|
| 1–29 | PDF + 0 | PDF 2, 11, 29 |
| 30–70 | PDF + 1 (printed p.30 blank, not scanned) | PDF 31 = p.32, 42 = p.43 (第2回 cover, TOC 43 ✓), 70 = p.71 |
| 71–111 | PDF + 2 (p.72 not scanned) | PDF 72 = p.74, 83 = p.85 (第3回 cover, TOC 85 ✓), 111 = p.113 |
| 112–129 | PDF + 3 (p.114 not scanned) | PDF 113 = p.116, 123 = p.126, 124 = 解答用紙 (TOC 127 ✓) |

No question pages are missing — only blank versos.

## 3. Unit definition

One unit = **one paper of one 回** → 3 回 × 3 papers = **9 units**. Paper boundaries:
- 言語知識（文字・語彙・文法）= 問題1–7, Q1–45
- 読解 = 問題8–13, Q46–71 (8 内容理解短文 46–49, 9 中文 50–58, 10 長文 59–62, 11 統合理解 63–65, 12 主張理解 66–69, 13 情報検索 70–71)
- 聴解 = 問題1 (例+6), 問題2 (例+7), 問題3 (例+6), 問題4 (例+13), 問題5 (1, 2, 3 質問1・2)

This is the older N1 format (45 language items). The book's 正答一覧 page covers all three papers of a 回.

## 4. Unit table

Filename | title | Tests printed pp | Tests PDF pp | Main 解説 PDF pp (= printed) | key PDF | audio
---|---|---|---|---|---|---
r1-gengo.html | 第1回 言語知識（文字・語彙・文法） | 2–11 | 2–11 (cover PDF 1) | 14–19 | M13 | —
r1-dokkai.html | 第1回 読解 | 12–29 | 12–29 | 20–25 | M13 | —
r1-choukai.html | 第1回 聴解 | 31–42 | 30–41 (cover PDF 30) | 26–38 | M13 | CD1 · Tracks 01–48
r2-gengo.html | 第2回 言語知識（文字・語彙・文法） | 44–53 | 43–52 (cover PDF 42) | 40–45 | M39 | —
r2-dokkai.html | 第2回 読解 | 54–71 | 53–70 | 46–51 | M39 | —
r2-choukai.html | 第2回 聴解 | 73–84 | 71–82 (cover PDF 71) | 52–64 | M39 | CD2 · Tracks 01–48
r3-gengo.html | 第3回 言語知識（文字・語彙・文法） | 86–95 | 84–93 (cover PDF 83) | 66–71 | M65 | —
r3-dokkai.html | 第3回 読解 | 96–113 | 94–111 | 72–77 | M65 | —
r3-choukai.html | 第3回 聴解 | 115–126 | 112–123 (cover PDF 112) | 78–91 | M65 | CD3 · Tracks 01–48

Notes: 問題7 (passage cloze) runs over two test pages (e.g. PDF 10–11) and belongs to 言語知識. 読解 問題8 starts on the page right after it. The 解説 for 言語知識 ends partway down the last page (e.g. M19 right column blank — not a scan gap).

Not units (optional extras for a later builder): 問題パターンと解答のポイント (Main p.7–12), 採点表 (p.92–93), 付録 重要語句・文型リスト (p.94–118: 文字 読み方 kanji, 語彙, 文法 70 patterns, 読解/聴解 keyword lists).

## 5. Answer key status

**Official and complete.** Each 回 opens with a 正答一覧 (M13, M39, M65) covering all three papers, followed by per-question 解説: 正答 number, the word's definition (Japanese, with EN/中/韓 glosses for some words), kanji readings with examples, 他の選択肢 notes (often naming the word that would be correct in a wrong 用法 sentence), full orders for 問題6 ★, a reasoning note for 問題7 and 読解 questions, and the **full 聴解 script** with 言葉と表現.

第1回 言語知識 key (verified against every question): 1-2 2-2 3-3 4-3 5-1 6-4 · 7-2 8-3 9-1 10-4 11-3 12-2 13-1 · 14-2 15-2 16-2 17-1 18-1 19-3 · 20-1 21-2 22-3 23-1 24-4 25-3 · 26-4 27-1 28-2 29-2 30-2 31-2 32-4 33-3 34-1 35-3 · 36-1 37-3 38-4 39-3 40-1 · 41-3 42-1 43-3 44-4 45-3.
第1回 読解 key: 46-4 47-2 48-2 49-3 · 50-4 51-2 52-1 53-2 54-1 55-4 56-3 57-2 58-4 · 59-4 60-1 61-3 62-4 · 63-2 64-3 65-1 · 66-3 67-1 68-4 69-2 · 70-2 71-4.
第1回 聴解 key: 問題1 例2, 1-3 2-4 3-4 4-2 5-3 6-2 · 問題2 例3, 1-3 2-2 3-4 4-2 5-3 6-2 7-4 · 問題3 例3, 1-1 2-4 3-4 4-2 5-2 6-2 · 問題4 例3, 1-3 2-2 3-2 4-1 5-2 6-1 7-3 8-1 9-2 10-1 11-2 12-2 13-3 · 問題5 1-1 2-4 3(1)-2 3(2)-3.
(Re-read M39/M65 for 第2回/第3回.)

**Known print quirk:** 第1回 Q28 options are numbered 1, 2, 2, 4; the key "2" = the first "2" (んじゃないの), confirmed by the 解説 heading 〜んじゃない(の)？. Watch for similar numbering slips in other 回.

## 6. Audio — track map (by number only; never publish or embed)

Each 聴解 script in the 解説 carries a round badge "NN / CD1" at the top right of every item. 第1回 (CD1) as read from the badges:

| 問題 | Items → Track |
|---|---|
| (opening) | 01–02 — no badge (exam announcement + 問題1 instructions, presumed) |
| 問題1 | 例 03 · 1番 04 · 2番 05 · 3番 06 · 4番 07 · 5番 08 · 6番 09 |
| 問題2 | (10 no badge — instructions) · 例 11 · 1番 12 … 7番 18 |
| 問題3 | (19–20 no badge) · 例 21 · 1番 22 … 6番 27 |
| 問題4 | (28 no badge) · 例 29 · 1番 30 … 13番 42 |
| 問題5 | (43 no badge) · 1番 44 · 2番 45 · (46 no badge) · 3番 47 · (48 no badge) |

CD2 (第2回) and CD3 (第3回) use the same numbering (spot-checked: 第2回/第3回 問題1 例 = 03, 1番 = 04; 第2回 問題5 2番 = 45, 3番 = 47). The builder of each 聴解 unit must still read every badge on its pages and use those numbers. Un-badged tracks are presumed instructions; say "presumed" unless confirmed. On pages, show tracks with the listening badge `<span class="ld-track">CD1 · Track 04</span>` (as in `n1/multi-skill/drill-and-drill/l-kadai-01.html`). **No `<audio>` elements, no file paths.**

## 7. How each paper maps to the page sections

All pages: `bp-header` (Source with printed+PDF pages and offsets, question types, answer key line, Notes) → §1 → §2 → §3 → `bp-day-nav` (prev / next unit). EN + HI + GU for every meaning, question sentence and option; `<span class="romaji">` under every Japanese line; mark our own additions "(added, not in book)".

### 言語知識 (template: r1-gengo.html)
- **§1 Points**: kanji table (`kd-kanji-table`) from the 問題1 解説 readings and examples; vocabulary table (`bp-table`) for 問題2–4 words with the book's definitions paraphrased + its example sentence; grammar table for 問題5–7 patterns (meaning, connection).
- **§2 Every question** (`bp-quiz` per item, `bp-options` with `tr.correct`): 問題1–3 = sentence + full sentence/underlined word + EN/HI/GU + options + Why (cite the 解説). 問題4 = each option sentence with EN, and for wrong options the book's "fix" word + HI/GU. 問題6 = tiles line + `bp-order-chain` + `bp-assembled` (orders are the book's own). 問題7 = a passage block (Passage summary in EN/HI/GU + the book's 注 glosses), then per blank quote only the sentence around the blank.
- Headings carry the book's suggested time (hourglass), e.g. 問題1 1分 (1問10秒), 問題2 2分, 問題3 2分, 問題4 3分, 問題5 5分, 問題6 4分, 問題7 6分.
- **§3 Confusion pairs** (`bp-confusion`) from the look-alike option sets + 2–3 `bp-callout` exam traps.

### 読解 (template to follow: n1/multi-skill/drill-and-drill/r-choubun-01.html)
- §1: question-type strategy (`rd-strategy`) for 問題8–13 (the book's 問題パターン p.9–11 can be summarised) + 言葉と表現 vocabulary from the 解説.
- §2: one block per passage: `rd-passage-label` (source line if printed), **Passage summary (not the book's text)** in EN/HI/GU (2–3 sentences), then each question: stem + options quoted (EN/HI/GU), the key sentence(s) the 解説 points to quoted (short), Why.
- §3: distractor patterns / confusing words.

### 聴解 (template to follow: n1/multi-skill/drill-and-drill/l-kadai-01.html)
- §1: strategy per 問題 type (課題理解, ポイント理解, 概要理解, 即時応答, 統合理解) + 言葉と表現 from the 解説.
- §2: per item: `ld-track` badge (CD · Track), **Script summary (not the book's text)** in EN/HI/GU, the question, options (printed in the test booklet for 問題1–2 and 5-3; for 問題3–5 options are only in the script), quote only the key line(s), answer + Why. 問題4 items are short exchanges: summarise the prompt, quote it only if it is one short line.
- §3: confusing expressions / traps.

## 8. Passage, script and audio rules (hard)

- **Never reproduce reading passages or listening scripts** in pages, scratch files, notes or messages. Write a 2–3 sentence summary in your own words (EN/HI/GU) and quote only the sentence(s) each question needs. If any output is blocked by the content filter, drop that part and report it.
- Question stems, options and the book's short 注 glosses may be quoted.
- Audio: refer by CD + track number only. Never link, embed or copy the mp3 files.
- Never invent questions or answers; the key is official — cite 正答一覧 page and 解説 page.

## 9. File naming & hub

- Files: `r{回}-{gengo|dokkai|choukai}.html` in `n1/mock-tests/kanzen-moshi/`.
- Hub groups by 回 (`.week-block` per 回, three chips each). Built chip: `<a class="day-chip ready" href="…">`; unbuilt: `<span class="day-chip soon" data-href="…">`. Update the note text `In progress — N of 9 units built`.
- Prev/next order: r1-gengo → r1-dokkai → r1-choukai → r2-gengo → … → r3-choukai.
