# N5 Textbook — できる日本語 初級 本冊 — lesson-by-lesson processing guide

Standing instructions for turning `初級 本冊.pdf` into the site's lesson pages at `n5/textbooks/shokyu-honsatsu/`. Give a lesson number (e.g. "Lesson 3") and this is the process to follow. This is the first **textbook** course on the site (not a JLPT drill book), so the unit and page layout below are designed for a beginner coursebook rather than a workbook.

---

## 1. Book identification

| Field | Value |
|---|---|
| Title | できる日本語 初級 本冊 (Dekiru Nihongo — Shokyuu, main textbook) |
| Publisher | 株式会社アルク (ALC Press Inc.), Tokyo |
| Supervisor / authors | 監修 嶋田和子 (アクラス日本語教育研究所); 著 できる日本語教材開発プロジェクト (澤田尚美・高見彩子・立原雅子・濱谷愛) |
| Edition in scan | 初版 2011-04-07, 第6刷 2015-08-06 (colophon, PDF p.303). ISBN 978-4-7574-1977-3 |
| Level | Beginner. Preface (p.2) maps 初級 to roughly JLPT N5–N4 / OPI 中級-上, 350 study hours. On this site it sits under N5 → Textbooks. |
| Series | できる日本語 初級 → 初中級 → 中級 (the other two are separate courses: `shochukyu-honsatsu`, `chukyu-honsatsu`) |

**Approach of the book:** can-do based. Each lesson (課) has a goal (行動目標), split into 3 スモールトピック, each with its own can-do statement. Grammar is not explained on the lesson pages — it is only flagged with "☞ ポイント N" in the bottom corner and listed with examples in the ポイント一覧 at the back.

## 2. Scan notes

- 308 PDF pages, 488.6 × 721.2 pt. **The text layer is garbled** (mojibake/replacement characters) — do not use `get_text()`. Render pages with PyMuPDF (`import pymupdf`) at 80–150 dpi and read them visually; zoom (200 dpi + clip) for small furigana or bold/plain distinctions.
- **Offset: none. PDF page = printed page** (verified: PDF 4 shows "4", PDF 29 shows "29", PDF 270 shows "270").
- Front matter: cover 1, 本書をお使いになる方へ 2–3, 目次 4–5, 本書の構成 6–7, 各課の構成と授業の流れ 8–12, 凡例 13, 登場人物 14.
- Back matter: 巻末資料 divider 269, **ポイント一覧 270–281**, 表 (活用表・数字・カレンダー・時間・年齢・助数詞・日週月年・自動詞他動詞・親族名称) 282–289, 索引 290–298, シラバス一覧 299–302, colophon 303, series page 304, blank/back cover 305–308.
- **Not in this PDF:** the separate 言ってみよう別冊 booklet, the CD audio, and the CD's PDF data.

## 3. Answer-key status

- **This volume prints no answers.** p.4 note: 「スクリプトと答え例は、付属CDのPDFデータに収められています」 and p.6 confirms the CD-ROM PDFs (1.pdf–15.pdf) hold the チャレンジ！ scripts, 言ってみよう答え例 and やってみよう scripts + answers. We do not have them.
- Consequences:
  - 言ってみよう (substitution drills): the cue pictures and 例 make the intended answer clear. Write the model answer and label it **"(our answer, not in book)"**.
  - やってみよう (CD listening tasks): the answer depends on audio we don't have. **Never invent an answer.** Show the task, the answer choices with translations, the track number (`.ld-track`), and say "Answer needs the CD audio; the book's answer is in the CD PDF, not this volume."
  - もう一度聞こう *is* printed (it is the script of the lesson-opening 聞いてみよう dialogue), so the opening dialogue can be summarised accurately.
- Audio: track numbers are printed (e.g. A-01, A-02–07). Audio is never published on the site (same policy as N1 listening); just name the track.

## 4. Unit = one lesson (課)

15 lessons, 16–20 printed pages each, but most pages are full-page illustrations, so one lesson fits one study page. File name `lesson-NN.html` (two digits).

