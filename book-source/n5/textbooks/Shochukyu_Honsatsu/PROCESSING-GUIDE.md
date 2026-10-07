# できる日本語 初中級 本冊 (Shochukyu Honsatsu): lesson-by-lesson processing guide

Standing instructions for turning `初中級 本冊.pdf` into the site's lesson pages at `n5/textbooks/shochukyu-honsatsu/lesson-NN.html`. Ask for "lesson N" and follow this guide. The finished example is **`n5/textbooks/shochukyu-honsatsu/lesson-01.html`**. Copy its structure.

---

## 1. Book identification

| Field | Value |
|---|---|
| Title | できる日本語 初中級 本冊 (Dekiru Nihongo, Pre-intermediate, main textbook) |
| Series | できる日本語 (初級 → **初中級** → 中級). This is the middle book. |
| Supervisor / authors | 監修 嶋田和子 (Shimada Kazuko, アクラス日本語教育研究所); 著 できる日本語教材開発プロジェクト |
| Publisher | 株式会社アルク (ALC PRESS INC.), first edition 2012, this copy is the 2015 5th printing |
| Level | The book's own table (p.2) puts it at OPI 中級-中, about 200 class hours after 初級. In JLPT terms that is about **N4 to N3**. The site lists it under N5 › Textbooks only because of where it sits in `book-source/`. Say "N4–N3 level material" in page text and do not call it N5 content. |
| Approach | Can-do based. Every lesson has a "できること" goal written in JP/EN/CN/KR. The book teaches through situations (illustrated scenes), not grammar chapters. |
| Audio | The book came with a CD (CD A: lessons 1–5, CD B: 6–10, CD C: 11–15). The CD is **not** in `book-source/`. Pages cite track numbers (e.g. "CD A-01") so readers can play their own copy. Never publish audio. |

## 2. Scan notes

- 252 PDF pages and a single file. **The text layer is useless** (garbled Shift-JIS). Render pages with PyMuPDF (`import pymupdf`) at 100–130 dpi and read them as images. A contact sheet at 45 dpi (6 pages per sheet) is enough to find section boundaries.
- **PDF page = printed page (offset 0)** across the whole book. Checked at p.5, 15, 28, 43, 119, 201, 214 and 245.
- Front matter: p.1 cover, p.2–3 本書をお使いになる方へ, p.4–5 目次, p.6–12 本書の構成 / 各課の構成と授業の流れ, p.13 凡例 (symbols), p.14 登場人物 (cast).
- Back matter (巻末資料, divider p.213): **p.214–227 ポイント一覧** (the list of all 121 grammar points, each with 1–4 model sentences), p.228–233 表 (verb-form tables, 普通形 patterns, 敬語 table, 友達言葉 casual-speech table, 自動詞・他動詞 pairs), p.234–241 索引 (word index giving lesson-topic for every ことば entry), p.242–245 シラバス一覧 (syllabus, printed sideways), p.246 colophon, p.247–252 blank.
- **Not in the scan:** the 別冊 (言ってみよう別冊, the mechanical pattern-drill booklet) and the CD PDF data (scripts for チャレンジ・やってみよう and 答え例). The 目次 note says: 「スクリプトと答え例は、付属CDのPDFデータに収められています。」

## 3. Answer-key status

- **No exercise answers are printed in this book.** Answer examples (答え例) were on the CD-ROM, which we do not have.
- The one script that **is** printed is もう一度聞こう (last page of each lesson). It is the transcript of the lesson's opening 聞いてみよう. Use it only to summarise. Never transcribe it.
- 言ってみよう drills are substitution drills: a model dialogue (例) plus picture or text cues ①②③…. The cue wording is often printed. Give the substituted key sentence for each cue, labelled **"(our answer, not in book)"**. When a cue is only a picture, say what the picture shows and mark the answer as one natural possibility.
- やってみよう listening tasks need the CD. Never invent their answers. Say "Audio task. The script and answers are on the CD data, which is not in this scan." Then describe the task and give a model for the role-play / pair-talk part, labelled "(our model, not in book)".
- 😊 marked drills and （　） personal-answer slots are free answers: give one model answer, labelled as ours.

## 4. Lesson table (unit = one 課)

15 lessons. Each lesson = 2 スモールトピック (small topics). ポイント numbers come from the ポイント一覧 (p.214–227).

