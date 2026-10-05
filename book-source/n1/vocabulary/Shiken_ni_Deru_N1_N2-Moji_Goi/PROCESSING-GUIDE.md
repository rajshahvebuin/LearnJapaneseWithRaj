# 試験に出る漢字と語彙 N1・N2 — unit-by-unit processing guide

Standing instructions for turning `Shiken_ni_Deru_N1_N2-Moji_Goi.pdf` (日本語能力試験 N1・N2 試験に出る漢字と語彙 50日完成, 桐原書店, 新版 2010) into the site's vocabulary pages under `n1/vocabulary/shiken-ni-deru/`. Give a unit id (e.g. "漢字 第5日目", "語彙 第12日目", "語彙N1 練習問題", "N2 模擬試験") and follow this process.

This guide adapts the vocabulary spec [`book-source/n1/vocabulary/PROCESSING-GUIDE.md`](../PROCESSING-GUIDE.md) and borrows the page chrome of the same series' grammar book ([`n1/grammar/shiken-ni-deru/day-01.html`](../../../../n1/grammar/shiken-ni-deru/day-01.html)). Everything there (shared header/footer, `bp-*` / `vd-*` classes, three required sections, EN + Hindi + Gujarati, romaji under every Japanese line, "(added, not in book)" marking) applies unless overridden here.

**Title note:** the site's library calls it "試験に出る 文字・語彙 N1・N2"; the book's real title is **試験に出る漢字と語彙** (Kanji to Goi). Pages use the real title.

**Level note:** the book covers **both N1 and N2** and does not tag individual day items by level — treat 第1部/第2部 days as shared N2/N1. The practice sets and mock tests are split by level (N2 / N1); build the N2 ones too, labelled "N2-level", because the book lives in the N1 module.

---

## 1. The PDF

- **194 PDF pages. PDF 1–144 = main book (incl. colophon p.144); PDF 145–194 = the 別冊** (解答・試験に出るポイント解説, 48 printed pages) scanned into the same PDF. PDF 145 = 別冊 cover, PDF 146 = blank, PDF 147 = 別冊 もくじ (p.1).
- **No usable text layer.** `page.get_text()` returns only the watermark `http://riyuxuexi.taobao.com/` on every page. Read everything visually with PyMuPDF (`import pymupdf`; `page.get_pixmap(dpi=200, clip=...)`), cropping each page into top/bottom halves at ~200 dpi so furigana in the 別冊 is legible. Ignore the watermark.
- The PDF's built-in bookmarks are just `000001…000144` (main) and `att000…att050` (別冊) — not useful as a TOC.
- **Offset (main book): PDF page = printed page (offset 0).** Verified on rendered page stamps at PDF 2, 3, 4, 6, 8, 10, 12, 14, 15, 16, 18, 19, 67, 68, 70, 72, 74, 122, 126, 132, 137, 138, 142. No drift.
- **Offset (別冊): PDF page = 別冊 printed page + 146.** Verified at 別冊 p.2 (PDF 148), p.17 (163), p.18 (164), pp.20–31 (166–177), p.46 (192), p.47 (193). PDF 194 = 別冊 back page (print history only).
- Not units: pp.2–5 この本を使う学習者のみなさんへ; pp.6–12 この本の使い方 (drill-type explanations — pp.7, 9, 11, 13 are annotated sample pages); pp.14–16 もくじ; part title pages 17, 73, 131; blank pages 130 and 143; colophon 144.

## 2. Answer key

- **Every item has an official answer in the 別冊.** Never guess.
  - 別冊 pp.2–17 (PDF 148–163): 第1部 漢字, by 第N日目, each followed by a boxed **試験に出るポイント解説** (reading rules, e.g. 力 = りき/りょく). p.17 also holds the 漢字N2/N1 練習問題 keys.
  - 別冊 pp.18–46 (PDF 164–192): 第2部 語彙, by 第N日目, each with a longer ポイント解説 (meaning + collocations for every word in Ⅰ/Ⅱ, notes on Ⅲ–Ⅵ). p.46 = 語彙N2/N1 練習問題 keys.
  - 別冊 p.47 (PDF 193): 模擬試験 keys (N2 問題1–6 = items 1–32; N1 問題1–4 = items 1–25).
