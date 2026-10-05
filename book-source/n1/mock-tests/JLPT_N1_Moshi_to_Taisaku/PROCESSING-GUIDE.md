# 日本語能力試験 模試と対策 N1 — processing guide

Standing instructions for turning `JLPT_N1_Moshi_to_Taisaku.pdf` (Nihongo Nouryoku Shiken Moshi to Taisaku N1, アスク出版) into the site's unit pages under `n1/mock-tests/moshi-to-taisaku/`. Pick a unit filename from the table in §4 and follow this guide.

## 1. The PDF

- 214 PDF pages: main book (PDF 1–153) + 別冊 解答・解説・対策編 bound at the end (PDF 154–214).
- **The text layer is useless.** PDF 3–91 carry a garbage OCR layer (Latin mojibake); PDF 92–214 have no text at all. Always render pages and read them visually.
- **PDF 3–91 are stored with `/Rotate 180`.** `page.get_pixmap()` honours the rotation and renders them the right way up. Do *not* use `show_pdf_page()` to build contact sheets — it drops the rotation and gives upside-down/mirrored pages.
- Render with PyMuPDF (`import pymupdf`): 120–130 dpi for question pages; **170 dpi, split into left/right halves** for the 別冊 explanation pages (two dense columns in four languages).
- Scratch renders go in the session scratch folder, never in the repo.

## 2. Offsets (verified on rendered images)

| Part | PDF range | Printed = | Verified on |
|---|---|---|---|
| Main book | 3–152 | **PDF − 1** | PDF 7 = p.6 (もくじ), PDF 21 = p.20, PDF 22 = p.21, PDF 30 = p.29, PDF 94 = p.93, PDF 97 = p.96, PDF 108 = p.107, PDF 145 = p.144 |
| 別冊 | 156–214 | **PDF − 155** | PDF 156 = p.1 (別冊もくじ), PDF 157 = p.2, PDF 161 = p.6, PDF 168 = p.13, PDF 213 = p.58 |

Other pages: PDF 1–2 covers; 153 colophon; 154 back cover; 155 別冊 cover. No missing or duplicated pages were found.

### Main-book map (printed pages)

| Printed | PDF | Content |
|---|---|---|
| 3 | 4 | はじめに |
| 4–6 | 5–7 | この本の使い方 (p.6 = もくじ) |
| 7 | 8 | 新しい「日本語能力試験」N1について |
| 8–9 | 9–10 | N1 問題の構成 (table of all question types) |
| 10–17 | 11–18 | 問題の説明 (文字・語彙 10–11, 文法 12–13, 読解 14–15, 聴解 16–17); p.18 blank |
| 19 | 20 | 第1回 言語知識・読解 title page (110分) |
| 20–29 | 21–30 | 第1回 問題1–7 (言語知識) |
| 30–49 | 31–50 | 第1回 問題8–13 (読解); p.50 blank |
| 51 | 52 | 第1回 聴解 title page (60分, CD1 01→40) |
| 52–61 | 53–62 | 第1回 聴解 問題1–5; p.62 blank |
| 63 | 64 | 第2回 言語知識・読解 title page |
| 64–73 | 65–74 | 第2回 問題1–7 |
| 74–93 | 75–94 | 第2回 問題8–13; p.94 blank |
| 95 | 96 | 第2回 聴解 title page (CD2 01→41) |
| 96–106 | 97–107 | 第2回 聴解 問題1–5 |
| 107 | 108 | 聴解スクリプト title page |
| 108–124 | 109–125 | 第1回 聴解スクリプト |
| 125–143 | 126–144 | 第2回 聴解スクリプト |
| 144–151 | 145–152 | マークシート (第1回, 第2回, 予備1, 予備2) — skip |

### 別冊 map (printed 別冊 pages)

| 別冊 p. | PDF | Content |
|---|---|---|
| 2 | 157 | 第1回 解答 (all 71 + 聴解) |
| 3 | 158 | 第2回 解答 |
| 4–5 | 159–160 | 模試の採点表と分析 (配点, convert to 60, 80 % = 48 pass line) |
| 6–13 | 161–168 | 第1回 解説 言語知識 (読解 header at foot of p.13) |
| 13–18 | 168–173 | 第1回 解説 読解 (問題8–13) |
| 18–23 | 173–178 | 第1回 解説 聴解 |
| 24–31 | 179–186 | 第2回 解説 言語知識 (読解 header on p.31) |
| 31–36 | 186–191 | 第2回 解説 読解 |
| 36–41 | 191–196 | 第2回 解説 聴解 |
| 42–43 | 197–198 | 「言語知識」の対策 (日本語) — 文字・語彙／文法／読解 |
| 44–45 | 199–200 | 「聴解」の対策 (日本語) |
| 46–48 | 201–203 | Strategy for Language Knowledge (English) |
| 48–51 | 203–206 | Strategy for Listening (English) |
| 52–55 | 207–210 | 中国語版 対策 (skip — same content) |
| 56–59 | 211–214 | 韓国語版 対策 (skip — same content) |

