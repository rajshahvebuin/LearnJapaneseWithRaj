# にほんごチャレンジ N4［文法と読む練習］ — unit-by-unit processing guide

This guide turns `Nihongo_Challenge_Bunpo_to_Yomu_N4.pdf` into the site pages under `n4/multi-skill/nihongo-challenge/`. To build a unit, take its file name from the table in §4 and follow the steps below.

Where this file says nothing, use the general guides:
- grammar → `book-source/n1/grammar/PROCESSING-GUIDE.md`
- reading → `book-source/n1/reading/PROCESSING-GUIDE.md`
- book-course conventions → `book-source/n5/multi-skill/Tanki_Master_Drill_N5/PROCESSING-GUIDE.md`

---

## 1. Book identification

- **Title:** 「日本語能力試験」対策 にほんごチャレンジ N4［文法と読む練習］ (Nihongo Challenge N4: Bunpou to yomu renshuu, *Grammar and Reading practice*). The file name says "Bunpo to Yomu"; the printed title is 文法と読む練習. Authors 山辺真理子・飯塚睦・金成フミ恵; publisher 株式会社アスク出版 (ASK); first edition 2010-11-12, our scan is the 3rd printing (2011-10-31); ISBN 978-4-87217-756-5 (colophon, p.240). The glosses and 別冊 are in **English and Brazilian Portuguese** (no Hindi/Gujarati, so those are always ours).
- **Level:** JLPT N4. The book says it chose about 150 文型・接続詞 from the old 3級 syllabus (p.18).
- **What it covers:** two parts plus a 別冊 (supplementary volume).
  - **PART 1 文法** (grammar): 32 story chapters (第1話–第32話), one every few weeks of a year (each title page carries a month tag such as 「1月-1」). After every 4 話 there is a ふくしゅう問題 (8 in total). Then four end sections: 「他動詞」と「自動詞」, 文と文をつなぐことば（接続詞）, 文章の文法 問題1–5 and 文法ふくしゅうテスト.
  - **PART 2 読解** (reading): 15 short texts (第1回–第15回), plus three 読むときに大切なこと tip boxes and a reference list 会話のときのことば.
  - **別冊**: grammar explanations and translations of every example (English p.3–30, Portuguese p.31–57), then all answers (p.58–78).
- **Story characters** (p.24): カルロス (Brazil, 18, factory worker, main character), マリア (Philippines, 25), ノーイ (Thailand, 22), ピーター (Australia, 27), ロベルト (Brazil, 28, Carlos's cousin), のり子 (Japanese, 20, volunteer Japanese teacher), 小林さん (Japanese, 60, Carlos's landlord). Name them the same way on every page.

---

## 2. Scan notes and page offsets

- **320 PDF pages, scanned, no text layer** (`get_text()` returns nothing). The PDF bookmarks are useless (`Gr_N40001` … one per page). Render with PyMuPDF: `import pymupdf; doc[i-1].get_pixmap(dpi=150)`. 120–150 dpi reads the body text; use 250–300 dpi crops for the furigana and the small English/Portuguese glosses. Keep renders in the scratchpad, never in the repo.
- **Main book: PDF page = printed page** (offset 0). Verified on footers: PDF 4 → p.4, 26 → 26, 28 → 28, 58 → 58, 168 → 168, 204 → 204, 237 → 237. PDF 240 is the colophon.
- **別冊: PDF page = 別冊 page + 240.** PDF 241 = 別冊 cover (p.1), PDF 242 blank, PDF 243 → p.3, 271 → 31, 298 → 58, 305 → 65, 313 → 73, 318 → 78. PDF 319 is blank, PDF 320 is the back cover. Always cite as "別冊 p.N (PDF M)".
- Nothing is missing. Every 練習問題 has its key row, the page sequence is continuous, and the 別冊 is complete.
- Front matter: p.2–3 forewords, p.4–8 もくじ, p.9–17 notes on the N4 exam (JP/EN/PT), p.18–21 この本の使い方, p.22–23 接続の表し方 (connection notation: N, V, Vます形, Vない形, Vた形, Vじしょ形, い形/な形, Vふつう形…), p.24 characters, p.25 PART 1 divider, p.203 PART 2 divider.
- The book icon next to each 文型 on a 話 title page prints two numbers, e.g. `3 / 31`: the **English** 別冊 page and the **Portuguese** 別冊 page for that point. Use the English one.

---

## 3. Answer-key status

The key is **complete and official**, in the 別冊.

