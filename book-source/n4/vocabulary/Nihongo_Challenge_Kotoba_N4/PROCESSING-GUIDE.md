# にほんごチャレンジ N4 ことば (Nihongo Challenge N4 Kotoba) — unit-by-unit processing guide

This guide covers turning `Nihongo_Challenge_Kotoba_N4.pdf` into the site's pages under `n4/vocabulary/nihongo-challenge/`. To build a unit, name it by its filename from the table in §4, then follow §5–§7.

Where this file is silent, the general vocabulary spec applies: `book-source/n1/vocabulary/PROCESSING-GUIDE.md` (word-list format, quiz format, confusion pairs), and for a lesson-type book with a reading text, `book-source/n5/textbooks/Chukyu_Honsatsu/PROCESSING-GUIDE.md`.

**Reference implementation:** `n4/vocabulary/nihongo-challenge/lesson-01.html` (① スーパーで買い物). Copy its structure, tone and depth.

---

## 1. Book identification

- **Title:** 「日本語能力試験」対策 にほんごチャレンジ N4 ことば (*Preparation for the Japanese Language Proficiency Test — Nihongo Challenge, Kotoba / Vocabulary / Vocabulário*).
- **Publisher:** アスク出版 (ASK), 2010-11-15 first edition (colophon, PDF 128). Translations: English and **Portuguese** (translator credits on the colophon) — the book is trilingual JP / EN / PT. We replace the Portuguese with Hindi and Gujarati; never copy the Portuguese.
- **What it is:** a themed, everyday-life vocabulary workbook for N4. "15〜20 N4 words per unit, 32 units and themes" (この本の使い方 p.12). Every 4 lessons there is a ふくしゅう問題 (revision set) in old-JLPT format; at the end, four まとめのテスト (final tests); then a 付表 (appendix of reference tables) and an index.
- **No audio.** The book has no CD.

## 2. Scan notes and offsets

- **144 PDF pages**, 476×722 pt, scanned images (Adobe Acrobat "Image Conversion"). **No usable text layer** (`get_text()` returns empty). Render with PyMuPDF (`import pymupdf; doc[i].get_pixmap(dpi=…)`, note `doc[i]` is 0-based, PDF page = i+1). 120–150 dpi reads body text; 200–250 dpi crops for furigana and to tell **bold** headwords from regular ones. Keep renders in the session scratchpad, never in the repo.
- The scan is clean and complete. Nothing is missing: every lesson has its 2 pages, every ふくしゅう and まとめ has its 2 pages, and every item in the key has its question page.

**Main book: PDF page = printed page (offset 0).** Verified on footers: PDF 16 → p.16, PDF 17 → 17, PDF 24 → 24, PDF 25 → 25, PDF 119 → 119, PDF 120 → 120, PDF 125 → 125, PDF 126 → 126. The cover is PDF 1 (= p.1).

| PDF pages | Content |
|---|---|
| 1 | Cover |
| 2 | はじめに (preface, JP/EN/PT) |
| 3–5 | もくじ (contents) |
| 6–11 | 新しい「日本語能力試験」N4 について (JLPT N4 explainer, JP / EN / PT) |
| 12–15 | この本の使い方 (how to use; **p.15 = notation legend**) |
| 16–95 | Lessons ①–㉜ (2 pp each) + ふくしゅう問題 1–8 (2 pp each) |
| 96–103 | まとめのテスト 1–4 (2 pp each) |
| 104–120 | 付表 (appendix tables) |
| 121–126 | ことばのさくいん (vocabulary index, gives the page where each word is taught) |
| 127 | blank (faint bleed-through) |
| 128 | colophon (ISBN 978-4-87217-758-9) |
| 129–144 | **別冊 訳と答え** bound in (see below) |

**別冊: PDF page = 別冊 printed page + 128.** PDF 129 = 別冊 cover (p.1, unnumbered). Verified: PDF 130 → 別冊 p.2, PDF 131 → 3, PDF 134 → 6, PDF 140 → 12, PDF 143 → 15. PDF 144 = blank (p.16).

| 別冊 pages | PDF | Content |
|---|---|---|
| p.2–6 | 130–134 | Translations of Texts (**English**) — each lesson's 文章 and もうちょっと, lessons 1–32 |
| p.7–11 | 135–139 | Tradução da Frase (Portuguese) — same texts. Not used |
| p.12–15 | 140–143 | **問題の答え** (answer key) |

