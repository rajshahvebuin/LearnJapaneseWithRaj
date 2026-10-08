# きらり☆日本語 N4 語彙 — unit-by-unit processing guide

This guide covers turning `Kirari_Nihongo_N4_Goi.pdf` (日本語能力試験対応 きらり☆日本語 N4 語彙 / Kirari Nihongo N4 Vocabulary — "Vocabulary Builder · Practice · Practice Test", 齋藤美幸・沼田宏・加藤早苗 著 (インターカルト日本語学校), 凡人社, 初版 2013年5月15日) into the site's pages under `n4/vocabulary/kirari-nihongo/`. To build a unit, name it by its filename from the table in §3, then follow the steps below.

Where this file is silent, the general vocabulary spec applies (`book-source/n1/vocabulary/PROCESSING-GUIDE.md`), and after it the sub-book pages already built (`n1/vocabulary/pattern-de-manabu/goi-i-01.html` for the question format).

---

## 0. Scan notes (read this first)

- **150 PDF pages, all scanned images.** The text layer is empty (`page.get_text()` returns `''` on every page). Render with PyMuPDF and read visually: `import pymupdf; doc[i-1].get_pixmap(dpi=130)`. 60–80 dpi is enough for contact sheets, 130–150 dpi to read text, 250–300 dpi crops for furigana and the accent marks in the 語彙リスト. Keep renders out of the repo (use the scratchpad).
- Print quality is good; furigana is readable at 130 dpi.
- **Pencil notes from a previous owner** on at least printed p.3 (PDF 14): handwritten じゅうしょ above 住所 and a scribble in the 年齢 box of the 問診票 form. Ignore any handwriting; it is not the book.
- **The bubble icons 1/2/3** (our "コラム" units, see §1) are printed as grey speech-bubble numbers, not as "コラム". The name "column" is ours.
- **Two printed pages are not in the scan:** p.61 (back of the 第2部 divider) and p.86 (back of the last test page). Both are almost certainly blank; nothing is missing from the questions or key (every test has 19 questions, matching its key).
- The 解答 (answer key) is a **separate booklet bound at the end of the PDF** (PDF 138–148) with its own page numbers.

### PDF ↔ printed page offsets (verified on rendered footers)

| PDF pages | Printed pages | Offset | Content |
|---|---|---|---|
| 1 | — | — | Cover |
| 2–11 | i–x (roman) | — | はじめに, 本書について (JP), About This Book / How to Use This Book (EN), もくじ (PDF 11 = p.x) |
| 12 | (p.1) | +11 | 第1部 divider, no footer |
| 13–70 | 2–59 | **PDF = printed + 11** | 第1部: topics 1–12, bubble sections 1–3. Verified: PDF 13→2, 16→5, 19→8, 58→47, 61→50, 65→54, 70→59 |
| 71 | (p.60) | — | 第2部 divider, no footer; p.61 not in scan |
| 72–95 | 62–85 | **PDF = printed + 10** | 第2部 模擬問題 1–4. Verified: 72→62, 75→65, 88→78, 95→85 |
| 96 | (p.87) | — | 巻末 語彙リスト divider + legend; p.86 not in scan |
| 97–136 | 88–127 | **PDF = printed + 9** | 語彙リスト p.88–115, 五十音索引 (index) p.116–127. Verified: 97→88, 99→90, 126→117, 136→127 |
| 137 | — | — | 奥付 (colophon) |
| 138 | — | — | 解答 booklet cover |
| 139–148 | 解答 p.1–10 | **PDF = 解答 page + 138** | Answer key. Verified: 139→1, 140→2, 144→6, 148→10 |
| 149–150 | — | — | Back covers |

Always cite pages as "p.N (PDF M)" and key pages as "解答 p.N (PDF M)".

---

## 1. What this book is

A topic-based N4 vocabulary builder in two parts (contents: PDF 11):

