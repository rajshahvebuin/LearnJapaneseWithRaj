# 試験に出る 読解 N1・N2 (Shiken ni Deru Dokkai N1・N2, 桐原書店, 40日完成) — processing guide

Book-specific instructions for turning `Shiken_ni_Deru_N1_N2-Dokkai.pdf` into pages under `n1/reading/shiken-ni-deru/`. Read this together with the module spec `book-source/n1/reading/PROCESSING-GUIDE.md` (page sections, chrome) — where the two differ, **this file wins** for this book.

Authors: インターカルト日本語学校 (筒井由美子・大村礼子・喜多民子), 2010. Same series as `n1/grammar/shiken-ni-deru/` (試験に出る文法と表現). The book covers **N1 and N2**; it lives in the N1 module. Units the book labels N2 are kept and marked "N2-level" on the page and the hub.

---

## 1. The scan

- 202 PDF pages, image-only. The text layer is just the watermark `http://riyuxuexi.taobao.com/` (twice per page): render pages with PyMuPDF (`import pymupdf`, 110–150 dpi) and read them visually. Never copy the watermark into a page.
- **Main book: PDF page = printed page (offset 0).** Verified on printed p.3, 4, 5, 6, 7, 10, 11, 32, 42, 72, 84, 100, 115, 124, 130, 140, 156, 161, 175.
- Blank pages: PDF 8, 30, 178. Upside-down scans (rotate 180° when rendering): PDF 9 (第1部 title page) and PDF 167, 173 (inside the N1 mock test; page numbers print upside down). PDF 168–169 are vertical-writing (縦書き) passages — read right-to-left.
- Part title pages: 第1部 PDF 9, 第2部 PDF 31, 第3部 PDF 139. Colophon PDF 176.
- **Answer key = the 別冊 解答・問題を解くヒント, bound into this scan at the end.** Cover PDF 177, 目次 PDF 179, content 別冊 p.2–24 = **PDF 180–202 (別冊 page = PDF − 178)**. Verified on 別冊 p.2 (PDF 180), p.6 (PDF 184), p.24 (PDF 202).
  - Each day: a line of answers (問題n 問1：x …), then a 「問題を解くヒント」 box: the key sentence(s) or the line numbers the answer hinges on, sometimes with arrows showing modifier structure, sometimes ×-notes on wrong options. Paraphrase the hint in each "Why"; reasons for other wrong options are ours, marked "(added, not in book)".
  - The two mock tests (第3部) have **answers only, no hints** (PDF 202).
- No audio. No vocabulary lists (ことば) in the book — any word table is ours and marked "(added, not in book)".

## 2. Book structure and unit definition

A **unit = one 日目 (day)**, plus one unit per mock test. **42 units.**

- 第1部 基本トレーニング (第1–10日目, printed p.10–29): ポイント別学習. Each day = 2 pages: a short intro paragraph explaining the skill, then 問題1–3 (sometimes 4–5) built on **short excerpts (1–6 sentences)**. Many answers are free-write or pick-two (e.g. 「だれがだれに」 = one option from 1–4 + one from 5–8; answer written 4・7).
- 第2部 模擬問題で練習 (第11–40日目, printed p.32–138): JLPT-format practice, grouped by question type and level (table below). **問題 numbers continue across the days of a group** (e.g. 内容理解(短文)N2: 11日目 = 問題1–4, 12日目 = 問題5–7 …) — keep the book's numbering.
- 第3部 模擬試験 (printed p.140–175): an N2 reading mock (問題1–5, 21 items) and an N1 reading mock (問題1–6, 26 items). Both say 解答は別冊24ページ.

## 3. Unit table

File names: `day-NN.html` (two digits, like the grammar book), `mock-n2.html`, `mock-n1.html`. Hub chip label = the book's 第N日目 / N2模擬試験 / N1模擬試験.

