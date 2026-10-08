# 実力アップ！日本語能力試験N4 読む — unit-by-unit processing guide

This guide covers turning `Jitsuyouku_Appu_N4_Yomu.pdf` (note the typo "Jitsuyouku" in the file name; the folder is spelled correctly) into the study pages at `n4/reading/jitsuryoku-appu/`. To build a unit, look up its file name in the table in §4, then follow §5–§6.

Read it together with:
- the N1 volume of the same series: `book-source/n1/reading/Jitsuryoku_Appu_JLPT_N1-Yomu/PROCESSING-GUIDE.md` (built pages: `n1/reading/jitsuryoku-appu/`). Its reading units (summary + key sentence + ○/× 解説) are the model for our units in group E.
- the general reading spec: `book-source/n1/reading/PROCESSING-GUIDE.md` (chrome, strategy box).
- the N5 drill guide `book-source/n5/multi-skill/Tanki_Master_Drill_N5/PROCESSING-GUIDE.md` (short-item drill pages; model for groups A–D).

**Reference implementation:** `n4/reading/jitsuryoku-appu/joshi-01.html` (助詞100問 Q1–20).

---

## 0. Book identification

- **Title:** 実力アップ！日本語能力試験N4 読む（文字・語彙・文法・読解） (Jitsuryoku Appu! Nihongo Nouryoku Shiken N4 Yomu — moji, goi, bunpou, dokkai)
- **Authors:** JLCI新試験研究会 (代表 松本節子). English translation: Craig Dibble.
- **Publisher:** ユニコム (UNICOM Inc.), 2014-04-25 初版. ISBN 978-4-89689-494-3.
- Same series as the N1 book, but **the N4 volume is mainly a grammar book.** About 60% of it is 文法 (one grammar point per two-page spread). The 文章の文法・読解 section (the part that is like the N1 book) is only printed p.229–265. The site files it under Reading because that is the book's own title (読む).
- Explanations are in Japanese with furigana. **Every example sentence and every answer sentence has an English translation in the book.** We keep the book's English, and we add Hindi and Gujarati.
- No audio.

## 1. The scan

- **153 PDF pages.** PDF 1 = front cover (one page). PDF 153 = back cover (one page). **PDF 2–152 are two-page spreads**: each PDF page shows a left (even) and a right (odd) printed page.
- **The text layer is garbage** (Cyrillic junk). Never use `get_text()`. Always render: `import pymupdf; doc[i-1].get_pixmap(dpi=130)`. Contact sheets at 28 dpi are good for finding structure. 130–140 dpi reads the kana and furigana. Use 200 dpi crops for the small `答え：` lines at the bottom of the reading pages.
- The scan is clean and complete: no missing pages, no watermark. Some pages are a little faint (light cyan design); 130 dpi is enough.
- Blank pages: printed p.40 (PDF 21 left), p.228 (PDF 115 left), p.266 (PDF 134 left).

## 2. Page offset (verified on rendered page numbers)

**PDF page n shows printed pages 2n−2 (left) and 2n−1 (right).**
**Printed page p is on PDF floor(p/2) + 1.**

Verified on: PDF 2 → 2/3, 5 → 8/9, 7 → 12/13, 8 → 14/15, 10 → 18/19, 11 → 20/21, 12 → 22/23, 22 → 42/43, 30 → 58/59, 46 → 90/91, 47 → 92/93, 86 → 170/171, 90 → 178/179, 94 → 186/187, 95 → 188/189, 114 → 226/227, 116 → 230/231, 119 → 236/237, 122 → 242/243, 125 → 248/249, 128 → 254/255, 131 → 260/261, 152 → 302/303 (colophon). Matches the 目次 (printed p.13–18, PDF 7–10).

Always cite pages as "p.N (PDF M)".

## 3. Book structure

Front matter: はじめに p.2, この本の特長 p.3, 構成と使い方 p.4–7, 文法用語 table (普通形) p.8, English FOREWORD p.9–12, 目次 p.13–18.

