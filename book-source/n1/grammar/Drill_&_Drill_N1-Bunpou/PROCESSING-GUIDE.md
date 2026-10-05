# ドリル&ドリル N1 文法 — round-by-round processing guide

Standing instructions for turning `Drill_&_Drill_N1-Bunpou.pdf` (ドリル&ドリル 日本語能力試験 N1 文法, 星野恵子 + 辻和子, UNICOM Inc.) into the site's grammar pages. Give a section + round (e.g. "文の文法1 第7回") and this is the process to follow.

This guide adapts the master spec [`../PROCESSING-GUIDE.md`](../PROCESSING-GUIDE.md) (日本語総まとめ N1 文法). Everything in the master spec still applies (site chrome, CSS classes, three required sections, language rules, romaji) **except** where this file says otherwise.

The PDF (172 pages) is scanned/image-only — no text layer. Render pages to PNG with PyMuPDF (`import pymupdf`; `doc[i-1].get_pixmap(dpi=130)`) and read them visually. 120–150 dpi is enough for the question pages; use 130+ dpi for the 別冊 explanations (small blue/Chinese/Korean text).

---

## 1. What this book is (and why the spec is adapted)

- It is a **pure drill book**: there are **no grammar-explanation pages** at all. Every round is a timed set of JLPT-format questions.
- The 【別冊】正解・解説 (answers + explanations) **is included at the end of the same PDF** (PDF 110–171). For 文の文法1 questions it gives: 正解, the completed sentence (blue), ポイント〈pattern〉, 形 (connection), 意味 (meaning, in Japanese), 使い方 (one or two example sentences), sometimes ⚠ notes (with English / Chinese / Korean translation), a 硬い表現 tag for formal patterns, and 参照【n】 cross-references to other question numbers. **Many 文の文法1 entries are thin**: they give only ポイント + 参照 with no 形/意味/使い方; take those details from the referenced entry and cite it. **文の文法2** entries give only 正解, the completed sentence, ポイント and 解き方 (step-by-step ordering logic), plus 問題文の意味 / ⚠ / ✎ on some questions — there are no 形/意味/使い方 fields and no 硬い表現 tags, so connection rules come from the 解き方 and register badges are our judgement. **文章の文法** gives the answers for all blanks in one line, a short 文章の大意 summary (with an English version) and per-blank notes — **not** a full passage translation; the full EN/HI/GU translation on our pages is ours. The 別冊 explains only the correct answer; wrong-option analysis is ours.
- So the answer key is **official** for every unit — never guess; cite the 別冊 page.

### Unit = one 回 (round)

| Section | Rounds | Questions per round | Pages per round | Question numbering |
|---|---|---|---|---|
| 文の文法1 (sentence grammar 1, fill the blank) | 30 | 10 (4 options) | 2 printed pages | continuous 【1】–【300】 |
| 文の文法2 (sentence grammar 2, ★ ordering) | 15 | 5 (4 tiles, find ★) | 1 printed page | restarts 【1】–【75】 |
| 文章の文法 (text grammar, passage cloze) | 10 | 5 blanks (some split 2a/2b, 4a/4b…) | 2 printed pages (passage + options) | 1–5 per passage |

55 units total. A round header looks like `第N回 / 文の文法1` with a 日付/得点 (date/score) grid — that grid is just a self-scoring box, not content. The section divider pages (PDF 11, 72, 89) carry the target score line (e.g. 文の文法1: 10問中7〜8問正解 = 合格ライン) — quote it in the header Notes. PDF 73 (printed p.75) is a 問題例 (worked example of the ★ format) for 文の文法2 — fold it into 文の文法2 第1回 as a short "How ★ questions work" callout.

---

## 2. Verified page offsets

Checked by reading the printed page number stamped on the rendered images (not by trusting the TOC):

**Main book: PDF page = printed page − 2** (from printed p.13 onward).
- PDF 12 → printed 14, PDF 13 → 15, PDF 40 → 42, PDF 71 → 73, PDF 74 → 76, PDF 88 → 90, PDF 100 → 102, PDF 109 → 111.
- Front matter is different: PDF 10 = printed 11 (目次). Printed p.12 (a blank verso) is not in the scan, so PDF 11 = p.13 (文の文法1 divider) and the −2 offset starts there. Don't apply −2 to front-matter pages.
- TOC page numbers (13 / 74 / 91) point at the **section divider pages**; the first round starts one page later (p.14 / p.76 / p.92).