- **第1部 言葉を増やそう (Vocabulary Builder)**: 12 topics × 4 printed pages, plus three short bubble sections.
  - **Dictionary pages (2 pages per topic)**: numbered word lists down the left and right margins, matched by number to pictures, tables and forms in the middle. Sub-headings group the words (e.g. 運動(する) 1–17, 健康のために 18–21, けが／風邪 22–36). Boxes show **sentence patterns** (e.g. 曲げられますか, 冷やしたほうがいいですよ) and **collocation boxes** (e.g. 気分／調子／具合／顔色 が いい／悪い). Each dictionary spread ends with **話しましょう** (Let's Talk, a 2–3 line model dialogue) and **書きましょう** (Let's Write, a prompt with a hand-written example).
  - **練習しましょう！ (2 pages per topic)**: **ウォーミングアップ** (warm-up: 4 rows of 4 words, pick the odd one out — the key gives a 解答例, an *example* answer with a reason, and says other answers are possible), then numbered exercises 1–5/6: grouping into a table, matching (a–d), "which explanation fits", fill in the blank from a word box (with conjugation), ○/× true-false on a short text, ordering pictures, etc.
  - **Bubble sections 1–3** (we call them コラム): 1 形・スピード・位置 and 2 動詞 are dictionary pages only (no exercises, no key). 3 日本語能力試験の準備 explains six question "points" plus 副詞, 接続詞 and こそあど・疑問詞, each with JLPT-style questions that **do** have a key.
- **第2部 日本語能力試験 模擬問題 1〜4 (JLPT Practice Tests)**: 4 tests × 6 pages × 19 questions, all in hiragana with spaces (old-JLPT style):
  - もんだいA (Q1–9): （　）に なにを いれますか — fill the blank (文脈規定)
  - もんだいB (Q10–14): ＿＿の ぶんと だいたい おなじ いみの ぶん — paraphrase (言い換え類義; options are full sentences)
  - もんだいC (Q15–19): つぎの ことばの つかいかたで いちばん いい もの — usage (用法; options are full sentences)
  - Each test ends with a score box "／19".
- **巻末 語彙リスト (Vocabulary List)** p.88–115 (PDF 97–124): one table per topic, columns **p. / no. / 日本語 / 読み方／アクセント / 英語**. The book's own English gloss for every word, in topic order. Legend (PDF 96): **no.** and **＊** = word numbers in 第1部 (＊ = related word not tied to a picture); **－** = word or phrase that appears in the page body (headings, forms, boxes) without a number. Accent is marked with overlines on the kana; **we do not reproduce accent marks**.
  - 語彙リスト per topic: topic N = p.88+2(N−1) to p.89+2(N−1), i.e. PDF 97+2(N−1) to 98+2(N−1). Bubble 1 = p.112–113 (PDF 121–122), bubble 2 = p.114–115 (PDF 123–124). Bubble 3 has no list.
- **五十音索引 (index)** p.116–127 (PDF 125–136): kana-order index giving topic + page. Not built into pages.
- From the How-to-use page (PDF 9): smaller-print words in the margin lists are **above N4**; ＊ words have no picture but are related; everyday words are written in kanji. Practice questions use old 3級 kanji and words separated by spaces (PDF 10).

### Answer key status — official, present, answers only

解答 booklet p.1–10 (PDF 139–148). Answers only, no explanations; warm-ups give one 解答例 with a one-line reason. Some open items are printed as （省略） (omitted, e.g. topic 9 ② and ⑥) and many fill-ins end with "etc." (any reasonable answer). 話しましょう / 書きましょう have **no key** (free production).

| 解答 page | PDF | Covers |
|---|---|---|
| p.1 | 139 | 1 健康 · 2 家の中 |
| p.2 | 140 | 3 人間関係 · 4 意見・説明 |
| p.3 | 141 | 5 町 · 6 失敗・事故 |
| p.4 | 142 | 7 コミュニティー · 8 連絡・情報 |
| p.5 | 143 | 9 学校・教育 · 10 職場 |
| p.6 | 144 | 11 自然 · 12 変わる |
| p.7 | 145 | Bubble 3 日本語能力試験の準備 (ポイント①–⑥, 副詞, 接続詞, こそあど・疑問詞) |
| p.8 | 146 | 第2部 header · 模擬問題1 |
| p.9 | 147 | 模擬問題2 · 模擬問題3 |
| p.10 | 148 | 模擬問題4 |

