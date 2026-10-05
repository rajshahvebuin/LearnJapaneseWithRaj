# 実力アップ！日本語能力試験 N1 聞く（聴解） — processing guide

Standing instructions for turning `Jitsuryoku_Appu_JLPT_N1-Kiku.pdf` (実力アップ！日本語能力試験 N1 聴解, JLCI 新試験研究会 / 代表 松本節子, ユニコム UNICOM Inc.) into the site's unit pages under `n1/listening/jitsuryoku-appu/`. Give a unit filename (e.g. `p1-mondai1-01.html`) and this is the process to follow.

Module-wide rules live in `book-source/n1/listening/PROCESSING-GUIDE.md`; this file overrides it where they differ. **Most important difference: this book is built in the summary-plus-key-line layout** of `n1/multi-skill/drill-and-drill/l-kadai-01.html` and `n1/multi-skill/pattern-betsu-tettei-drill/choukai-kadai-2.html`, **NOT** the full-script style of the old `n1/listening/chapter-*/` pages.

**Reference implementation:** `n1/listening/jitsuryoku-appu/mondai-rei.html` (問題例と答え方, built 2026-10-02). Copy its head/header/footer, section order and markup.

## 1. The scan

- 254 PDF pages. **Text layer exists but is useless**: it is Shift-JIS mojibake (only ASCII digits like page numbers and the odd `CD#A-21` survive). Read every page **visually** — render with PyMuPDF (`import pymupdf`, 110–150 dpi) into your scratch folder.
- Every page carries a `facebook.com/duytrieuftu` watermark from the scanner. Ignore it.
- **Offset: printed page = PDF index + 3**, constant through the whole book. Verified on PDF 14→p.17, 16→p.19, 25→p.28 (目次), 37→p.40, 139→p.142, 199→p.202, 251→p.254.
- Front matter (PDF 0–12): cover, はじめに, この本の特長, 構成と使い方, Foreword (EN), 前言 (CN). 目次 = PDF 25–26 (p.28–29). **CD track list (CDトラックNo一覧) = PDF 27–29 (p.30–32)**, which gives the track for every item.
- The book is trilingual in places (JP + EN + CN glosses in 重要語 boxes; Part 4 also prints EN/CN translations of each exchange). Reuse the English gloss where it helps; Hindi and Gujarati are always ours.

## 2. Audio

- Two CDs next to the PDF: `Jitsuryoku_Appu_JLPT_N1-Kiku-AudioCD1/` (46 files, `01 Track 1.mp3` … `46 Track 46.mp3`) and `…-AudioCD2/` (97 files). Total 143, which matches the book's track list exactly.
- The book labels tracks **CD#A-nn = CD1 Track nn** and **CD#B-nn = CD2 Track nn** (1:1, no offset). A-01 is the title track.
- On pages write the badge as `<span class="ld-track">CD1 · Track 8</span>` and mention the book's label (CD#A-08) once in the header.
- **Audio is copyrighted and is never published.** No `<audio>` elements, no links to the mp3s, no copying them out of `book-source/`.

## 3. Book structure and answer key

Each Part = one test question type. **Questions first** (options only, as on the test paper), **then a 《スクリプトと解説》 block** with one item per ~2–3 pages: 番号 + 正解 N + CD#, the script, the question and options again, then 解説 (覚えておきたい会話表現 with 例 sentences), 重要語 / 関連語 (JP + reading + EN + CN) and occasional column boxes (e.g. 「怒り」を表す言葉 p.61, お金に関する言葉 p.109).

- **Answer key: complete and official, printed in the book.** The 正解 mark sits at the top of each script item (in 問題例, at the bottom of the script). There is **no 別冊**. Parts 6 and 7 have no questions, so they have no key.
- Part 1 問題1 and Part 2 items show options as text; Part 1 問題2 options are pictures (ア–オ combinations), so describe each picture in the options table (as in `choukai-kadai-2.html`).
- Part 3 and Part 4 print nothing but `［1 2 3 4］` / `［1 2 3］`, so options come from the script pages.
- Part 5 問題1 (1番) has 1 question; 問題2 (2番–6番) has 質問1 + 質問2 each, with separate 正解 (問1 正解 / 問2 正解).

## 4. Units (25)

Unit = a run of consecutive 番 within one Part, sized to ~8–10 printed pages. "Q pp" = the question page(s), "S pp" = the スクリプトと解説 pages. Key = the 正解 mark on the S pages (same PDF pages).