**別冊 (answer booklet, restarts at p.1): PDF page = 別冊 printed page + 109.**
- PDF 111 → 別冊 2 (〈形〉提示の凡例), PDF 112 → 3 (文の文法1 starts), PDF 113 → 4, PDF 130 → 21, PDF 149 → 40 (文の文法2 starts), PDF 165 → 56, PDF 166 → 57 (文章の文法 starts), PDF 171 → 62.
- PDF 110 = 別冊 cover (正解・解説). PDF 172 = back cover. 別冊 p.1 is not in the scan.
- Always cite 別冊 pages as "別冊 p.N (PDF M)" so nobody confuses them with main-book pages.

〈形〉提示の凡例 (別冊 p.2, PDF 111) explains the notation used in 形: 普通形 / 辞書形 / ない形 / て形 / 可能形 / ば形, and the [A + B] bracket notation (A = 動詞・普通形 etc.). Use it when translating 形 into the site's Connection (接続) field.

---

## 3. Unit table

Printed pp are main-book pages; "Answer PDF" is the PDF range in the 別冊 where that round's 解説 lives (first page = where the 第N回 box appears; last page = where the next round's box appears, unless the next box is at the very top of the page). A round's 解説 often begins mid-page — read from the 第N回 box to the next 第N+1回 box.

### 文の文法1 (Q【1】–【300】)

| File | Title | Qs | Printed pp | PDF pp | Answer PDF pp (別冊 pp) |
|---|---|---|---|---|---|
| bun1-01.html | 文の文法1 第1回 | 1–10 | 14–15 | 12–13 | 112–113 (3–4) |
| bun1-02.html | 文の文法1 第2回 | 11–20 | 16–17 | 14–15 | 113–114 (4–5) |
| bun1-03.html | 文の文法1 第3回 | 21–30 | 18–19 | 16–17 | 114–116 (5–7) |
| bun1-04.html | 文の文法1 第4回 | 31–40 | 20–21 | 18–19 | 116–117 (7–8) |
| bun1-05.html | 文の文法1 第5回 | 41–50 | 22–23 | 20–21 | 117–118 (8–9) |
| bun1-06.html | 文の文法1 第6回 | 51–60 | 24–25 | 22–23 | 118–119 (9–10) |
| bun1-07.html | 文の文法1 第7回 | 61–70 | 26–27 | 24–25 | 119–121 (10–12) |
| bun1-08.html | 文の文法1 第8回 | 71–80 | 28–29 | 26–27 | 121–122 (12–13) |
| bun1-09.html | 文の文法1 第9回 | 81–90 | 30–31 | 28–29 | 122–123 (13–14) |
| bun1-10.html | 文の文法1 第10回 | 91–100 | 32–33 | 30–31 | 124–125 (15–16) |
| bun1-11.html | 文の文法1 第11回 | 101–110 | 34–35 | 32–33 | 125–126 (16–17) |
| bun1-12.html | 文の文法1 第12回 | 111–120 | 36–37 | 34–35 | 126–127 (17–18) |
| bun1-13.html | 文の文法1 第13回 | 121–130 | 38–39 | 36–37 | 128–129 (19–20) |
| bun1-14.html | 文の文法1 第14回 | 131–140 | 40–41 | 38–39 | 129–130 (20–21) |
| bun1-15.html | 文の文法1 第15回 | 141–150 | 42–43 | 40–41 | 130–131 (21–22) |
| bun1-16.html | 文の文法1 第16回 | 151–160 | 44–45 | 42–43 | 131–132 (22–23) |
| bun1-17.html | 文の文法1 第17回 | 161–170 | 46–47 | 44–45 | 132–133 (23–24) |
| bun1-18.html | 文の文法1 第18回 | 171–180 | 48–49 | 46–47 | 133–134 (24–25) |
| bun1-19.html | 文の文法1 第19回 | 181–190 | 50–51 | 48–49 | 134–135 (25–26) |
| bun1-20.html | 文の文法1 第20回 | 191–200 | 52–53 | 50–51 | 135–136 (26–27) |
| bun1-21.html | 文の文法1 第21回 | 201–210 | 54–55 | 52–53 | 136–138 (27–29) |
| bun1-22.html | 文の文法1 第22回 | 211–220 | 56–57 | 54–55 | 138 (29) |
| bun1-23.html | 文の文法1 第23回 | 221–230 | 58–59 | 56–57 | 139–140 (30–31) |
| bun1-24.html | 文の文法1 第24回 | 231–240 | 60–61 | 58–59 | 140–141 (31–32) |
| bun1-25.html | 文の文法1 第25回 | 241–250 | 62–63 | 60–61 | 141–142 (32–33) |
| bun1-26.html | 文の文法1 第26回 | 251–260 | 64–65 | 62–63 | 142–143 (33–34) |
| bun1-27.html | 文の文法1 第27回 | 261–270 | 66–67 | 64–65 | 143–144 (34–35) |
| bun1-28.html | 文の文法1 第28回 | 271–280 | 68–69 | 66–67 | 144–146 (35–37) |
| bun1-29.html | 文の文法1 第29回 | 281–290 | 70–71 | 68–69 | 146–147 (37–38) |
| bun1-30.html | 文の文法1 第30回 | 291–300 | 72–73 | 70–71 | 147–148 (38–39) |

