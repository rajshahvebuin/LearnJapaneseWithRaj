# できる日本語 中級 本冊 (Dekiru Nihongo Chuukyuu Honsatsu) — lesson-by-lesson processing guide

Standing instructions for turning `中級 本冊.pdf` into the site's lesson pages under `n5/textbooks/chukyu-honsatsu/`. Give a lesson number (e.g. "Lesson 3") and this is the process to follow.

---

## 1. Book identification

| Field | Value |
|---|---|
| Title | できる日本語 中級 本冊 (Dekiru Nihongo — Intermediate, main textbook) |
| Series | できる日本語 (初級 → 初中級 → 中級). The sibling courses `shokyu-honsatsu` and `shochukyu-honsatsu` are the earlier books in the same series. |
| Publisher | アルク (ALC Press Inc.). The preface says the series was made with アルク and 凡人社 (Bonjinsha) together. |
| Supervisor / authors | 監修 嶋田和子 (アクラス日本語教育研究所); 著 できる日本語教材開発プロジェクト (teachers at イーストウエスト日本語学校) |
| Edition in scan | 2013-04-10 first edition, 2016-02-18 4th printing (colophon, PDF p.320) |
| Structure | 20 課 (lessons). Each lesson has 4–5 タスク (tasks) and builds to a can-do goal. |
| Audio | CD (tracks marked Ⓐ01, Ⓐ02 …). It is **not** in the repo and is never published. Pages give the track number only. |

### Level warning: this is NOT an N5 book

The book is filed under N5 → Textbooks only because the three できる日本語 volumes were uploaded together. The preface (printed p.2) says plainly: 「中級」では **N3レベル後半からN2レベル** の日本語能力の獲得を目指す. Its OPI target is 中級-上 〜 上級-下, about 6 months / 350 hours of study after 初中級. Treat the content as **late N3 to N2**. Every lesson page should say this in the header, so N5 learners know what they are opening.

---

## 2. Scan notes and offsets

- 324 PDF pages, scanned images. There is a text layer, but it is broken Shift-JIS mojibake (unreadable). **Ignore it. Render pages with PyMuPDF at 100–150 dpi and read them visually.** Use 250–300 dpi crops for the ことば lists, so you can tell bold from regular type.
- **Offset: PDF page = printed page** (offset 0). This was checked on p.3, 4, 13, 15, 26 and 278: the printed number on each page matches its PDF index (1-based).
- Front matter: p.1 cover · p.2–3 本書をお使いになる方へ (preface, with the level table) · p.4–5 目次 · p.6–12 各課の構成と授業の流れ (how a lesson works) · p.13 凡例 (symbols and connection-form notation) · p.14 登場人物 (characters).
- Back matter: p.277 巻末資料 divider · **p.278–289 解答とスクリプト** · p.290–310 索引 (index) · p.311–318 シラバス一覧 (syllabus table) · p.319 credits · p.320 colophon · p.321–324 blank.

---

## 3. Answer-key status

The book prints **解答とスクリプト on p.278–289**, ordered by lesson, with a 第N課 heading for each. It has:

- answers for the ● content questions under チャレンジ！ 見つけた！ / 耳でキャッチ and 知って楽しむ (e.g. 第1課: チャレンジ！1 p.17 Q1–4, チャレンジ！3 p.17 = c, 知って楽しむ p.25 Q1–2 + 種明かし);
- scripts for the audio that is *not* already printed in the lesson (e.g. 第2課 使ってみよう やってみよう 1 p.31, track Ⓐ05).

It does **not** answer:

- ■ questions (personal: 「〜したことがありますか」);
- こんなときどうする？ role-plays, 伝えてみよう, やってみよう and できる！ — these are open tasks.

For these, give a short model answer or model role-play and label it **(our answer, not in book)**. Book answers are labelled with the answer-key page, e.g. "Book answer (p.278)".

Every 使ってみよう model dialogue / monologue is printed in full in the lesson with its track number. It is the "sample" for the matching こんなときどうする？ / 伝えてみよう task, and often also the 耳でキャッチ script.

---

## 4. Lesson table

PDF page = printed page for every row.

