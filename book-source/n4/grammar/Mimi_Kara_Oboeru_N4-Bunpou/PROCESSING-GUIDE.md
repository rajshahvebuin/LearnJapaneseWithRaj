# 耳から覚える 日本語能力試験 文法トレーニング N4 — unit-by-unit processing guide

Standing instructions for turning `Mimi_Kara_Oboeru_N4-Bunpou.PDF` into the site's study pages under `n4/grammar/mimi-kara-oboeru/`. Give a file name from the unit table in §4 (e.g. "unit-02-a") and this is the process to follow.

Where this file is silent, the general grammar spec applies: `book-source/n1/grammar/PROCESSING-GUIDE.md` (the `.bp-point` / `.bp-quiz` / `.bp-confusion` format). The hub and nav rules copy `book-source/n5/multi-skill/Tanki_Master_Drill_N5/PROCESSING-GUIDE.md`.

---

## 1. Book identification

| Field | Value |
|---|---|
| Title (cover) | 耳から覚える 日本語能力試験 文法トレーニング N4 (Mimi kara Oboeru — JLPT Grammar Training N4) |
| Site name | 耳から覚える N4 文法 (Mimi kara Oboeru N4 Grammar) |
| Authors | 安藤栄里子 (Andou Eriko), 今川和 (Imagawa Kazu) — colophon, PDF 128 |
| Publisher | アルク (ALC Press Inc.), 2010-06-30 first edition |
| Size | 138 PDF pages = main book printed p.1–127 + colophon (PDF 128) + 解答 booklet (PDF 129–137) + 1 blank (PDF 138) |
| Content | **90 numbered grammar points (1–90)** in **10 Units**, each Unit followed by a ディクテーション (dictation) page and a 練習 (practice) set; **3 まとめテスト** (review tests) after Units 03, 07 and 10; **4 総合問題** (JLPT-format mock grammar sections) at the end |
| Difficulty | Each Unit's header has a レベル box with 1–3 ★ (★ = Units 01–03, ★★ = 04–07, ★★★ = 08–10). The preface says more ★ = harder |
| Audio | CD folder beside the PDF: `Mimi_Kara_Oboeru_N4_Bunpou-AudioCD/01 - Track 01.mp3` … `11 - Track 11.mp3`. **Kept locally, never published, never linked, never embedded.** |

The book's meaning lines are printed in Japanese + English + Chinese + Korean. We use the book's English as a starting point, write our own simple English, and add Hindi and Gujarati. We never reproduce the Chinese or Korean lines.

---

## 2. Scan notes and offsets

