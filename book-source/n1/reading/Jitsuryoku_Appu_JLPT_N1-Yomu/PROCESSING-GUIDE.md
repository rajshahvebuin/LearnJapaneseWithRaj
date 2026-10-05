# 実力アップ！日本語能力試験N1 読む（読解） — processing guide

Standing instructions for turning `Jitsuryoku_Appu_JLPT_N1-Yomu.pdf` (実力アップ！日本語能力試験N1 読む（文章の文法・読解）, ユニコム, JLPT新試験研究会) into study pages at `n1/reading/jitsuryoku-appu/`. Read this together with the master reading spec `book-source/n1/reading/PROCESSING-GUIDE.md` (chrome, strategy box) — but the **page layout** follows the summary-plus-key-sentence pages `n1/multi-skill/drill-and-drill/r-choubun-01.html` and `n1/multi-skill/pattern-betsu-tettei-drill/dokkai-naiyou.html`, not the old Soumatome day pages (which transcribe passages).

**Reference implementation:** `n1/reading/jitsuryoku-appu/bunpou-01.html` (文章の文法 ①).

---

## 1. The scan

- 207 PDF pages. There is a text layer, but it is OCR of a photocopy: the Japanese is mostly usable for searching, the English/Chinese front matter is garbled. **Always read the rendered page image** (PyMuPDF, 120–140 dpi) before quoting anything; never copy text-layer output into a page without checking it against the image.
- Explanatory prose is in Japanese (front matter also has English 'Preface' p.7 and Chinese 前言 p.11). Vocabulary lists give English + Chinese glosses; translate into EN/HI/GU and drop the Chinese.
- Every page has a "facebook.com/duytrieuftu" stamp at the bottom (scanner's watermark) — ignore it.

## 2. Page offset (verified on rendered images)

- Front matter: printed = PDF (目次 page PDF 13 is printed "13").
- **From PDF 14 onward: printed = PDF + 1.** Verified on PDF 15→16, 16→17, 17→18, 40→41, 41→42, 150→151, 170→171, 176→177, and against the TOC (文章の文法 15 / 内容理解 40 / 短文 45 / 中文 64 / 長文 84 / 統合理解 92 / 主張理解 150 / 情報検索 170 = section opener at PDF 14 / 39 / 44 / 63 / 83 / 91 / 149 / 169). Section opener pages carry no number. One front-matter page is evidently missing from the scan (printed 14). PDF 207 is the 奥付 (colophon).

## 3. Book structure

5 sections (この本の構成と使い方, printed p.4–6). Each section opens with a one-paragraph description page, then (except 文章の文法) a スタート問題 warm-up, then numbered exercises ①②…. **Every exercise has the same internal order:**

1. Passage (本文) with (※) footnote glosses, source line in （ ）.
2. Questions + options. **Answer line printed at the bottom of the question page**: `答え：1-1、2-2、…` (blank/question number – correct option).
3. 漢字リスト (kanji words in the passage with readings).
4. ◆答えるための解説 — for every option a reason with ○ / ×, usually quoting the passage sentence that decides it ("「…」とあるので、○"). This is the book's own explanation: paraphrase it in each `.bp-why`.
5. ◆読むための解説 — 重要単語 (word / reading / English / Chinese).
6. ◆重要表現を覚えましょう — expression from the passage = easier paraphrase, plus one 例 sentence.
7. 関連語 and/or a boxed 「○○」のつく言葉 word family (word / reading / English / Chinese).

Section formats:
- **文章の文法** — cloze: 5 numbered blanks in one passage (some split a/b), 4 options each.
- **内容理解** — 短文 (1 question), 中文 (3 questions), 長文 (4 questions); underlined parts ①②③.
- **統合理解** — two texts A/B; questions often use 正/誤 tables (A/B both, only one, neither). Keep the table structure in the options.
- **主張理解** — one long argumentative text, 4 questions.
- **情報検索** — flyer / listings / timetables plus 1–2 questions about a named person's conditions; the 解説 highlights キーワード in colour.

## 4. Answer key

**Complete and in the book itself** — no 別冊. Each exercise's answers are on its own question page (`答え：…` footer) and every option is explained in ◆答えるための解説. Cite both (printed + PDF page) in the header "Answer key" box. The スタート問題 have model answers (正解 / underline answers) instead of numbered options.

## 5. Unit table

One exercise = one unit = one page. 28 units. "Key" = PDF page carrying the `答え：` footer line (or 正解 for スタート問題), located from the text layer; "?" = not found by text search (OCR miss) — the estimate is the question page, confirm on the image when building. The ◆答えるための解説 follows 1–2 pages later.

| filename | title | printed pp | PDF pp | key PDF pp |
|---|---|---|---|---|
| bunpou-01.html | 文章の文法 ① | 16–21 | 15–20 | 16 (verified; 解説 17) |
| bunpou-02.html | 文章の文法 ② | 22–27 | 21–26 | 22 |
| bunpou-03.html | 文章の文法 ③ | 28–33 | 27–32 | 28 |
| bunpou-04.html | 文章の文法 ④ | 34–39 | 33–38 | 34? |
| naiyou-start.html | 内容理解 スタート問題 | 41–44 | 40–43 | 42 (正解) |
| tanbun-01.html | 短文 ① | 45–48 | 44–47 | 44 |
| tanbun-02.html | 短文 ② | 49–54 | 48–53 | 48 |
| tanbun-03.html | 短文 ③ | 55–58 | 54–57 | 54 |
| tanbun-04.html | 短文 ④ | 59–60 | 58–59 | 58 |
| tanbun-05.html | 短文 ⑤ | 61–63 | 60–62 | 60 |
| chuubun-01.html | 中文 ① | 64–69 | 63–68 | 64–65? |
| chuubun-02.html | 中文 ② | 70–75 | 69–74 | 70–71? |
| chuubun-03.html | 中文 ③ | 76–83 | 75–82 | 76–77? |
| choubun-01.html | 長文 ① | 84–91 | 83–90 | 84 (+85?) |
| tougou-start.html | 統合理解 スタート問題 | 94–101 | 93–100 | 99 (正解) |
| tougou-01.html | 統合理解 ① | 102–111 | 101–110 | 102, 104 |
| tougou-02.html | 統合理解 ② | 112–119 | 111–118 | 112 |
| tougou-03.html | 統合理解 ③ | 120–129 | 119–128 | 122 |
| tougou-04.html | 統合理解 ④ | 130–137 | 129–136 | 130 |
| tougou-05.html | 統合理解 ⑤ | 138–149 | 137–148 | 140 |
| shuchou-start.html | 主張理解 スタート問題 | 151–153 | 150–152 | 152 (正解) |
| shuchou-01.html | 主張理解 ① | 154–161 | 153–160 | 154 |
| shuchou-02.html | 主張理解 ② | 162–169 | 161–168 | 162? |
| kensaku-start.html | 情報検索 スタート問題1・2 | 171–177 | 170–176 | 172, 175 (正解) |
| kensaku-01.html | 情報検索 ① | 178–187 | 177–186 | 177 |
| kensaku-02.html | 情報検索 ② | 188–193 | 187–192 | 187–188? |
| kensaku-03.html | 情報検索 ③ | 194–201 | 193–200 | 193–194? |
| kensaku-04.html | 情報検索 ④ | 202–207 | 201–206 | 201–202? |

Section intro pages (no unit of their own; use them in the strategy box of the section's first unit): 文章の文法 PDF 14, 内容理解 PDF 39, 統合理解 PDF 91–92 (sample ○/× table), 主張理解 PDF 149, 情報検索 PDF 169.

## 6. Page sections

- **Header (`.bp-header`)**: section + exercise, source (printed + PDF pages), skills, answer-key box (book's own 答え line + 答えるための解説, with pages), notes box stating the passage is summarised, not reproduced.
- **§1 Strategy & Key Words** — `.rd-strategy` with the section's task instruction (quoted, short) + the section intro paraphrased + tips marked "(added, not in book)" where ours; then tables for 漢字リスト, 重要単語, 重要表現 (expression / = paraphrase / 例 with romaji + EN/HI/GU), 関連語 and the 「○○」のつく言葉 box. The passage's (※) glosses go in a `.bp-notes` line.
- **§2 Exercise** — first a `.bp-quiz` with "Passage summary (not the book's text)" (2–3 sentences, EN/HI/GU, own words) and the source line; then one `.bp-quiz` per question/blank: the one sentence containing the blank or underline (quoted, with romaji + EN/HI/GU), the question stem, `.bp-options` (Option / Japanese+romaji / EN / HI / GU, correct row `class="correct"`), `.bp-why` paraphrasing the book's ○/× reasons and citing the page; anything beyond the book marked "(added, not in book)".
- **§3 Confusion Pairs / Nuance Notes** — `.bp-confusion` table on the grammar forms / connectors / similar options that the wrong answers exploit, plus a `.bp-callout` exam trap.
- `.bp-day-nav` prev / next (first unit's prev = hub index).

## 7. Hard rules

- **No long passages.** Never transcribe a passage — not in pages, scratch files, notes or messages. Summarise in your own words; quote only the sentence(s) each question needs (for cloze: the sentence with the blank, trimmed with … where possible; plus any sentence the 解説 quotes as the deciding clue). If the content filter blocks an output, leave that part out and report it.
- Question stems, options, the book's short glosses, 重要表現 and their 例 sentences may be quoted.
- Never invent questions or answers. Illegible text is marked as such.
- EN + Hindi + Gujarati for every meaning, example and question sentence; `<span class="romaji">` under every Japanese line; "(added, not in book)" for our additions.
- Reuse existing CSS classes only; no audio in this book.

## 8. Hub

`n1/reading/jitsuryoku-appu/index.html`: one `.week-block` per section (文章の文法 / 内容理解 / 統合理解 / 主張理解 / 情報検索) with a chip per unit. Built = `<a class="day-chip ready" href="FILE">`, unbuilt = `<span class="day-chip soon" data-href="FILE">`. Update the `.sample-note` count `In progress — N of 28 units built` after each build.