| File | 課 | Title (romaji · English) | Small topics | ポイント | Printed pages | PDF pages |
|---|---|---|---|---|---|---|
| lesson-01.html | 第1課 | 新しい一歩 (Atarashii ippo · A new step) | ① アルバイトを探す ② 新しい友達 | 1–9 | 15–28 | 15–28 |
| lesson-02.html | 第2課 | 楽しいショッピング (Tanoshii shoppingu · Fun shopping) | ① 上手に買い物 ② 一緒に食事 | 10–21 | 29–42 | 29–42 |
| lesson-03.html | 第3課 | 私の目標 (Watashi no mokuhyou · My goals) | ① これからの計画 ② 夢に向かって | 22–29 | 43–54 | 43–54 |
| lesson-04.html | 第4課 | 住んでいる町で (Sunde iru machi de · In the town where I live) | ① 生活を楽しむ ② 行き方を教える | 30–36 | 55–66 | 55–66 |
| lesson-05.html | 第5課 | 大変な1日 (Taihen na ichinichi · A rough day) | ① 困ったな…… ② 駅で | 37–42 | 67–78 | 67–78 |
| lesson-06.html | 第6課 | 旅行に行こう (Ryokou ni ikou · Let's go on a trip) | ① 旅行の計画 ② 旅行の準備 | 43–49 | 79–90 | 79–90 |
| lesson-07.html | 第7課 | 西川さんの家へ (Nishikawa-san no ie e · Visiting the Nishikawas) | ① 初めての訪問 ② 一緒に作りましょう | 50–56 | 91–102 | 91–102 |
| lesson-08.html | 第8課 | ありがとう (Arigatou · Thank you) | ① うれしい出来事 ② お世話になりました | 57–63 | 103–118 | 103–118 |
| lesson-09.html | 第9課 | アルバイト先で (Arubaito-saki de · At my part-time job) | ① アルバイト先のルール ② 楽しいアルバイト | 64–73 | 119–134 | 119–134 |
| lesson-10.html | 第10課 | 旅行に行って (Ryokou ni itte · After the trip) | ① ハプニング！ ② ガイドブックを片手に | 74–82 | 135–150 | 135–150 |
| lesson-11.html | 第11課 | 地域社会の中で (Chiiki shakai no naka de · In the local community) | ① 慣れてくると ② スポーツチームに入って | 83–89 | 151–162 | 151–162 |
| lesson-12.html | 第12課 | 私の健康法 (Watashi no kenkouhou · How I stay healthy) | ① 体調不良 ② 毎日、元気に！ | 90–100 | 163–176 | 163–176 |
| lesson-13.html | 第13課 | 親の気持ち・子の気持ち (Oya no kimochi, ko no kimochi · Parents' feelings, children's feelings) | ① 町で見かけた子どもたち ② 思い出すと | 101–106 | 177–188 | 177–188 |
| lesson-14.html | 第14課 | イベント・行事 (Ibento, gyouji · Events and festivals) | ① 私の国の行事 ② 贈り物の習慣 | 107–114 | 189–200 | 189–200 |
| lesson-15.html | 第15課 | 気になるニュース (Ki ni naru nyuusu · News that catches my interest) | ① 発表の準備 ② みんなの前で発表 | 115–121 | 201–212 | 201–212 |

Lessons 8, 9 and 10 are 16 pages long because their やってみよう sections run longer. The section order is the same.

## 5. What every lesson contains (book order)

1. **Title page**: 話してみよう (photos and pictures for warm-up talk) and 聞いてみよう (an opening listening, CD track `x-01`, `x-16` and so on).
2. **Small topic 1** (`□1 title`):
   - **チャレンジ！**: a big scene illustration with a one-line situation in JP/EN/CN/KR, numbered cue panels [1]–[6], the topic's can-do line, and 「☞ ポイント n, n…」 (which grammar points it uses).
   - **言ってみよう**: numbered substitution drills [1], [2]… Each has a 例) model dialogue with underlined slots, then cues ①②③④. 💬 marks a line where learners swap in their own content. 😊 marks a free-answer drill.
   - **やってみよう**: a CD listening task (fill-in table or match a–f) plus a ロールプレイ (A/B role cards). Often comes with realia such as flyers or menus.
3. **Small topic 2**: same three parts.
4. **できる！**: a real-world task list for the lesson, sometimes with a 教室でできる！ classroom version.
5. **話読聞書**: a short reading text of 5–8 lines, usually written in the first person (self-introduction, a story, a speech), with question bubbles beside it. CD track given.
6. **ことば**: the vocabulary list, split by small topic. It gives kanji with furigana only and **no meanings**. Verbs are tagged with their group number (1/2/3). Example phrases sometimes appear under a word in small type.
7. **もう一度聞こう**: the transcript of 聞いてみよう, with 2–3 scenes. Footnote words at the bottom are extra vocabulary.

Grammar is **not** explained inside the lesson. Find it through the 「☞ ポイント」 references and read the matching entries in ポイント一覧 (p.214+). Look at both places every time.

## 6. Page layout for `lesson-NN.html`