- Scanned on a Toshiba MFP (2013). **No text layer at all** (`get_text()` returns empty strings). Render with PyMuPDF and read visually: `import pymupdf; doc[i-1].get_pixmap(dpi=150)`. Contact sheets at ~110 dpi (20 pages per sheet) to find structure; 150 dpi to read points and exercises; 250–300 dpi crops for furigana and the small EN/中/韓 meaning lines. Keep renders in the scratchpad, never in the repo.
- Scan is clean and complete. Pages are slightly grey with some speckle, but everything is readable at 150 dpi. Furigana on N4–N2 kanji are printed (the book's own rule, p.3 ④).
- **Main book: PDF page = printed page (offset 0).** Verified on printed footers p.2, 3, 7, 11, 12, 13, 14, 15, 17, 18, 21, 26, 31, 37, 41, 53, 61, 71, 81, 91, 101, 111, 121, 125, 127.
- **解答 booklet: PDF page = 解答 page + 128.** PDF 129 = 解答 cover (p.1, no number); PDF 130 footer "2", PDF 131 "解答 3" … PDF 137 "解答 9". Cite as "解答 p.N (PDF M)".
- Front matter: p.1 cover · p.2–3 本書で勉強する方へ (features, how to use, notation legend) · p.4 English version · p.5 Chinese · p.6 Korean · p.7–11 CONTENTS.
- Back matter: p.112 blank · p.113 総合問題 divider · p.126–127 さくいん (index, 50音順) · PDF 128 colophon · PDF 138 blank.
- Notation (p.3): 接続 / 意味 / 注意 / 復習 / 〜形の作り方 boxes; `*` = exceptional use; **the headphone icon marks the sentences that are on the CD — these are exactly the dictation sentences.** 「え段」「お段」 in formation boxes mean the え-row / お-row kana.

Nothing is missing from the scan: every 練習, まとめテスト and 総合問題 in the 解答 booklet has its question page, and every Unit has its dictation page.

---

## 3. Answer-key status

**Official key, answers only — 解答 booklet p.2–9 (PDF 130–137).** No explanations; all reasoning on our pages is ours.

| 解答 page (PDF) | Covers |
|---|---|
| p.2 (PDF 130) | Unit 01 練習 (p.18) · Unit 02 練習 (p.25) · Unit 03 練習 (p.32) |
| p.3 (PDF 131) | まとめテスト1 (p.34) I–III · Unit 04 練習 (p.45) I–V (V 1–5) |
| p.4 (PDF 132) | Unit 04 練習 V 6–7 (top left) · Unit 05 練習 (p.54) · Unit 06 練習 (p.62) |
| p.5 (PDF 133) | Unit 07 練習 (p.71) · まとめテスト2 (p.74) I–III |
| p.6 (PDF 134) | Unit 08 練習 (p.84) · Unit 09 練習 (p.94) I–V |
| p.7 (PDF 135) | Unit 10 練習 (p.105) I–VI · まとめテスト3 (p.108) I–II (to II 24) |
| p.8 (PDF 136) | まとめテスト3 II 25 (top left) and III · 総合問題 I (p.114) · 総合問題 II (p.117) |
| p.9 (PDF 137) | 総合問題 III (p.120) · 総合問題 IV (p.123) |

- Fill-in answers are given as the word/kana (e.g. Unit 01 練習 I 1 「を、の」); choice answers as a–d; 総合問題 もんだい2 (★) as the full tile order (e.g. `c → b → d → a`) — the ★ answer is the tile in the ★ slot, which you work out from the order.
- **Dictation has no entry in the 解答 booklet.** Its answers are the book's own headphone-marked example sentences on the point pages. Cite them as "Answer: the CD sentence on p.N (book's own text)". This is book-sourced, not "our answer".
- 練習 II conjugation tables (e.g. Unit 01 可能形・意志形, Unit 09 受身・使役・使役受身) are answered in full in the key.
- Read the key at 150 dpi; small particles (に／は, が／か) need a 250 dpi crop. Never change a book answer; if one looks wrong, keep it and flag it in the Why note.
- If you ever meet an item with no key entry (none found so far), give a worked answer labelled **(our answer, not in book)**.

### Audio track map (CD in the folder beside the PDF)

| Track | Content |
|---|---|
| 01 | Opening / title (~20 s) |
| 02–11 | Units 01–10 in order: the headphone-marked example sentences of that Unit = the Unit's ディクテーション. The CD number is printed on each dictation page (CD 02 … CD 11) and in the CONTENTS |

まとめテスト and 総合問題 have no audio. Cite as `<span class="ld-track">CD, Track N</span>` in the header only. **Never publish the mp3, never link to it, never add `<audio>`.**

---

## 4. Unit table (43 study pages)

Each book Unit is split into **three pages**: grammar points (first half) `-a`, grammar points (second half) `-b`, and the 練習 set `-renshuu`. Each `-a`/`-b` page also carries the dictation items for its own points (the dictation page is numbered by point). Each まとめテスト is split into three pages, one per 問題 (I/II/III = a/b/c). Each 総合問題 is one page. All pages: PDF = printed (offset 0).