| File | Lesson | Title | Printed = PDF pages | Small topics (start page) | ポイント |
|---|---|---|---|---|---|
| lesson-01.html | 第1課 | はじめまして | 15–30 | 私の名前・国・仕事 (16) · 私の誕生日 (20) · 私の趣味 (24) | 1–6 |
| lesson-02.html | 第2課 | 買い物・食事 | 31–46 | どこですか (32) · いくらですか (36) · レストラン (40) | 7–15 |
| lesson-03.html | 第3課 | スケジュール | 47–66 | 何時までですか (48) · 私のスケジュール (52) · どんな毎日？ (58) | 16–23 |
| lesson-04.html | 第4課 | 私の国・町 | 67–82 | どこ？ (68) · どんなところ？ (72) · 季節・料理 (76) | 24–36 |
| lesson-05.html | 第5課 | 休みの日 | 83–100 | 週末 (84) · 休みの後で (88) · 今度の休みに (94) | 37–47 |
| lesson-06.html | 第6課 | 一緒に！ | 101–116 | 一緒に行きませんか (102) · どちらがいいですか (106) · 約束 (110) | 48–60 |
| lesson-07.html | 第7課 | 友達の家で | 117–136 | 道がわかりません (118) · パーティーの準備 (122) · みんなで楽しいパーティー (128) | 61–71 |
| lesson-08.html | 第8課 | 大切な人 | 137–152 | 家族・友達 (138) · こんな人 (142) · プレゼント (146) | 72–80 |
| lesson-09.html | 第9課 | 好きなこと | 153–168 | いろいろな趣味 (154) · できること・できないこと (158) · 楽しい週末 (162) | 81–87 |
| lesson-10.html | 第10課 | バスツアー | 169–184 | 集合 (170) · いろいろな注意 (174) · 動物園で (178) | 88–97 |
| lesson-11.html | 第11課 | 私の生活 | 185–204 | 今の生活 (186) · 今の私・前の私 (192) · 友達と (196) | 98–103 |
| lesson-12.html | 第12課 | 病気・けが | 205–220 | 体の調子 (206) · アドバイス (210) · 病院で (214) | 104–107 |
| lesson-13.html | 第13課 | 私のおすすめ | 221–236 | 経験から (222) · おすすめします (226) · 教えてください (230) | 108–112 |
| lesson-14.html | 第14課 | 国の習慣 | 237–252 | 初めて見た！初めて聞いた！ (238) · ルール・マナー (242) · 私の意見 (246) | 113–118 |
| lesson-15.html | 第15課 | テレビ・雑誌から | 253–268 | これ、知ってる？ (254) · 雑誌を見て町へ (258) · 町を歩いて (262) | 119–124 |

Within every lesson the last three pages are: できる！ (+ 話読聞書 box), ことば, もう一度聞こう — e.g. L1 = 28, 29, 30; L2 = 44, 45, 46; L3 = 64, 65, 66. Verify per lesson; long lessons (L3, L7, L11) have 6-page small topics.

### Internal structure of one lesson (as printed)

1. Title page: 話してみよう (photo warm-up) + 聞いてみよう (CD, opening dialogue).
2. For each of 3 スモールトピック: **チャレンジ！** (2 illustrated pages; situation line in JA/EN/中/한 + numbered scenes; can-do statement in a box) → **言ってみよう** (model mini-dialogues with underlined substitution slots and cues 例 ① ②…) → **やってみよう** (CD listening task + a ■ class activity). Bottom right: "☞ ポイント n, n".
3. **できる！** — the lesson's final real-world task, plus a **話読聞書** box (short model text, e.g. a self-introduction).
4. **ことば** — new words per small topic, in the order noun, verb, adjective, adverb, conjunction, expression. **Bold = core words** (old JLPT 3/4級 or "should learn now"); plain = extra. Verbs carry group numbers 1–3.
5. **もう一度聞こう** — script of the opening 聞いてみよう dialogue.

## 5. Page layout for every lesson page