| Section | Where | What the key gives |
|---|---|---|
| 第1–13話 練習問題, ふくしゅう問題1–3 | 別冊 p.58 (PDF 298) | Answer numbers only. ふくしゅう 問題II (Q11–15, ★ ordering) also gives the full order, e.g. `2 (4→1→3→2)` |
| 第14–27話, ふくしゅう問題4–6 | 別冊 p.59 (PDF 299) | as above |
| 第28–32話, ふくしゅう問題7–8 | 別冊 p.60 (PDF 300) top | as above. Some ★ items accept a second order: 「でも(…)でもよい」. Quote both |
| 接続詞 (p.172–179) | 別冊 p.60–65 (PDF 300–305) | EN/PT translations of the example sentences and model answers to each チャレンジ |
| 文章の文法 問題1–5 | 別冊 p.65–68 (PDF 305–308) | Answer + explanation (JP, EN, PT), often with a cross-reference "(p.92 文型4)" |
| 文法ふくしゅうテスト | 別冊 p.68–72 (PDF 308–312) | 問題I (Q1–15) and 問題II (Q16–20, with order): answers only, p.68. 問題III [問題1]–[問題5]: answer + explanation, p.68–72 |
| 読解 第1–15回 | 別冊 p.73–78 (PDF 313–318) | Answer + explanation (JP, EN, PT). ①–④ p.73, ④–⑦ p.74, ⑦–⑨ p.75, ⑨–⑪ p.76, ⑪–⑭ p.77, ⑭–⑮ p.78 |
| チャレンジ in each 話, 他動詞・自動詞 quiz | **bottom of the same page in the main book** (`▶▶▶答え`) | Answers only |

**The 練習問題 have no explanations.** Every "Why" note for them is ours. For sections with an official explanation (文章の文法, テスト 問題III, 読解), base the Why note on the book's explanation, in our own words, and cite the 別冊 page. Never change a book answer. If one looks wrong, keep it and flag it in the Why note.

Full 練習問題 key (transcribed at 150 dpi from 別冊 p.58–60; re-check against the scan when building):