| File | Title (hub chip) | Romaji / English | Content | Printed = PDF pp | Answers |
|---|---|---|---|---|---|
| unit-01-a.html | Unit 01 · 1–5 | Unit 01 points 1–5: ability, potential form, change, intention, volitional | 1 〜ができる／〜ことができる · 2 〜る／られる (可能形) · 3 〜ようになる (+復習 〜(に)なる) · 4 〜つもり · 5 〜う／よう (意志形); dictation 1–5 (10 sentences) | 12–15 (+ dict. 17) | CD sentences p.12–15 · Track 02 |
| unit-01-b.html | Unit 01 · 6–9 | 意志形+と思う, 〜かた, 〜とか, 〜の／こと | 6 意志形+と思う · 7 〜かた · 8 〜とか · 9 〜の／こと; dictation 6–9 | 15–16 (+ 17) | CD sentences p.15–16 · Track 02 |
| unit-01-renshuu.html | Unit 01 練習 | Renshuu — practice | I particles (7) · II 可能形・意志形 table (10 verbs) · III forms (10) · IV a–d (6) | 18–19 | 解答 p.2 (PDF 130) |
| unit-02-a.html | Unit 02 · 10–13 | ため(に), 〜たことがある, comparison, は…が+adj | 10 〜ため(に) · 11 〜たことがある · 12 比較 · 13 〜は…が+形容詞／状態を表す動詞; dictation 10–13 | 20–22 (+ 24) | CD sentences · Track 03 |
| unit-02-b.html | Unit 02 · 14–18 | にする, だろう(と思う), quoting, ほうがいい, 疑問詞+でも | 14 〜にする · 15 〜だろう／(〜だろう)と思う · 16 〜と言う／聞く／書く など · 17 〜ほうがいい · 18 疑問詞+でも; dictation 14–18 | 22–23 (+ 24) | CD sentences · Track 03 |
| unit-02-renshuu.html | Unit 02 練習 | | I (12) · II (8) · III question words (7) · IV a–d (6) | 25–26 | 解答 p.2 (PDF 130) |
| unit-03-a.html | Unit 03 · 19–22 | かどうか, か, そうだ (hearsay), ので | 19 〜かどうか · 20 〜か · 21 〜そうだ (伝聞) · 22 〜ので; dictation 19–22 | 27–28 (+ 31) | CD sentences · Track 04 |
| unit-03-b.html | Unit 03 · 23–27 | のに, てしまう, てみる, やすい／にくい, がる | 23 〜のに · 24 〜てしまう · 25 〜てみる · 26 〜やすい／にくい · 27 〜がする; dictation 23–27 | 29–30 (+ 31) | CD sentences · Track 04 |
| unit-03-renshuu.html | Unit 03 練習 | | I (5) · II (11) · III ○ choice (15) · IV a–d (6) | 32–33 | 解答 p.2 (PDF 130) |
| matome-1-a.html | まとめテスト1 · I | Review test 1 (points 1–27), 問題I particles | I ( ) にひらがな (19 items, 20 marks) | 34 | 解答 p.3 (PDF 131) |
| matome-1-b.html | まとめテスト1 · II | 問題II forms | II ( ) のことばを適当な形に (20) | 35 | 解答 p.3 (PDF 131) |
| matome-1-c.html | まとめテスト1 · III | 問題III choose a–d | III a–d (20) | 36–37 | 解答 p.3 (PDF 131) |
| unit-04-a.html | Unit 04 · 28–31 | (よ)うか／ましょうか, てはいけない, なければならない, てもいい | 28–31; dictation 28–31 | 38–39 (+ 44) | CD sentences · Track 05 |
| unit-04-b.html | Unit 04 · 32–35 | commands, こと／ということ, giving & receiving | 32 命令の表現 · 33 〜こと／ということ · 34 あげる／もらう／くれる · 35 さしあげる／やる／いただく／くださる; dictation 32–35 | 40–43 (+ 44) | CD sentences · Track 05 |
| unit-04-renshuu.html | Unit 04 練習 | | I (8) · II 命令形 table (10 verbs) · III (10) · IV ○ choice (11) · V a–d (7) | 45–47 | 解答 p.3–4 (PDF 131–132) |
| unit-05-a.html | Unit 05 · 36–40 | そうだ (appearance), ため(に) cause, すぎる, ておく, 〜し | 36–40; dictation 36–40 | 48–50 (+ 53) | CD sentences · Track 06 |
| unit-05-b.html | Unit 05 · 41–45 | でも, のようだ, ことが(も)ある, のだ, も | 41–45; dictation 41–45 | 50–52 (+ 53) | CD sentences · Track 06 |
| unit-05-renshuu.html | Unit 05 練習 | | I (10) · II (12) · III ○ choice (14) · IV a–d (6) | 54–55 | 解答 p.4 (PDF 132) |
| unit-06-a.html | Unit 06 · 46–50 | ようだ, らしい, かもしれない, ところだ, ばかり | 46–50; dictation 46–50 | 56–58 (+ 61) | CD sentences · Track 07 |
| unit-06-b.html | Unit 06 · 51–55 | がる／たがる, だす／はじめる／おわる／つづける, でも, の, かな(あ) | 51–55; dictation 51–55 | 58–60 (+ 61) | CD sentences · Track 07 |
| unit-06-renshuu.html | Unit 06 練習 | | I (7) · II (13) · III ○ choice (7) · IV a–d (6) | 62–63 | 解答 p.4 (PDF 132) |
| unit-07-a.html | Unit 07 · 56–59 | conditionals と, たら, ば, なら | 56–59 (58 has the 仮定形 table); dictation 56–59 | 64–67 (+ 70) | CD sentences · Track 08 |
| unit-07-b.html | Unit 07 · 60–65 | asking advice, と／たら／ばいい, ても／でも, こんな／こう | 60–65; dictation 60–65 | 68–69 (+ 70) | CD sentences · Track 08 |
| unit-07-renshuu.html | Unit 07 練習 | | I (8) · II (11) · III ○ choice (15) · IV a–d (7) | 71–73 | 解答 p.5 (PDF 133) |
| matome-2-a.html | まとめテスト2 · I | Review test 2 (points 28–65), 問題I | I (24 items, 25 marks) | 74 | 解答 p.5 (PDF 133) |
| matome-2-b.html | まとめテスト2 · II | 問題II | II (24 items, 25 marks) | 75 | 解答 p.5 (PDF 133) |
| matome-2-c.html | まとめテスト2 · III | 問題III | III a–d (25) | 76–77 | 解答 p.5 (PDF 133) |
| unit-08-a.html | Unit 08 · 66–67 | てあげる／てもらう／てくれる and humble/plain variants | 66 〜てあげる／もらう／くれる · 67 〜てさしあげる／やる／いただく／くださる; dictation 66–67 | 78–79 (+ 83) | CD sentences · Track 09 |
| unit-08-b.html | Unit 08 · 68–72 | ことにする／なる, (よ)うとする, ようにする, てくる／いく | 68–72; dictation 68–72 | 80–82 (+ 83) | CD sentences · Track 09 |
| unit-08-renshuu.html | Unit 08 練習 | | I (13) · II (9) · III ○ choice (16) · IV a–d (6) | 84–86 | 解答 p.6 (PDF 134) |
| unit-09-a.html | Unit 09 · 73–75 | passive, causative, causative-passive | 73 受身 · 74 使役 · 75 使役受身; dictation 73–75 | 87–90 (75 ends top of p.90) (+ 93) | CD sentences · Track 10 |
| unit-09-b.html | Unit 09 · 76–82 | (さ)せてください, まで, までに, あいだ(は), あいだに, ように言う, 〜さ | 76–82; dictation 76–82 | 90–92 (+ 93) | CD sentences · Track 10 |
| unit-09-renshuu.html | Unit 09 練習 | | I (12) · II 受身・使役・使役受身 table (7 verbs) · III (15) · IV ○ choice (22) · V a–d (9) | 94–97 | 解答 p.6 (PDF 134) |
| unit-10-a.html | Unit 10 · 83–85 | respectful, humble, other polite forms | 83 尊敬表現 · 84 謙譲表現 (+ special-form table p.99) · 85 そのほかのていねいな言い方; dictation 83–85 | 98–101 (+ 104) | CD sentences · Track 11 |
| unit-10-b.html | Unit 10 · 86–90 | まま, ずに, はず, たばかり, ちゃ／ちゃう | 86–90; dictation 86–90 | 101–103 (+ 104) | CD sentences · Track 11 |
| unit-10-renshuu.html | Unit 10 練習 | | I (8) · II お〜になる／お〜する (8) · III special keigo forms (8) · IV forms (5) · V plain／casual forms (6) · VI a–d (11) | 105–107 | 解答 p.7 (PDF 135) |
| matome-3-a.html | まとめテスト3 · I | Review test 3 (points 66–90), 問題I | I (25) | 108 | 解答 p.7 (PDF 135) |
| matome-3-b.html | まとめテスト3 · II | 問題II | II (25) | 109 | 解答 p.7–8 (PDF 135–136) |
| matome-3-c.html | まとめテスト3 · III | 問題III | III a–d (25) | 110–111 | 解答 p.8 (PDF 136) |
| sougou-1.html | 総合問題 I | Sougou mondai — mock grammar section 1 | もんだい1 (15) · もんだい2 ★ (5) · もんだい3 cloze passage (5) | 114–116 | 解答 p.8 (PDF 136) |
| sougou-2.html | 総合問題 II | mock section 2 | same layout | 117–119 | 解答 p.8 (PDF 136) |
| sougou-3.html | 総合問題 III | mock section 3 | same layout | 120–122 | 解答 p.9 (PDF 137) |
| sougou-4.html | 総合問題 IV | mock section 4 (もんだい1 has 14 items) | same layout | 123–125 | 解答 p.9 (PDF 137) |