Always cite as "別冊 p.N (PDF M)".

## 3. Answer-key status — complete, official, answers only

The 別冊 問題の答え gives the answer to **every** exercise: each lesson's れんしゅう 1 and 2, all ふくしゅう問題 and all four まとめのテスト. It gives **no explanations** — all "Why" notes are ours. The English text translations (別冊 p.2–6) are a reference for meaning only; write our own EN and never copy them verbatim.

| 別冊 page (PDF) | Covers |
|---|---|
| p.12 (PDF 140) | Lessons 1–8, ふくしゅう 1 and 2 |
| p.13 (PDF 141) | Lessons 9–18, ふくしゅう 3 and 4 |
| p.14 (PDF 142) | Lessons 19–28, ふくしゅう 5 and 6 |
| p.15 (PDF 143) | ふくしゅう 7, lessons 29–32, ふくしゅう 8, まとめのテスト 1–4 |

Key notation: lesson answers are `1 ① 2 ② 3 …` (れんしゅう 1, option number) and `2 ① a ② b …` (れんしゅう 2, letter). ふくしゅう / まとめ: 問題Ⅰ/Ⅱ/Ⅲ, boxed item number → option number.

Key quirks (do not "fix" them, mention them on the page):
- The key's headings differ slightly from the lesson pages: ④ is 「学校からの手紙」 (page: 子どもの学校からの手紙), ⑫ is 「旅行へ行こう」 (page and もくじ: 旅行に行こう), and **⑰ is 「インターネット」** (page and もくじ: 日本語勉強中). The answers match the lesson pages; use the lesson page's title.
- Lesson ㉛ れんしゅう 2 is a pairing task: the key gives `1 d 2 h 3 c 4 b 5 f 6 g 7 e`.
- Lessons ③ and ㉑ れんしゅう 2 use a word box a–d; lessons ④ and others use 1–4 (key gives numbers).
- Never change a key answer. If one looks odd (e.g. ふくしゅう1 問題Ⅱ-1 = 4, "ほとんどおわりました ≈ もうすぐおわります"), keep it and explain the book's logic in the Why note.

## 4. Unit table (50 units)

A unit = one lesson (2 pages, 15–20 words + exercises), one ふくしゅう問題 set (15 items), one まとめのテスト (15 items) or one 付表 group. Every unit is one study page of sensible size; none needs splitting.

File naming: `lesson-NN.html` (two digits), `fukushuu-N.html`, `matome-N.html`, `fuhyou-N.html`.