| # | filename | title | printed pp | PDF pp | answer-key PDF pp | audio |
|---|---|---|---|---|---|---|
| 1 | mondai-rei.html | 問題例と答え方 問題1〜5 (例1・例2・問題2–5) | 16–27 | 13–24 | 14, 16, 18, 20, 21, 24 (in-page 正解) | CD1 T2–7 |
| 2 | p1-mondai1-01.html | Part 1 問題1 1番〜4番 | Q 34–35, S 40–47 | 31–32, 37–44 | 37–44 | CD1 T8–11 |
| 3 | p1-mondai1-02.html | Part 1 問題1 5番〜8番 | Q 35–36, S 48–57 | 32–33, 45–54 | 45–54 | CD1 T12–15 |
| 4 | p1-mondai1-03.html | Part 1 問題1 9番〜11番 | Q 37–38, S 58–65 | 34–35, 55–62 | 55–62 | CD1 T16–18 |
| 5 | p1-mondai1-04.html | Part 1 問題1 12番〜14番 | Q 38–39, S 66–74 | 35–36, 63–71 | 63–71 | CD1 T19–21 |
| 6 | p1-mondai2-01.html | Part 1 問題2 1番〜4番 (picture options) | Q 75–78, S 82–89 | 72–75, 79–86 | 79–86 | CD1 T22–25 |
| 7 | p1-mondai2-02.html | Part 1 問題2 5番〜7番 (picture options) | Q 79–81, S 90–96 | 76–78, 87–93 | 87–93 | CD1 T26–28 |
| 8 | p2-01.html | Part 2 1番〜4番 | Q 98–99, S 102–111 | 95–96, 99–108 | 99–108 | CD1 T29–32 |
| 9 | p2-02.html | Part 2 5番〜8番 | Q 100–101, S 112–122 | 97–98, 109–119 | 109–119 | CD1 T33–36 |
| 10 | p3-01.html | Part 3 1番〜3番 | Q 124, S 126–133 | 121, 123–130 | 123–130 | CD1 T37–39 |
| 11 | p3-02.html | Part 3 4番〜7番 | Q 124–125, S 134–142 | 121–122, 131–139 | 131–139 | CD1 T40–43 |
| 12 | p3-03.html | Part 3 8番〜10番 | Q 125, S 143–151 | 122, 140–148 | 140–148 | CD1 T44–46 |
| 13 | p4-01.html | Part 4 1番〜9番 | Q 153–154, S 158–166 | 150–151, 155–163 | 155–163 | CD2 T1–9 |
| 14 | p4-02.html | Part 4 10番〜18番 | Q 154, S 167–175 | 151, 164–172 | 164–172 | CD2 T10–18 |
| 15 | p4-03.html | Part 4 19番〜27番 | Q 155, S 176–184 | 152, 173–181 | 173–181 | CD2 T19–27 |
| 16 | p4-04.html | Part 4 28番〜36番 | Q 155–156, S 185–193 | 152–153, 182–190 | 182–190 | CD2 T28–36 |
| 17 | p4-05.html | Part 4 37番〜45番 | Q 156–157, S 194–202 | 153–154, 191–199 | 191–199 | CD2 T37–45 |
| 18 | p5-01.html | Part 5 1番 (問題1) + 2番〜3番 (問題2) | Q 204–206, S 208–217 | 201–203, 205–214 | 205–214 | CD2 T46–48 |
| 19 | p5-02.html | Part 5 4番〜6番 (問題2) | Q 206–207, S 218–228 | 203–204, 215–225 | 215–225 | CD2 T49–51 |
| 20 | p6-01.html | Part 6 第1部 挨拶 | 230–233 | 227–230 | none (no questions) | CD2 T52–55 |
| 21 | p6-02.html | Part 6 第2部 場面1〜6 | 234–237 | 231–234 | none | CD2 T56–61 |
| 22 | p6-03.html | Part 6 第2部 場面7〜12 | 237–240 | 234–237 | none | CD2 T62–67 |
| 23 | p7-01.html | Part 7 1〜10 | 242–245 | 239–242 | none | CD2 T68–77 |
| 24 | p7-02.html | Part 7 11〜20 | 245–249 | 242–246 | none | CD2 T78–87 |
| 25 | p7-03.html | Part 7 21〜30 | 250–254 | 247–251 | none | CD2 T88–97 |

Item → script start page (printed), for quick lookup:
- Part 1 問題1: 1:40 2:42 3:44 4:46 5:48 6:50 7:52 8:54–57 9:58–61 10:62 11:64 12:66–68 13:69–71 14:72–74. Question pages: 1–2 p.34, 3–5 p.35, 6–8 p.36, 9–10 p.37, 11–12 p.38, 13–14 p.39.
- Part 1 問題2: questions one per page p.75–81; scripts 1:82 2:84 3:86 4:88 5:90 6:92 7:94–96.
- Part 2: questions 1–2 p.98, 3–4 p.99, 5–6 p.100, 7–8 p.101; scripts 1:102 2:104 3:106–109 4:110 5:112–114 6:115–117 7:118–119 8:120–122.
- Part 3: questions 1–5 p.124, 6–10 p.125; scripts 1:126 2:129 3:132 4:134 5:136 6:138 7:140 8:143 9:146 10:149–151.
- Part 4: questions 1–8 p.153, 9–18 p.154, 19–28 p.155, 29–38 p.156, 39–45 p.157; script for n番 = printed p.(157+n), one per page.
- Part 5: questions 1番 p.204, 2番 p.205, 3–4 p.206, 5–6 p.207; scripts 1:208–210 2:211–213 3:214–217 4:218–219 5:220–222 6:223–228.
- Part 6: 第1部 挨拶 p.230 (B-52) · 231 (B-53) · 232 (B-54) · 233 (B-55); 第2部 場面1–2 p.234, 3 p.235, 4–5 p.236, 6–7 p.237, 8–9 p.238, 10–11 p.239, 12 p.240 (場面n = B-(55+n)).
- Part 7: 1–3 p.242, 4–6 p.243, 7–9 p.244, 10–11 p.245, 12–13 p.246, 14–16 p.247, 17–18 p.248, 19–20 p.249, 21–22 p.250, 23–24 p.251, 25–26 p.252, 27–28 p.253, 29–30 p.254 (passage n = B-(67+n)).