| Block | Answers |
|---|---|
| 第1話 | 1-3 2-1 3-2 4-3 5-3 6-3 7-1 8-4 9-2 10-4 |
| 第2話 | 1-2 2-3 3-4 4-3 5-1 6-2 7-2 8-2 9-3 10-3 |
| 第3話 | 1-4 2-3 3-1 4-3 5-1 6-2 7-3 8-4 9-2 10-1 |
| 第4話 | 1-2 2-3 3-1 4-2 5-3 6-1 7-1 8-3 9-1 10-4 |
| ふくしゅう1 | I: 1-2 2-3 3-2 4-1 5-3 6-4 7-2 8-2 9-3 10-4 · II: 11-2 (4→1→3→2) 12-1 (1→3→4→2) 13-3 (2→4→3→1) 14-3 (4→1→3→2) 15-4 (3→4→2→1) |
| 第5話 | 1-3 2-1 3-3 4-2 5-3 6-4 7-4 8-4 9-3 10-1 |
| 第6話 | 1-2 2-2 3-3 4-3 5-2 6-1 7-4 8-2 9-3 10-2 |
| 第7話 | 1-3 2-3 3-1 4-4 5-3 6-2 7-4 8-1 9-2 10-3 |
| 第8話 | 1-2 2-4 3-2 4-2 5-3 6-3 7-4 8-1 9-2 10-2 |
| ふくしゅう2 | I: 1-3 2-4 3-1 4-2 5-1 6-2 7-3 8-2 9-4 10-3 · II: 11-1 (3→4→2→1) 12-3 (3→1→4→2) 13-3 (4→1→3→2) 14-2 (3→2→4→1) 15-1 (3→1→4→2) |
| 第9話 | 1-2 2-4 3-2 4-2 5-3 6-3 7-2 8-3 9-1 10-1 |
| 第10話 | 1-2 2-3 3-2 4-1 5-1 6-3 7-1 8-2 9-4 10-3 |
| 第11話 | 1-1 2-3 3-1 4-1 5-3 6-4 7-2 8-1 9-3 10-2 |
| 第12話 | 1-2 2-1 3-2 4-3 5-4 6-1 7-2 8-3 9-2 10-1 |
| ふくしゅう3 | I: 1-2 2-4 3-3 4-2 5-1 6-3 7-1 8-4 9-2 10-3 · II: 11-3 (2→4→3→1) 12-1 (4→2→1→3) 13-2 (4→2→3→1) 14-3 (4→1→3→2) 15-4 (4→3→2→1) |
| 第13話 | 1-2 2-2 3-4 4-1 5-3 6-2 7-2 8-2 9-3 10-1 |
| 第14話 | 1-1 2-2 3-1 4-1 5-3 6-1 7-4 8-1 9-4 10-2 |
| 第15話 | 1-2 2-2 3-3 4-1 5-1 6-4 7-2 8-3 9-2 10-1 |
| 第16話 | 1-4 2-2 3-1 4-4 5-4 6-4 7-1 8-2 9-2 10-4 |
| ふくしゅう4 | I: 1-3 2-2 3-1 4-3 5-1 6-3 7-1 8-4 9-2 10-2 · II: 11-2 (3→4→1→2) 12-3 (2→4→3→1) 13-4 (2→4→3→1) 14-1 (4→3→2→1) 15-3 (4→2→3→1; also 2→4→3→1) |
| 第17話 | 1-4 2-1 3-1 4-4 5-4 6-3 7-4 8-2 9-3 10-3 |
| 第18話 | 1-3 2-1 3-3 4-1 5-2 6-4 7-4 8-2 9-2 10-3 |
| 第19話 | 1-2 2-4 3-3 4-2 5-4 6-4 7-3 8-4 9-3 10-3 |
| 第20話 | 1-2 2-4 3-2 4-2 5-1 6-1 7-2 8-1 9-4 10-1 |
| ふくしゅう5 | I: 1-3 2-2 3-1 4-3 5-4 6-3 7-4 8-4 9-1 10-3 · II: 11-2 (3→2→4→1) 12-1 (1→2→4→3) 13-2 (3→1→2→4) 14-4 (2→4→1→3) 15-3 (4→2→3→1; also 2→4→3→1) |
| 第21話 | 1-3 2-3 3-1 4-3 5-3 6-2 7-2 8-3 9-4 10-1 |
| 第22話 | 1-1 2-4 3-3 4-1 5-2 6-2 7-2 8-3 9-3 10-3 |
| 第23話 | 1-3 2-2 3-1 4-4 5-2 6-3 7-3 8-1 9-3 10-3 |
| 第24話 | 1-1 2-1 3-2 4-1 5-4 6-3 7-3 8-2 9-1 10-3 |
| ふくしゅう6 | I: 1-1 2-3 3-4 4-3 5-2 6-1 7-1 8-2 9-3 10-4 · II: 11-3 (1→4→3→2) 12-4 (1→3→4→2) 13-1 (4→1→3→2) 14-2 (4→1→2→3) 15-3 (3→2→1→4) |
| 第25話 | 1-3 2-1 3-4 4-4 5-3 6-2 7-3 8-3 9-4 10-1 |
| 第26話 | 1-2 2-4 3-3 4-1 5-3 6-1 7-2 8-3 9-2 10-1 |
| 第27話 | 1-3 2-3 3-4 4-1 5-3 6-3 7-3 8-1 9-3 10-2 |
| 第28話 | 1-1 2-2 3-1 4-4 5-1 6-3 7-4 8-1 9-2 10-3 |
| ふくしゅう7 | I: 1-2 2-3 3-2 4-1 5-3 6-4 7-4 8-3 9-1 10-2 · II: 11-2 (3→2→4→1) 12-3 (2→1→4→3; also 1→2→4→3) 13-1 (4→3→1→2) 14-2 (3→4→2→1) 15-1 (4→2→1→3) |
| 第29話 | 1-4 2-3 3-3 4-2 5-1 6-4 7-2 8-2 9-3 10-3 |
| 第30話 | 1-3 2-3 3-2 4-1 5-3 6-4 7-2 8-1 9-2 10-1 |
| 第31話 | 1-2 2-4 3-3 4-4 5-4 6-1 7-2 8-3 9-1 10-2 |
| 第32話 | 1-1 2-3 3-1 4-4 5-3 6-2 7-4 8-1 9-2 10-2 |
| ふくしゅう8 | I: 1-2 2-3 3-1 4-4 5-3 6-3 7-4 8-2 9-1 10-2 · II: 11-2 (3→2→1→4; also 3→2→4→1) 12-3 (2→4→1→3) 13-3 (1→3→2→4) 14-1 (4→2→3→1; also 2→4→3→1) 15-2 (3→1→2→4; also 1→3→2→4) |
| 文法ふくしゅうテスト | I: 1-2 2-3 3-1 4-4 5-2 6-2 7-4 8-1 9-4 10-2 11-3 12-2 13-1 14-2 15-2 · II: 16-4 (4→3→1→2) 17-1 (2→4→1→3) 18-4 (2→3→4→1; also 3→2→4→1) 19-3 (2→3→4→1) 20-2 (4→2→3→1) |