| File | Title | Romaji / English | Printed pp = PDF pp | Answer key |
|---|---|---|---|---|
| lesson-01.html | ① スーパーで買い物 | Suupaa de kaimono — Shopping at the supermarket | 16–17 | 別冊 p.12 (PDF 140) |
| lesson-02.html | ② ショッピング | Shoppingu — Shopping | 18–19 | p.12 (140) |
| lesson-03.html | ③ 近所迷惑 | Kinjo meiwaku — A neighbourhood nuisance | 20–21 | p.12 (140) |
| lesson-04.html | ④ 子どもの学校からの手紙 | Kodomo no gakkou kara no tegami — A letter from the children's school | 22–23 | p.12 (140) |
| fukushuu-1.html | ふくしゅう問題1 (①〜④) | Fukushuu mondai 1 — Revision 1 | 24–25 | p.12 (140) |
| lesson-05.html | ⑤ 引っ越し | Hikkoshi — Moving house | 26–27 | p.12 (140) |
| lesson-06.html | ⑥ 町 | Machi — A town | 28–29 | p.12 (140) |
| lesson-07.html | ⑦ 交通 | Koutsuu — Traffic | 30–31 | p.12 (140) |
| lesson-08.html | ⑧ 道をたずねる | Michi o tazuneru — Asking for directions | 32–33 | p.12 (140) |
| fukushuu-2.html | ふくしゅう問題2 (⑤〜⑧) | Revision 2 | 34–35 | p.12 (140) |
| lesson-09.html | ⑨ 母の誕生日 | Haha no tanjoubi — My mother's birthday | 36–37 | p.13 (141) |
| lesson-10.html | ⑩ パーティー | Paatii — A party | 38–39 | p.13 (141) |
| lesson-11.html | ⑪ ホテルの予約 | Hoteru no yoyaku — Making a hotel reservation | 40–41 | p.13 (141) |
| lesson-12.html | ⑫ 旅行に行こう | Ryokou ni ikou — Let's go on a trip | 42–43 | p.13 (141) |
| fukushuu-3.html | ふくしゅう問題3 (⑨〜⑫) | Revision 3 | 44–45 | p.13 (141) |
| lesson-13.html | ⑬ アルバイト | Arubaito — A part-time job | 46–47 | p.13 (141) |
| lesson-14.html | ⑭ 会社 | Kaisha — At the company | 48–49 | p.13 (141) |
| lesson-15.html | ⑮ ランチタイム | Ranchi taimu — Lunch time | 50–51 | p.13 (141) |
| lesson-16.html | ⑯ 仕事 | Shigoto — Work | 52–53 | p.13 (141) |
| fukushuu-4.html | ふくしゅう問題4 (⑬〜⑯) | Revision 4 | 54–55 | p.13 (141) |
| lesson-17.html | ⑰ 日本語勉強中 | Nihongo benkyouchuu — Studying Japanese | 56–57 | p.13 (141) — key calls it 「インターネット」 |
| lesson-18.html | ⑱ 大学生活 | Daigaku seikatsu — University life | 58–59 | p.13 (141) |
| lesson-19.html | ⑲ 将来の夢 | Shourai no yume — A dream for the future | 60–61 | p.14 (142) |
| lesson-20.html | ⑳ 子ども時代 | Kodomo jidai — Childhood | 62–63 | p.14 (142) |
| fukushuu-5.html | ふくしゅう問題5 (⑰〜⑳) | Revision 5 | 64–65 | p.14 (142) |
| lesson-21.html | ㉑ 風邪 | Kaze — A cold | 66–67 | p.14 (142) |
| lesson-22.html | ㉒ 落し物 | Otoshimono — Lost articles | 68–69 | p.14 (142) |
| lesson-23.html | ㉓ 忘れ物 | Wasuremono — Forgotten items | 70–71 | p.14 (142) |
| lesson-24.html | ㉔ 失敗 | Shippai — A mistake | 72–73 | p.14 (142) |
| fukushuu-6.html | ふくしゅう問題6 (㉑〜㉔) | Revision 6 | 74–75 | p.14 (142) |
| lesson-25.html | ㉕ 季節 | Kisetsu — Seasons | 76–77 | p.14 (142) |
| lesson-26.html | ㉖ 天気予報 | Tenki yohou — Weather forecast | 78–79 | p.14 (142) |
| lesson-27.html | ㉗ 事故 | Jiko — An accident | 80–81 | p.14 (142) |
| lesson-28.html | ㉘ 火事 | Kaji — A fire | 82–83 | p.14 (142) |
| fukushuu-7.html | ふくしゅう問題7 (㉕〜㉘) | Revision 7 | 84–85 | p.15 (143) |
| lesson-29.html | ㉙ 手紙 | Tegami — A letter | 86–87 | p.15 (143) |
| lesson-30.html | ㉚ 健康 | Kenkou — Health | 88–89 | p.15 (143) |
| lesson-31.html | ㉛ 趣味 | Shumi — Hobbies | 90–91 | p.15 (143) |
| lesson-32.html | ㉜ 会話はむずかしい | Kaiwa wa muzukashii — Conversation problems | 92–93 | p.15 (143) |
| fukushuu-8.html | ふくしゅう問題8 (㉙〜㉜) | Revision 8 | 94–95 | p.15 (143) |
| matome-1.html | まとめのテスト1 | Matome no tesuto 1 — Final test 1 | 96–97 | p.15 (143) |
| matome-2.html | まとめのテスト2 | Final test 2 | 98–99 | p.15 (143) |
| matome-3.html | まとめのテスト3 | Final test 3 | 100–101 | p.15 (143) |
| matome-4.html | まとめのテスト4 | Final test 4 | 102–103 | p.15 (143) |
| fuhyou-1.html | 付表 あいさつとよく使う表現 | Aisatsu to yoku tsukau hyougen — Greetings and common expressions (incl. 店員が使う表現, その他) | 104–105 | — (no exercises) |
| fuhyou-2.html | 付表 家族の呼び方・人の体・世界の国々・日本の47の地域 | Family terms, the body, countries, Japan's 47 prefectures | 106–109 | — |
| fuhyou-3.html | 付表 時間と数 | Jikan to kazu — Time and numbers (days, weeks, months, years, times of day, counters, calendar) | 110–113 | — |
| fuhyou-4.html | 付表 敬語・組み合わせて使うことば | Keigo; kumiawasete tsukau kotoba — Polite language; combined words (〜員, 〜会, 〜家, 〜代 …) | 114–115 | — |
| fuhyou-5.html | 付表 動詞 | Doushi — Verbs (Group I/II/III lists, verbs with many meanings, 自動詞・他動詞 pairs) | 116–118 | — |
| fuhyou-6.html | 付表 形容詞・副詞 | Keiyoushi・fukushi — Adjectives and adverbs (incl. 「ない」と使う副詞, 時間の副詞, 返事の副詞) | 119–120 | — |