## 5. Page layout (Parts 1–5 and 問題例)

Copy `mondai-rei.html`. Header `bp-header`: source + printed/PDF pp, skill chips, audio badges (CD1/CD2 + the book's CD#A/B label), answer-key line ("book 正解, p.X"), and the standing copyright + no-transcript note.

- **§1 Strategy & Key Words.** A short `.rd-strategy` box for the question type (summarise the book's own guidance, or mark tips "(added, not in book)"), then a word table built from the unit's **覚えておきたい会話表現 + 重要語/関連語** boxes (Japanese | EN | HI | GU | 番). These boxes are the book's, so label the table with their page numbers. Quote 会話表現 headwords and their ＝ paraphrases; 例 sentences are short and may be quoted.
- **§2 Every question.** One `.bp-quiz` per 番: `q-label`, `ld-track`, the setting line + question (`q-jp` + romaji, with EN/HI/GU in `q-translations`), a **Script summary (not the book's text)** box in EN/HI/GU (2–3 sentences each), **The line the answer hinges on** (one line, at most two short ones, with romaji + EN/HI/GU), the `bp-options` table with `tr class="correct"` on the answer, and `bp-why` citing "book 正解, p.X". Use the book's 解説 where it explains the answer, otherwise mark the reasoning "(added, not in book)".
- **§3 Confusion Pairs / Nuance Notes.** `bp-confusion` table of the traps (paraphrase vs literal, final decision vs earlier wish, maybe vs aim, etc.) plus one `bp-callout` exam trap.
- `bp-day-nav`: previous ← / next → by unit order (first unit's "previous" is the hub).

Part-specific notes:
- **Part 1 問題2 (picture options)**: describe each picture/combination in words in the options table; never embed scans.
- **Part 4 (即時応答)**: the opening line *is* the hinge line, so quote it (it's one sentence) plus all three short replies as options. Do not reproduce the book's EN/CN translation block; write your own EN + HI + GU. No script summary is needed beyond a one-line setting.
- **Part 5**: one quiz per 番; for 問題2 items show 質問1 and 質問2 as two option tables inside the same quiz, each with its own answer.

## 6. Parts 6 and 7 (no questions)

- **Part 6 シャドーイング**: short A/B exchanges grouped by situation (年末, 葬式, 転職… / 誘う, 頼む, 断る…). These are audio scripts, so **do not transcribe the dialogues**. For each situation give: the function in EN/HI/GU, a 1-sentence summary of each exchange, and quote only the fixed set phrase being drilled (e.g. ご愁傷様でございました) with romaji + meaning + usage note. §2 becomes a "shadowing drill" checklist pointing to the track; §3 = politeness/situation confusion pairs.
- **Part 7 パラレルリーディング**: 30 short (~5-line) passages, each built around one grammar pattern printed as its title (〜げ, 〜きり, 〜あまり, 〜を通して, 〜ことか, 〜せいだ…). These are read-aloud passages, so **do not reproduce them**. Per passage: the pattern headword + book gloss (EN/CN from the title) with our HI/GU, a 1–2 sentence passage summary in EN/HI/GU, and quote only the one sentence containing the pattern. §3 = similar-pattern confusion pairs.

## 7. Hard content rules (from the setup brief)

- **Never transcribe listening scripts** (or Part 6/7 texts), whether in pages, scratch files, notes or messages. Summaries in our own words; quote only the line each answer hinges on. If output is ever blocked by the content filter, leave that part out and report it. Do not work around it.
- Audio by CD + track number only (see §2).
- Never invent questions or answers; the key is complete, so every answer must cite its 正解 page.
- EN + HI + GU for every meaning/example/question sentence; `<span class="romaji">` under every Japanese line; mark our additions "(added, not in book)".
- Reuse existing CSS classes only (bp-*, rd-*, ld-track, day chips); do not edit CSS/JS.

## 8. Hub upkeep

`n1/listening/jitsuryoku-appu/index.html`: when a unit is built, change its `<span class="day-chip soon" data-href="X.html">` to `<a class="day-chip ready" href="X.html">` and bump the note `In progress — N of 25 units built`. Then check balanced tags (Python `html.parser`), that relative links resolve, and that the file ends with `</html>`.