Item counts were checked against the 解答 booklet; recount on the 150 dpi render when building. The point-to-page split for `-a`/`-b` follows where each point starts; a point that runs onto the next page stays with its own half.

Hub groups (one `.week-block` each): Unit 01 … Unit 10 (three chips each), まとめテスト1 / 2 / 3 placed after Units 03 / 07 / 10 in book order, and 総合問題 (four chips).

---

## 5. What each kind of unit contains

**Grammar-point pages (`unit-NN-a/b`).** Each point in the book has: a number and heading (e.g. 「1 〜ができる／〜ことができる」); 接続 (connection); one or more 意味 (meanings, numbered ①②…) each followed by 2–6 example sentences, underlined at the target form; sometimes a 〜形の作り方 conjugation box, 注意 boxes with ×/○ sentences, a 復習 (review of an N5 pattern) box and `*` exceptional-use notes. Headphone icons mark CD sentences. The dictation page prints those CD sentences with the target part blank, grouped by point number.

**練習 pages (`unit-NN-renshuu`).** Typical sections: I `( ) にひらがなを1字ずつ書きなさい` (particles, one kana per box); II a conjugation table or `( ) のことばを適当な形にして___に書きなさい`; III more form-filling, or 正しいものに○をつけなさい (circle the right one of two or three); IV/V/VI `( ) に入るのはどれですか` (a–d). Many 練習 sentences re-use the example sentences.