---

## 4. Unit table (56 units)

One unit = one study page. A 話 is always 4 pages and is one unit. Each ふくしゅう問題 is its own unit (15 questions). Long end sections are split. Short reading texts are paired so that each page has 2–4 questions.

### PART 1 文法 — 第1話–第32話 (`wa-01.html` … `wa-32.html`)

| File | Title | Romaji / English | Grammar points (from もくじ) | Printed = PDF pp | 練習問題 p. | Answer key |
|---|---|---|---|---|---|---|
| wa-01.html | 第1話 日本のお正月 | Nihon no oshougatsu — New Year's in Japan | 〜ます・〜ません／〜ました・〜ませんでした／〜から〜まで／【場所】で | 26–29 | 28 | 別冊 p.58 (PDF 298) |
| wa-02.html | 第2話 雪が降りました | Yuki ga furimashita — It snowed | 〜ながら、…／〜たい・〜たくない／〜ことがある | 30–33 | 32 | p.58 (298) |
| wa-03.html | 第3話 ボランティア教室へ | Borantia kyoushitsu e — To the volunteer class | 〜てください／〜てから、…／〜たことがある・〜たことがない | 34–37 | 36 | p.58 (298) |
| wa-04.html | 第4話 好きな人にチョコレートを！ | Suki na hito ni chokoreeto o — Chocolate for the one you love | もらう／くれる／あげる・やる／〜から、… | 38–41 | 40 | p.58 (298) |
| fukushu-1.html | ふくしゅう問題1（第1–4話） | Fukushuu mondai 1 — Revision 1 | 問題I Q1–10, 問題II Q11–15 (★) | 42–43 | — | p.58 (298) |
| wa-05.html | 第5話 フットサルのチームに入る | Futtosaru no chiimu ni hairu — Joining the futsal team | 〜ことになる／〜かどうか、…／〜ようになる／〜だす | 44–47 | 46 | p.58 (298) |
| wa-06.html | 第6話 日本料理を作りたい！ | Nihon ryouri o tsukuritai — I want to make Japanese food | 〜てもらう／〜てくれる／〜てあげる・〜てやる／〜始める・〜終わる | 48–51 | 50 | p.58 (298) |
| wa-07.html | 第7話 けがをした！ | Kega o shita — I hurt myself | 〜たり(…たり)する／〜たまま、…／〜たらどう？／〜ても、… | 52–55 | 54 | p.58 (298) |
| wa-08.html | 第8話 日本人は桜が大好き | Nihonjin wa sakura ga daisuki — The Japanese love cherry blossoms | 〜ておく／〜てもいい・〜てもかまわない／〜つづける／〜という… | 56–59 | 58 | p.58 (298) |
| fukushu-2.html | ふくしゅう問題2（第5–8話） | Revision 2 | 問題I Q1–10, 問題II Q11–15 | 60–61 | — | p.58 (298) |
| wa-09.html | 第9話 自転車に乗りたい！ | Jitensha ni noritai — I want to ride a bicycle | 〜かた／〜てみる／〜やすい・〜にくい | 62–65 | 64 | p.58 (298) |
| wa-10.html | 第10話 自転車がない！ | Jitensha ga nai — Where's my bicycle? | 〜ている／〜てある／〜のに、… | 66–69 | 68 | p.58 (298) |
| wa-11.html | 第11話 日本人の家を訪ねる | Nihonjin no ie o tazuneru — Visiting a Japanese home | いただく・くださる・さしあげる／お〜になる・ご〜になる／〈そんけい語の特別な形〉／お〜する・ご〜する | 70–73 | 72 | p.58 (298) |
| wa-12.html | 第12話 どんな人が好き？ | Donna hito ga suki — Who is your type? | 〜ば、…／〜なら、…／〜とか…とか／〜し、(…し) | 74–77 | 76 | p.58 (298) |
| fukushu-3.html | ふくしゅう問題3（第9–12話） | Revision 3 | 問題I, 問題II | 78–79 | — | p.58 (298) |
| wa-13.html | 第13話 パンにカビが！ | Pan ni kabi ga — My bread is moldy | 〜と、…／〜たら、…／〜ほうがいい | 80–83 | 82 | p.58 (298) |
| wa-14.html | 第14話 待ち合わせはだいじょうぶ？ | Machiawase wa daijoubu — Stood up? | 〜ように、…／〜はず／〜はずがない／〜かもしれない | 84–87 | 86 | p.59 (299) |
| wa-15.html | 第15話 日本の大学 | Nihon no daigaku — Japanese university | 〜そう〈様態〉／【ぎもん詞】+か／【ぎもん詞】+でも／〜ようにする | 88–91 | 90 | p.59 (299) |
| wa-16.html | 第16話 アルバイトの面接 | Arubaito no mensetsu — A part-time job interview | 〜られる〈かのう形〉／〜ことができる／〜んです／〜んですが、… | 92–95 | 94 | p.59 (299) |
| fukushu-4.html | ふくしゅう問題4（第13–16話） | Revision 4 | 問題I, 問題II | 96–97 | — | p.59 (299) |
| wa-17.html | 第17話 約束の時間に遅れると大変！ | Yakusoku no jikan ni okureru to taihen — Never be late | 〜なければならない・〜なくてはいけない／〜なくてもいい・〜なくてもかまわない／〜てはいけない・〜てはだめ／〜の？ | 98–101 | 100 | p.59 (299) |
| wa-18.html | 第18話 ゆかたで花火大会へ！ | Yukata de hanabi taikai e — To the fireworks in a yukata | 〜そうだ〈伝聞〉／〜ようだ〈比ゆ〉／〜に行く・〜に来る・〜に帰る | 102–105 | 104 | p.59 (299) |
| wa-19.html | 第19話 道を聞く | Michi o kiku — Asking for directions | 〜て、…／〜てしまう／〜ずに、…／【場所】を | 106–109 | 108 | p.59 (299) |
| wa-20.html | 第20話 デパートで | Depaato de — At the department store | 〈けんじょう語の特別な形〉／ございます／〜でございます／お〜ください・ご〜ください | 110–113 | 112 | p.59 (299) |
| fukushu-5.html | ふくしゅう問題5（第17–20話） | Revision 5 | 問題I, 問題II | 114–115 | — | p.59 (299) |
| wa-21.html | 第21話 はじめてのデート | Hajimete no deeto — The first date | 〜ことにする／〜つもりだ・〜つもりはない／〜ようだ／〜でも | 116–119 | 118 | p.59 (299) |
| wa-22.html | 第22話 地震はこわい！ | Jishin wa kowai — Earthquakes are scary | 〜まえに、…／〜あと(で)、…／〜の〈名詞化〉 | 120–123 | 122 | p.59 (299) |
| wa-23.html | 第23話 仕事と家族とどちらが大切？ | Shigoto to kazoku to dochira ga taisetsu — Work or family? | 〜と…(と)、どちら〜？・〜と…(と)、どちらも〜ない／〜より…ほうが、〜／〜が/は…より、〜／〜ため(に)、… | 124–127 | 126 | p.59 (299) |
| wa-24.html | 第24話 自分の気持ちを相手に伝える | Jibun no kimochi o aite ni tsutaeru — Telling others how you feel | 〜(よ)う〈いこう形〉／〜だろう・〜だろうと思う／〜と言う／〜(よ)うとする | 128–131 | 130 | p.59 (299) |
| fukushu-6.html | ふくしゅう問題6（第21–24話） | Revision 6 | 問題I, 問題II | 132–133 | — | p.59 (299) |
| wa-25.html | 第25話 ふられて悲しい… | Furarete kanashii — Being rejected hurts | 〜(ら)れる〈うけみ形〉／〜ので、…／〜になる・〜くなる | 134–137 | 136 | p.59 (299) |
| wa-26.html | 第26話 元気出して！ | Genki dashite — Snap out of it! | 〜にする・〜くする／〜ところ／〜(ら)れる〈ものが主語のうけみ〉 | 138–141 | 140 | p.59 (299) |
| wa-27.html | 第27話 ごみの捨て方、知っていますか？ | Gomi no sutekata, shitte imasu ka — Throwing out garbage | 〜なさい／〜ように言う／〜(さ)せる〈しえき形〉／〜(さ)せられる〈しえきうけみ形〉 | 142–145 | 144 | p.59 (299) |
| wa-28.html | 第28話 秋の京都に行こう！ | Aki no Kyouto ni ikou — Let's visit Kyoto in autumn | 〜らしい〈推量〉／〜までに、…／〜が見える・〜が聞こえる | 146–149 | 148 | p.60 (300) |
| fukushu-7.html | ふくしゅう問題7（第25–28話） | Revision 7 | 問題I, 問題II | 150–151 | — | p.60 (300) |
| wa-29.html | 第29話 夜は静かに！ | Yoru wa shizuka ni — Keep it down at night | 〜がっている・〜がる／〜な〈きんし形〉／〈めいれい形〉 | 152–155 | 154 | p.60 (300) |
| wa-30.html | 第30話 いい部屋を見つけるのは、むずかしい！ | Ii heya o mitsukeru no wa muzukashii — Hard to find a nice room | 〜すぎる／〜は…ほど〜ない／〜さ／〜にする | 156–159 | 158 | p.60 (300) |
| wa-31.html | 第31話 お金がない！ | Okane ga nai — I'm broke | 〜しか…ない・〜も・〜で／〜ばかり／〜らしい〈てんけい的〉／〜(よ)うと思う | 160–163 | 162 | p.60 (300) |
| wa-32.html | 第32話 みんなと仲よくしていきたい | Minna to nakayoku shite ikitai — Getting along with everyone | 【におい・音・味】がする／【ぎもん詞】〜か、…／〜ていく・〜てくる | 164–167 | 166 | p.60 (300) |
| fukushu-8.html | ふくしゅう問題8（第29–32話） | Revision 8 | 問題I, 問題II | 168–169 | — | p.60 (300) |