## 3. Answer key status

**Official and complete.** 別冊 p.2–3 give every answer (言語知識・読解 1–71; 聴解 問題1 1–6, 問題2 1–7, 問題3 1–6, 問題4 1–14, 問題5 1/2(1)/2(2) in 第1回 and 1/2(1)/2(2)/3(1)/3(2) in 第2回). 別冊 p.6–41 explain **every** item in Japanese with English, Chinese and Korean versions. For 問題6 (★) the 解説 prints the whole correct sentence, so full orders are the book's (no need to reason them). Paraphrase the 解説 as "Book's 解説"; mark anything you add "(added, not in book)".

Known 別冊 slips (第1回): item 26 — the Japanese line calls べく "2" (key and English say 1); item 39 — the English line prints 変えない for 買えない. Note such slips in the page's Notes.

Scoring (別冊 p.4): 言語知識 56 pts (問題1 1×6, 2 1×7, 3 1×6, 4 2×6, 5 1×10, 6 1×5, 7 2×5) → ÷56×60; 読解 and 聴解 have their own rows (p.5). The book's benchmark: ≤ 48/60 (80 %) → study the 解説 and 対策.

## 4. Units (9)

A unit = one paper of one mock test, or one strategy section. Hub order: 第1回 → 第2回 → 対策.

| Filename | Title | Printed pp | PDF pp | Key / 解説 PDF pp | Audio |
|---|---|---|---|---|---|
| mock-1-gengo.html ✅ | 第1回 言語知識（文字・語彙・文法） 問題1–7, Q1–45 | 19–29 | 20–30 | key 157; 解説 161–168 | — |
| mock-1-dokkai.html | 第1回 読解 問題8–13, Q46–71 | 30–49 | 31–50 | key 157; 解説 168–173 | — |
| mock-1-choukai.html | 第1回 聴解 問題1–5 | 51–61 (+ script 108–124) | 52–62 (+ 109–125) | key 157; 解説 173–178 | CD1 · Tracks 01–40 |
| mock-2-gengo.html | 第2回 言語知識（文字・語彙・文法） Q1–45 | 63–73 | 64–74 | key 158; 解説 179–186 | — |
| mock-2-dokkai.html | 第2回 読解 Q46–71 | 74–93 | 75–94 | key 158; 解説 186–191 | — |
| mock-2-choukai.html | 第2回 聴解 問題1–5 | 95–106 (+ script 125–143) | 96–107 (+ 126–144) | key 158; 解説 191–196 | CD2 · Tracks 01–41 |
| taisaku-mondai-setsumei.html | N1 問題の構成・問題の説明 (+ この本の使い方 study plan) | 4–17 | 5–18 | — | — |
| taisaku-gengo-chishiki.html | 「言語知識」の対策 (文字・語彙／文法／読解) | 別冊 42–43 (EN 46–48) | 197–198 (EN 201–203) | — | — |
| taisaku-choukai.html | 「聴解」の対策 | 別冊 44–45 (EN 48–51) | 199–200 (EN 203–206) | — | — |

### Question layout per mock (same in both 回)

- 言語知識: 問題1 漢字読み 1–6 · 問題2 文脈規定 7–13 · 問題3 言い換え類義 14–19 · 問題4 用法 20–25 · 問題5 文法形式の判断 26–35 · 問題6 文の組み立て★ 36–40 · 問題7 文章の文法 41–45 (one passage).
- 読解 (第1回, checked): 問題8 内容理解(短文) 46–49 ((1)–(4)) · 問題9 内容理解(中文) 50–58 ((1)–(3), 3 Qs each) · 問題10 内容理解(長文) 59–62 · 問題11 統合理解 A/B 63–65 · 問題12 主張理解(長文) 66–69 · 問題13 情報検索 70–71. 第2回 has the same 71-item total; confirm the split on its pages.
- Each 問題 heading has a clock icon with a target time per item (e.g. 1問 10秒×6) — put these in the §1 table.

### Audio track map (from the CD badges on the question pages and scripts)

Both CDs follow the same pattern; the first track of each 問題 is the instructions + example.

| 問題 | 第1回 (CD1) | 第2回 (CD2) |
|---|---|---|
| 問題1 課題理解 | 01 instructions, 1番–6番 = 02–07 | same: 01, 02–07 |
| 問題2 ポイント理解 | 08 instructions, 1番–7番 = 09–15 | 08, 09–15 |
| 問題3 概要理解 | 16 instructions, 1番–6番 = 17–22 | 16, 17–22 |
| 問題4 即時応答 | 23 instructions, 1番–14番 = 24–37 | 23, 24–37 |
| 問題5 統合理解 | 38 instructions, 1番 = 39, 2番 = 40 | 38, 1番 = 39, 2番 = 40, 3番 = 41 |