| File | Title | Printed pp | PDF pp | Key 別冊 pp (PDF) |
|---|---|---|---|---|
| day-01.html | 第1日目 「だれが？」「だれを？」「だれに？」 | 10–11 | 10–11 | 2 (180) |
| day-02.html | 第2日目 連体修飾 | 12–13 | 12–13 | 2 (180) |
| day-03.html | 第3日目 文の骨組み | 14–15 | 14–15 | 3 (181) |
| day-04.html | 第4日目 中身は何か | 16–17 | 16–17 | 3 (181) |
| day-05.html | 第5日目 筆者の言いたいこと | 18–19 | 18–19 | 3–4 (181–182) |
| day-06.html | 第6日目 あとに続く内容 | 20–21 | 20–21 | 4 (182) |
| day-07.html | 第7日目 心情の理解 | 22–23 | 22–23 | 4 (182) |
| day-08.html | 第8日目 言葉の組み合わせを問う問題 | 24–25 | 24–25 | 5 (183) |
| day-09.html | 第9日目 正しい順序に並べる | 26–27 | 26–27 | 5 (183) |
| day-10.html | 第10日目 手紙、メールを読む | 28–29 | 28–29 | 5 (183) |
| day-11.html | 第11日目 内容理解(短文) N2 | 32–33 | 32–33 | 6 (184) |
| day-12.html | 第12日目 内容理解(短文) N2 | 34–35 | 34–35 | 6 (184) |
| day-13.html | 第13日目 内容理解(短文) N2 | 36–37 | 36–37 | 7 (185) |
| day-14.html | 第14日目 内容理解(短文) N2 | 38–39 | 38–39 | 7 (185) |
| day-15.html | 第15日目 内容理解(短文) N2 | 40–41 | 40–41 | 7–8 (185–186) |
| day-16.html | 第16日目 内容理解(短文) N1 | 42–43 | 42–43 | 8 (186) |
| day-17.html | 第17日目 内容理解(短文) N1 | 44–45 | 44–45 | 8 (186) |
| day-18.html | 第18日目 内容理解(短文) N1 | 46–47 | 46–47 | 8–9 (186–187) |
| day-19.html | 第19日目 内容理解(短文) N1 | 48–49 | 48–49 | 9 (187) |
| day-20.html | 第20日目 内容理解(短文) N1 | 50–51 | 50–51 | 9 (187) |
| day-21.html | 第21日目 内容理解(中文) N2 | 52–53 | 52–53 | 10 (188) |
| day-22.html | 第22日目 内容理解(中文) N2 | 54–56 | 54–56 | 10 (188) |
| day-23.html | 第23日目 内容理解(中文) N2 | 57–59 | 57–59 | 11 (189) |
| day-24.html | 第24日目 内容理解(中文) N1 | 60–63 | 60–63 | 11–12 (189–190) |
| day-25.html | 第25日目 内容理解(中文) N1 | 64–67 | 64–67 | 12 (190) |
| day-26.html | 第26日目 内容理解(中文) N1 | 68–71 | 68–71 | 12–13 (190–191) |
| day-27.html | 第27日目 内容理解(長文) N1 | 72–76 | 72–76 | 13 (191) |
| day-28.html | 第28日目 内容理解(長文) N1 | 77–80 | 77–80 | 14 (192) |
| day-29.html | 第29日目 内容理解(長文) N1 | 81–83 | 81–83 | 14–15 (192–193) |
| day-30.html | 第30日目 統合理解 N2 | 84–89 | 84–89 | 15 (193) |
| day-31.html | 第31日目 統合理解 N1 | 90–95 | 90–95 | 16 (194) |
| day-32.html | 第32日目 統合理解 N1 | 96–99 | 96–99 | 17 (195) |
| day-33.html | 第33日目 主張理解 N2 | 100–105 | 100–105 | 18 (196) |
| day-34.html | 第34日目 主張理解 N2 | 106–114 | 106–114 | 19–20 (197–198) |
| day-35.html | 第35日目 主張理解 N1 | 115–120 | 115–120 | 20 (198) |
| day-36.html | 第36日目 主張理解 N1 | 121–123 | 121–123 | 20–21 (198–199) |
| day-37.html | 第37日目 情報検索 N2 | 124–126 | 124–126 | 21 (199) |
| day-38.html | 第38日目 情報検索 N2 | 127–129 | 127–129 | 21–22 (199–200) |
| day-39.html | 第39日目 情報検索 N1 | 130–133 | 130–133 | 22 (200) |
| day-40.html | 第40日目 情報検索 N1 | 134–138 | 134–138 | 23 (201) |
| mock-n2.html | N2模擬試験 読解 | 140–155 | 140–155 | 24 (202), answers only |
| mock-n1.html | N1模擬試験 読解 | 156–175 | 156–175 | 24 (202), answers only |