- A day's key often runs over a page break (e.g. 漢字 第3日目 = 別冊 pp.3–4): cite every page used.
- The 漢字 key also gives readings of distractors in Ⅵ (e.g. 災害 (再会 さいかい)) and Ⅶ (耐 (忍ぶ)) — use these for the distractor rows.
- The ポイント解説 is short explanatory text: paraphrase it in English and say "the book's tip"; do not reproduce it as a block.

## 3. What a unit is

One site page per unit, in book order: 25 漢字 days, 2 漢字 practice sets, 25 語彙 days, 2 語彙 practice sets, 2 mock tests = **56 units**. Each 日目 is exactly 2 printed pages (a spread). Prev/next (`bp-day-nav`) follows the table order; unit 1's "prev" is the hub `index.html`, unit 56's "next" is the hub.

## 4. Full unit table

Printed pp = PDF pp (offset 0). 別冊 PDF = 別冊 page + 146.

| # | Unit | Title (book's もくじ, each line ends 「など」) | Printed pp | PDF pp | Answer key 別冊 pp (PDF pp) | File |
|---|---|---|---|---|---|---|
| | **第1部** | **漢字** (part title p.17) | 17 | 17 | | |
| 1 | 漢字 第1日目 | 引力・安易・交渉—故障・市場・私情・島国 | 18–19 | 18–19 | 2 (148) | kanji-01.html |
| 2 | 漢字 第2日目 | 広大・戸外・取得—習得・肯定・校庭・足首 | 20–21 | 20–21 | 2–3 (148–149) | kanji-02.html |
| 3 | 漢字 第3日目 | 外科・強引・視線—自然・高層・構想・真心 | 22–23 | 22–23 | 3–4 (149–150) | kanji-03.html |
| 4 | 漢字 第4日目 | 口調・仮病・固体—交代・受容・需要・片言 | 24–25 | 24–25 | 4 (150) | kanji-04.html |
| 5 | 漢字 第5日目 | 工夫・景色・一周—一種・時候・事項・消印 | 26–27 | 26–27 | 4–5 (150–151) | kanji-05.html |
| 6 | 漢字 第6日目 | 軽率・解熱・誇張—好調・習性・修正・親心 | 28–29 | 28–29 | 5 (151) | kanji-06.html |
| 7 | 漢字 第7日目 | 中傷・直訴・少女—症状・施設・使節・手柄 | 30–31 | 30–31 | 6 (152) | kanji-07.html |
| 8 | 漢字 第8日目 | 細工・極秘・乾燥—簡素・深層・新装・家柄 | 32–33 | 32–33 | 6–7 (152–153) | kanji-08.html |
| 9 | 漢字 第9日目 | 憎悪・行為・違反—違法・意志・医師・悪者 | 34–35 | 34–35 | 7 (153) | kanji-09.html |
| 10 | 漢字 第10日目 | 引火・押収・演技—延期・解凍・回答・海辺 | 36–37 | 36–37 | 7–8 (153–154) | kanji-10.html |
| 11 | 漢字 第11日目 | 陰気・一服・改修—解消・仮想・仮装・間柄 | 38–39 | 38–39 | 8 (154) | kanji-11.html |
| 12 | 漢字 第12日目 | 屋外・会釈・合唱—合奏・感染・観戦・近道 | 40–41 | 40–41 | 9 (155) | kanji-12.html |
| 13 | 漢字 第13日目 | 皆勤・横柄・決行—結合・休講・急行・下見 | 42–43 | 42–43 | 9–10 (155–156) | kanji-13.html |
| 14 | 漢字 第14日目 | 正直・拡張・精神—成人・症状・賞状・生水 | 44–45 | 44–45 | 10 (156) | kanji-14.html |
| 15 | 漢字 第15日目 | 天井・繁盛・措置—処置・不正・父性・大型 | 46–47 | 46–47 | 10–11 (156–157) | kanji-15.html |
| 16 | 漢字 第16日目 | 性分・率先・世界—政界・状況・上京・船旅 | 48–49 | 48–49 | 11 (157) | kanji-16.html |
| 17 | 漢字 第17日目 | 把握・折衷・防衛—放映・闘技・討議・内気 | 50–51 | 50–51 | 11–12 (157–158) | kanji-17.html |
| 18 | 漢字 第18日目 | 是正・大木・本名—本命・自体・辞退・昼寝 | 52–53 | 52–53 | 12 (158) | kanji-18.html |
| 19 | 漢字 第19日目 | 天然・平等・一層—一斉・成人・聖人・仲間 | 54–55 | 54–55 | 13 (159) | kanji-19.html |
| 20 | 漢字 第20日目 | 世間・人物・先導—先頭・潜在・洗剤・見本 | 56–57 | 56–57 | 13–14 (159–160) | kanji-20.html |
| 21 | 漢字 第21日目 | 規模・体裁・悲観—美観・要請・陽性・大物 | 58–59 | 58–59 | 14 (160) | kanji-21.html |
| 22 | 漢字 第22日目 | 大陸・木造・徒歩—途方・点火・転嫁・手際 | 60–61 | 60–61 | 14–15 (160–161) | kanji-22.html |
| 23 | 漢字 第23日目 | 用心・遺言・優等—誘導・対象・大勝・悪口 | 62–63 | 62–63 | 15 (161) | kanji-23.html |
| 24 | 漢字 第24日目 | 素朴・門戸・展望—電報・伝統・電灯・人出 | 64–65 | 64–65 | 15–16 (161–162) | kanji-24.html |
| 25 | 漢字 第25日目 | 発作・便乗・展示—天地・反省・半生・目印 | 66–67 | 66–67 | 16–17 (162–163) | kanji-25.html |
| 26 | 漢字N2 練習問題 | 問題1–4 × 5 items (問題1 漢字読み, 問題2 表記; check 問題3–4 on pp.69–70) | 68–70 | 68–70 | 17 (163) | kanji-renshu-n2.html |
| 27 | 漢字N1 練習問題 | 問題1 (10 items) + 問題2 (10 items) 漢字読み | 71–72 | 71–72 | 17 (163) | kanji-renshu-n1.html |
| | **第2部** | **語彙** (part title p.73) | 73 | 73 | | |
| 28 | 語彙 第1日目 | 見通し・見当・つまずく・すべる・いまさら・いまだに | 74–75 | 74–75 | 18–19 (164–165) | goi-01.html |
| 29 | 語彙 第2日目 | けち・節約・きざむ・ちぎる・がっかり・しっかり | 76–77 | 76–77 | 19 (165) | goi-02.html |
| 30 | 語彙 第3日目 | タイミング・チャンス・あきらめる・あこがれる・ずっと・ざっと | 78–79 | 78–79 | 20 (166) | goi-03.html |
| 31 | 語彙 第4日目 | 心がけ・心残り・さける・どける・たった・単に | 80–81 | 80–81 | 21 (167) | goi-04.html |
| 32 | 語彙 第5日目 | 勧め・試み・からかう・ふざける・それとも・ところが | 82–83 | 82–83 | 22 (168) | goi-05.html |
| 33 | 語彙 第6日目 | きり・びり・つかむ・つまむ・あいにく・せっかく | 84–85 | 84–85 | 23 (169) | goi-06.html |
| 34 | 語彙 第7日目 | 月並み・なおざり・おさえる・かぶせる・きっぱり・くっきり | 86–87 | 86–87 | 24 (170) | goi-07.html |
| 35 | 語彙 第8日目 | 手入れ・手ごろ・わずらわしい・まぎらわしい・あらかじめ・とっくに | 88–89 | 88–89 | 25 (171) | goi-08.html |
| 36 | 語彙 第9日目 | 都合・合図・せつない・あっけない・まるで・まさか | 90–91 | 90–91 | 26 (172) | goi-09.html |
| 37 | 語彙 第10日目 | 無口・早口・心強い・心細い・せいぜい・せめて | 92–93 | 92–93 | 27 (173) | goi-10.html |
| 38 | 語彙 第11日目 | パターン・マスター・心がける・はたす・とかく・どうやら | 94–95 | 94–95 | 28 (174) | goi-11.html |
| 39 | 語彙 第12日目 | バランス・ペース・打ち込む・打ち明ける・いやいや・うろうろ | 96–97 | 96–97 | 29 (175) | goi-12.html |
| 40 | 語彙 第13日目 | こつ・アイディア・そうぞうしい・はなばなしい・ぶつぶつ・まごまご | 98–99 | 98–99 | 30 (176) | goi-13.html |
| 41 | 語彙 第14日目 | アプローチ・ガイド・やぶれる・くずれる・にもかかわらず・ゆえに | 100–101 | 100–101 | 31 (177) | goi-14.html |
| 42 | 語彙 第15日目 | あやまち・誤り・すれちがう・追いかける・あいかわらず・あくまで | 102–103 | 102–103 | 32 (178) | goi-15.html |
| 43 | 語彙 第16日目 | 裏返し・あべこべ・つなげる・重ねる・および・かつ | 104–105 | 104–105 | 33–34 (179–180) | goi-16.html |
| 44 | 語彙 第17日目 | インテリ・ベテラン・またぐ・渡る・てっきり・めっきり | 106–107 | 106–107 | 34 (180) | goi-17.html |
| 45 | 語彙 第18日目 | 愛想・好み・激しい・厳しい・たちまち・続々と | 108–109 | 108–109 | 35 (181) | goi-18.html |
| 46 | 語彙 第19日目 | うぬぼれ・誇り・なでる・こする・とたんに・ようやく | 110–111 | 110–111 | 36 (182) | goi-19.html |
| 47 | 語彙 第20日目 | おおざっぱ・おおすじ・なごやか・おだやか・むしろ・ひとまず | 112–113 | 112–113 | 37–38 (183–184) | goi-20.html |
| 48 | 語彙 第21日目 | 外見・人目・ほめる・おだてる・はたして・ひたすら | 114–115 | 114–115 | 39 (185) | goi-21.html |
| 49 | 語彙 第22日目 | 説・筋・励ます・慰める・さぞ・さも | 116–117 | 116–117 | 40–41 (186–187) | goi-22.html |
| 50 | 語彙 第23日目 | 席・順・取り扱う・取り組む・うんざり・げっそり | 118–119 | 118–119 | 42 (188) | goi-23.html |
| 51 | 語彙 第24日目 | ストレス・ショック・もったいない・だらしない・しみじみ・ずばり | 120–121 | 120–121 | 43–44 (189–190) | goi-24.html |
| 52 | 語彙 第25日目 | 我慢・苦労・引き止める・引き起こす・そろそろ・だぶだぶ | 122–123 | 122–123 | 45 (191) | goi-25.html |
| 53 | 語彙N2 練習問題 | 問題1–4 × 5 items | 124–126 | 124–126 | 46 (192) | goi-renshu-n2.html |
| 54 | 語彙N1 練習問題 | 問題1–3 × 5 items (p.130 blank) | 127–129 | 127–129 | 46 (192) | goi-renshu-n1.html |
| | **第3部** | **模擬試験** (part title p.131) | 131 | 131 | | |
| 55 | N2 模擬試験 漢字・語彙 | 問題1–6, items 1–32 | 132–137 | 132–137 | 47 (193) | mogi-n2.html |
| 56 | N1 模擬試験 漢字・語彙 | 問題1–4, items 1–25 (p.143 blank) | 138–142 | 138–142 | 47 (193) | mogi-n1.html |