Check each badge on the rendered page before using it (the badges are small; zoom in).

## 5. Page sections

Templates: **`n1/mock-tests/moshi-to-taisaku/mock-1-gengo.html`** (this book's reference implementation — follow it for mock-2-gengo exactly), plus `n1/grammar/shin-kanzen-master/mock-test-1.html` (mock layout), `n1/multi-skill/pattern-betsu-tettei-drill/moji-kanji-yomi-1.html` and `moji-youhou-na-keiyoushi.html` (vocabulary items), `n1/multi-skill/drill-and-drill/r-choubun-01.html` (reading), `n1/multi-skill/drill-and-drill/l-kadai-01.html` (listening). Shared CSS only (bp-*, kd-*, vd-*, rd-*, ld-*); no new CSS/JS. Keep the head/header/footer and the `../../../` depth of the existing pages.

- **Header `.bp-header`**: source (printed + PDF pp, offset check), question types (`.bp-points`), answer key (official, 別冊 page), notes (passage/audio rules, 別冊 slips).
- **§1 Points**
  - 言語知識: paper table (問題 · type · items · clock target · points) + words table (問題1–4 correct answers) + grammar table (問題5–6 patterns, meaning, connection).
  - 読解: one row per passage (問題 · topic in own words · source credit as printed · items · clock target) + key vocabulary from the passages/注.
  - 聴解: track table (問題 · items · tracks) + the useful expressions the 解説 picks out (e.g. 即時応答 set phrases).
  - 対策 units: the book's advice as a summary in our own words, EN/HI/GU, organised by question type, with the book's own examples. The English 別冊 version (p.46–51) can be used to check understanding but must not be copied out — paraphrase.
- **§2 Every question** — `.bp-quiz` cards: stem + romaji, full answer sentence, EN/HI/GU, `.bp-options` table with the correct row `class="correct"`, `.bp-why` = "Book's 解説" paraphrase + "(added, not in book)" notes for anything ours. 用法: each option sentence in the table, wrong ones explained (✗ + the word it should have been, from the 解説). ★ items: tiles line, `.bp-order-chain`, `.bp-assembled`. Listening: `<span class="ld-track">CD1 · Track 09</span>` on every card.
- **§3 Confusion pairs** — `.bp-confusion` from that paper's distractors + 2–3 `.bp-callout` exam traps.
- **`.bp-day-nav`** prev/next in hub order (first unit's prev = index.html).

## 6. Passage / transcript / audio rules (hard)

- **Never reproduce reading passages or listening scripts verbatim** — not in pages, scratch files, notes or messages (the content filter blocks it). For each passage/script give a 2–3 sentence **"Passage summary (not the book's text)"** / **"Script summary (not the book's text)"** in EN/HI/GU in your own words, then quote **only the sentence(s) a question needs** (the underlined part, or the line the 解説 points to). 問題7 文章の文法: summary + only the sentence around each blank. 問題13 情報検索: describe the notice/table in your own words; quote only the cells a question turns on. If an output is blocked, leave that part out and report it — do not work around it.
- **Audio is copyrighted and never published.** No `<audio>` elements, no links to the .mp3 files. Refer to tracks only by CD + number with the `ld-track` badge. The .mp3 files stay in `book-source/…/JLPT_N1_Moshi_to_Taisaku-AudioCD1|2/`.
- 聴解 問題3, 問題4 and 問題5 1番 have no printed choices (spoken only) — take the options from the script pages, quoted as option text only; summarise the talk itself. 問題5 2番 (and 3番 in 第2回) print their choices.
- Never invent questions or answers. If something is illegible, say so.
- Language: EN + Hindi + Gujarati for every meaning/example/question sentence; `<span class="romaji">` under every Japanese line; "(added, not in book)" for anything you add.

## 7. Hub (`n1/mock-tests/moshi-to-taisaku/index.html`)

- `.week-list` > `.week-block` (第1回 / 第2回 / 対策) > `.week-head` + `.day-chips`.
- Built: `<a class="day-chip ready" href="FILE.html">LABEL</a>`; not built: `<span class="day-chip soon" data-href="FILE.html">LABEL</span>`.
- `.sample-note` must keep the exact text `In progress — N of 9 units built`; bump N when a unit is built (switch to "Complete — 9 of 9 units built" at the end).

## 8. Checks before finishing a unit

Balanced tags (Python `html.parser`), every relative link resolves (the next unit may not exist yet), file ends with `</html>`, LF line endings, no passage/script text beyond the per-question quotes, no audio links.