Day starts in 第2部 were read from each page's 第N日目 banner; ends = page before the next banner. Key page ranges were read from the 別冊's black 「N日目」 tags; a day whose key spills onto the next page is shown as a range. Re-check on render before building.

## 4. Page sections (how the book maps onto a page)

Copy the layout of `day-01.html` (reference implementation) — header/strategy chrome from `n1/reading/week-1/day-1.html`, summary + key-sentence layout from `n1/multi-skill/drill-and-drill/r-choubun-01.html` and `n1/multi-skill/pattern-betsu-tettei-drill/dokkai-naiyou.html`.

- **Header (`.bp-header`)**: part / day / skill; Source = book + printed pp (PDF pp); Answer key = 別冊 p.N (PDF N), what the hint gives; Notes = the passage rule below + "N2-level" flag where it applies.
- **§1 Strategy & words**: 第1部 — paraphrase the day's intro paragraph (EN/HI/GU) in a `.rd-strategy` box, plus 1–2 tips marked "(added, not in book)". 第2部 — the book has no per-day intro, so give the JLPT question-type instruction line (quoted, with romaji + EN/HI/GU) and our own tips for that type, marked "(added, not in book)". An optional word table (`.bp-table`) of the hard words in the quoted sentences/options, marked "(added, not in book)".
- **§2 Every exercise**: one `.bp-quiz` per 問題 (passage) with: `.rd-passage-label` source line; "Passage summary (not the book's text)" in EN/HI/GU (2–3 sentences, own words); then per 問: the key sentence(s) quoted (`.q-jp` + romaji + EN/HI/GU), the question stem, a `.bp-options` table (correct row `class="correct"`), and `.bp-why` = "Answer X (別冊 p.N)" + paraphrase of the 別冊 hint + why the other options fail "(added, not in book)". Free-write answers (第1部): show the book's model answer in a `.q-translations` box instead of an options table. Pick-two questions (「だれがだれに」): one options table with both columns, both correct rows marked.
- **§3 Confusion / nuance**: a `.bp-confusion` table comparing the traps of the day (who-does-what swaps, near-identical options, reversed cause/effect…) + a `.bp-callout` exam trap. Mark the table "(added, not in book)".
- **Footer nav (`.bp-day-nav`)**: previous / next unit.
- Mock tests: same per-問題 blocks; the key gives answers only, so every "Why" is ours — say so in the header.

## 5. Passage rules (hard)

- **Never transcribe passages** — not on pages, not in scratch files, notes or messages. Even 第1部's short excerpts get a summary in our own words; quote only the sentence(s) a question needs (normally the underlined sentence, or the sentence the 別冊 hint points to). For 情報検索, describe the notice/table in words and quote only the rows/lines needed.
- Question stems, options and the book's short (注)/※ glosses may be quoted.
- If a filter blocks an output, leave that part out and report it.
- English + Hindi + Gujarati for every meaning/sentence; romaji (`<span class="romaji">`) under every Japanese line; "(added, not in book)" on everything that is ours.
- Never invent questions or answers. Answers come from the 別冊; if a scan page is illegible, mark it.

## 6. Hub

`n1/reading/shiken-ni-deru/index.html`: one `.week-block` per 部 / 第2部 group (第1部; 内容理解(短文)N2; 内容理解(短文)N1; 内容理解(中文)N2; 内容理解(中文)N1; 内容理解(長文)N1; 統合理解N2; 統合理解N1; 主張理解N2; 主張理解N1; 情報検索N2; 情報検索N1; 第3部 模擬試験). Built = `<a class="day-chip ready" href="…">`, not built = `<span class="day-chip soon" data-href="…">`. Keep the `.sample-note` text `In progress — N of 42 units built` up to date.