56 units. 漢字 day N = printed pp. 18+2(N−1) and the next page; 語彙 day N = 74+2(N−1) and the next page.

## 5. Delivery

- Output folder: `n1/vocabulary/shiken-ni-deru/`. Depth 3: assets `../../../assets/...`, site home `../../../index.html`, N1 home `../../index.html`, module hub `../../vocabulary.html`, book hub `index.html`.
- Copy `<head>`/header/footer from `kanji-01.html` (same as the hub): `auth.js` in `<head>`, `style.css` + `day-page.css`, `main.js` before `</body>`, `<body class="level-page n1">`. Change only `<title>` and the meta description.
- Breadcrumb: Home / JLPT N1 / Vocabulary / 試験に出る漢字と語彙 (`index.html`) / {unit label, e.g. 漢字 第1日目}.
- `.bp-header`: `bp-week` = "JLPT N1 · Vocabulary · 試験に出る漢字と語彙 · 第1部 — 漢字 (romaji)" (or 第2部 — 語彙 / 第3部 — 模擬試験); `h1` = unit label + the もくじ title line + romaji; meta grid: Source (printed + PDF pages), Drills on this page (`bp-points` chips), Answer key (別冊 page + PDF page, "confirmed, not guessed"), Notes.
- A `.vd-legend` under the header explains the drill numerals Ⅰ–Ⅷ (漢字) or Ⅰ–Ⅵ (語彙) and any symbol used.

