# スピードマスター 日本語能力試験N1 読解 — processing guide

Standing instructions for turning `Speed_Master_N1-Dokkai.pdf` (日本語能力試験問題集 N1読解 スピードマスター, Jリサーチ出版; authors 菊池富美子・黒岩しづ可・武田伸吾・青木洋子 — see colophon PDF 101) into unit pages at `n1/reading/speed-master/`. Read the master reading spec `book-source/n1/reading/PROCESSING-GUIDE.md` for general conventions; where this file differs, this file wins.

**Reference implementation:** `n1/reading/speed-master/tanbun-01.html` (内容理解(短文) 問題1–5). Copy its chrome, header block, section order and quiz markup.

---

## 1. The scan

- 115 PDF pages. There **is** a text layer, but it is poor OCR (furigana merged into lines, wrong kanji, handwriting picked up). Never trust it — always render pages (PyMuPDF, 110–150 dpi) and read the images.
- A previous owner wrote on many pages (hand-drawn underlines, brackets, ✗ marks next to options, pencil notes on PDF 3). **Ignore all handwriting**; only printed underlines (①②… labels) belong to the book.
- Every page carries a `facebook.com/duytrieuftu` header from the scanner — ignore it.
- There is **no 目次 page** in the scan (only a faint bleed-through behind はじめに on PDF 4). The unit list below was built from the section banners, the 実戦練習 answer sheet (PDF 61) and the 別冊 正解 table (PDF 103).

### Page offsets (verified on rendered page numbers)

| PDF range | Printed range | Rule |
|---|---|---|
| 2–48 | 2(?)–49 | **PDF = printed − 1** (checked: PDF 4 = p.3, PDF 7 = p.8, PDF 17 = p.18, PDF 21 = p.22, PDF 44 = p.45, PDF 48 = p.49) |
| — | **50–51** | **MISSING from the scan** (統合理解 問題3) |
| 49–98 | 52–101 | **PDF = printed − 3** (checked: PDF 49 = p.52, PDF 60 = p.63, PDF 63 = p.66, PDF 80 = p.83, PDF 98 = p.101) |
| 99–100 | — | 模擬試験 answer sheets (解答用紙) |
| 101 | — | author bios / colophon |
| 102–114 | 別冊 p.1–13 | **PDF = 別冊 p. + 101** (PDF 103 = 別冊 p.2, PDF 104 = p.3, PDF 114 = p.13) |
| 115 | — | blank |

