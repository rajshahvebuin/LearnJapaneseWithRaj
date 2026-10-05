# 日本語能力試験 予想問題集 N1 — processing guide

Standing instructions for turning `JLPT_Yosou_Mondaishuu_N1.pdf` (Nihongo Nouryoku Shiken Yosou Mondaishuu N1, 改訂版, 執筆 青山豊 他 / 〇〇日本語学校編) into the site's unit pages under `n1/mock-tests/yosou-mondaishuu/`. Pick a unit filename from the table in §8 and follow this process.

## 1. What this book is (read first)

- **It is NOT a set of numbered full mock exams (第1回／第2回…).** Despite the 予想問題集 title, the book is a *question bank ordered by JLPT question type*: 第1部 言語知識（文字・語彙・文法）・読解 = 問題1 漢字読み → 問題13 情報検索, then 第2部 聴解 = 問題1 課題理解 → 問題5 統合理解. Each 問題 holds far more items than the real exam (e.g. 25 漢字読み items vs 6 on the test). There is no 回 split, no time limits and no score tables beyond the exam-format table on p.3.
- So a unit = one 問題 type (or half of one, where the type is long). Units follow book order.
- 本書の使い方 (p.3–4, PDF 3–4): exam format table (言語知識・読解 110分 / 聴解 60分, item counts per type, 得点区分 0–60 ×3 = 180) and book notes: CD = 第2部 聴解 only (Disc1 = 聴解 問題1–2, Disc2 = 聴解 問題3–5); spoken instructions are left off the CD; reading passages may carry added furigana/注 and be abridged; 別冊 = 解答・解説 + 聴解問題スクリプト. This content lives on the **hub page** (no separate unit).
- The only "strategy" text in the book is the short intro paragraph that opens each 問題 in the 別冊 (Japanese + English + Chinese + Korean versions of the same text). Summarise it (own words, EN/HI/GU) in §1 of the first unit of that 問題 type. There are no separate strategy pages to turn into units.

## 2. The PDF

- 207 PDF pages. **Has a text layer, but it is poor OCR**: the front matter and headers are mojibake, furigana are scrambled into the line, boxed item numbers come out as □/回/日/国. Use it only to locate pages and skim answer grids. **Always render pages (PyMuPDF `import pymupdf`, 110–150 dpi) and read them visually** before writing anything. Python on this machine needs Windows paths (`C:/Users/...`), not `/c/...`.
- Every page carries a `facebook.com/duytrieuftu` scanner watermark — ignore it.
- PDF 1 blank, 2 まえがき, 3–4 本書の使い方, 5 目次, 6 第1部 title, 7 blank, 8–90 第1部, 91 blank (bleed-through), 92 第2部 title, 93 blank, 94–122 第2部 聴解, 123 執筆者紹介, 124 credit, **125–207 別冊** (bound in at the end).

## 3. Offsets (verified on rendered pages)

| PDF range | Printed page = | Verified on |
|---|---|---|
| 8–122 (main book) | PDF + 1 | PDF 8 = p.9 (問題1 漢字読み, page stamp "9"), PDF 9 = p.10, PDF 10 = p.11, PDF 94 = p.95 (聴解 問題1), PDF 99 = p.100, PDF 104 = p.105, PDF 109 = p.110, PDF 115 = p.116, PDF 122 = p.123 |
| 125–147 (別冊) | 別冊 p. = PDF − 123 | PDF 125 = 別冊 p.2, PDF 127 = p.4, PDF 130 = p.7, PDF 131 = p.8, PDF 132 = p.9, PDF 134 = p.11, PDF 137 = p.14, PDF 145 = p.22, PDF 147 = p.24 |
| — | **別冊 pp.25–30 missing from the scan** | PDF 147 = p.24 is followed directly by PDF 148 = p.31 |
| 148–207 (別冊) | 別冊 p. = PDF − 117 | PDF 148 = p.31, PDF 150 = p.33, PDF 152 = p.35, PDF 167 = p.50, PDF 177 = p.60, PDF 199 = p.82, PDF 207 = p.90 |

Inside the 別冊, explanations are headed with the main-book page they belong to, e.g. "(P.9)", "(P.30‐31)" — use these to cross-check.

## 4. Answer key status

The 別冊 解答・解説 gives a 【解答】 grid **and** a 【解説】 for every item (Japanese, with an English + Chinese + Korean version of the explanation for 聴解 items and for the section intros). Treat it as the official key. Paraphrase the 解説 — never copy it at length.