Rules: never change a key answer; if one looks wrong, keep it and flag it in the Why note. Where the key says （省略）, "etc.", or gives no answer (話しましょう / 書きましょう, bubble 1–2), give a worked answer labelled **"(our answer, not in book)"**. Where the key gives a 解答例, say it is the book's example answer and that others are possible.

---

## 2. Units (one topic or one test per page)

One unit = one 第1部 topic (4 printed pages: dictionary spread + practice spread, plus that topic's 語彙リスト rows) or one bubble section, or one 模擬問題. Topic word lists are 50–90 entries; that plus ~20 exercise items is one sensible page. Nothing needs splitting. **19 units.**

## 3. Unit table

| File | Title (hub chip) | Romaji / English | Printed pp | PDF pp | 語彙リスト | Answer key |
|---|---|---|---|---|---|---|
| topic-01.html | 1 健康 | Kenkou — Health | 2–5 | 13–16 | p.88–89 (PDF 97–98) | 解答 p.1 (PDF 139) |
| topic-02.html | 2 家の中 | Ie no naka — House | 6–9 | 17–20 | p.90–91 (PDF 99–100) | 解答 p.1 (PDF 139) |
| topic-03.html | 3 人間関係 | Ningen kankei — Relationship | 10–13 | 21–24 | p.92–93 (PDF 101–102) | 解答 p.2 (PDF 140) |
| topic-04.html | 4 意見・説明 | Iken / setsumei — Opinion/Explanation | 14–17 | 25–28 | p.94–95 (PDF 103–104) | 解答 p.2 (PDF 140) |
| topic-05.html | 5 町 | Machi — Town | 18–21 | 29–32 | p.96–97 (PDF 105–106) | 解答 p.3 (PDF 141) |
| topic-06.html | 6 失敗・事故 | Shippai / jiko — Failure/Accident | 22–25 | 33–36 | p.98–99 (PDF 107–108) | 解答 p.3 (PDF 141) |
| topic-07.html | 7 コミュニティー | Komyunitii — Community | 26–29 | 37–40 | p.100–101 (PDF 109–110) | 解答 p.4 (PDF 142) |
| topic-08.html | 8 連絡・情報 | Renraku / jouhou — Contact/Information | 30–33 | 41–44 | p.102–103 (PDF 111–112) | 解答 p.4 (PDF 142) |
| topic-09.html | 9 学校・教育 | Gakkou / kyouiku — School/Education | 34–37 | 45–48 | p.104–105 (PDF 113–114) | 解答 p.5 (PDF 143) |
| topic-10.html | 10 職場 | Shokuba — Workplace | 38–41 | 49–52 | p.106–107 (PDF 115–116) | 解答 p.5 (PDF 143) |
| topic-11.html | 11 自然 | Shizen — Nature | 42–45 | 53–56 | p.108–109 (PDF 117–118) | 解答 p.6 (PDF 144) |
| topic-12.html | 12 変わる | Kawaru — Change | 46–49 | 57–60 | p.110–111 (PDF 119–120) | 解答 p.6 (PDF 144) |
| column-1.html | ① 形・スピード・位置 | Katachi / supiido / ichi — Shape/Speed/Position | 50–51 | 61–62 | p.112–113 (PDF 121–122) | none (no exercises) |
| column-2.html | ② 動詞 | Doushi — Verbs (自動詞・他動詞, 活用, 接続) | 52–53 | 63–64 | p.114–115 (PDF 123–124) | none (no exercises) |
| column-3.html | ③ 日本語能力試験の準備 | Nihongo nouryoku shiken no junbi — Preparation for JLPT | 54–59 | 65–70 | — | 解答 p.7 (PDF 145) |
| mogi-1.html | 模擬問題 1 | Mogi mondai 1 — Practice Test 1 | 62–67 | 72–77 | — | 解答 p.8 (PDF 146) |
| mogi-2.html | 模擬問題 2 | Practice Test 2 | 68–73 | 78–83 | — | 解答 p.9 (PDF 147) |
| mogi-3.html | 模擬問題 3 | Practice Test 3 | 74–79 | 84–89 | — | 解答 p.9 (PDF 147) |
| mogi-4.html | 模擬問題 4 | Practice Test 4 | 80–85 | 90–95 | — | 解答 p.10 (PDF 148) |

Page notes:
- Topic layout is always: dictionary p.N (left page, word list in the left margin), p.N+1 (right page, word list in the right margin, 話しましょう + 書きましょう at the bottom), 練習 p.N+2 (warm-up + exercises 1–3), p.N+3 (exercises 4–5/6).
- Bubble 2 動詞: p.52 自動詞・他動詞 pairs with pictures, p.53 活用 table (ます形 / 辞書形 / 可能形 / 受身形 / て形) and 接続 patterns.
- Bubble 3: p.54 explains ポイント①–⑥ with one example each; p.55–59 give the questions per point, then 副詞, 接続詞, こそあど・疑問詞. Question counts per block are in 解答 p.7.
- 模擬問題: もんだいA Q1–9 run onto the 2nd page; もんだいB Q10–14 on pages 3–4; もんだいC Q15–19 on pages 4–6.

---

## 4. Delivery

- Pages live in `n4/vocabulary/kirari-nihongo/`, at depth 3. Assets are `../../../assets/...`. Copy the chrome exactly from `topic-01.html`: `auth.js` first in `<head>`, favicon, fonts, `style.css` + `day-page.css`, `body.level-page.n4`, the header with the N4 `level-nav` (Vocabulary active), footer and `main.js`.
- Breadcrumb: Home / JLPT N4 / Vocabulary / きらり日本語 N4 語彙 / <unit chip title>.
- `.bp-day-nav`: prev = previous unit in table order (topic-01 links back to the hub `index.html`), next = next unit (mogi-4 links back to the hub). If the next unit is not built, write it as plain text `<span>Next: … — coming soon</span>`; when you build a unit, turn the previous unit's "coming soon" span into a link.
- Reuse existing classes only: `.bp-header`, `.bp-week`, `.bp-meta-grid`, `.bp-points`, `.bp-note(s)`, `.bp-section-title`, `.bp-point`, `.bp-quiz`, `.q-label`, `.q-jp`, `.q-translations`, `.bp-options` (+ `tr.correct`), `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-table-wrap`, `.vd-legend`, `.vd-warmup` (`.vd-warmup-label`, `.vd-prompt`, `.vd-answer`), `.vd-table-wrap`, `.vd-wordlist`, `.jp`, `.note`, `.romaji`, `.bp-day-nav`. Do not edit CSS or JS.
- **Hub update rule** (`index.html`): every unit is a chip in one of three `.week-block`s (第1部 topics / コラム / 第2部 模擬問題). When a unit is built, change `<span class="day-chip soon" data-href="FILE.html">LABEL</span>` to `<a class="day-chip ready" href="FILE.html">LABEL</a>` and update the `.sample-note` header `In progress — N of 19 units built`. At 19, change it to `Complete — 19 of 19 units built` (with ✅, as in other finished hubs).
- Do not run `tools/build_site.py` or git unless the owner asks; do not touch hub pages outside this folder.

## 5. Page format — topic units (topic-NN.html)

1. **Header** (`.bp-header`): `.bp-week` = "JLPT N4 · Vocabulary · きらり日本語 N4 語彙 — 第1部 言葉を増やそう (Vocabulary Builder)". `h1` = "N 漢字title" + romaji + English (the book's English topic name). Meta grid: **Source** (printed + PDF pages, plus 語彙リスト pages); **Sub-groups** chips (the book's sub-headings with their number ranges); **Answer key** ("Official, answers only — 解答 p.N (PDF M)" + the full answer string); **Notes** (what is the book's and what is ours; pictures described not embedded; accent marks not reproduced; any handwriting/scan issues).
2. **§1 Word list**: a `.vd-legend` (no. / ＊ / － meaning, smaller print = above N4) then one `.vd-wordlist` table per book sub-heading, in the book's order, numbers kept. Columns: **No.** / **Japanese** (kanji + kana reading + romaji) / **English** (the book's 語彙リスト gloss, refined if too terse) / **Hindi** / **Gujarati** / **Note** (what the picture shows, collocation, "above N4", related ＊ word). Include the － words (headings, form fields, hospital departments) in the sub-group where they appear.
3. **Sentence patterns and boxes**: each pattern box and collocation box from the dictionary pages, with romaji + EN/HI/GU. Then 話しましょう (quote the 2–3 line model, romaji + EN/HI/GU, it is short) and 書きましょう (the prompt + the book's example + our own model answer labelled "(our answer, not in book)").
4. **§2 練習しましょう — every question**: the warm-up as a `.vd-warmup` per row (4 words with romaji + meaning, the book's 解答例 and reason, translated, and note other answers are possible). Then each exercise: the instruction (JP + romaji + EN/HI/GU); each item as a `.bp-quiz` with the sentence/word + romaji + translations, an options table where it is a choice (correct row `class="correct"`), and a `.bp-why` starting "**Answer X** (book key, 解答 p.N)". Reading-style exercises (doctor's instructions, exercise routines etc.) are short: summarise in EN/HI/GU and quote only the line each item needs — do not transcribe the full text. Pictures are described in one line ("Picture (described): …").
5. **§3 Confusion pairs / nuance notes**: a `.bp-confusion` table of words from the topic that EN/HI/GU would flatten (e.g. 治る／治す, 気分／具合／調子／顔色, 医者／お医者さん), plus `.bp-callout`s for collocation traps (風邪を**ひく**, 骨を**折る**, 薬を**飲む**).
6. `.bp-day-nav`.

## 6. Page format — other units

- **column-1 / column-2**: header + word list (§1 as above, from the 語彙リスト p.112–115) + the tables (数え方 counters, 自動詞・他動詞 pairs, 活用 table) rebuilt as `.bp-table-wrap` tables with romaji + meanings, + 話しましょう / 書きましょう, + confusion pairs. No questions in the book: add 4–6 short check questions only if useful, each labelled "(our question and answer, not in book)".
- **column-3**: header; §1 the six ポイント, each with the book's example (romaji + EN/HI/GU) and a one-line tip of ours; §2 every question per block with the 解答 p.7 answer; §3 confusion pairs (e.g. 長音・促音 reading traps, 破れる／割れる).
- **mogi-N**: header (19 Qs, もんだいA/B/C, key string); §1 "Words tested" chips; §2 every question as `.bp-quiz` — A: the sentence with （　）, options table; B and C: options are full sentences, give each with romaji + EN/HI/GU; `.bp-why` with the key answer and why each distractor fails; §3 confusion pairs drawn from the distractors.

## 7. Hard rules

- `<span class="romaji">` on every Japanese line: words, sentences, options, patterns, warm-up words.
- EN + Hindi + Gujarati for every meaning, example, instruction, question and option. Simple English (N4 learners).
- Every question with the book's answer, citing 解答 p.N. Where the book has no answer (省略, "etc.", 話しましょう/書きましょう, bubbles 1–2): give a worked answer labelled "(our answer, not in book)". Anything else we add: "(added, not in book)".
- Never transcribe the short reading texts in the exercises in full: summarise, quote only the key line per item.
- No audio exists for this book; never add `<audio>` or media links. Never embed the book's pictures — describe them.
- No emoji glyphs in body text (the hub `.sample-note` icon is the only exception, as on other hubs).
- Do not edit CSS, JS, `tools/`, other courses or hub pages outside this folder. Do not run build_site.py or git.

## 8. Checks before finishing a unit

- Every answer matches the 解答 page (read it at 130+ dpi).
- Word numbers and sub-groups match the dictionary pages; English glosses checked against the 語彙リスト.
- Tags balance (Python `html.parser`), all relative links resolve, file ends with `</html>`.
- Hub chip flipped and `In progress — N of 19 units built` updated; previous unit's "coming soon" span turned into a link.

---

**Reference implementation:** `n4/vocabulary/kirari-nihongo/topic-01.html` (1 健康 Health).