Path `n5/textbooks/shokyu-honsatsu/lesson-NN.html`, body class `level-page n5`, chrome + breadcrumb copied from the course `index.html` (same depth, `../../../`), stylesheets `style.css` + `day-page.css`. Reuse existing classes only: `.bp-header`, `.bp-meta-grid`, `.bp-note`, `.bp-points`, `.bp-section-title`, `.bp-point`, `.bp-point-head`, `.bp-badge`, `.bp-table(-wrap)`, `.bp-formation-table`, `.bp-examples-table`, `.bp-notes`, `.bp-quiz` (`.q-label`, `.q-jp`, `.q-translations`), `.bp-options` (+`tr.correct`), `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`, `.vd-legend`, `.vd-table-wrap`, `.vd-wordlist`, `.vd-warmup`, `.rd-strategy`, `.rd-passage-label`, `.ld-track`, `.added`. **Do not add CSS.**

- **Header (`.bp-header`)** — "JLPT N5 · Textbook · できる日本語 初級", h1 `第N課 — title (romaji)`. Meta: Source (book + printed/PDF pages), small topics as `.bp-points` chips, Answer key note (no answers in this volume), Notes (audio tracks not published; lesson can-do goal in EN).
- **Lesson map** — small table: section / pages / what it trains (can-do statements translated EN/HI/GU).
- **§1 Vocabulary (ことば)** — `.vd-legend` (★ = bold core word in the book) + one `.vd-wordlist` per small topic, as the book groups them. Columns: Japanese (+ romaji) / English / Hindi / Gujarati / Note. Every word from the ことば page, in book order. Extra helpful tables (e.g. irregular date readings) are allowed but headed "(added, not in book)".
- **§2 Sentence patterns (ポイント)** — one `.bp-point` per ポイント number of the lesson: field table (Pattern / Meaning EN/HI/GU / How it works / Used in small topic), a formation table (affirmative / negative / question, etc.; cells the book doesn't show go in `class="added"` with "(added, not in book)"), and an examples table with **every** example the book gives for that point (ポイント一覧 + the 言ってみよう model lines) in JA+romaji/EN/HI/GU. 2–4 sentences of beginner-friendly notes (assume the learner knows no grammar terms; explain particles plainly).
- **§3 Practice (言ってみよう / やってみよう)** — grouped by small topic. For each 言ってみよう item: the model exchange (short, it's a drill frame, OK to quote) with romaji and EN/HI/GU, then each cue ①②… as a `.bp-quiz` with the completed line and "(our answer, not in book)". For やってみよう: `.ld-track`, the task, the answer choices translated, and the no-answer notice from §3 above. Class activities (■) and できる！ get a one-line explanation of what to do + a model of our own.
- **§4 Dialogue (聞いてみよう / もう一度聞こう)** — `.rd-strategy` with a short summary in our own words, then a `.bp-examples-table` quoting only **3–5 key lines**, each translated. Never transcribe the whole dialogue. Same for the 話読聞書 model text: summary + at most 2 quoted sentences, then our own template.
- **§5 Confusion pairs** — `.bp-confusion` table for the lesson's beginner traps (particles, look-alike words, polite vs plain) + a `.bp-callout` for the biggest trap.
- **Nav** — `.bp-day-nav` with previous/next lesson (a `<span>` if that lesson isn't built yet).

## 6. Hard rules

- No long text transcription: dialogues and model texts are summarised; quote only key lines. Word lists and grammar examples are fine (short, needed for study).
- English + Hindi + Gujarati for every word, sentence, option and explanation-level meaning.
- **Romaji under every Japanese line** (`<span class="romaji">`), Hepburn with "ou/uu" for long vowels (koukou, gakusei, juuyokka) as elsewhere on the site.
- Beginner-friendly: short sentences, explain every particle and politeness choice, no grammar jargon without a plain gloss.
- Answers: only from the book when printed; otherwise "(our answer, not in book)". Listening answers that need audio are never guessed.
- After building a lesson: flip its chip on `n5/textbooks/shokyu-honsatsu/index.html` from `<span class="day-chip soon" data-href=…>` to `<a class="day-chip ready" href=…>`, update the "In progress — X of 15 units built" note, link the previous lesson's "next" nav, then run `python tools/build_site.py`.

---

**Reference implementation:** `n5/textbooks/shokyu-honsatsu/lesson-01.html` (第1課 はじめまして).
