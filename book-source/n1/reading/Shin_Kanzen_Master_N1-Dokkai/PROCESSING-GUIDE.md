# 新完全マスター読解 日本語能力試験N1 — processing guide

Standing instructions for turning `Shin_Kanzen_Master_N1-Dokkai.pdf` (新完全マスター読解 N1, 福岡理恵子・清水知子・初鹿野阿れ・中村則子・田代ひとみ, スリーエーネットワーク 2011) into pages under `n1/reading/shin-kanzen-master/`. This guide is book-specific; the general reading spec is `book-source/n1/reading/PROCESSING-GUIDE.md`.

**Reference implementation:** `n1/reading/shin-kanzen-master/part1-01.html` (第1部 1-1)［対比］).

---

## 1. The scan

- 265 PDF pages, image-only (no text layer). Render pages with PyMuPDF (`import pymupdf`, 110–130 dpi is enough to read furigana-free body text; go to 150 dpi for small (注) lines and the 別冊). Scratch renders go in your scratch folder, never in the repo.
- Page size changes at PDF 11 (cover/front matter 512×721 pt, body and 別冊 595×775 pt) — irrelevant except for crop scripts.
- Layout: PDF 1 cover · 2 title · 3 copyright · 4 はじめに · 5–6 目次 · 7–10 本書をお使いになる方へ (vi–ix, incl. a table mapping JLPT 読解 question types to the book's sections) · 11 第1部 title (p.1) · … · 196 模擬試験 title · 197–214 模擬試験 · 215 colophon · 216 series ad · 217 back cover · **218 別冊 cover · 219–265 別冊 解答と解説 printed p.2–48**.

### PDF ↔ printed offsets (verified on rendered page footers — they drift because blank versos were dropped)

| Printed pages | PDF = printed + | Verified on |
|---|---|---|
| p.1–111 (第1部, 第2部) | **+10** | p.2→12, p.4→14, p.11→21, p.20→30, p.50→60, p.66→76, p.70→80, p.100→110, p.111→121 |
| p.113 (第3部 title) | +9 | PDF 122 (p.112 blank, not in scan) |
| p.115–187 (第3部) | **+8** | p.115→123, p.116→124, p.122→130, p.152→160, p.182→190, p.187→195 |
| p.189 (模擬試験 title) | +7 | PDF 196 (p.188 blank, not in scan) |
| p.190–207 (模擬試験) | **+7** | p.190→197, p.203→210, p.207→214 |
| 別冊 p.2–48 | **+217** | 別冊 p.2→219, p.5→222, p.48→265 |

Missing printed pages p.112, p.114 and p.188 are blank versos — no content is lost.

## 2. Answer key status

- **Complete official key in the scan:** 別冊「解答と解説」 = PDF 219–265 (printed 別冊 p.2–48). It covers 練習1–68 and 模擬試験 問題1–11 (questions [1]–[26]); it ends cleanly on 問題11 [26] at 別冊 p.48.
- 別冊 format per 練習: one line saying what the passage is about, the reading move to make (e.g. 「旧ソ連やニューヨーク」と「日本」の対比に注目して…), bullet points citing paragraphs (第n段落), then a line for every option: `n：正解` or the reason it is wrong. Use it for the "Why" (paraphrased, cite 別冊 page) and keep our own extra trap notes marked "(added, not in book)".
- **例題 (worked examples) are answered in the main text**, not the 別冊: right after each 例題 the book walks through 全体をつかもう / ステップ1–3 and 選択肢と比べよう ending with `n：正解`. Cite the printed page of that walkthrough.
- Each 別冊 page footer names the 練習 it covers (e.g. 「練習8〜10」) — use that to find a unit's key pages quickly.

## 3. Unit definition and full unit table

A unit = one numbered section from the 目次 (e.g. 第1部 1-1)［対比］) with its 例題, all its 練習 and any コラム printed inside it. Part title/intro pages are folded into the first unit of that part. 第3部 sections and the 模擬試験 are long (12–18 pages); keep them as one unit each (the page will be long — that is fine).