### PART 1 end sections

| File | Title | Romaji / English | Contents | Printed = PDF pp | Answers |
|---|---|---|---|---|---|
| tadoushi-jidoushi.html | 「他動詞」と「自動詞」 | Tadoushi to jidoushi — Transitive and intransitive verbs | Pair table (落とす／落ちる …) + どっちを使う？ picture quiz (4 items) | 170–171 | bottom of p.171 |
| setsuzokushi-1.html | 接続詞 1: そして・それから・それに・そのうえ／だから・それで・すると | Setsuzokushi 1 — Conjunctions (adding, cause/result) | Explanations, examples, チャレンジ | 172–175 | 別冊 p.60–62 (PDF 300–302) |
| setsuzokushi-2.html | 接続詞 2: けれど・でも・しかし・ところが／たとえば／それでは・では・じゃあ・ところで | Setsuzokushi 2 — Conjunctions (contrast, example, topic change) | Explanations, examples, チャレンジ | 176–179 | 別冊 p.62–65 (PDF 302–305) |
| bunsho-bunpou-1.html | 文章の文法 問題1–3 | Bunshou no bunpou — Text grammar 1–3 | Three 200–300-character texts, 5 blanks each (15 Qs) | 180–185 | 別冊 p.65–67 (PDF 305–307) |
| bunsho-bunpou-2.html | 文章の文法 問題4–5 | Text grammar 4–5 | 問題4 回転ずし guide, 問題5 lost-dog notice (10 Qs) | 186–189 | 別冊 p.67–68 (PDF 307–308) |
| bunpou-test-1.html | 文法ふくしゅうテスト 問題I・II | Bunpou fukushuu tesuto — Grammar revision test I–II | 問題I Q1–15 (blank), 問題II Q16–20 (★) | 190–191 | 別冊 p.68 (PDF 308) |
| bunpou-test-2.html | 文法ふくしゅうテスト 問題III [問題1–3] | Grammar revision test III, texts 1–3 | 3 texts × 5 blanks | 192–197 | 別冊 p.68–70 (PDF 308–310) |
| bunpou-test-3.html | 文法ふくしゅうテスト 問題III [問題4–5] | Grammar revision test III, texts 4–5 | 2 texts × 5 blanks | 198–201 | 別冊 p.70–72 (PDF 310–312) |