### 文の文法2 (★ ordering, Q【1】–【75】)

| File | Title | Qs | Printed p | PDF p | Answer PDF pp (別冊 pp) |
|---|---|---|---|---|---|
| bun2-01.html | 文の文法2 第1回 | 1–5 | 76 (+ 問題例 p.75) | 74 (+73) | 149–150 (40–41) |
| bun2-02.html | 文の文法2 第2回 | 6–10 | 77 | 75 | 150–151 (41–42) |
| bun2-03.html | 文の文法2 第3回 | 11–15 | 78 | 76 | 151–152 (42–43) |
| bun2-04.html | 文の文法2 第4回 | 16–20 | 79 | 77 | 152–153 (43–44) |
| bun2-05.html | 文の文法2 第5回 | 21–25 | 80 | 78 | 153–154 (44–45) |
| bun2-06.html | 文の文法2 第6回 | 26–30 | 81 | 79 | 154–155 (45–46) |
| bun2-07.html | 文の文法2 第7回 | 31–35 | 82 | 80 | 155–156 (46–47) |
| bun2-08.html | 文の文法2 第8回 | 36–40 | 83 | 81 | 157–158 (48–49) |
| bun2-09.html | 文の文法2 第9回 | 41–45 | 84 | 82 | 158–159 (49–50) |
| bun2-10.html | 文の文法2 第10回 | 46–50 | 85 | 83 | 159–160 (50–51) |
| bun2-11.html | 文の文法2 第11回 | 51–55 | 86 | 84 | 160–161 (51–52) |
| bun2-12.html | 文の文法2 第12回 | 56–60 | 87 | 85 | 161–162 (52–53) |
| bun2-13.html | 文の文法2 第13回 | 61–65 | 88 | 86 | 162–163 (53–54) |
| bun2-14.html | 文の文法2 第14回 | 66–70 | 89 | 87 | 163–164 (54–55) |
| bun2-15.html | 文の文法2 第15回 | 71–75 | 90 | 88 | 164–165 (55–56) |

### 文章の文法 (passage cloze)

| File | Title | Printed pp | PDF pp | Answer PDF pp (別冊 pp) |
|---|---|---|---|---|
| bunsho-01.html | 文章の文法 第1回 | 92–93 | 90–91 | 166 (57) |
| bunsho-02.html | 文章の文法 第2回 | 94–95 | 92–93 | 166–167 (57–58) |
| bunsho-03.html | 文章の文法 第3回 | 96–97 | 94–95 | 167 (58) |
| bunsho-04.html | 文章の文法 第4回 | 98–99 | 96–97 | 167–168 (58–59) |
| bunsho-05.html | 文章の文法 第5回 | 100–101 | 98–99 | 168 (59) |
| bunsho-06.html | 文章の文法 第6回 | 102–103 | 100–101 | 168–169 (59–60) |
| bunsho-07.html | 文章の文法 第7回 | 104–105 | 102–103 | 169 (60) |
| bunsho-08.html | 文章の文法 第8回 | 106–107 | 104–105 | 170 (61) |
| bunsho-09.html | 文章の文法 第9回 | 108–109 | 106–107 | 170–171 (61–62) |
| bunsho-10.html | 文章の文法 第10回 | 110–111 | 108–109 | 171 (62) |