The ことばのさくいん (p.121–126) is not a unit; use it to check which lesson first taught a word.

## 5. What each unit contains (book layout)

### Lesson (2 pages)
- **Page 1:** header bar (number, title, EN/PT title) · **文章** — a short 4–7 sentence text (diary, letter, dialogue or notice) with a picture; target words in **bold** · **新しいことば** — the word list: headword (bold = N4 word) with furigana, EN + PT gloss, and for most words one example sentence with EN + PT translation.
- **Page 2:** **もうちょっと** ("a little more") — a 2–4 line mini-text or A/B dialogue + 3–6 more words in the same format · **れんしゅう** — usually:
  - 1 (　)に入ることばをえらんでください — 3–4 items, 4 options (1–4);
  - 2 どちらがいいですか — 2–4 items, a/b choice. Variants: a word box (a–d) to match (③, ㉑), a paraphrase task 「＿＿とだいたい同じ意味の文」 (④), a pairing task 「ふたつが組になることば」 (㉛).
- Some lessons add a small boxed table of related words (seen on the contact sheet, confirm on the scan: ⑦ p.31 vehicles, ⑧ p.33 words for asking the way, ⑱ p.59 school stages, ㉕ p.77 seasonal events, ㉖ p.79 compass directions). Treat it as an extra word group.

### Notation (この本の使い方 p.15, PDF 15) — put it in the page's `.vd-legend`
| Book mark | Meaning | Our mark |
|---|---|---|
| **太字** (bold headword) | N4-level word | ★ before the headword |
| ➡ (black circle arrow) | 関連することば, related word | "Related:" in the Note column |
| ⇔-style (white circle arrow) | 反対の意味のことば, antonym | "⇔" in the Note column |
| N / V / (i.) / (t.) | noun / verb / intransitive / transitive | keep in Note |
| ☞p×× | see page ×× | "see p.×× (lesson N)" |
| ※ | footnote gloss under a text (e.g. ※警官 ☞p80) | translate in Note |

Kanji: 新しいことば and examples use normal newspaper kanji with furigana; ふくしゅう問題 deliberately use more kana (old-JLPT style). Keep the book's spelling exactly in quotes and options.

### ふくしゅう問題 (2 pages, 15 items)
- 問題Ⅰ (　)になにをいれますか — 10 items, 4 options (文脈規定).
- 問題Ⅱ つぎの＿＿の文とだいたいおなじいみの文はどれですか — 2 items, full-sentence options (言い換え類義).
- 問題Ⅲ つぎのことばのつかいかたでいちばんいいもの — 3 items, full-sentence options (用法). ふくしゅう5 has 問題Ⅲ ×2, ふくしゅう7 ×2 (check the key).

### まとめのテスト (2 pages, 15 items)
Same three 問題 as ふくしゅう (Ⅰ ×10, Ⅱ ×2–3, Ⅲ ×2–3; exact counts from the key on 別冊 p.15).

### 付表 (reference)
Picture pages and tables, no exercises and no answers. Rebuild them as word tables only (never embed the pictures).

## 6. Site page format

Pages live in `n4/vocabulary/nihongo-challenge/`, three levels deep (`../../../`). Copy the chrome from `lesson-01.html`: `auth.js` first in `<head>`, favicon, fonts, `style.css` + `day-page.css`, `body class="level-page n4"`, the N4 header with `level-nav` (Vocabulary active), footer, `main.js`. Breadcrumb: Home / JLPT N4 / Vocabulary / にほんごチャレンジ N4 ことば / ① スーパーで買い物 (unit short title). Reuse existing classes only.