### PART 2 読解 (`dokkai-1.html` … `dokkai-8.html`)

| File | Texts | Romaji / English | Printed = PDF pp | Answers |
|---|---|---|---|---|
| dokkai-1.html | 第1回 バレンタインデー · 第2回 フィリピンのお正月 · 第3回 けいたいメール + 読むときに大切なこと1・2 | Valentine's Day · New Year in the Philippines · Text messages · Reading tips 1–2 | 204–207 | 別冊 p.73 (PDF 313) |
| dokkai-2.html | 第4回 アルバイトのチラシ · 第5回 料理教室 | Part-time job leaflet · Cooking class | 208–211 | p.73–74 (313–314) |
| dokkai-3.html | 第6回 温泉が大好き · 第7回 インフルエンザ | We love onsen · Influenza | 212–215 | p.74 (314) |
| dokkai-4.html | 第8回 レジ袋の有料化 · 第9回 七夕に願いごとを | Charging for shopping bags · A wish on Tanabata | 216–219 | p.75 (315) |
| dokkai-5.html | 第10回 「今度、遊びに来てください」ってどういう意味？ + 読むときに大切なこと3〈情報検索の問題〉 | What does "come over sometime" mean? · Reading tip 3 (information search) | 220–223 | p.76 (316) |
| dokkai-6.html | 第11回 工場での健康診断 · 第12回 クーポン・マガジン | Health check at the factory · Coupon magazine | 224–227 | p.76–77 (316–317) |
| dokkai-7.html | 第13回 病院の薬 · 第14回 今日のランチ | Medicine from the hospital · Today's lunch | 228–231 | p.77–78 (317–318) |
| dokkai-8.html | 第15回 部屋探し + 会話のときのことば | House hunting · Conversational language | 232–236 | p.78 (318) |