| # | File | Title | Romaji | English | Pages |
|---|---|---|---|---|---|
| 1 | `lesson-01.html` | 新たな出会い | Arata na deai | New encounters | 15–26 |
| 2 | `lesson-02.html` | 楽しい食事・上手な買い物 | Tanoshii shokuji, jouzu na kaimono | Enjoyable meals, smart shopping | 27–38 |
| 3 | `lesson-03.html` | 時間を生かす | Jikan o ikasu | Making the most of time | 39–50 |
| 4 | `lesson-04.html` | 地域を知って生活する | Chiiki o shitte seikatsu suru | Living with knowledge of your area | 51–62 |
| 5 | `lesson-05.html` | 緊急事態！ | Kinkyuu jitai! | Emergency! | 63–74 |
| 6 | `lesson-06.html` | 地図を広げる | Chizu o hirogeru | Broadening your map | 75–86 |
| 7 | `lesson-07.html` | 世代を超えた交流 | Sedai o koeta kouryuu | Exchange across generations | 87–100 |
| 8 | `lesson-08.html` | 気持ちを伝える | Kimochi o tsutaeru | Conveying your feelings | 101–114 |
| 9 | `lesson-09.html` | 言葉を楽しむ | Kotoba o tanoshimu | Enjoying language | 115–128 |
| 10 | `lesson-10.html` | 日本を旅する | Nihon o tabi suru | Travelling in Japan | 129–142 |
| 11 | `lesson-11.html` | ライフスタイル | Raifusutairu | Lifestyles | 143–156 |
| 12 | `lesson-12.html` | 心と体の健康 | Kokoro to karada no kenkou | Health of mind and body | 157–170 |
| 13 | `lesson-13.html` | トレンドに乗ってつながる | Torendo ni notte tsunagaru | Connecting through trends | 171–182 |
| 14 | `lesson-14.html` | カルチャーショック | Karuchaa shokku | Culture shock | 183–194 |
| 15 | `lesson-15.html` | 情報社会に生きる | Jouhou shakai ni ikiru | Living in an information society | 195–206 |
| 16 | `lesson-16.html` | 学校生活 | Gakkou seikatsu | School life | 207–222 |
| 17 | `lesson-17.html` | 働くということ | Hataraku to iu koto | What it means to work | 223–234 |
| 18 | `lesson-18.html` | 地球に生きる | Chikyuu ni ikiru | Living on Earth | 235–246 |
| 19 | `lesson-19.html` | 科学の力 | Kagaku no chikara | The power of science | 247–260 |
| 20 | `lesson-20.html` | 豊かさと幸せ | Yutakasa to shiawase | Affluence and happiness | 261–276 |

Each lesson ends on the page before the next lesson's title page. Lesson 20 ends at p.276, because p.277 is the 巻末資料 divider. To find a lesson's answers, look for its 第N課 heading in p.278–289 (第1課 starts at p.278).

---

## 5. Inside a lesson (book layout)

All lessons follow the same order:

1. **Title page + 話してみよう**: lesson number, title, a warm-up picture with a discussion prompt.
2. **チャレンジ！**: a box listing the lesson's 4–5 can-do goals (numbered 1–5), then one task per goal. The tasks are of these types:
   - 見つけた！ (read a poster, flyer or notice, then ● questions and a ■ question);
   - こんなときどうする？ (A/B role-play cards);
   - 耳でキャッチ (listen to audio, then ● questions);
   - 伝えてみよう (speech or monologue task).
3. **使ってみよう やってみよう 1…N**: one block per task, with the same number as the task. Each block has:
   - a model dialogue or monologue (使ってみよう, with a CD track);
   - 3 numbered grammar/expression points (`1. 〜において [N+において]` with ①②③ examples);
   - one or two ≫ expression/word boxes;
   - a やってみよう real-world follow-up task.
4. **知って楽しむ**: a one- or two-page reading text with ● questions and a ■ question, and its own ことば list.
5. **できる！**: an end-of-lesson project (例) with numbered steps.
6. **ことば**: the new words for each task, grouped by task number. Words in **bold** are old-JLPT 2級-and-below words, or words worth learning at this stage (p.10).

Connection notation (p.13): V-マス形 = 読み, V-ナイ形 = 読ま, イA = 楽し, ナA = 元気, 普通形(ナAな/Nの) = an exception for な-adjectives and nouns.

---

## 6. Site page format: `n5/textbooks/chukyu-honsatsu/lesson-NN.html`