Each 文章の文法 round is a passage page (left) plus an options page (right). Double-check answer-page ranges for 文章の文法 when you build them — several rounds share a 別冊 page in two columns, so a round may start in the right column.

---

## 4. Delivery

- Pages live in `n1/grammar/drill-and-drill/` (depth 3: assets are `../../../assets/...`, N1 home `../../index.html`, grammar hub `../../grammar.html`, book hub `index.html`).
- File names: `bun1-01.html … bun1-30.html`, `bun2-01.html … bun2-15.html`, `bunsho-01.html … bunsho-10.html` (two-digit, zero-padded).
- Copy the chrome exactly from the reference unit `n1/grammar/drill-and-drill/bun1-01.html`: `auth.js` script first in `<head>`, favicon, Noto Sans JP, `style.css` + `day-page.css`, `body.level-page.n1`, site header/nav, footer, `main.js`.
- Breadcrumb: Home / JLPT N1 / Grammar (`../../grammar.html`) / ドリル&ドリル N1 文法 (`index.html`) / <current unit>.
- `.bp-day-nav` at the bottom: prev = previous unit file (for the very first unit, the hub `index.html`); next = next unit file in book order (bun1-30 → bun2-01, bun2-15 → bunsho-01; bunsho-10's "next" = back to the hub). Label with the unit title, e.g. `Next: 文の文法1 第2回 (Q11–20) →`. Linking to a not-yet-built page is fine — it will exist once the book is finished — but say so in your report.
- Reuse existing classes only: `.bp-header`, `.bp-meta-grid`, `.bp-point`, `.bp-badge(.formal)`, `.bp-table`, `.bp-formation-table`, `.bp-examples-table`, `.bp-quiz`, `.bp-options` (+ `tr.correct`), `.bp-why`, `.bp-order-chain`, `.bp-assembled`, `.bp-confusion`, `.bp-callout`, `.bp-notes`, `.bp-day-nav`, `.rd-passage-label` (for passage headings). Don't invent CSS.

### Hub update rule

`n1/grammar/drill-and-drill/index.html` has three `.week-block`s (文の文法1 / 文の文法2 / 文章の文法), one chip per round. When a unit is built, flip its chip from `<span class="day-chip soon">第N回</span>` to `<a class="day-chip ready" href="bun1-NN.html">第N回</a>` and update the progress `sample-note` count (x / 55). Don't touch `n1/grammar.html` unless asked (it already links to the hub via its module card).

---

## 5. Header block (every unit)

`.bp-header` with: `bp-week` = "JLPT N1 · Grammar · ドリル&ドリル N1 文法 — <section>"; `h1` = "<section> 第N回" + romaji/English gloss; meta grid:
- **Source**: book name + printed pp (PDF pp) of the questions.
- **Grammar points covered**: chips for each tested pattern (the 別冊 ポイント labels).
- **Answer key**: "Official — 【別冊】正解・解説 p.X–Y (PDF A–B)". Note any question where the 別冊 has no ポイント (e.g. vocabulary-ish items).
- **Notes**: must state that *this book is drill-only, so the Grammar Points explanations, field tables, formation tables and Hindi/Gujarati glosses are added by us, built from the 別冊 解説 (ポイント / 形 / 意味 / 使い方 / ⚠)*; examples not in the book are marked "(added, not in book)". Also the section's 合格ライン and any 硬い表現 tags.

## 6. The three required sections, per question type

### 6a. 文の文法1 (fill the blank, 10 Qs)

1. **Grammar Points** — one `.bp-point` per tested pattern (normally one per question = 10 points; merge if two questions test the same pattern; skip only if a question is pure vocabulary and say so). Order = question order. For each:
   - `【Qn】〜pattern〜` heading + badge (`bp-badge formal` "硬 formal/written" when the 別冊 shows 硬い表現; `bp-badge` "neutral register"/"honorific (謙譲語)" etc. otherwise).
   - Field table: Reading / Meaning (EN) / Meaning (HI) / Meaning (GU) / Connection (接続, from 別冊 形, translated) / Register / Typical use. Cite "別冊 意味:「…」" inside Meaning (EN) when helpful.
   - Formation table: cover only the word types the 形 line allows; anything not in 形 is `class="added"` "(added, not in book)" — or "not used" if the pattern doesn't take that type.
   - Examples table (JP / EN / HI / GU): (a) the 別冊 使い方 example(s) — label "(別冊 使い方)"; (b) the completed quiz sentence — label "(book, Q n)"; (c) optional extra sentences, each labelled "(added, not in book)".
   - Notes: 2–4 sentences, include any ⚠ note from the 別冊 (translate it), and the 参照【n】 cross-reference (which other question in the book re-tests this pattern).
2. **Quiz / Exercise** — every question: `q-jp` with blank + romaji; "Full sentence" + EN / HI / GU; options table `Option / Japanese / English / Hindi / Gujarati` with `tr.correct` on the 別冊 正解; `.bp-why` = why the answer fits (cite 別冊 p.) + why each distractor fails. Distractor analysis is ours unless the 別冊 ⚠ covers it — the 別冊 rarely explains wrong options.
3. **Confusion Pairs** — `.bp-confusion` table built mainly from the *distractors*: the four options of a 文の文法1 question are usually a ready-made confusion set (e.g. ごとく/ごとき/ごとし/ごとに, ずにはすまない/ずにはいられない/ずにはおかない). Pick the 4–8 most exam-relevant contrasts from the round + one or more `.bp-callout` exam traps.

### 6b. 文の文法2 (★ ordering, 5 Qs)

1. **Grammar Points** — the pattern(s) named in each question's 別冊 ポイント (one `.bp-point` each, same format as 6a). The completed 問題文 and the 別冊 解き方 example sentences count as book examples.
2. **Quiz** — show the stem with `＿＿＿ ＿＿＿ ★ ＿＿＿` (this book DOES use the official ★ format), the 4 tiles with romaji, the `.bp-order-chain` (mark the ★ tile `★ n …`), `.bp-assembled` sentence + romaji, EN / HI / GU, the ★ answer (別冊 正解 = the tile number at ★), and a `.bp-why` that walks through the 別冊 解き方 steps ①②③ in English. 第1回 also gets the 問題例 (PDF 73) as a "How ★ questions work" callout.
3. **Confusion Pairs** — contrasts between the round's patterns and the near-miss orderings (connection traps: what may come before/after each tile).

### 6c. 文章の文法 (passage, 5 blanks)

1. **Grammar Points** — the grammar/connective items the blanks test (conjunctions like したがって/ところが, sentence-end patterns like ものだ/わけではない, 指示語, voice/aspect). Use the 別冊 notes; mark all field-table content as added.
2. **Quiz** — reproduce the passage (`.rd-passage-label` + `.bp-quiz` with the passage in `q-jp`, blanks as **［1］**…; romaji paragraph by paragraph), full EN translation (the 別冊 gives one — say so) + HI + GU translation; then one `.bp-quiz` per blank (split blanks like 2a/2b go in one question) with options table + `.bp-why` citing the 別冊.
3. **Confusion Pairs** — the connectors/patterns among the options (e.g. それなのに vs それなら vs それでも) with when-to-use.

## 7. Language rules (unchanged from master)

- EN + Hindi + Gujarati for every meaning, example and quiz sentence; simple English explanations.
- `<span class="romaji">` under every Japanese line (questions, options, tiles, examples, formation cells, confusion forms).
- Don't reproduce the 別冊's Chinese/Korean translations; translate its English ones into our own words.

## 8. Checks before finishing a unit

- Every 正解 matches the 別冊 (re-read the 第N回 block, the numbers are easy to misread at low dpi).
- Tags balanced, all relative links resolve (assets `../../../`, hub `index.html`, prev/next files).
- Hub chip flipped + progress count updated.

---

**Reference implementation:** [`n1/grammar/drill-and-drill/bun1-01.html`](../../../../n1/grammar/drill-and-drill/bun1-01.html) (文の文法1 第1回).

## Notes from the build

- 文章の文法 answer ranges, more precisely: 第6回 starts in the right column of PDF 168 and continues into the left column of 169; 第9回 spills two lines onto the top of PDF 171. Several rounds start partway down a column — read from one 第N回 box to the next.
- Long passages: on new or rebuilt pages, quote only the sentence(s) containing each blank and summarise the rest in our own words, labelled "Passage summary (not the book's text)".