Not units: p.237–239 文型さくいん (pattern index) and p.240 colophon. Use the index only to look up where a pattern is taught.

---

## 5. Inside a unit (book layout)

**A 話 (4 pages):**
1. **Title page** (p.1): month tag + 第N話 + title (JP/EN/PT), a picture with one theme line, then the 文型 list numbered 1–4 in large grey digits. Each 文型 shows a sample phrase, the connection (e.g. `Vます+ませんでした`, `N1【場所/時】からN2【場所/時】まで`), an EN/PT gloss, and the 別冊 book icon. When a 文型 has two uses they are ①, ②.
2. **Examples page** (p.2): one box per 文型. The box opens with the story sentence (with a picture), then 4 numbered examples ❶–❹, each tagged …① / …② when the 文型 has two uses. The first sentences of the boxes join into the chapter's story.
3. **練習問題** (p.3): 10 questions, "＿＿に何を入れますか。1・2・3・4からいちばんいいものを一つえらんでください。" Difficult words carry a `*` with an EN/PT gloss under the question. The corner icon gives the 別冊 answer page.
4. **もうちょっと** (p.4): extra notes (verb-form tables, a related word list, culture notes), one or two **チャレンジ** (write-in or choose), and the チャレンジ answers in a `▶▶▶答え` strip at the bottom.

The 別冊 English pages give, per 文型: the meaning, the usage notes marked `*` (JP + EN), and an English translation of the story sentence and of every ❶–❹ example. Use those translations as the base for our EN column, then give our own HI and GU.

**ふくしゅう問題** (2 pages): 問題I Q1–10 (fill the blank), 問題II Q11–15 (★ sentence ordering: four parts, the ★ slot is the answer).

**読解 回** (1–2 pages): the text (200–450 characters, or a notice, menu, table or coupon page), 1–3 questions, and a ことば box of glosses (JP/EN/PT).

---

## 6. Site page format

Pages live in `n4/multi-skill/nihongo-challenge/`, at depth 3. Copy the chrome from `wa-01.html`: `auth.js` first in `<head>`, favicon, fonts, `style.css` + `day-page.css`, `body class="level-page n4"`, the N4 `level-nav` with **All-in-one** active, footer and `main.js`. Breadcrumb: Home / JLPT N4 / All-in-one / にほんごチャレンジ N4 / <unit short title>. Reuse existing classes only. **Do not edit CSS or JS.**

### 6a. 話 pages (`wa-NN.html`), in this order