**Gap: 別冊 pp.25–30 are not in the scan.** Effects:

| Lost | Effect |
|---|---|
| 解説 for 第1部 問題10 内容理解（長文）, 問題11 統合理解, 問題12 主張理解, 問題13 情報検索 (only the 問題10 intro paragraph survives, bottom of PDF 147) | No official answers for 10-1…13-3. Work every answer out at N1 level from the passage and flag each one "not from the official key (別冊 pages missing from the scan)". |
| 第2部 intro + 聴解 問題1 課題理解 intro, 【解答】 grid and the start of 1番's 解説 | 1番's answer number is lost (only the English/Chinese/Korean tail of its 解説 survives at the top of PDF 148). Work 1番 out from the script (scripts survive, PDF 168) and flag it. 2番–14番 answers are in their 解説 headings (PDF 148–150). |
| 聴解 問題1 15番 | **No 解説 at all**: PDF 150 (p.33) ends with 14番 and PDF 151 (p.34) starts 問題2. The 15番 answer was presumably only in the lost grid. Work it out from the script (PDF 176) and flag it. |

Everything else (第1部 問題1–9, 聴解 問題2–5 and all 聴解 scripts PDF 168–207) is present.

## 5. Unit page structure

Templates: `n1/mock-tests/yosou-mondaishuu/moji-kanji-yomi.html` (**reference implementation for this book**), plus the site references `n1/multi-skill/pattern-betsu-tettei-drill/moji-kanji-yomi-1.html` (文字・語彙 items), `n1/grammar/shin-kanzen-master/mock-test-1.html` (文法 items, ★ ordering, passage cloze), `n1/multi-skill/drill-and-drill/r-choubun-01.html` (reading: passage summary + key sentences), `n1/multi-skill/drill-and-drill/l-kadai-01.html` (listening: track badge + script summary). Shared CSS only (bp-*, kd-*, vd-*, rd-*, ld-track …). No new CSS/JS. Keep the head/header/footer and `../../../` depth of the hub.