| Part | Printed pp | PDF | What is on a spread |
|---|---|---|---|
| **N5の復習 助詞100問** | 19–39 | 10–20 | Left: 10 sentences, each with （ ）: write ○ if the particles are right, × if one is wrong. Right: **解答例** — 正解 ○/×, the corrected sentence (with the wrong particle fixed), and an English translation. |
| **文法** (13 chapters) | 41–227 | 21–114 | Each grammar point = one spread. Left: 問題 X-1 (choose one of two words in （1 … 2 …）, どちらでしょう), 例 (examples, the target in colour), 用法 (usage line, Japanese + English), a ▽ note box with rules, then 問題 X-2 (a ★ sentence-building question, 4 parts). Right: **おぼえよう！正解文** — 正解 number for X-1 and X-2, the full correct sentences, and English for every 例. A chapter opens with a **[表]** spread: a conjugation table to fill in (left) and the filled table, 正解 (right). |
| 文法 練習問題 | 90–95; 170–187; 222–227 | 46–48; 86–94; 112–114 | Left: questions; right: **解答** with 正解 number, full sentence and English. |
| **文章の文法・読解** | 229–265 | 115–133 | Same plan as the N1 book: passage + questions, `答え：` line at the bottom right of the question page, then ◆ふりがな付き正解文 (文章の文法 only) / ◆こたえるためのかいせつ (○/× reason per option, Japanese + English) / ◆よむためのかいせつ たいせつなたんご (word, reading, English) / ◆おぼえましょう (expression = easier paraphrase, sometimes 例). |
| 文字・語彙 便利帳 | 267–302 | 134–152 | Reference lists: 普通形・て形の作り方 p.268–269, おぼえたい動詞 p.270–277, 動詞活用表 p.278–283, おぼえたい漢字語彙 (example sentences) p.284–295, おぼえたい漢字語彙リスト p.296–302. **Not built as units** (long word lists with no questions; they would be a copy of the book). Mention them in the hub prose only. |

The 13 文法 chapters (from the 目次): 復習しよう！ · 形容詞 · 可能形 · 授受動詞 · 意志形 · 命令形・禁止形 · (練習問題) · 動詞て形 · 〜そう · 条件形 · 受身形 · 使役形・使役受身形 · 尊敬表現・謙譲表現 · (練習問題) · どう ちがう？ · (練習問題).

## 4. Answer key

**Complete and inside the book. There is no 別冊.** Every question has its answer on the facing right-hand page or in an answer line:
- 助詞100問: 解答例 on the right page of each spread (○/× + corrected sentence + English).
- 文法 points: おぼえよう！正解文, right page (正解 number + sentence + English).
- 練習問題: 解答, right page.
- 文章の文法・読解: `答え：` line at the bottom right of the question page, plus ◆こたえるためのかいせつ explaining every option with ○/×.

Answer lines read so far (200 dpi crops):

| Unit | 答え line | Page |
|---|---|---|
| bunshou-01 | 1-2、2-3、3-2、4-4、5-1 | p.231 (PDF 116) |
| bunshou-02 | 1-3、2-4、3-1、4-4、5-2 | p.237 (PDF 119) |
| naiyou-01 | 1-3、2-4、3-2 | p.243 (PDF 122) |
| naiyou-02 | 1-3、2-4、3-1、4-2 | p.249 (PDF 125) |
| kensaku-01 | 1-1、2-4 | p.254 (PDF 128) |
| kensaku-02 | 1-3、2-1 | p.260 (PDF 131) |

The book explains **why** only in the reading section (こたえるためのかいせつ) and in the grammar notes (用法, ▽ box). It gives **no reasons** for the 助詞100問 or the 練習問題. Our "Why" notes there are ours: mark them "(our explanation, not in book)". Never change a book answer. If one looks doubtful, keep the book's answer and add a note.

## 5. Unit table

Units follow the book's own blocks and never split a grammar point or a passage. 30 units.

**A. N5の復習 — 助詞100問** (10 items per spread; 20 items per unit)

| File | Title (chip) | Romaji / English | Printed pp | PDF | Answers |
|---|---|---|---|---|---|
| joshi-01.html | 助詞100問 1–20 | Joshi hyaku-mon — particle check, Q1–20 | 20–23 | 11–12 | 解答例 p.21, 23 (PDF 11–12) |
| joshi-02.html | 助詞100問 21–40 | Q21–40 | 24–27 | 13–14 | 解答例 p.25, 27 |
| joshi-03.html | 助詞100問 41–60 | Q41–60 | 28–31 | 15–16 | 解答例 p.29, 31 |
| joshi-04.html | 助詞100問 61–80 | Q61–80 | 32–35 | 17–18 | 解答例 p.33, 35 |
| joshi-05.html | 助詞100問 81–100 | Q81–100 | 36–39 | 19–20 | 解答例 p.37, 39 |

**B. 文法 — grammar chapters** (one spread per point; answers on each right page)