### Front matter
PDF 2 title (faint) · PDF 4 はじめに (p.3) · PDF 5 日本語能力試験と読解問題 (p.6) · PDF 6 N1について / 読解問題の内容 (p.7: the six 読解 question types with their ねらい — use this for each section's strategy box) · PDF 7–8 この本の使い方 (p.8–9: warm-up, PART 1 実戦練習 with a target time per problem, PART 2 模擬試験, 別冊).

## 2. Answer key — present

- **別冊 正解 table: PDF 103 (別冊 p.2)** — every answer for 実戦練習 and both 模擬試験.
- **別冊 ことばと表現: PDF 104–114 (別冊 p.3–13)** — for every problem: a short title the editors gave the passage (「…」), 【解答】, and a ことばと表現 glossary (Japanese definitions, a few with EN/CN/KR glosses). There is **no 解説** (no explanation of why an answer is right). So on the pages: the answer comes from the key; the "why" and the reasons the wrong options fail are ours and must be marked "(added, not in book)".
- 別冊 page map: 短文 PDF 104–105 (p.3–4) · 中文 PDF 106 (p.5) · 長文 PDF 107 (p.6) · 統合 PDF 108 (p.7) · 主張 PDF 109 (p.8) · 情報検索 PDF 110 (p.9) · 模擬1 PDF 111–112 (p.10–11) · 模擬2 PDF 113–114 (p.12–13).
- The two sources agree wherever checked (短文 1–5). If they ever disagree, report it and use the 別冊 p.3+ entry (it sits next to the glossary for that problem).

## 3. Unit definition and full unit table

A **unit** = one page on the site = a small group of 実戦練習 problems of the same question type (short passages are grouped 5 per unit, 中文 2 per unit, long passages 1 per unit), or half a mock test. Each problem's printed target time (③分, ⑤分, ⑨分, ⑧分) goes in the header.

| File | Title | Printed pp | PDF pp | Key PDF pp | Questions |
|---|---|---|---|---|---|
| keywords.html | ウォーミングアップ — キーワードを覚えよう | 10–16 | 9–15 | — (no key; word lists) | none — topic word lists |
| tanbun-01.html | 内容理解(短文) 問題1–5 | 18–22 | 17–21 | 103, 104 | 5 × 1 Q |
| tanbun-02.html | 内容理解(短文) 問題6–10 | 23–27 | 22–26 | 103, 104–105 | 5 × 1 Q |
| chuubun-01.html | 内容理解(中文) 問題1–2 | 28–31 | 27–30 | 103, 106 | 2 × 3 Q |
| chuubun-02.html | 内容理解(中文) 問題3–4 | 32–35 | 31–34 | 103, 106 | 2 × 3 Q |
| chuubun-03.html | 内容理解(中文) 問題5–6 | 36–39 | 35–38 | 103, 106 | 2 × 3 Q |
| choubun-01.html | 内容理解(長文) 問題1 | 40–41 | 39–40 | 103, 107 | 4 Q |
| choubun-02.html | 内容理解(長文) 問題2 | 42–43 | 41–42 | 103, 107 | 4 Q |
| choubun-03.html | 内容理解(長文) 問題3 | 44–45 | 43–44 | 103, 107 | 4 Q |
| tougou-01.html | 統合理解 問題1 | 46–47 | 45–46 | 103, 108 | 3 Q |
| tougou-02.html | 統合理解 問題2 | 48–49 | 47–48 | 103, 108 | 3 Q |
| tougou-03.html | 統合理解 問題3 「家電と人間の進化・退化」 | 50–51 | **missing** | 103, 108 | 3 Q — pages not in scan |
| shuchou-01.html | 主張理解(長文) 問題1 | 52–53 | 49–50 | 103, 109 | 4 Q |
| shuchou-02.html | 主張理解(長文) 問題2 | 54–55 | 51–52 | 103, 109 | 4 Q |
| shuchou-03.html | 主張理解(長文) 問題3 | 56–57 | 53–54 | 103, 109 | 4 Q |
| jouhou-01.html | 情報検索 問題1 (sports-gym guide) | 58–59 | 55–56 | 103, 110 | 2 Q |
| jouhou-02.html | 情報検索 問題2 (hospital outpatient guide) | 60–61 | 57–58 | 103, 110 | 2 Q |
| jouhou-03.html | 情報検索 問題3 (water-bureau FAQ) | 62–63 | 59–60 | 103, 110 | 2 Q |
| mock-1a.html | 模擬試験 第1回 問題1–2 (Q1–13: 短文 ×4, 中文 ×3) | 66–75 | 63–72 | 103, 111 | 13 Q |
| mock-1b.html | 模擬試験 第1回 問題3–6 (Q14–26: 長文, 統合, 主張, 情報検索) | 76–83 | 73–80 | 103, 111–112 | 13 Q |
| mock-2a.html | 模擬試験 第2回 問題1–2 (Q1–13) | 84–93 | 81–90 | 103, 113 | 13 Q |
| mock-2b.html | 模擬試験 第2回 問題3–6 (Q14–26) | 94–101 | 91–98 | 103, 113–114 | 13 Q |

**22 units.** PDF 16 = PART 1 cover, PDF 61 = 実戦練習 answer sheet, PDF 62 = PART 2 cover.

## 4. Page layout (per unit)

Use the shared chrome (head/header/footer, `../../../` depth, `style.css` + `day-page.css`) exactly as in `tanbun-01.html`. Breadcrumb: Home / JLPT N1 / Reading (`../../reading.html`) / スピードマスター N1 読解 (`index.html`) / unit title.

- **Header (`.bp-header`)**: source with printed + PDF pages, target time(s), question type, answer key (別冊 PDF pages; "no 解説 in the 別冊 — reasons are ours"), and the passage-rule note.
- **§1 Strategy & key words**: `.rd-strategy` box built from p.7's ねらい for that question type (paraphrased) + the PART 1 target-time rule (p.8) + any tips marked "(added, not in book)". Then the 別冊 ことばと表現 table for the unit's problems: Japanese + romaji, the book's Japanese definition (short, quoted — these are glossary lines, not passage text), EN/HI/GU.
- **§2 Every exercise**: one `.bp-quiz` per question. Order inside: `.rd-passage-label` "Passage — 問題N (the 別冊 title)", **Passage summary (not the book's text)** in EN/HI/GU (2–3 sentences, own words), the book's (※) footnote glosses, the **key sentence(s)** only (`.q-jp` + romaji + EN/HI/GU), the question stem (+ romaji + EN/HI/GU), the `.bp-options` table (correct row `class="correct"`), and `.bp-why` citing the 別冊 page and ruling out each wrong option.
- **§3 Confusion / nuance notes**: `.bp-confusion` table — question / where the answer is / the trap in the wrong options; plus a `.bp-callout` exam tip.
- `.bp-day-nav` prev/next to neighbouring units (hub link for the ends).

### Section-type notes
- **keywords.html** is a vocabulary list (topic headings 教育・研究, 政治, 法律・行政, 経済, 裁判, 科学・技術, 自然, 医療・健康 …; each word + a collocation + EN/CN/KR). Build it like a vocabulary page: `.bp-table` per topic, word + romaji + collocation + EN/HI/GU (drop the book's Chinese/Korean). No questions.
- **情報検索** materials (gym fees, hospital hours, FAQ) are tables/notices, not prose: summarise the layout, then reproduce only the rows/lines the question needs (a fee row, an opening-hours line). Do not rebuild the whole leaflet.
- **統合理解** has texts A and B: summarise each separately (A / B), then quote the key line from each.
- **Mock tests**: same quiz markup; group by 問題 with `<h3>` headings, Q numbers 1–26 as in the book.

## 5. Hard rules

- **No long passages.** Never transcribe a passage anywhere (pages, scratch files, notes, messages). Each passage gets a 2–3 sentence "Passage summary (not the book's text)" in EN/HI/GU in our own words; quote only the sentence(s) each question needs. Question stems, options, (※) footnotes and 別冊 glossary lines may be quoted. If output is ever blocked by the content filter, leave that part out and report it.
- EN + Hindi + Gujarati for every meaning, example and question sentence; `<span class="romaji">` under every Japanese line.
- Anything not in the book is marked "(added, not in book)".
- Never invent questions or answers; missing pages are marked as missing.
- Reuse existing CSS classes only (bp-*, rd-*, day chips). No CSS/JS edits.

## 6. Hub

`n1/reading/speed-master/index.html` — `.week-list` > `.week-block` (one per section: キーワード, 短文, 中文, 長文, 統合, 主張, 情報検索, 模擬試験) > `.day-chips`. Built: `<a class="day-chip ready" href="FILE">`; unbuilt: `<span class="day-chip soon" data-href="FILE">`. Keep `.sample-note` text `In progress — N of 22 units built` in sync when a unit is added.

## 7. Oddities

- **Printed pp.50–51 (統合理解 問題3) are missing from the scan.** The 別冊 still has its title 「家電と人間の進化・退化」, answers (1)3 (2)4 (3)2 and ことば (PDF 108). `tougou-03.html` can only show the key + glossary with a "pages missing from this scan" notice — do not reconstruct the questions.
- Short-passage titles in the 別冊 (e.g. 「マンションの買い時」) are editor-added labels — useful as passage names on the page.
- The 長文/主張 passages carry author/source credits under the box; cite them in the passage label.
