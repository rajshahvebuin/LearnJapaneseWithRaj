# 新完全マスター聴解 日本語能力試験N1 — processing guide

Standing instructions for turning **新完全マスター聴解 日本語能力試験N1** (Shin Kanzen Master N1 Choukai; 中村かおり・福島佐知・友松悦子, スリーエーネットワーク, 2011) into the site's unit pages under `n1/listening/shin-kanzen-master/`. Give a unit filename from the table below and this is the process to follow.

Inherit everything in the module spec `book-source/n1/listening/PROCESSING-GUIDE.md` (classes, header block, language rules, §3 confusion section) **except its delivery style**: this book uses the **summary-plus-key-line layout** of `n1/multi-skill/drill-and-drill/l-kadai-01.html` and `n1/multi-skill/pattern-betsu-tettei-drill/choukai-kadai-2.html`, NOT the full-script layout of `n1/listening/chapter-*/` pages.

**Reference implementation:** `n1/listening/shin-kanzen-master/mondai-shoukai.html` (問題紹介 例題1–6), built 2026-10-02.

## 1. Files

| File | What |
|---|---|
| `Shin_Kanzen_Master_N1_Choukai.pdf` | main book, 100 PDF pages, scanned (no text layer) |
| `Shin_Kanzen_Master_N1_Choukai_Answers.pdf` | 別冊 解答とスクリプト, 46 PDF pages, scanned |
| `Kanzen_Master_N1_Choukai_CD/CD1/01–76.mp3` | the book's CD **A** (76 tracks) |
| `Kanzen_Master_N1_Choukai_CD/CD2/01–73.mp3` | the book's CD **B** (73 tracks) |

Render pages with PyMuPDF (`import pymupdf`, 110–150 dpi) into your scratch folder only. The CD icons are small: use ≥120 dpi to read their numbers.

## 2. Offsets (verified on rendered pages)

- **Main book: printed page = PDF index − 8**, constant across the whole book. Checked: PDF 10 = p.2, PDF 22 = p.14, PDF 47 = p.39, PDF 61 = p.53, PDF 71 = p.63, PDF 85 = p.77, PDF 90 = p.82, PDF 97 = p.89. (PDF 0 cover, 1 title, 2 copyright, 3 はじめに, 4–5 目次, 6–8 本書をお使いになる方へ p.vi–viii, 9 問題紹介 divider = p.1, 21 実力養成編 divider = p.13, 89 模擬試験 divider = p.81, 98–99 ads/back cover.)
- **Answers 別冊: printed page = PDF index + 1** (PDF 0 is the 別冊 cover/TOC). Checked: PDF 1 = p.2, PDF 6 = p.7, PDF 11 = p.12, PDF 31 = p.32, PDF 45 = p.46. 別冊 TOC: I p.2 · II p.3 · III p.7 · IV p.12 · V p.18 · VI p.27 · 模擬試験 p.32.

## 3. Audio

- The book's CD icon shows disc letter + track (e.g. **A01**, **B33**). **CD A = folder CD1, CD B = folder CD2**, file number = track number (A07 → `CD1/07.mp3`). Verified: A ends at A76 (V-3 例題3 ②) and B runs B01–B73 (last = 模擬試験 問題5 3番), matching 76 + 73 = 149 files.
- On pages write the badge as `<span class="ld-track">CD1 · Track 07</span>` and mention once in the header that the book prints it as "A07".
- Several tracks are **instruction-only** (the 問題 intro of each mock section, and the 確認問題 heading icons in III/IV/V); say so instead of inventing content. 概要理解 two-step drills (V-2, V-3) replay the talk: ② "もう一度話を聞いて" uses the same track as ① plus a question track.
- **Audio is copyrighted and never published.** No `<audio>` elements, no copying of mp3s out of `book-source/`.

## 4. Unit definition