| File | Title (chip) | Romaji / English | Points | Printed pp | PDF |
|---|---|---|---|---|---|
| bunpou-01.html | 復習しよう！① こ/そ/あ・の・のが | Fukushuu shiyou — review 1 | こ/そ/あ, の, 〜のが①, 〜のが② | 42–49 | 22–25 |
| bunpou-02.html | 復習しよう！② のは・のを・とき | Fukushuu shiyou — review 2 | 〜のは①, 〜のは②, 〜のを, 〜とき | 50–57 | 26–29 |
| bunpou-03.html | 形容詞 | Keiyoushi — adjectives | [表], 〜ほうが（〜より）, 〜がいちばん, 〜く/〜に, 〜さ, 〜がる | 58–69 | 30–35 |
| bunpou-04.html | 可能形・授受動詞 | Kanoukei, juju doushi — potential form; giving and receiving | 可能形[表], (ら)れる; あげます/〜てあげます, もらいます/〜てもらいます, くれます/〜てくれます | 70–79 | 36–40 |
| bunpou-05.html | 意志形・命令形・禁止形 | Ishikei, meireikei, kinshikei — volitional, imperative, prohibitive | 意志形[表], 〜う/〜よう, 〜う/〜ようと思っている; 命令形・禁止形[表], 命令形・禁止形 | 80–89 | 41–45 |
| bunpou-06.html | 動詞て形 | Doushi te-kei — te-form patterns | 〜てある, 〜ている①②, 「て形+いる」いろいろ, 〜てみる, 〜ておく, 〜てしまう | 96–109 | 49–55 |
| bunpou-07.html | 〜そう | ~sou — looks like / I hear | [表], 〜そう①, 〜そう② | 110–115 | 56–58 |
| bunpou-08.html | 条件形① と・ば | Joukenkei — conditionals と, ば | 〜と[表], 〜と, 〜ば[表], 〜ば, 〜ば〜ほど | 116–125 | 59–63 |
| bunpou-09.html | 条件形② たら・なら | Joukenkei — conditionals たら, なら | 〜たら[表], 〜たら, 〜なら(ば)[表], 〜なら(ば) | 126–133 | 64–67 |
| bunpou-10.html | 受身形 | Ukemikei — passive | [表], 〜(ら)れる①–⑤ | 134–145 | 68–73 |
| bunpou-11.html | 使役形・使役受身形 | Shiekikei, shieki-ukemikei — causative, causative-passive | 使役形[表], 〜(さ)せる①–③, 使役受身形[表], 〜される/〜させられる | 146–157 | 74–79 |
| bunpou-12.html | 尊敬表現・謙譲表現 | Sonkei / kenjou hyougen — honorific and humble | 尊敬①[表], とくべつな形/お〜になる, 尊敬②[表], 〜(ら)れる, 謙譲[表], とくべつな形/お〜する | 158–169 | 80–85 |

**C. どう ちがう？ — similar expressions**

| File | Title (chip) | Romaji / English | Points | Printed pp | PDF |
|---|---|---|---|---|---|
| chigau-01.html | どうちがう？① 見える・聞こえる・てほしい・しか | Dou chigau — what's the difference 1 | 見える・見る・見られる; 聞こえる・聞く・聞ける; 〜たい・〜てほしい; 〜しか〜ない・〜だけ | 188–199 | 95–100 |
| chigau-02.html | どうちがう？② のに・ために・ように | 2 | 〜のに・〜ために・〜ように; 〜ようになる・〜ようにしている | 200–209 | 101–105 |
| chigau-03.html | どうちがう？③ はず・なくて・ばかり | 3 | 〜かもしれない・〜はず; 〜ないで・〜なくて; 〜たばかり・〜てばかり | 210–221 | 106–111 |

**D. 練習問題 — review questions** (answers on each right page, 解答)

| File | Title (chip) | Content | Printed pp | PDF |
|---|---|---|---|---|
| renshuu-01.html | 練習問題 自動詞・他動詞 | 43 pairs: write the transitive verb for 〜が+自動詞 (grouped by ending type in the 解答) | 90–95 | 46–48 |
| renshuu-02.html | 練習問題 1–25 | 4-option grammar questions mixing all the 文法 chapters (passive, ている, comparison, causative-passive, …) | 170–179 | 86–90 |
| renshuu-03.html | 練習問題 26–44 | same | 180–187 | 91–94 |
| renshuu-04.html | 練習問題（どうちがう？）1–17 | 4-option questions on the どうちがう points | 222–227 | 112–114 |