## 6. Section mapping

### 6.1 漢字 days (第1部) — every day has the same eight drills

| Drill | What it is | Printed options? |
|---|---|---|
| Ⅰ 難しい読み | 6 words, choose the right reading | yes, 4 readings |
| Ⅱ 似ている読み | 7–8 pairs, write both readings (゛/っ/long vowel/ん traps) | no — open |
| Ⅲ 読み グループ分け | boxes of words, sort into 2 readings per box | no — sorting |
| Ⅳ 訓読み・音訓読み | ~10 words/verbs, write the kun or mixed reading | no — open |
| Ⅴ 形が似ている漢字 | 8 kana prompts, choose the right kanji of two look-alike shapes | yes, 2 |
| Ⅵ 読み方が似ている漢字 | 8 short phrases, choose the right word of two similar sounds | yes, 2 (both real words) |
| Ⅶ 意味が似ている漢字 | 8 phrases, choose the kanji of two with similar meaning | yes, 2 kanji |
| Ⅷ 同じ読み方の漢字 | ~10 sentences, fill one of 5 same-reading kanji from a side box | yes, 5 |

- **§1 Vocabulary List:** one `.vd-wordlist` per drill (Ⅰ…Ⅷ, the book's own grouping) listing every word the drills use: Japanese (word + `<span class="romaji">かな · romaji</span>`), EN, HI, GU, Note (reading rule, distractor ⇔ with its reading, rendaku…). Readings come from the key; meanings are ours. Fake distractor forms in Ⅴ (e.g. 牛後) are not listed as words.
- **§2 Quiz:** every item as a `bp-quiz`, numbered Q1… continuously with the book number in brackets ("Q7 (Ⅱ-①)"). Ⅰ/Ⅴ/Ⅵ/Ⅶ/Ⅷ: book options in `bp-options`, correct row `class="correct"`. Ⅱ/Ⅳ (open): no options table — show the answer + meaning in `q-translations` and a Why. Ⅲ: one quiz per reading line, all box words as option rows, every word on that line marked correct. Romaji under a prompt must not give the answer away ("(___) — choose the reading").
- **§3 Confusion:** (A) the book's ポイント解説 reading rules as a `bp-confusion` table; (B) the day's sound traps (゛, っ, long vowel, ん, consonant) grouped; (C) Ⅶ meaning pairs (耐える/忍ぶ…); `bp-callout` exam traps (double readings like 市場 しじょう/いちば, okurigana deciding the reading, rendaku).

### 6.2 語彙 days (第2部) — six drills

| Drill | What it is | Printed options? |
|---|---|---|
| Ⅰ 意味が似ている | (1)(2): 5 similar 漢語 (活気・活動・活躍…) for 5 blanks each | word bank, no per-item options |
| Ⅱ 使い方を覚える | (1)(2): 5 nouns/verbs/loanwords for 5 blanks, conjugate as needed | word bank |
| Ⅲ 副詞 (or 接続詞) | 5 adverbs for 5 blanks | word bank |
| Ⅳ 同じものは？ | 5 sentences with one homonym (上がる…), pick the two (sometimes two pairs) with the same use | answer like ①と③ |
| Ⅴ 正しい？ | (1)(2): 4 sentences each using one word, mark 正 or 誤 | 正/誤 |
| Ⅵ 意味と言葉 | (1)(2): paraphrase, 4 options | yes, 4 |

- **§1:** one `.vd-wordlist` per drill group (Ⅰ(1), Ⅰ(2), Ⅱ(1), Ⅱ(2), Ⅲ, plus the Ⅳ–Ⅵ target words). Use the 別冊 ポイント解説 collocations (活気→活気がある, 見当→見当がつく) in the Note column, marked "from the book's notes"; our own example phrases are "(added, not in book)".
- **§2:** word-bank items (Ⅰ–Ⅲ): one `bp-quiz` per blank; the options table is that group's 5-word bank (it *is* printed), correct row = key; Why = why the collocation fits and the others don't. Where the key conjugates, show the conjugated form. Ⅳ: options table = the 5 sentences with their meanings, the key's pair(s) marked correct. Ⅴ: each sentence a row with 正/誤 from the key; for 誤 give the book's correction from the ポイント解説 (e.g. 「いちおうです」とは言わない). Ⅵ: normal 4-option table.
- **§3:** near-synonym tables from Ⅰ (休暇／休業／休憩／休養／休日 type sets — the book's main point), adverb nuance (Ⅲ), homonym senses (Ⅳ); `bp-callout` traps for the Ⅴ misuse patterns.

### 6.3 練習問題 and 模擬試験

- JLPT format: 漢字読み, 表記, 語形成, 文脈規定, 言い換え類義, 用法 (N1 has no 表記/語形成). Each 問題 is an `h3`; each item a `bp-quiz` with the printed options 1–4 and the 別冊 answer (p.17 / p.46 / p.47). §1 = review list of every tested word (with the day that teaches it, if any); §3 = the look-alike options the items test. 用法 items: show all four sentences as option rows with meanings.
- No reading passages or audio in this book. If a long text ever appears, follow the site rule: a 2–3 sentence summary in our own words (EN/HI/GU), quoting only the needed sentence.

## 7. Hub page update rule

`n1/vocabulary/shiken-ni-deru/index.html` has one `week-block` per group (第1部 漢字 days, 漢字 練習問題, 第2部 語彙 days, 語彙 練習問題, 第3部 模擬試験). When a unit is built, flip its chip from `<span class="day-chip soon" data-href="FILE">…</span>` to `<a class="day-chip ready" href="FILE">…</a>` and update `In progress — N of 56 units built` in the `sample-note`. Do not edit `n1/vocabulary.html`.

## 8. Language rules (unchanged)

EN + Hindi + Gujarati for every meaning and every quiz sentence/phrase; `<span class="romaji">` under every Japanese line (words, options, prompts, full sentences); "(added, not in book)" on anything we add beyond explanation. Romaji style: long vowels as ou/uu/ei (kouka, kyuuyo), っ doubled (jikkan), ん before a vowel with an apostrophe (an'i).

---

**Reference implementation:** [`n1/vocabulary/shiken-ni-deru/kanji-01.html`](../../../../n1/vocabulary/shiken-ni-deru/kanji-01.html) — 漢字 第1日目, the first unit built under this guide. The first 語彙 day (`goi-01.html`, key 別冊 pp.18–19 = PDF 164–165) should be built next as the reference for §6.2.