### Lesson page, section by section
0. **`.bp-header`** — `.bp-week` = "JLPT N4 · Vocabulary · にほんごチャレンジ N4 ことば — Lesson N" (+ romaji). `h1` = number + title + romaji + English. `.bp-meta-grid`:
   - **Source:** printed p.X–Y (PDF X–Y, same numbers), what is on each page.
   - **Words (n):** `.bp-points` chips listing all headwords.
   - **Answer key:** "Official, answers only — 別冊 問題の答え p.N (PDF M)" + the full answer string.
   - **Notes:** the main traps of the lesson; "the book has no explanations: translations, Hindi/Gujarati, Why notes and §3 are ours".
1. **`.vd-legend`** — ★ = bold in book (N4 word), Related, ⇔, ☞ — only the marks that occur.
2. **§1 文章を読みましょう** (`.bp-point`) — a **summary in our own words** (EN/HI/GU, 2–3 sentences) and at most 3 short key lines quoted (JP + romaji + EN/HI/GU). Never transcribe the whole text.
3. **§1 Words** — `.bp-point` + `.kd-group-head` (h3 + `.bp-badge` "p.N") per book block: 新しいことば, then もうちょっと (its 2–4 line dialogue may be quoted line by line: it is short), then any boxed table. Each block is a `.vd-table-wrap` > `.vd-wordlist`: **Japanese** (★ + headword + `<span class="romaji">`) / **English** / **Hindi** / **Gujarati** / **Note** (related/antonym words with romaji; the book's example sentence with romaji + EN/HI/GU). Book order. Give our EN gloss (not a copy of the book's), and add a useful note (verb group, particle, kanji reading) where helpful.
4. **§2 れんしゅう** — section title, each instruction JP + romaji + EN/HI/GU, then one `.bp-quiz` per item: `q-label`, `q-jp` (sentence with blank + romaji), `q-translations` (completed sentence + romaji, EN/HI/GU), `.bp-options` (Option / Japanese / EN / HI / GU, `tr.correct`), `.bp-why` ending "Key: 別冊 p.N → answer".
5. **§3 Confusion pairs** — `.bp-confusion` (Form / Meaning / Key difference / Use when) from the lesson's words and distractors, plus one `.bp-callout` "Exam trap". Mark our example phrases as ours.
6. **`.bp-day-nav`** — back to contents + next unit. If the next unit is not built, write `<span>Next: … — coming soon</span>` (no dead link); when building a unit, turn the previous unit's span into a link.

### ふくしゅう / まとめ pages
Header as above (Source, Question types chips, Answer key, Notes). Then §1 "Words tested" — a `.vd-wordlist` of every target word and distractor, each with the lesson where the book teaches it (from the index). §2 every item as `.bp-quiz` (問題Ⅱ and Ⅲ: every full-sentence option translated EN/HI/GU). §3 confusion pairs.

### 付表 pages
Header + one `.vd-wordlist` (or `.bp-table` for counters/calendar) per book table, with romaji + EN/HI/GU. Describe picture-only pages in words. No quiz section (say "The appendix has no exercises").

### Hub update rule (`index.html`)
Each unit is one chip in its `.week-block` (Lessons ①–④ + ふくしゅう1, … , まとめのテスト, 付表). When a unit is built, change `<span class="day-chip soon" data-href="FILE.html">LABEL</span>` to `<a class="day-chip ready" href="FILE.html">LABEL</a>` and update the `.sample-note` to `In progress — N of 50 units built`. At 50, change it to `Complete — 50 of 50 units built`.

## 7. Hard rules

- **Romaji on every Japanese line** (`<span class="romaji">`): headwords, examples, quoted lines, questions, options, table cells. Hepburn, long vowels as ou/uu, ん before a vowel as n'.
- **EN + Hindi + Gujarati** for every meaning, example, question, option and summary. Simple English (N4 learners).
- **Every question with the book's answer**, citing 別冊 p.N (PDF M). The key is complete; never invent an answer. Anything else we add is labelled "(added, not in book)".
- **No long passages:** the 文章 is summarised, with at most 3 short key lines quoted. Don't copy the book's EN/PT translations.
- **Never reproduce the pictures**; describe them in one line if a question depends on them.
- No emoji in body text. No audio (the book has none). Don't edit CSS, JS, `tools/`, other courses or hub pages other than this course's `index.html`.

## 8. Checks before finishing a unit

- Every answer matches the 別冊 grid (re-read at 150 dpi).
- Every Japanese line has romaji; every meaning has EN/HI/GU.
- Tags balance (Python `html.parser`), relative links resolve, file ends with `</html>`.
- Hub chip flipped and count updated; previous unit's "coming soon" span turned into a link.