0. **`.bp-header`**:
   - `.bp-week` = "JLPT N4 · All-in-one · にほんごチャレンジ N4 — PART 1 文法 · <month tag>"; `h1` = 第N話 + title + romaji/English.
   - Meta grid: **Source** (printed = PDF pages, which page holds what); **Grammar points** (chips); **Answer key** ("Official, answers only — 別冊 p.N (PDF M)" + the full string; チャレンジ answers: bottom of p.X); **Notes** (what is the book's and what is ours: the 別冊 gives EN/PT translations of the examples and short usage notes; HI/GU, romaji, Why notes and §4 are ours).
1. **Story & theme**: the title-page theme line (JP + romaji + EN/HI/GU) and a 2–3 sentence summary of the story told by the first sentences of the example boxes. Quote the story sentences one per grammar point (they are short single sentences, so quoting them is allowed).
2. **Grammar points**: one `.bp-point` per numbered 文型 (split ①/② uses into rows, not separate points). Each has:
   - a field table: Reading, Meaning EN/HI/GU, Connection (接続) exactly as the book prints it, Typical use (from the 別冊 notes, in our words);
   - a `bp-formation-table`. Any form the book does not show goes in `class="added"` cells marked "(added, not in book)";
   - an examples table with the story sentence and **every** ❶–❹ example: Japanese + romaji, EN, HI, GU;
   - 1–3 sentences of notes.
3. **練習問題**: every question in a `.bp-quiz`: the sentence with ＿＿ + romaji, EN/HI/GU of the completed sentence, a `bp-options` table (Option / Japanese / English / Hindi / Gujarati) with the correct row `class="correct"` and ✓, the book's `*` glosses in the translations, and a `bp-why` note (ours).
4. **もうちょっと**: the extra table or notes (verb tables as `bp-table`, word lists as `vd-wordlist` with JP + romaji, EN, HI, GU, Note) and each チャレンジ with the book's answer from the bottom strip (cite the page). If a チャレンジ is open-ended and the strip gives only one answer, say so and add a second model marked "(our answer, not in book)".
5. **Confusion pairs**: a `.bp-confusion` table (Form / Meaning / Key difference with HI/GU / Use when) for this chapter's points and their usual N4 rivals, plus one `.bp-callout` exam trap.
6. **`.bp-day-nav`**: prev / next unit in §4 order. The first unit's prev is the course `index.html`. An unbuilt neighbour is written as plain text `<span>Next: … — coming soon</span>`; when you build a unit, turn the previous unit's "coming soon" span into a link.

### 6b. ふくしゅう / テスト 問題I・II pages
Header as 6a (patterns tested as chips). Short "Patterns tested" table (pattern, EN/HI/GU, which 話 teaches it, Q). Then every question as in 6a §3. For ★ ordering: the four parts with romaji and meaning, the assembled sentence (`.bp-assembled`) with EN/HI/GU, the order chain (`.bp-order-chain`) and the ★ answer. Where the key allows a second order (「でもよい」), show both. Then confusion pairs and nav.

### 6c. 文章の文法 / テスト 問題III pages
Per text: a 2–3 sentence summary (EN/HI/GU). **Do not transcribe the text.** Quote only the sentence around each blank (with romaji). Each blank is a `.bp-quiz` with options, the book answer and a Why note that follows the 別冊 explanation in our words (cite 別冊 p.N and the book's cross-reference "p.xx 文型y"). Then the ことば box as a `vd-wordlist`.

### 6d. 読解 pages (`dokkai-N.html`)
Follow `book-source/n1/reading/PROCESSING-GUIDE.md`. Per 回: what kind of text it is, a summary (EN/HI/GU), the key lines quoted (2–4 at most, each with romaji), each question with options in all three languages, the book answer and a Why note based on the 別冊 explanation (cite the page). Tables, menus and coupons: describe the layout and quote only the cells a question needs. Then the ことば box as a `vd-wordlist`. Translate and summarise the 読むときに大切なこと tip boxes. Put 会話のときのことば (p.234–236) on `dokkai-8.html` as `vd-wordlist` tables (casual form → standard form, EN/HI/GU).

### 6e. Hub update rule (`index.html`)
Each unit is one chip. When a unit is built, change `<span class="day-chip soon" data-href="FILE.html">LABEL</span>` to `<a class="day-chip ready" href="FILE.html">LABEL</a>` and update the `.sample-note` to `In progress — N of 56 units built`. When N = 56, change it to `Complete — 56 of 56 units built`.

---

## 7. Hard rules

- **Romaji** (`<span class="romaji">`) under every Japanese line: points, examples, questions, options, quoted lines, word lists.
- **EN + Hindi + Gujarati** for every meaning, example, question, option and summary. Use simple English: these are N4 learners.
- **Every question has its answer**: the book's answer when the key gives one (cite 別冊 p.N (PDF M), or the main-book page for チャレンジ). If the book has none, write the answer as "(our answer, not in book)". Never pass our answer off as the book's.
- **Never transcribe reading texts or 文章の文法 passages in full.** Summarise and quote short key lines. Single example sentences and question sentences may be quoted in full.
- Do not invent example sentences for the examples tables. Anything added (formation rows, extra notes, extra examples) is marked "(added, not in book)".
- Keep the book's order for points, examples and questions.
- No pictures from the book. Describe a picture in one line when a question needs it.
- The book has no audio. Do not add any.
- No emoji glyphs in body text (the ✓ in a correct option and the ✅ in a completed hub note are the only marks).
- Do not edit CSS, JS, `tools/`, other courses or hub pages.

## 8. Checks before finishing a unit

- Every answer matches the table in §3 and the 別冊 scan.
- No passage reproduced beyond the quoted lines.
- Tags balance (Python `html.parser`), all relative links resolve, and the file ends with `</html>`.
- Hub chip flipped and the count updated.

---

**Reference implementation:** `n4/multi-skill/nihongo-challenge/wa-01.html` (第1話 日本のお正月).