**E. 文章の文法・読解** (model: the N1 book's units)

| File | Title (chip) | Content | Printed pp | PDF | Answer line |
|---|---|---|---|---|---|
| bunshou-01.html | 文章の文法 ① | cloze, 5 blanks (kanji story 迷う) | 230–235 | 116–118 | p.231 |
| bunshou-02.html | 文章の文法 ② | cloze, 5 blanks | 236–241 | 119–121 | p.237 |
| naiyou-01.html | 内容理解 ① | one passage, 3 questions | 242–247 | 122–124 | p.243 |
| naiyou-02.html | 内容理解 ② | one passage, 4 questions | 248–253 | 125–127 | p.249 |
| kensaku-01.html | 情報検索 ① | sale notice, 2 questions | 254–259 | 128–130 | p.254 |
| kensaku-02.html | 情報検索 ② | campaign notice + two postcards, 2 questions | 260–265 | 131–133 | p.260 |

Hub order = book order: A, B (with renshuu-01 after bunpou-05, renshuu-02/03 after bunpou-12), C, renshuu-04, E. `.day-nav` prev/next follow the same order.

## 6. Site page format

Chrome: copy `n4/reading/jitsuryoku-appu/joshi-01.html` (paths `../../../`, `body class="level-page n4"`, n4 level-nav with Reading active, breadcrumb Home / JLPT N4 / Reading / 実力アップ！ N4 読む / unit). Reuse only classes from `assets/css/style.css` and `day-page.css`.

- **Header (`.bp-header`)**: `.bp-week` = "JLPT N4 · Reading · 実力アップ！ N4 読む — <part>" with romaji; `h1` = chip title + romaji/English; Source (book, part, printed + PDF pages, question numbers); Skill/points chips (`.bp-points`); **Answer key** box (where the answers are, with pages; list the answers); Notes (`.bp-note`) saying what is the book's and what is ours.
- **§1 Points** (`.bp-point`, `.bp-table`):
  - A (助詞): the particles tested in this set as a table (particle / use / EN / HI / GU / Q). The book gives no particle notes, so the table is "(added, not in book)".
  - B/C (文法, どうちがう): one `.bp-point` per grammar point: 用法 line (book's Japanese + its English) + HI/GU; the ▽ rules paraphrased; the 例 sentences with romaji and the book's English + HI/GU; the [表] tables in full (they are conjugation tables, short).
  - D: a short "what this set tests" table (ours).
  - E: `.rd-strategy` with the instruction (quoted) + 構成と使い方 p.6 paraphrased + tips "(added, not in book)"; then tables for たいせつなたんご and おぼえましょう (expression / ＝ paraphrase / 例).
- **§2 Exercise** (`.bp-quiz` per question): instruction line (Japanese + romaji + EN/HI/GU); each question sentence with romaji + EN/HI/GU (use the book's English where it has one); options in `.bp-options` with the correct row `class="correct"`; for ○/× items a two-row table (○ / ×) plus the book's corrected sentence; `.bp-why` citing the answer page. For E: first a `.bp-quiz` "Passage summary (not the book's text)" in our own words, then per question only the sentence(s) the かいせつ quotes; `.bp-why` paraphrases the book's ○/× reasons.
- **§3 Confusion Pairs / Nuance Notes**: `.bp-confusion` table + `.bp-callout` exam trap. Ours unless taken from a どうちがう page.
- `.bp-day-nav`: prev / next in hub order (first unit's prev = index.html, last unit's next = index.html).

## 7. Hard rules

- `<span class="romaji">` under every Japanese line (sentences, options, table cells).
- EN + Hindi + Gujarati for every meaning, example and question sentence. Keep the book's English when it has one; Hindi and Gujarati are ours.
- Give every question with the book's answer and the page it is on. All answers are in the book (§4). If a reason is ours, say "(our explanation, not in book)".
- **No long passages.** Never transcribe a reading passage (文章の文法, 内容理解) or a whole notice (情報検索) — not in pages, scratch files or messages. Summarise in your own words; quote only the sentence with the blank or underline and the clue sentence the かいせつ quotes. For 情報検索, give only the facts the question needs (dates, prices, conditions) in a short list.
- The short drill sentences (助詞100問, 問題 X-1/X-2, 練習問題) and the 例 sentences may be quoted: each is one line.
- Do not reproduce the 便利帳 word lists.
- Never publish or link audio (the book has none anyway). No emoji glyphs in body text.
- Never invent questions or answers. Mark illegible text as illegible.
- After building a unit: change its hub chip from `<span class="day-chip soon" data-href="X">` to `<a class="day-chip ready" href="X">` and update the `.sample-note` count "In progress — N of 30 units built".