| File | Title | Printed pp | PDF pp | Items | 別冊 key (printed → PDF) |
|---|---|---|---|---|---|
| part1-01.html | 第1部 1-1)［対比］ほかのものと比べる (+第1部 intro p.1–3, コラム1 常識の落とし穴) | 1–11 | 11–21 | 例題1, 練習1–4 | 例題1 in text p.5; 練習 別冊 p.2–3 → 219–220 |
| part1-02.html | 1-2)［言い換え］ほかの言葉で言い換える | 12–19 | 22–29 | 例題2, 練習5–10 | 別冊 p.3–6 → 220–223 |
| part1-03.html | 1-3)［比喩］ほかのものにたとえる (+コラム2 あなたの意見・筆者の意見) | 20–25 | 30–35 | 例題3, 練習11–14 | 別冊 p.6–7 → 223–224 |
| part1-04.html | 1-4)［疑問提示文］疑問文を使って論点を提示する (+コラム3 疑問文に注意) | 26–31 | 36–41 | 例題4, 練習15–17 | 別冊 p.7–9 → 224–226 |
| part1-05.html | 2-1) 指示語を問う | 32–39 | 42–49 | 例題5–6, 練習18–21 | 別冊 p.9–10 → 226–227 |
| part1-06.html | 2-2)「だれが」「何を」などを問う (+コラム4 カタカナ言葉に注意) | 40–45 | 50–55 | 例題7, 練習22–25 | 別冊 p.10–12 → 227–229 |
| part1-07.html | 2-3) 下線部の意味を問う | 46–53 | 56–63 | 例題8, 練習26–31 | 別冊 p.12–15 → 229–232 |
| part1-08.html | 2-4) 理由を問う | 54–61 | 64–71 | 例題9–10, 練習32–35 | 別冊 p.15–16 → 232–233 |
| part1-09.html | 2-5) 例を問う | 62–66 | 72–76 | 例題11, 練習36–38 | 別冊 p.16–18 → 233–235 |
| part2-01.html | 第2部 1. 全体をつかむ—全体的な内容を尋ねる問い (+第2部 title/intro p.67–69) | 67–81 | 77–91 | 例題12–14, 練習39–41 | 別冊 p.18 → 235 |
| part2-02.html | 2-1) 広告 | 82–91 | 92–101 | 例題15–16, 練習42–43 | 別冊 p.18–19 → 235–236 |
| part2-03.html | 2-2) お知らせ | 92–101 | 102–111 | 例題17–18, 練習44–46 | 別冊 p.19 → 236 |
| part2-04.html | 2-3) 説明書き | 102–107 | 112–117 | 例題19, 練習47–49 | 別冊 p.20 → 237 |
| part2-05.html | 2-4) 表・リスト | 108–111 | 118–121 | 例題20, 練習50 | 別冊 p.20 → 237 |
| part3-01.html | 第3部 1. 内容理解（中文） (+第3部 title/intro p.113, 115) | 113–127 | 122–135 | 例題21, 練習51–54 | 別冊 p.21–25 → 238–242 |
| part3-02.html | 2. 内容理解（長文） | 128–141 | 136–149 | 例題22–23, 練習55–56 | 別冊 p.25–28 → 242–245 |
| part3-03.html | 3. 主張理解（長文） | 142–152 | 150–160 | 例題24, 練習57–59 | 別冊 p.28–32 → 245–249 |
| part3-04.html | 4. 統合理解 | 153–170 | 161–178 | 例題25–26, 練習60–63 | 別冊 p.32–36 → 249–253 |
| part3-05.html | 5. 情報検索 | 171–187 | 179–195 | 例題27–28, 練習64–68 | 別冊 p.36–39 → 253–256 |
| mock-test.html | 模擬試験 (問題1–11, questions [1]–[26]) | 189–207 | 196–214 | 問題1–11 | 別冊 p.39–48 → 256–265 |

20 units. 例題 numbers for 第1部 units 2–9 were read from page tops at low resolution — confirm when building (練習 numbers are certain). 別冊 boundary pages are shared between neighbouring units (e.g. p.3 has 練習3 end + 練習4–5); the ranges above are from the 別冊 footers.

## 4. What each part looks like

