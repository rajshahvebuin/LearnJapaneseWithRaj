# にほんごチャレンジ N4・N5 かんじ — unit-by-unit processing guide

Standing instructions for turning `Nihongo_Challenge_Kanji_N4-N5.pdf` into the site's pages under `n4/kanji/nihongo-challenge/`. To build a unit, name it by its file name from the table in §4, then follow the steps below.

Where this file is silent, the general kanji spec applies (`book-source/n1/kanji/PROCESSING-GUIDE.md`), and for the JLPT-style multiple-choice units the N5 drill guide (`book-source/n5/multi-skill/Tanki_Master_Drill_N5/PROCESSING-GUIDE.md`, §6–7).

---

## 1. Book identification

| Field | Value |
|---|---|
| Title | 「日本語能力試験」対策 にほんごチャレンジ N4・N5 かんじ (Nihongo Challenge N4–N5 Kanji) |
| Publisher | アスク出版 (ASK Publishing). Colophon on PDF 279. |
| Edition | Preface dated 2010年9月 (Japanese) / September 2010 (English); first edition 2010 (colophon, PDF 279) |
| Languages in book | Japanese with English, Korean and Portuguese translations. **No Hindi or Gujarati**: every HI/GU line is ours. Korean and Portuguese are never copied to the site. |
| Content | **310 kanji** in two parts: **Part 1 = N5 kanji 110** (Lesson 1–11, kanji #1–110) and **Part 2 = N4 kanji 200** (Lesson 1–20, kanji #111–310). Every lesson teaches exactly 10 kanji. |
| Audio | None. The book has no CD. |

The PDF's bookmarks are only scan file names (`_Kanji_5-4_001-040`, `kandji540001` …); ignore them.

---

## 2. Scan notes and offset

- **280 PDF pages**, image-only scan (Adobe Acrobat "Image Conversion"). **There is no text layer** (`get_text()` returns empty). Render pages with PyMuPDF and read them visually:
  - contact sheets at 72 dpi to find structure;
  - **130–150 dpi** to read a page;
  - **200–250 dpi crops** for the compound-word rows of each kanji chart, where you must tell the **grey-shaded words** (must-learn words, see §5) from plain ones, and for the small superscript lesson numbers (日本⁵, 休¹⁰日).
- **Offset: PDF page = printed page (offset 0).** Checked against printed footers on p.7, 12, 13, 25–30, 43, 44, 105, 109, 121, 189, 221, 235, 255, 259–267. Every page in the book has its PDF twin; nothing is missing and nothing is out of order. The only blank pages are p.2, p.22 and p.280.
- Front matter: p.1 cover · p.2 blank · p.3 はじめに / Introduction · p.4 Korean + Portuguese preface · p.5–9 目次 (contents; p.7 Part 1, p.8–9 Part 2) · p.10–17 この本の使い方 / How to use this book (Japanese, English p.12–13, Korean, Portuguese; **p.13 = the chart legend**, read this first) · p.18–21 漢字について / Introduction to kanji (history, the four kinds of kanji, on/kun) · p.22 blank.
- Part dividers: p.23 (Part 1 "N5 かんじ 110"), p.24 (Part 1 kanji list), p.107 (Part 2 "N4 かんじ 200"), p.108 (第2部の漢字一覧, Part 2 kanji list).
- Back matter: **p.259–267 解答 (answer key)** · p.268–270 音訓索引 (on/kun index) · p.271–278 語彙索引 (vocabulary index) · p.279 colophon · p.280 blank.
- The scan is clean and straight. Some lesson opener pages (e.g. p.25, 31, 45) have a dark grey page edge from the scanner bed; it does not hide any text.

---

## 3. Answer-key status — official, complete, in the scan

**解答 p.259–267** covers **every exercise in the book**, keyed by the **printed page number of the exercise** ("P29", "P30" …):

- each lesson's opener activity (P25, P31, P37 …), 練習1 (reading) and 練習2 (writing);
- every じっせんれんしゅう (JLPT test practice, もんだい1 and もんだい2);
- both そうごうれんしゅう (comprehensive exercises).

The **コラム (column) answers are not in the 解答**: they are on the column's own こたえ page (Part 1: p.100; Part 2: p.244, 246, 248).

How the key prints answers:
- Reading answers are in hiragana. **Underlined kana = the part read by the kanji; kana in brackets = okurigana or neighbouring kana that are already printed in the question.** E.g. P29 Q11 「にち（よう）び・（ふじ）さん」 means 日 = にち and び, 山 = さん.
- Writing answers print the kanji; brackets again mark the printed context, e.g. P50 Q16 「上手（な）」.
- Multiple-choice answers are the option number after a circled question number: ①3 ②2 ….
- Matching activities print number–letter pairs: 「2—C 3—D …」 (item 1 is the book's worked example and is never in the key).

The key gives **no explanations**. All "Why" notes are ours. Never change an answer; if one looks wrong, keep the book's answer and flag it in the Why note.

Key page map (cite as "解答 p.N"):

| 解答 page | Covers |
|---|---|
| p.259 | Part 1 Lesson 1–4 and じっせんれんしゅう 1–3 (P43, P44) |
| p.260 | Part 1 Lesson 5–9 (Lesson 9 P82 runs on to p.261) and じっせんれんしゅう 4–6 (P63, P64) |
| p.261 | Part 1 Lesson 9 (end), じっせんれんしゅう 7–9 (P83, P84), Lesson 10–11, じっせんれんしゅう 10–11 (P97, P98), Part 1 そうごうれんしゅう (P101, P103, P105, P106) |
| p.262 | Part 2 Lesson 1–3, じっせんれんしゅう 1–3 (P127, P128), Lesson 4 (start) |
| p.263 | Part 2 Lesson 4 (end, P134), Lesson 5–6, じっせんれんしゅう 4–6 (P147, P148), Lesson 7–8, Lesson 9 (start) |
| p.264 | Part 2 Lesson 9 (end), じっせんれんしゅう 7–9 (P167, P168), Lesson 10–12, じっせんれんしゅう 10–12 (P187, P188), Lesson 13 (start) |
| p.265 | Part 2 Lesson 13 (end), Lesson 14–15, じっせんれんしゅう 13–15 (P207, P208), Lesson 16, Lesson 17 (start) |
| p.266 | Part 2 Lesson 17 (end), Lesson 18, じっせんれんしゅう 16–18 (P227, P228), Lesson 19–20 |
| p.267 | Part 2 じっせんれんしゅう 19–20 (P241, P242), Part 2 そうごうれんしゅう (P249–P258) |

Always locate the exercise by its "P" number in the key; several lessons run across a page break.

Oddities in the key:
- **p.265, end of Lesson 14**: after P200 (練習2, which has 12 items) there is a stray line 「⑪1 ⑫3 ⑬2 ⑭1」 with no page label. It matches no Lesson 14 exercise (it looks like a leftover fragment of a じっせんれんしゅう line). Ignore it, and mention it in the Lesson 14 Notes.
- Part 1 Lesson 3 P37 and similar matching keys skip item 1 (the worked example).

---

## 4. Unit table (49 units)

One unit = one lesson (6 pages, 10 kanji), one じっせんれんしゅう (2 pages, 28 multiple-choice items), one コラム, or one block of the そうごうれんしゅう. PDF page = printed page for every row.

File names: `part1-…` = Part 1 (N5 kanji #1–110), `part2-…` = Part 2 (N4 kanji #111–310). Lessons are zero-padded (`part2-lesson-07.html`); tests are named by the lessons they review (`part2-test-10-12.html`).

### Part 1 — N5 かんじ 110 (18 units)

| File | Title | Romaji / English | Kanji | Pages | 解答 |
|---|---|---|---|---|---|
| part1-lesson-01.html | Lesson 1 絵からできた漢字1 | E kara dekita kanji 1 — Kanji made from pictures 1 | 山川田日月火水木金土 (#1–10) | 25–30 | p.259 (P25, P29, P30) |
| part1-lesson-02.html | Lesson 2 数字 | Suuji — Numbers | 一二三四五六七八九十 (#11–20) | 31–36 | p.259 (P31, P35, P36) |
| part1-lesson-03.html | Lesson 3 数字と記号 | Suuji to kigou — Numbers & signs | 百千万円年上下中半分 (#21–30) | 37–42 | p.259 (P37, P41, P42) |
| part1-test-01-03.html | じっせんれんしゅう 1–3 | Jissen renshuu — JLPT test practice, Lessons 1–3 | もんだい1 ①–⑭, もんだい2 ①–⑭ | 43–44 | p.259 (P43, P44) |
| part1-lesson-04.html | Lesson 4 絵からできた漢字2 | Kanji made from pictures 2 | 人子女男目口耳手足力 (#31–40) | 45–50 | p.259 (P45, P49, P50) |
| part1-lesson-05.html | Lesson 5 絵からできた漢字3 | Kanji made from pictures 3 | 父母先生学校友本毎何 (#41–50) | 51–56 | p.260 (P51, P55, P56) |
| part1-lesson-06.html | Lesson 6 方角 | Hougaku — Directions | 前後外左右東西南北名 (#51–60) | 57–62 | p.260 (P57, P61, P62) |
| part1-test-04-06.html | じっせんれんしゅう 4–6 | JLPT test practice, Lessons 4–6 | もんだい1–2, ①–⑭ each | 63–64 | p.260 (P63, P64) |
| part1-lesson-07.html | Lesson 7 絵からできた漢字4 | Kanji made from pictures 4 | 牛馬魚貝雨天気車門午 (#61–70) | 65–70 | p.260 (P65, P69, P70) |
| part1-lesson-08.html | Lesson 8 形容詞 | Keiyoushi — Adjectives | 大小高安新古長多少早 (#71–80) | 71–76 | p.260 (P71, P75, P76) |
| part1-lesson-09.html | Lesson 9 動詞 | Doushi — Verbs | 行来食見入出立書言飲 (#81–90) | 77–82 | p.260–261 (P77, P81, P82) |
| part1-test-07-09.html | じっせんれんしゅう 7–9 | JLPT test practice, Lessons 7–9 | もんだい1–2, ①–⑭ each | 83–84 | p.261 (P83, P84) |
| part1-lesson-10.html | Lesson 10 組み合わせ漢字1 | Kumiawase kanji 1 — Combinations 1 | 話読語間聞買休時週道 (#91–100) | 85–90 | p.261 (P85, P89, P90) |
| part1-lesson-11.html | Lesson 11 組み合わせ漢字2 | Combinations 2 | 今会社店駅花国白空電 (#101–110) | 91–96 | p.261 (P91, P95, P96) |
| part1-test-10-11.html | じっせんれんしゅう 10–11 | JLPT test practice, Lessons 10–11 | もんだい1–2, ①–⑭ each | 97–98 | p.261 (P97, P98) |
| part1-column.html | コラム | Koramu — Column (find katakana inside kanji; write numbers) | もんだい1–2 | 99–100 | p.100 こたえ (not in 解答) |
| part1-sougou-1.html | そうごうれんしゅう もんだい1 | Sougou renshuu — Comprehensive exercise, reading | ①–㉘ | 101–102 | p.261 (P101) |
| part1-sougou-2.html | そうごうれんしゅう もんだい2–4 | Comprehensive exercise, writing + picture tasks | もんだい2 ①–㉘; 3-1 ①–⑤, 3-2 A–D (北海道 travel ad); 4-1 ①–③, 4-2 A–C (survey pie chart) | 103–106 | p.261 (P103, P105, P106) |

### Part 2 — N4 かんじ 200 (31 units)

| File | Title | Romaji / English | Kanji | Pages | 解答 |
|---|---|---|---|---|---|
| part2-lesson-01.html | Lesson 1 住所 | Juusho — Address | 住所京都府県市区町村 (#111–120) | 109–114 | p.262 (P109, P113, P114) |
| part2-lesson-02.html | Lesson 2 形容詞1 | Keiyoushi 1 — Adjectives 1 | 明暗遠近強弱重軽太細 (#121–130) | 115–120 | p.262 (P115, P119, P120) |
| part2-lesson-03.html | Lesson 3 形容詞2 | Adjectives 2 | 特別有便利不切元好急 (#131–140) | 121–126 | p.262 (P121, P125, P126) |
| part2-test-01-03.html | じっせんれんしゅう 1–3 | JLPT test practice, Lessons 1–3 | もんだい1–2, ①–⑭ each | 127–128 | p.262 (P127, P128) |
| part2-lesson-04.html | Lesson 4 形容詞3 | Adjectives 3 | 低広短良悪正変赤青黒 (#141–150) | 129–134 | p.262–263 (P129, P133, P134) |
| part2-lesson-05.html | Lesson 5 趣味 | Shumi — Hobbies | 映画音楽歌写真旅世界 (#151–160) | 135–140 | p.263 (P135, P139, P140) |
| part2-lesson-06.html | Lesson 6 仕事 | Shigoto — Work, professions | 仕事銀員医者働屋産業 (#161–170) | 141–146 | p.263 (P141, P145, P146) |
| part2-test-04-06.html | じっせんれんしゅう 4–6 | JLPT test practice, Lessons 4–6 | もんだい1–2, ①–⑭ each | 147–148 | p.263 (P147, P148) |
| part2-lesson-07.html | Lesson 7 自然 | Shizen — Nature | 林森地池海洋雪光台風 (#171–180) | 149–154 | p.263 (P149, P153, P154) |
| part2-lesson-08.html | Lesson 8 季節 | Kisetsu — Seasons | 季節春夏秋冬暑寒暖涼 (#181–190) | 155–160 | p.263 (P155, P159, P160) |
| part2-lesson-09.html | Lesson 9 体 | Karada — Body | 体頭顔首心声病薬科内 (#191–200) | 161–166 | p.263–264 (P161, P165, P166) |
| part2-test-07-09.html | じっせんれんしゅう 7–9 | JLPT test practice, Lessons 7–9 | もんだい1–2, ①–⑭ each | 167–168 | p.264 (P167, P168) |
| part2-lesson-10.html | Lesson 10 時 | Toki — Time | 朝昼夜夕方晩計曜以度 (#201–210) | 169–174 | p.264 (P169, P173, P174) |
| part2-lesson-11.html | Lesson 11 動詞1 | Doushi 1 — Verbs 1 | 止歩走起特待借貸始終 (#211–220) | 175–180 | p.264 (P175, P179, P180) |
| part2-lesson-12.html | Lesson 12 家族 | Kazoku — Family | 家族私自親両兄弟姉妹 (#221–230) | 181–186 | p.264 (P181, P185, P186) |
| part2-test-10-12.html | じっせんれんしゅう 10–12 | JLPT test practice, Lessons 10–12 | もんだい1–2, ①–⑭ each | 187–188 | p.264 (P187, P188) |
| part2-lesson-13.html | Lesson 13 生活 | Seikatsu — Everyday life | 活回主色形品民服犬同 (#231–240) | 189–194 | p.264–265 (P189, P193, P194) |
| part2-lesson-14.html | Lesson 14 食べ物 | Tabemono — Food | 米料理肉鳥野菜茶飯味 (#241–250) | 195–200 | p.265 (P195, P199, P200) |
| part2-lesson-15.html | Lesson 15 部首 | Bushu — Radicals | 代使作化信進送返洗注 (#251–260) | 201–206 | p.265 (P201, P205, P206) |
| part2-test-13-15.html | じっせんれんしゅう 13–15 | JLPT test practice, Lessons 13–15 | もんだい1–2, ①–⑭ each | 207–208 | p.265 (P207, P208) |
| part2-lesson-16.html | Lesson 16 場所 | Basho — Places | 場建物院館堂室工図号 (#261–270) | 209–214 | p.265 (P209, P213, P214) |
| part2-lesson-17.html | Lesson 17 交通 | Koutsuu — Traffic, transport | 交通動乗降運転帰発着 (#271–280) | 215–220 | p.265–266 (P215, P219, P220) |
| part2-lesson-18.html | Lesson 18 学校1 | Gakkou 1 — School 1 | 漢字文教勉習英考研究 (#281–290) | 221–226 | p.266 (P221, P225, P226) |
| part2-test-16-18.html | じっせんれんしゅう 16–18 | JLPT test practice, Lessons 16–18 | もんだい1–2, ①–⑭ each | 227–228 | p.266 (P227, P228) |
| part2-lesson-19.html | Lesson 19 学校2 | School 2 | 問題試験質合答用紙意 (#291–300) | 229–234 | p.266 (P229, P233, P234) |
| part2-lesson-20.html | Lesson 20 動詞2 | Verbs 2 | 引開閉去死集知売説思 (#301–310) | 235–240 | p.266 (P235, P239, P240) |
| part2-test-19-20.html | じっせんれんしゅう 19–20 | JLPT test practice, Lessons 19–20 | もんだい1–2, ①–⑭ each | 241–242 | p.267 (P241, P242) |
| part2-column.html | コラム (3 columns) | 人の漢字 (kanji with a person inside) · 手と足の漢字 (hand and foot kanji) · 漢字をつくりましょう (make kanji from parts) | 3 sorting / building puzzles | 243–248 | こたえ p.244, 246, 248 (not in 解答) |
| part2-sougou-1.html | そうごうれんしゅう もんだい1 | Comprehensive exercise, reading | ①–㊷ | 249–251 | p.267 (P249–P251) |
| part2-sougou-2.html | そうごうれんしゅう もんだい2 | Comprehensive exercise, writing | ①–㊷ | 252–254 | p.267 (P252–P254) |
| part2-sougou-3.html | そうごうれんしゅう もんだい3–6 | Comprehensive exercise, real-life texts | 3 メモ ①–⑦ · 4 お知らせ (rubbish rules) 4-1 ①–⑦, 4-2 Ⓐ–Ⓔ · 5 掲示物 (toilet notice) ①–④ · 6 広告 (flat advert) 6-1 ①–③, 6-2 Ⓐ–Ⓒ | 255–258 | p.267 (P255–P258) |

Note on numbering: in the 解答, the そうごうれんしゅう Part 2 もんだい1 is split by page: P249 ①–⑭, P250 ⑮–㉘, P251 ㉙–㊷ (same for もんだい2 on P252–P254).

---

## 5. Inside a lesson (book layout)

Every lesson is 6 pages in the same order:

1. **Opener page** (lesson number on a grey tab, title in JP + EN + KO + PT, the 10 kanji in a row). It has one small warm-up activity, which **is in the key**:
   - "Kanji made from pictures" lessons: a scene drawing with the kanji hidden in it; write the reading/meaning from a word box (P25), or match picture → kanji → reading (P45, P51, P65).
   - other lessons: match pictures or old forms to kanji and readings (letters A–L), or fill a short sentence (P115, P129, P135, P195, P215).
   Item 1 is always the book's worked example.
2. **Kanji charts**, 3 per page (10 charts over about 3½ pages). Each chart (legend on p.13):
   - ① serial number (1–310) and ② the kanji;
   - ③ meaning(s) in EN/KO/PT; ④ old form (when there is one, e.g. 學);
   - ⑤ stroke order, ⑥ empty practice boxes, ⑦ stroke count in brackets, e.g. (3);
   - ⑧ kun-reading in hiragana (a hyphen marks okurigana: まな-ぶ) and ⑨ on-reading in katakana (a slash marks alternatives: ガク／ガッ-);
   - ⑩ an illustration of how the kanji was made and ⑪ its explanation (Japanese line + EN/KO/PT);
   - ⑫ **compound words** (2–4 per kanji) with reading and EN/KO/PT meaning. **Grey-shaded words are must-learn words**: shaded in Part 1 = N5 level, shaded in Part 2 = N4 level. A small superscript number (日本⁵) = the lesson where the other kanji is taught (Part 1 lesson numbers up to #110, Part 2 lesson numbers after). A kanji with hiragana above it in a word (登山, 油田) is not taught in this book's part. A footnote line under the chart (本→Lesson 5 休→Lesson 10) repeats the cross-reference.
   - ⑬ `*` marks a special reading (今日 *きょう).
3. **練習1: 漢字の 読み方を 書きましょう** — write the reading in hiragana: items 1–10 single kanji/words, items 11–15 sentences with underlined kanji words.
4. **練習2: 下の □に 漢字を 書きましょう** — write the kanji in the boxes; each item gives the reading above and the meaning in EN/KO/PT below. 11–18 items, later items are short sentences.

練習1 sometimes starts on the last chart page (e.g. p.29, p.35, p.41) and 練習2 fills the last page.

**じっせんれんしゅう** (2 pages): もんだい1 = 漢字読み (choose the hiragana reading), 7 sentences × 2 underlined words = ①–⑭; もんだい2 = 表記 (choose the kanji spelling), same shape. 4 options each, like JLPT N5/N4 文字・語彙 問題1–2.

---

## 6. Site page format

### 6a. Lesson pages: `n4/kanji/nihongo-challenge/partN-lesson-NN.html`

Chrome: copy from `part1-lesson-01.html` exactly (`auth.js` first in `<head>`, favicon, fonts, `style.css` + `day-page.css`, `body.level-page.n4`, header with the N4 `level-nav` (Kanji active), footer, `main.js`). Depth 3: assets are `../../../assets/...`.

Breadcrumb: Home / JLPT N4 / Kanji / にほんごチャレンジ かんじ (→ `index.html`) / Part N Lesson N.

**Header** (`.bp-header`):
- `.bp-week`: "JLPT N4 · Kanji · にほんごチャレンジ N4・N5 かんじ — Part 1 (N5 kanji)" or "Part 2 (N4 kanji)", with romaji.
- `h1`: "Lesson N — <title>" + romaji and English gloss.
- Meta grid: **Source** (book, Part, printed pp = PDF pp, kanji serial range) · **Kanji covered** (chips, the 10 kanji) · **Answer key** ("Official, answers only — 解答 p.N", listing the P-numbers) · **Notes** (what is ours: HI/GU, romaji, all Why notes and §3; the book's KO/PT are not copied; any oddity).

**Legend** (`.kd-legend`): grey-shaded = must-learn word (N5 in Part 1, N4 in Part 2), marked with a `.bp-badge` "must-learn" on our site; superscript lesson numbers; katakana = on, hiragana = kun; `*` special reading.

**Section 1 — Kanji Charts** (`.bp-section-title` "1"):
- One `.bp-point` per lesson theme block (Part 1 Lesson 1: one block; for long lessons you may split by chart page). Inside, a `.kd-kanji-table` with columns: № · Kanji · Strokes / readings · Word · Kana · English · Hindi · Gujarati. One row per compound word in **book order**; the first row of a kanji carries №, kanji, stroke count and readings; the kanji's own meaning goes in the first row's English cell after the word if needed. Mark shaded words with `<span class="bp-badge">must-learn</span>` in the Word cell. Romaji under every word.
- After the table, a second `.kd-kanji-table` "How each kanji was made": № · Kanji · book picture (described in words; never embed the image) · EN · HI · GU, translating the book's ⑪ explanation. Old forms (④) go here too.

**Section 2 — Quiz / Exercise Section** (in book order):
- **Opener activity**: one `.bp-quiz` with the instruction (JP + romaji + EN/HI/GU) and a `.bp-options` table of all items with the book's answer row-by-row. Item 1 is labelled "(book's example)".
- **練習1**: items 1–10 as one `.bp-quiz` table (Item · Kanji · Answer kana · romaji · EN · HI · GU). Items 11–15 (sentences) each get their own `.bp-quiz` card: sentence with `<u>` on the underlined kanji, romaji, EN/HI/GU, the answer (with the key's brackets explained), and a short **Why** note.
- **練習2**: one `.bp-quiz` table (Item · Reading given · Meaning · Answer kanji · romaji · EN · HI · GU); sentence items get their own cards like 練習1 11–15.
- Every answer is the book's: say "Book answer (解答 p.N, P-number)". If an item has no key, give **(our answer, not in book)**.

**Section 3 — Confusion Pairs / Nuance Notes**: a `.bp-confusion` table built from the day's real traps: same kun-reading different kanji (ひ 日／火), one kanji with many readings (日: ひ・び・にち・に・じつ), sound changes (川 かわ → がわ, 田 た → だ), look-alike kanji (土／士, 木／本, 日／目). Finish with one `.bp-callout` on the single most testable point. Anything not printed in the book is marked "(added, not in book)".

**Nav** (`.bp-day-nav`): prev = previous unit in the §4 table (the first unit links to the hub), next = next unit. If the next unit is not built, write `<span>Next: … — coming soon</span>` (no dead link); when you build a unit, turn the previous unit's span into a link.

### 6b. じっせんれんしゅう pages: `partN-test-AA-BB.html`

Same as the N5 drill guide's 漢字読み / 表記 pages (`n5/multi-skill/tanki-master-drill/moji-goi-1.html` and `moji-goi-2.html`): §1 Key Words table (the 28 tested words, EN/HI/GU, note on the lesson where the kanji is taught), §2 every question (sentence + romaji + EN/HI/GU, 4-option `.bp-options` table with Japanese + romaji + EN/HI/GU, the correct row `class="correct"`, Why note), §3 confusion pairs (wrong options are the traps: voicing, long vowels, small っ, look-alike kanji). Each 7-sentence question covers two numbered items (①②, ③④ …); give one card per sentence with two option tables.

### 6c. コラム and そうごうれんしゅう

- **コラム**: describe the puzzle in words (we never embed the drawings), give each answer from the こたえ page, and add the meaning of each kanji in EN/HI/GU.
- **そうごうれんしゅう**: like 6b. For the picture/real-life tasks (北海道 ad, survey chart, memo, rubbish notice, toilet notice, flat advert), **do not transcribe the whole text**: summarise it in 1–2 sentences (EN/HI/GU) and quote only the line each question underlines.

### 6d. Hub (`index.html`)

Five `.week-block`s: Part 1 Lessons 1–6 (+ tests 1–3, 4–6) · Part 1 Lessons 7–11 (+ tests, column, そうごう) · Part 2 Lessons 1–9 (+ tests) · Part 2 Lessons 10–20 (+ tests) · Part 2 コラム・そうごうれんしゅう. Built unit: `<a class="day-chip ready" href="FILE.html">LABEL</a>`; unbuilt: `<span class="day-chip soon" data-href="FILE.html">LABEL</span>`. Update the `.sample-note` text `In progress — N of 49 units built`; at 49 change it to `Complete — 49 of 49 units built` with the ✅ icon, as on the other finished hubs.

---

## 7. Hard rules

- **Romaji on every Japanese line**: kanji readings, words, sentences, options, instructions (`<span class="romaji">`).
- **EN + HI + GU** for every meaning, example word, question and option. The book gives EN/KO/PT; KO and PT are never copied; HI and GU are always ours.
- **Every question with the book's answer**, citing the 解答 page (or the コラム's こたえ page). If there is no printed answer, give a worked answer labelled **(our answer, not in book)**.
- **Never transcribe long texts.** The そうごうれんしゅう real-life texts are summarised; quote only the underlined line.
- **Never embed the book's pictures** (charts, stroke-order drawings, illustrations). Describe them in words.
- Keep the book's order (kanji serial numbers, compound order, exercise order).
- The book has no audio; never add `<audio>` or links to media.
- No emoji glyphs in body text. Reuse existing classes only (`.bp-*`, `.kd-*`, `.vd-*`); do not edit CSS, JS, `tools/`, other courses or hub pages outside this course.

## 8. Checks before finishing a unit

- Every answer matches the 解答 page (re-read it at 150 dpi; underlines matter).
- Shaded words checked on a 200–250 dpi crop of the compound rows.
- Tags balance (Python `html.parser`), all relative links resolve, the file ends with `</html>`.
- Hub chip flipped and `In progress — N of 49 units built` updated; previous unit's "coming soon" span turned into a link.

---

**Reference implementation:** `n4/kanji/nihongo-challenge/part1-lesson-01.html` (Part 1 Lesson 1 絵からできた漢字1). Copy its structure, tone and depth.