Use the chrome from `n5/index.html`, with paths 3 levels deep (`../../../`). The level-nav has **Textbooks** active. Load `style.css` + `day-page.css`. Body class is `level-page n5`. The breadcrumb is Home / JLPT N5 / Textbooks / 中級 本冊 / 第N課. Reuse existing classes only. **Do not edit CSS or JS.**

Sections, in this order:

0. **`.bp-header`**:
   - lesson number + title + romaji;
   - Source (printed and PDF pages; they are the same);
   - the can-do goals as `.bp-points` chips;
   - Answer key (which answer-key page covers the lesson);
   - Notes. These always include the **level warning** (late N3–N2 content, not N5) and "CD tracks Ⓐxx–Ⓐyy are not published".
1. **Lesson goals**: the チャレンジ！ can-do list, translated EN/HI/GU, plus the 話してみよう warm-up prompt.
2. **Tasks (チャレンジ！)**: one `.bp-quiz` per task.
   - Summarise the reading or listening material in EN/HI/GU. Quote only the key lines, each with romaji.
   - Give every ● question with its book answer (cite the page).
   - Give every ■ question, the role-play, and 伝えてみよう with **(our answer, not in book)** models.
3. **Grammar and expressions**: one `.bp-point` per numbered point, with:
   - a field table (Reading, Meaning EN/HI/GU, Connection 接続 exactly as the book prints it, Typical use);
   - a formation table. Anything not in the book is marked `class="added"` "(added, not in book)";
   - an examples table with **every** book example in Japanese + romaji, EN, HI, GU;
   - short notes.
   
   Before each task's points, put the 使ってみよう model text as a `.rd-strategy`-style summary: who speaks, what happens, key lines quoted. **Never transcribe the full dialogue.**
4. **Expression boxes (≫)**: each box as a `.vd-wordlist` (Japanese + romaji, EN, HI, GU, Note).
5. **知って楽しむ (reading)**:
   - a summary in EN/HI/GU and the key lines quoted (2–4 at most);
   - the ● questions with book answers;
   - the ■ question with our answer;
   - any 種明かし (reveal) from the answer pages.
6. **できる！ project**: steps translated and summarised.
7. **ことば (vocabulary)**: one `.vd-wordlist` per task group (1, 2, 3 … and 知って楽しむ). The columns are Japanese + romaji / English / Hindi / Gujarati / Note.
   - Note column: ★ = bold in book (core word), plus the book's example phrase in parentheses.
   - Keep the book's order.
8. **Confusion / nuance notes**: a `.bp-confusion` table comparing the lesson's look-alike points, plus a `.bp-callout`.
9. **`.bp-day-nav`**: previous/next lesson. Link unbuilt lessons too, because the hub chips already point there.

Then update `index.html` in the course folder:

- flip that lesson's `<span class="day-chip soon" data-href="lesson-NN.html">` to `<a class="day-chip ready" href="lesson-NN.html">`;
- bump the `.sample-note` count `In progress — K of 20 units built`;
- when all 20 are built, change it to `✅ Complete — 20 of 20 units built`.

Run `python tools/build_site.py` afterwards. It keeps any index containing `class="day-chip`, and it refreshes the level and module hubs.

---

## 7. Hard rules

- **Romaji on every Japanese line**: words, examples, quoted lines, options and box items (`<span class="romaji">`).
- **EN + HI + GU** for every meaning, example sentence, question and summary.
- **Never transcribe reading texts, dialogues or audio scripts in full.** Summarise them in our own words and quote only short key lines. The book, its pictures and its audio are never hosted.
- **Answers**: use the book's answer when p.278–289 prints one (cite the page). Otherwise write **(our answer, not in book)**. Never present our answer as the book's.
- Do not invent example sentences in the examples tables. Anything added (formation rows, extra notes) is marked "(added, not in book)".
- Keep the book's order for tasks, points, examples and ことば.
- Every page carries the level warning: this book is late N3–N2, filed under N5 textbooks.
- No edits to other books, CSS or JS.

---

**Reference implementation:** [`n5/textbooks/chukyu-honsatsu/lesson-01.html`](../../../../n5/textbooks/chukyu-honsatsu/lesson-01.html) (第1課 新たな出会い). Copy its structure, tone and depth.