**まとめテスト (`matome-N-a/b/c`).** Three 問題 with a score box: I particles (×1 point each), II forms (×1), III a–d (×2). The preface says most items reuse example and 練習 sentences, so each Why note should point back to the point number and page where it was taught.

**総合問題 (`sougou-N`).** Real JLPT N4 文法 format, in hiragana-heavy spacing: もんだい1 (fill the blank, a–d), もんだい2 (★ sentence ordering, 4 tiles), もんだい3 (a short passage with 5 numbered blanks, a–d). The preface says the four sets together cover all N4 grammar plus some N5.

---

## 6. Page format (section by section)

Copy the chrome from `n4/grammar/mimi-kara-oboeru/unit-01-a.html`: `auth.js` first in `<head>`, favicon, fonts, `style.css` + `day-page.css`, `<body class="level-page n4">`, the N4 header with `level-nav lv-n4` (Grammar active), footer and `main.js`. Depth 3, so assets are `../../../assets/...`. Breadcrumb: Home / JLPT N4 / Grammar / 耳から覚える N4 文法 (`index.html`) / <chip title>.

### Header (`.bp-header`)
- `.bp-week`: "JLPT N4 · Grammar · 耳から覚える N4 文法 — Unit NN (first〜last) ★…" with romaji.
- `h1`: the points on this page with romaji and a short English gloss.
- `.bp-meta-grid`: **Source** (book, Unit, points, printed pp = PDF pp, dictation page); **Grammar points covered** (`.bp-points` chips); **Answer key** (for points pages: "Dictation answers are the book's own CD sentences on p.N–M; the 解答 booklet does not list them"; for 練習/test pages: "Official, answers only — 解答 p.N (PDF M)" plus the answer string); **Audio** (`.ld-track` CD, Track N — not published); **Notes** (level ★, what is ours, register traps).