One unit = one numbered skill section of 実力養成編 (the section's 問題形式と内容 intro page goes into its first unit), or one 確認問題, or one 問題 of the 模擬試験. II-1 is split in two because it has five sub-skills (1-A … 1-E). 問題紹介 is one unit. **29 units.**

| # | File | Title | Printed pp | PDF pp | Answer key | Tracks |
|---|---|---|---|---|---|---|
| 1 | `mondai-shoukai.html` | 問題紹介 1–5 (例題1–6) | 1–12 | 9–20 | in main book: 答え on p.3, 5, 7, 9, 11, 12 | A01–A06 |
| 2 | `onsei-1.html` | I-1 似ている音の聞き分け | 14 | 22 | 別冊 p.2 (PDF 1) | A07 |
| 3 | `onsei-2.html` | I-2 音の変化や縮約形 | 15–16 | 23–24 | 別冊 p.2–3 (PDF 1–2) | A08–A09 |
| 4 | `sokuji-1abc.html` | II 問題形式と内容 + 1 最初の文を理解する 1-A〜1-C | 17–20 | 25–28 | 練習: 別冊 p.3–4 (PDF 2–3) | A10–A13 |
| 5 | `sokuji-1de.html` | II-1 1-D イントネーション · 1-E 会話でよく使われる表現 | 21–24 | 29–32 | 例題: main book p.22, 24; 練習: 別冊 p.5 (PDF 4) | A14–A18 |
| 6 | `sokuji-2.html` | II-2 返事の文を考える | 25–26 | 33–34 | 別冊 p.6 (PDF 5) | A19 |
| 7 | `sokuji-kakunin.html` | II 確認問題 | 26 | 34 | 別冊 p.6 (PDF 5) | A20 |
| 8 | `kadai-1.html` | III 問題形式と内容 + 1 するべきことを理解する | 27–30 | 35–38 | 例題: main book p.29, 30; 練習: 別冊 p.7–8 (PDF 6–7) | A21–A25 |
| 9 | `kadai-2.html` | III-2 優先される課題を判断する | 31–32 | 39–40 | 例題: main book p.32; 練習: 別冊 p.8–9 (PDF 7–8) | A26–A29 |
| 10 | `kadai-3.html` | III-3 条件を整理しながら聞く | 33–37 | 41–45 | 例題: main book p.34; 練習: 別冊 p.10–11 (PDF 9–10) | A30–A33 |
| 11 | `kadai-kakunin.html` | III 確認問題 | 38 | 46 | 別冊 p.11–12 (PDF 10–11) | A34–A36 |
| 12 | `point-1.html` | IV 問題形式と内容 + 1 話し手の意図を考えて、必要な情報かどうかを判断する | 39–42 | 47–50 | 例題: main book p.41, 42; 練習: 別冊 p.12–14 (PDF 11–13) | A37–A42 |
| 13 | `point-2.html` | IV-2 言い換えに注意する | 43–46 | 51–54 | 例題: main book p.44, 45; 練習: 別冊 p.14–15 (PDF 13–14) | A43–A50 |
| 14 | `point-3.html` | IV-3 多くの情報の中から必要な情報を拾う | 47–51 | 55–59 | 例題: main book p.48, 50; 練習: 別冊 p.16–17 (PDF 15–16) | A51–A55 |
| 15 | `point-kakunin.html` | IV 確認問題 | 52 | 60 | 別冊 p.17–18 (PDF 16–17) | A56–A58 |
| 16 | `gaiyou-1.html` | V 問題形式と内容 + 1 例と例をまとめる言葉を聞き分けて、話題をつかむ | 53–57 | 61–65 | 例題: main book p.55, 56; 練習 + ステップアップ1: 別冊 p.18–19 (PDF 17–18) | A59–A65 |
| 17 | `gaiyou-2.html` | V-2 キーワードを関連づけて、話の構造をつかむ | 58–62 | 66–70 | 例題: main book p.59; 練習 + SU2: 別冊 p.19–21 (PDF 18–20) | A66–A74 |
| 18 | `gaiyou-3.html` | V-3 文を関連づけて、話の主題をまとめる | 63–65 | 71–73 | 例題: main book p.64; 練習 + SU3: 別冊 p.22–23 (PDF 21–22) | A75–A76, B01–B07 |
| 19 | `gaiyou-4.html` | V-4 表現を手がかりに意見や主張を聞き取る | 66–67 | 74–75 | 例題: main book p.67; 練習 + SU4: 別冊 p.24–25 (PDF 23–24) | B08–B12 |
| 20 | `gaiyou-5.html` | V-5 表現を手がかりに意図を考える | 68–69 | 76–77 | 例題: main book p.69; 練習: 別冊 p.25–26 (PDF 24–25) | B13–B15 |
| 21 | `gaiyou-kakunin.html` | V 確認問題 | 70 | 78 | 別冊 p.26–27 (PDF 25–26) | B16–B18 |
| 22 | `tougou-1.html` | VI 問題形式と内容 + 1 2人以上の人の話を整理する | 71–76 | 79–84 | 例題: main book p.73–74; 練習: 別冊 p.27–29 (PDF 26–28) | B19–B24 |
| 23 | `tougou-2.html` | VI-2 2種類の話を整理する | 77–79 | 85–87 | 例題: main book p.78; 練習: 別冊 p.29–30 (PDF 28–29) | B25–B30 |
| 24 | `tougou-kakunin.html` | VI 確認問題 | 80 | 88 | 別冊 p.30–32 (PDF 29–31) | B31–B32 |
| 25 | `mogi-mondai-1.html` | 模擬試験 問題1 課題理解 (1–6番) | 82–83 | 90–91 | 別冊 p.32–35 (PDF 31–34) | B33 (intro), B34–B39 |
| 26 | `mogi-mondai-2.html` | 模擬試験 問題2 ポイント理解 (1–7番) | 84–85 | 92–93 | 別冊 p.35–38 (PDF 34–37) | B40 (intro), B41–B47 |
| 27 | `mogi-mondai-3.html` | 模擬試験 問題3 概要理解 (1–6番) | 86 | 94 | 別冊 p.38–41 (PDF 37–40) | B48 (intro), B49–B54 |
| 28 | `mogi-mondai-4.html` | 模擬試験 問題4 即時応答 (1–14番) | 87 | 95 | 別冊 p.41–44 (PDF 40–43) | B55 (intro), B56–B69 |
| 29 | `mogi-mondai-5.html` | 模擬試験 問題5 統合理解 (1–3番) | 88–89 | 96–97 | 別冊 p.44–46 (PDF 43–45) | B70 (intro), B71–B73 |

Answer-key page ranges inside the 別冊 are from a page-by-page scan of its headings; a unit's last 別冊 page may also hold the start of the next unit. The per-exercise track numbers above were read off the CD icons on every page; recheck the icon on the page you are building before writing the badge.

## 5. Answer-key status

**Complete.** Every 例題 has its 答え + スクリプト + explanation printed on the main-book page right after it (grey ◆スクリプト box + 答え). Every 練習, ステップアップ問題, 確認問題 and 模擬試験 item has its 答え + full スクリプト in the 別冊. Answers are always "(book key, p.X)"; any explanation beyond what the book's 答え paragraph says is marked `(added, not in book)`. Where the book gives only a number, the "Why" is ours.

## 6. How the book's sections map to page sections

- **Header (`bp-header`)**: unit title, source with printed + PDF pages, skills covered, where the answer key is (main book page / 別冊 page with PDF index), tracks, and the standing audio + no-transcript note.
- **§1 Points / Strategy**: the section's explanation (解説), 問題形式と内容 flow boxes, expression tables (e.g. II-1-E 表現 table, IV-1 同意・不同意 lists, V-4 一般論→主張 patterns) → `bp-point` / `rd-strategy` + `bp-table` with EN/HI/GU. These are the book's teaching text, not scripts: paraphrase the explanations, and quote the short expressions/example phrases they list. Add a key-vocabulary table drawn from the unit's options and scripts `(added, not in book)`.
- **§2 Every exercise** (`bp-quiz` per item, in book order: 例 → 例題 → 練習 → ステップアップ問題): `q-label` + `ld-track`; the printed instruction or the question line (setting + question, from the 答え/スクリプト page when it is spoken only); **Script summary (not the book's text)** in EN/HI/GU, 2–3 sentences, your own words; **The line the answer hinges on** — one short quoted line (two at most) + romaji + EN/HI/GU; options in `bp-options` (`tr.correct` for MCQ). For fill-in / ○× / table / diagram drills (III 練習, IV ○×, V 図), give the expected answer in a `bp-options`-style table instead of options. `bp-why` = "Answer N (book key, p.X)" + reasoning.
  - 即時応答 (II, 模擬 問題4): the "options" are spoken replies. Quote the prompt line as the key line, give the **correct reply** quoted, and the wrong replies as **gist only** (`（要旨）…`), following `pattern-betsu-tettei-drill/choukai-sokuji-1.html`.
  - 概要理解 / 統合理解 with spoken-only question + options: quote the question and the short options (they are 1-line items), as in `choukai-gaiyou-1.html`.
  - Big drills with 10+ one-line items (I 練習, II 練習1-A〜1-E): a single `bp-table` per drill (item # · what you hear, gist or the 2–6-word target phrase · answer · EN/HI/GU) is fine — never a line-by-line transcript.
- **§3 Confusion pairs** (`bp-confusion`): the traps in the wrong options, or the unit's own contrast set (sound pairs, contracted vs full forms, 同意/不同意 markers, 例 vs 例をまとめる言葉…), plus a `bp-callout` exam tip.
- **Nav (`bp-day-nav`)**: previous / next unit in the table order; the hub for the first unit's "previous".

## 7. Hard content rules (from the setup brief — do not relax)

- **Never transcribe listening scripts** — not in pages, scratch files, notes or messages. The book prints full scripts (main book for 例題, 別冊 for everything else); read them, then write a 2–3 sentence **Script summary (not the book's text)** in EN/HI/GU and quote only the line the answer hinges on. If a content filter ever blocks an output, leave that part out and report it.
- Tracks by **CD + track number only**, `ld-track` badge; never `<audio>`.
- Never invent questions or answers; mark missing/illegible scans as such (none found in this scan).
- EN + Hindi + Gujarati for every meaning, question and example; `<span class="romaji">` under every Japanese line; "(added, not in book)" for anything ours.

## 8. Hub

`n1/listening/shin-kanzen-master/index.html` groups the 29 chips into blocks: 問題紹介 · I 音声 · II 即時応答 · III 課題理解 · IV ポイント理解 · V 概要理解 · VI 統合理解 · 模擬試験. Built chip = `<a class="day-chip ready" href="FILE.html">`; unbuilt = `<span class="day-chip soon" data-href="FILE.html">`. Keep the `.sample-note` text `In progress — N of 29 units built` in step when you flip a chip.