Chrome: copy the `<head>`, header, level-nav and footer from `n5/textbooks/shochukyu-honsatsu/index.html` (same folder depth, so the same `../../../` paths). `<body class="level-page n5">`. Load `style.css` and `day-page.css`. Breadcrumb: Home / JLPT N5 / Textbooks / 初中級 本冊 / Lesson N. The `<title>` is `N5 Textbook · 初中級 本冊 · Lesson N · <課 title>`.

Sections, in this order (headings use `.bp-section-title` with `<span class="n">`):

0. **`.bp-header`**: `.bp-week` reads "JLPT N5 · Textbooks · できる日本語 初中級 本冊 · 第N課" and the `h1` is the 課 title with romaji. The `.bp-meta-grid` has **Source** (printed p.X–Y = PDF p.X–Y, plus the ポイント一覧 page), **Small topics** (`.bp-points` spans), **Answer key** (the status from §3), **Audio** (CD tracks, not published), and **Notes**.
1. **Lesson goals**: a `.rd-strategy` box with each small topic's can-do line in JP + romaji + EN/HI/GU.
2. **Warm-up and opening listening**: what the 話してみよう pictures show, then a **summary** of 聞いてみよう (taken from もう一度聞こう) in EN/HI/GU. Quote at most 2–3 key lines with romaji. Do not copy the transcript.
3. **Vocabulary (ことば)**: `.vd-table-wrap > table.vd-wordlist` with columns Japanese (+ `<span class="romaji">`) / English / Hindi / Gujarati / Note. Use one `<h3>` per small topic, plus "Extra words" for the もう一度聞こう footnote words. Keep the book's word order. The Note column holds the verb group (Group 1/2/3), (な) for な-adjectives, keigo type, and the book's example phrase if one is printed. Every word goes in. The meanings are ours because the book prints none.
4. **Grammar points (ポイント)**: one `.bp-point` per ポイント number. The head is `【n】 pattern`, with a badge saying which small topic uses it. Then a `.bp-table` (Reading, Meaning EN/HI/GU, Connection 接続, Use), a `.bp-formation-table` (word type / formation / example + romaji; mark anything we add as `class="added"` and "(added, not in book)"), and a `.bp-examples-table` with **every** model sentence from ポイント一覧 for that number plus the 例) line from the drill that uses it, each with romaji and EN/HI/GU. Finish with `.bp-notes`.
5. **Small topic 1 practice**: a short summary of the チャレンジ！ scene in EN/HI/GU, without the book's wording. Then each 言ってみよう drill as a `.bp-quiz`: `.q-label` like "言1", the 例) model key line in `.q-jp` with romaji, `.q-translations` (EN/HI/GU), and a `.bp-table` of cue → our answer sentence (JP + romaji + EN). Label it "(our answer, not in book)". Then やってみよう, following §3.
6. **Small topic 2 practice**: same as section 5.
7. **できる！ and 話読聞書**: できる！ tasks listed in EN/HI/GU. For 話読聞書, give a summary in EN/HI/GU (inside `.q-translations`), quote no more than 2 key sentences with romaji, then answer the bubble questions (our answers, taken from the text).
8. **Confusion pairs / nuance notes**: a `.bp-confusion` table for the lesson's easy-to-mix forms (for example humble vs honorific verbs, のが vs のは, なら vs だったら) and a `.bp-callout` with one usage trap.
9. **`.bp-day-nav`**: link to the contents page on one side and the next lesson on the other (or "(not built yet)").

## 7. Contents page

`n5/textbooks/shochukyu-honsatsu/index.html` is hand-built. `tools/build_site.py` leaves alone any course index that contains `class="day-chip`. Mark built lessons `<a class="day-chip ready" href="lesson-NN.html">`. Mark unbuilt lessons `<span class="day-chip soon" data-href="lesson-NN.html">`. When you build a lesson, flip its chip, update the `.sample-note` count ("In progress — K of 15 units built"), and run `python tools/build_site.py`. When no `soon` chip is left, the build marks the book as ready.

## 8. Hard rules

- **Romaji with every piece of Japanese**: words, sentences, pattern names and headings (site-wide rule).
- EN + HI + GU for every meaning, example sentence and summary.
- **Never transcribe** the 聞いてみよう / もう一度聞こう scripts or the 話読聞書 texts. Summarise them, and quote only the key lines a point needs.
- **Never invent answers to CD tasks.** Mark every answer the book does not print as "(our answer, not in book)" or "(our model, not in book)".
- Every word on the ことば list goes into the vocabulary table, in book order.
- Every ポイント example sentence on ポイント一覧 for the lesson's point numbers gets a translation.
- Do not describe this book as JLPT N5 content. It is pre-intermediate (about N4–N3).
- Do not publish audio, images or scans from the book.
- Do not edit other books, shared CSS or JS. Use only existing `day-page.css` / `style.css` classes.