- **第1部 評論・解説・エッセイなど (p.1–66).** One short-to-medium essay per item, one 問い each, four options. Part intro (p.2–3) gives the method: section 1 (文章のしくみ) = 全体をつかもう (guess the theme from key words → follow the structure feature → sum up) then 選択肢と比べよう; section 2 (問いを解く技術) = ステップ1 本文を読んで全体をつかもう / ステップ2 問いを見て本文から答えを探そう / ステップ3 選択肢と比べよう. Each section opens with a ◆ one-line definition of the skill. 例題 have a full worked walkthrough (keywords, a diagram, a 3-line summary, option-by-option check) and a dotted tip box (marking advice). Some sections carry a コラム (a one-page essay on reading habits; コラム1 contains a mini 問い).
- **第2部 広告・お知らせ・説明書きなど (p.67–111).** Practical "information" texts (business letters/emails, job ads, shop pages, notices, instructions, tables). Each 例題 has ステップ1–3 plus a "…の一般的な形式" layout diagram and a 重要語彙 box (重要語彙 / 関連語彙 / 練習の語彙).
- **第3部 実戦問題 (p.113–187).** Exam-format: one passage with 2–4 問 (中文/長文/主張), A・B two-text comparisons (統合理解), and 情報検索 sheets. 例題 have 問n のカギ-style walkthroughs; 練習 keys are in the 別冊.
- **模擬試験 (p.189–207).** A full 読解 section in JLPT order, 問題1–11 with continuously numbered questions [1]–[26].

## 5. Page layout (how sections map)

Follow the summary-plus-key-sentence layout of `n1/multi-skill/pattern-betsu-tettei-drill/dokkai-naiyou.html` and `n1/multi-skill/drill-and-drill/r-choubun-01.html`, with the `.rd-strategy` box of `n1/reading/week-1/day-1.html`:

- **Header (`.bp-header`)**: Source (printed + PDF pages and the offset), Skill covered (`.bp-points` chips), Answer key (which 別冊/text page each answer comes from), Notes (the no-passage rule).
- **§1 Strategy & key words**: `.rd-strategy` = the section's ◆ definition + the part's method steps (and for 第2部 the 一般的な形式 / 重要語彙 lists as tables). Put a コラム here as a `.bp-point` summary (in our own words). Add a small key-word table if useful, marked "(added, not in book)" when the book has no list.
- **§2 Every question**: one `.bp-quiz` per 例題 / 練習 (per 問 in 第3部): `.rd-passage-label` with the source line printed under the passage → `.q-translations` "Passage summary (not the book's text)" EN/HI/GU (2–3 sentences, our words) → "Key lines (quoted)" = only the sentence(s) the answer hinges on, each with romaji and EN/HI/GU → the book's (注) glosses (quoted, short) → 【問い】 stem + translations → `.bp-options` table (Option / Japanese+romaji / EN / HI / GU, correct row `class="correct"`) → `.bp-why` with the answer source and the book's reasons paraphrased, then our extra notes "(added, not in book)".
- **§3 Confusion pairs**: `.bp-confusion` table per question — what the structure clue was (対比 pair, 言い換え chain, etc.), the correct option's point, how each wrong option bends the text — plus a `.bp-callout` exam habit.
- `.bp-day-nav` prev/next (hub ↔ units in table order).
- Breadcrumb: Home / JLPT N1 / Reading (`../../reading.html`) / 新完全マスター N1 読解 (`index.html`) / unit.

## 6. Hard rules

- **No long passages.** Never transcribe a reading passage — not on pages, not in scratch files or notes. Each passage gets a 2–3 sentence "Passage summary (not the book's text)" in EN/HI/GU written in your own words; quote only the sentence(s) each question needs (trim with …). Question stems, options and (注) glosses may be quoted. 第2部 information texts: describe the layout and quote only the row/line that decides the answer. If the content filter ever blocks output, drop that part and report it.
- No audio in this book.
- Never invent questions or answers; every answer must come from the 別冊 or the 例題 walkthrough. Mark anything we add "(added, not in book)".
- EN + Hindi + Gujarati for every meaning/sentence; `<span class="romaji">` under every Japanese line.

## 7. File naming & hub

- Files: `part1-01.html` … `part1-09.html`, `part2-01.html` … `part2-05.html`, `part3-01.html` … `part3-05.html`, `mock-test.html` in `n1/reading/shin-kanzen-master/`.
- Hub `index.html`: `.week-list` blocks — 第1部 1 (part1-01–04), 第1部 2 (part1-05–09), 第2部 (part2-01–05), 第3部 (part3-01–05), 模擬試験. Built chip `<a class="day-chip ready" href=…>`, unbuilt `<span class="day-chip soon" data-href=…>`. Keep `In progress — N of 20 units built` in `.sample-note` up to date.