### Section 1 — Grammar Points (points pages)
One `.bp-point` per book point, exactly as `n1/grammar/week-1/day-1.html`:
- `h3` 【N】 form, plus a `.bp-badge` (★ level or register).
- Field table: Reading / Meaning (EN) / Meaning (HI) / Meaning (GU) / Connection (接続) / Register / Typical use. Where a point has 意味①②, give each meaning its own rows.
- `.bp-formation-table`: the book's 作り方 box in full (verb groups I/II/III). For points without a box, fill verb / い-adj / な-adj / noun, marking added cells `class="added"` and "(added, not in book)".
- `.bp-examples-table`: **every** example sentence of the point (Japanese + romaji, EN, HI, GU), in book order, with ① / ② labels. Mark CD sentences "(CD)" in the Japanese cell. Include 注意 ×/○ sentences and 復習 boxes as their own small example tables.
- `.bp-notes`: 2–4 short sentences, simple English for N4 learners.

For 練習 / test pages, Section 1 is a short "Patterns tested" recap (a `.bp-point` table: pattern, meaning EN/HI/GU, point number and book page), like `n5/multi-skill/tanki-master-drill/bunpou-1.html`.

### Section 2 — Quiz / Exercise
- **Dictation** (points pages): one `.bp-quiz` per sentence. `q-jp` = the gapped sentence as printed on the dictation page (+ romaji); `.bp-assembled` = the full sentence with the answer (+ romaji); `q-translations` EN/HI/GU; `.bp-why` = the answer, "CD sentence, p.N", and the point it tests.
- **練習 / まとめ fill-ins**: gapped sentence + romaji; full sentence + romaji; EN/HI/GU; "Book answer (解答 p.N): …"; Why note (why this particle/form, what the common wrong choice would mean).
- **Conjugation tables**: one `.bp-table` (dictionary form / each target form, with romaji), answers from the key.
- **○ choice and a–d**: `.bp-options` table (Option / Japanese / English / Hindi / Gujarati), correct row `class="correct"`; Why note covers every wrong option.
- **★ ordering (総合 もんだい2)**: tiles with romaji, `.bp-order-chain`, `.bp-assembled`, EN/HI/GU, and which tile is ★.
- **もんだい3 cloze passage**: do **not** transcribe the passage. Summarise it in 2–3 sentences (EN/HI/GU) and quote only the sentence around each blank.

### Section 3 — Confusion Pairs / Nuance Notes
A `.bp-confusion` table (Form / Meaning / Connection / Key difference / Use when) over the page's points (plus close points from other units, with their numbers), and a `.bp-callout` for the main exam trap. Required on every page.

### Day nav (`.bp-day-nav`)
Prev / next in unit-table order; the first and last pages link back to `index.html` ("Contents"). If the next page is not built yet, write `<span>Next: … — coming soon</span>` (no dead link); when you build a page, turn the previous page's "coming soon" span into a link.

### Hub update rule (`index.html`)
Change `<span class="day-chip soon" data-href="FILE.html">LABEL</span>` to `<a class="day-chip ready" href="FILE.html">LABEL</a>` and update the `.sample-note` header `<strong>In progress — N of 43 units built</strong>`. When N = 43, change it to `Complete — 43 of 43 units built` with the ✅ icon, as in the N5 Tanki hub.

---

## 7. Hard rules

- `<span class="romaji">` under **every** Japanese line: example sentences, gapped and full quiz sentences, options, formation examples, tiles, chips where practical.
- EN + Hindi + Gujarati for every meaning, example, question and option. Simple English: readers are N4 learners.
- Every question with the book's answer and its 解答 page. Dictation answers cite the CD sentence's page. If an item has no key, give a worked answer labelled **(our answer, not in book)**. Anything else we add (formation cells, extra notes) is labelled **(added, not in book)**.
- Never transcribe long passages (総合問題 もんだい3) in full: summarise and quote short key lines. The example sentences and short exercise sentences are fine to reproduce one by one.
- Never publish, link or embed audio. Track numbers only.
- No emoji glyphs in body text (the hub's `.sample-note` icon span is chrome).
- Reuse existing classes only (`style.css`, `day-page.css`). Do not edit CSS, JS, `tools/`, other courses or hub pages outside this course folder. `python tools/build_site.py` normalises the chrome later; do not run it as part of building a page.
- Checks before finishing a page: answers match the key (150–250 dpi), tags balance (`html.parser`), all relative links resolve, file ends with `</html>`, hub chip flipped and count updated.

---

**Reference implementation:** `n4/grammar/mimi-kara-oboeru/unit-01-a.html` (Unit 01, points 1–5 + their dictation).