- **Header `.bp-header`**: breadcrumb Home / JLPT N1 / Mock tests (`../../mock-tests.html`) / 予想問題集 N1 (`index.html`) / unit. Source = printed pp + PDF pp; answer key = 別冊 pp + PDF pp (or "missing from the scan — answers worked out, not from the official key"); audio tracks for 聴解.
- **§1 Points** — by section type:
  - 漢字読み: the 別冊 intro summary + a `.kd-kanji-table` of every tested kanji with the on/kun readings and 例 words the 別冊 gives (add EN/HI/GU).
  - 文脈規定 / 言い換え類義 / 用法: intro summary + a `.bp-table` of the tested words (word, reading, meaning, the 別冊's 言い換え／参考 words) in EN/HI/GU.
  - 文法形式の判断 / 文の組み立て / 文章の文法: intro summary + a pattern table (item → pattern → meaning EN/HI/GU → connection), like mock-test-1 §1.
  - 読解 units: intro summary + strategy box (`.rd-strategy`) + key-word table for the passages (from the passages' own (注) glosses; translations ours).
  - 聴解 units: intro summary + strategy box + key-word table per item.
- **§2 Every exercise** — every item in a `.bp-quiz` card: q-label, the sentence + romaji, translations (EN/HI/GU), `.bp-options` table (Option | Japanese/Reading | English | Hindi | Gujarati) with the correct row `class="correct"`, and `.bp-why` = the 別冊 解説 paraphrased ("別冊 p.N") plus our own notes on the other options, marked "(added, not in book)".
  - 用法: each option is a full sentence — give each one EN/HI/GU and say why the wrong ones misuse the word.
  - 文の組み立て: give the full ordered sentence and the ★ tile; the 別冊 shows the full order.
  - 文章の文法 / 読解: a "Passage summary (not the book's text)" in EN/HI/GU, then only the sentence(s) each question needs (`.rd-passage-label` "Key sentence (quoted)"). Source line (author/book) if printed.
  - 聴解: `<span class="ld-track">CD1 · Track 5</span>` badge, the printed options (if any), "Script summary (not the book's text)" in EN/HI/GU, the one or two key lines quoted from the 別冊 script, answer + why.
- **§3 Confusion pairs** — `.bp-confusion` table from that unit's distractors (look-alike kanji, wrong readings, near-synonyms, similar grammar, listening traps) + 2–3 `.bp-callout` exam traps.
- `.bp-day-nav` prev/next in hub order (first unit: prev = ← the hub).

## 6. Passage / transcript / audio rules (hard)

- **Never reproduce reading passages or listening scripts verbatim** — not in pages, scratch files, notes or messages (the API content filter blocks it). For each passage/script write a 2–3 sentence **"Passage summary (not the book's text)"** / **"Script summary (not the book's text)"** in EN/HI/GU in your own words, then quote only the sentence(s) each question needs. 文章の文法 (問題7): summary + only the sentence around each blank. If any output is blocked by the filter, leave that part out and report it — do not work around it.
- **Audio is copyrighted and never published.** No audio was uploaded with this book, and pages must never contain `<audio>` elements or links to audio files anyway. Refer to tracks by number only with the badge `<span class="ld-track">CD1 · Track 5</span>` (the book prints "Disc 1-5"; write it as CD1 · Track 5).
- Never invent questions or answers. Missing scan pages are marked "missing from the scan". Answers you work out yourself are flagged "not from the official key".
- Language: EN + Hindi + Gujarati for every meaning / example / question sentence; `<span class="romaji">` under every Japanese line; "(added, not in book)" on anything you add.

## 7. Audio track map (from the badges printed beside each 番)

| 聴解 問題 | Items | Tracks |
|---|---|---|
| 問題1 課題理解 | 1番–15番 | CD1 · Tracks 1–15 |
| 問題2 ポイント理解 | 1番–14番 | CD1 · Tracks 16–29 |
| 問題3 概要理解 | 1番–14番 | CD2 · Tracks 1–14 |
| 問題4 即時応答 | 1番–26番 | CD2 · Tracks 15–40 |
| 問題5 統合理解 | 1番–10番 | CD2 · Tracks 41–50 |

Track = item number + fixed offset within each 問題 (no intro tracks on the CD per 本書の使い方). Verified on PDF 94 (1番 = Disc1-1), 99 (13–15番 = Disc1-13–15), 104 (12–14番 = Disc1-27–29), 105 (1番 = Disc2-1), 108 (14番 = Disc2-14), 109 (1番 = Disc2-15), 115 (26番 = Disc2-40), 122 (10番 = Disc2-50).

## 8. Unit table (hub order = book order)

Item counts: 問題1 25 · 問題2 27 · 問題3 25 · 問題4 27 · 問題5 25 · 問題6 25 · 問題7 7 passages × 5 = 35 · 問題8 8 texts × 1 · 問題9 5 passages × 3 = 15 · 問題10–13 3 passages each · 聴解 15 / 14 / 14 / 26 / 10.

| # | File | Title | Items | Printed pp | PDF pp | Key PDF pp (別冊 pp) | Audio |
|---|---|---|---|---|---|---|---|
| 1 | moji-kanji-yomi.html | 問題1 漢字読み | 1–25 | 9–11 | 8–10 | 125–127 (2–4) | — |
| 2 | moji-bunmyaku-kitei.html | 問題2 文脈規定 | 1–27 | 12–14 | 11–13 | 127–129 (4–6) | — |
| 3 | moji-iikae-ruigi.html | 問題3 言い換え類義 | 1–25 | 15–17 | 14–16 | 129–131 (6–8) | — |
| 4 | moji-youhou-1.html | 問題4 用法 ① | 1–13 | 18–20 | 17–19 | 131–133 (8–10) | — |
| 5 | moji-youhou-2.html | 問題4 用法 ② | 14–27 | 21–23 | 20–22 | 133–134 (10–11) | — |
| 6 | bunpou-keishiki.html | 問題5 文の文法1（文法形式の判断） | 1–25 | 24–26 | 23–25 | 134–137 (11–14) | — |
| 7 | bunpou-kumitate.html | 問題6 文の文法2（文の組み立て） | 1–25 | 27–29 | 26–28 | 137–140 (14–17) | — |
| 8 | bunpou-bunshou-1.html | 問題7 文章の文法 ① (7-1–7-4) | 20 | 30–37 | 29–36 | grid 140; 141–142 (17–19) | — |
| 9 | bunpou-bunshou-2.html | 問題7 文章の文法 ② (7-5–7-7) | 15 | 38–43 | 37–42 | grid 140; 142–143 (19–20) | — |
| 10 | dokkai-tanbun.html | 問題8 内容理解（短文） (8-1–8-8) | 8 | 44–51 | 43–50 | 144–145 (21–22) | — |
| 11 | dokkai-chuubun-1.html | 問題9 内容理解（中文） ① (9-1–9-3) | 9 | 52–57 | 51–56 | 145–146 (22–23) | — |
| 12 | dokkai-chuubun-2.html | 問題9 内容理解（中文） ② (9-4–9-5) | 6 | 58–61 | 57–60 | 147 (24) | — |
| 13 | dokkai-choubun.html | 問題10 内容理解（長文） (10-1–10-3) | 3 passages | 62–69 | 61–68 | **missing** (intro only, 147) | — |
| 14 | dokkai-tougou.html | 問題11 統合理解 (11-1–11-3) | 3 passages | 70–75 | 69–74 | **missing** | — |
| 15 | dokkai-shuchou.html | 問題12 主張理解（長文） (12-1–12-3) | 3 passages | 76–84 | 75–83 | **missing** | — |
| 16 | dokkai-jouhou.html | 問題13 情報検索 (13-1–13-3) | 3 texts | 85–91 | 84–90 | **missing** | — |
| 17 | choukai-kadai-1.html | 聴解 問題1 課題理解 ① | 1番–8番 | 95–98 | 94–97 | 148–149 (31–32); 1番 answer missing | CD1 · 1–8 |
| 18 | choukai-kadai-2.html | 聴解 問題1 課題理解 ② | 9番–15番 | 98–100 | 97–99 | 149–150 (32–33); 15番 missing | CD1 · 9–15 |
| 19 | choukai-point-1.html | 聴解 問題2 ポイント理解 ① | 1番–7番 | 101–103 | 100–102 | grid 151; 151–153 (34–36) | CD1 · 16–22 |
| 20 | choukai-point-2.html | 聴解 問題2 ポイント理解 ② | 8番–14番 | 103–105 | 102–104 | 153–154 (36–37) | CD1 · 23–29 |
| 21 | choukai-gaiyou-1.html | 聴解 問題3 概要理解 ① | 1番–7番 | 106–108 | 105–107 | grid 155; 155–157 (38–40) | CD2 · 1–7 |
| 22 | choukai-gaiyou-2.html | 聴解 問題3 概要理解 ② | 8番–14番 | 108–109 | 107–108 | 157–158 (40–41) | CD2 · 8–14 |
| 23 | choukai-sokuji-1.html | 聴解 問題4 即時応答 ① | 1番–13番 | 110–113 | 109–112 | grid 159; 159–161 (42–44) | CD2 · 15–27 |
| 24 | choukai-sokuji-2.html | 聴解 問題4 即時応答 ② | 14番–26番 | 113–116 | 112–115 | 161–163 (44–46) | CD2 · 28–40 |
| 25 | choukai-tougou-1.html | 聴解 問題5 統合理解 ① | 1番–5番 | 117–120 | 116–119 | grid 164; 164–165 (47–48) | CD2 · 41–45 |
| 26 | choukai-tougou-2.html | 聴解 問題5 統合理解 ② | 6番–10番 | 120–123 | 119–122 | 166–167 (49–50) | CD2 · 46–50 |

聴解 scripts (別冊 聴解問題スクリプト, PDF 168–207 = 別冊 pp.51–90): 問題1 PDF 168–176 · 問題2 176–184 · 問題3 184–192 · 問題4 192–198 · 問題5 199–207. Exact page per 番 — search the text layer for "N番" and confirm on the image.

Split points for page 21–22 / 36–37 / etc. are approximate where a unit boundary falls mid-page — confirm the first and last item on the rendered page and fix the unit header (not the filename).

## 9. File naming

`moji-*` (文字・語彙), `bunpou-*` (文法), `dokkai-*` (読解), `choukai-*` (聴解); `-1` / `-2` only where a 問題 is split. All files flat in `n1/mock-tests/yosou-mondaishuu/`.

## 10. After building a unit

1. Hub `index.html`: turn its chip from `<span class="day-chip soon" data-href="FILE.html">` into `<a class="day-chip ready" href="FILE.html">` and update the note `In progress — N of 26 units built`.
2. Check: balanced tags (Python html.parser), every relative link resolves (the next unit's link may not exist yet), file ends with `</html>`, no `<audio>`, no passage/script text beyond the quoted key sentences.
