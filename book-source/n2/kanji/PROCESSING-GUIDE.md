# N2 Kanji (漢字) — day-by-day processing guide

Standing instructions for turning `Nihongo_SouMatome_N2-Kanji.pdf` (日本語総まとめ N2 漢字, by 佐々木仁子・松本紀子, Ask Publishing) into the site's day-by-day kanji pages.

The PDF is scanned/image-only — render pages to PNG (PyMuPDF/`fitz`, ~2.2x zoom) and read visually.

## 1. Unit location & verification — CONFIRMED

- **Printed page number = PDF page index directly** (0-based `fitz` index), same as N2 Vocabulary. Cover/front matter occupy index 0–10; content starts at index 11.
- Full TOC (confirmed, PDF index 4–5, printed p.4–5): **8 weeks, 7 days each, organized by real-life SKILL/SITUATION, not by shared kanji component/reading** (unlike N1 Kanji) — this book teaches kanji you actually encounter doing something:
  - 第1週 みる① (Look and See①) — p.11–26 — 1日目 立て札・注意書き／2日目 建物の中でよく見る表示／3日目 建物の内外でよく見る表示／4日目 駅でよく見る表示／5日目 乗り物でよく見る表示／6日目 郵便局・病院で見る表示／7日目 実戦問題
  - 第2週 つかう① (Use①) — p.27–42 — 1自動券売機／2現金自動支払機／3自動販売機・自動券売機／4家電のリモコン／5電話・携帯電話／6携帯電話・パソコン／7実戦問題
  - 第3週 よむ① (Read①) — p.43–58 — 1料金通知・払込用紙／2不在通知／3ポイントカード・商品券・クリーニング預かり票／4ゴミの分別／5いろいろな通知①／6いろいろな通知②／7実戦問題
  - 第4週 かく (Write) — p.59–74 — 1伝票・申込書／2返事を書く／3メール・はがき／4ビジネスメール／5答案用紙／6作文／7実戦問題
  - 第5週 つかう② (Use②) — p.75–90 — 1家庭用品（ポット・ヒーター）／2家庭用品 洗剤①／3家庭用品 洗剤②／4家庭用品（薬）／5食品／6インターホン・パソコン／7実戦問題
  - 第6週 みる② (Look and See②) — p.91–106 — 1広告・チラシ／2折り込み広告／3広告／4地図／5文化財・展示／6どっち？／7実戦問題
  - 第7週 よむ② (Read②) — p.107–122 — 1求人・募集／2掲示板・地域新聞／3メニュー・成分表示／4受験案内／5交通情報／6気象情報／7実戦問題
  - 第8週 しる (Know) — p.123–138 — 1速報／2見出し①／3見出し②／4記事①／5記事②／6記事③／7実戦問題
  - [付録] 漢字・語彙リスト (kanji/vocab index, sorted by stroke count) starts p.139 — back matter, not day content.
- **Cadence CONFIRMED identical to N2 Vocabulary**: each week is a 16-page block — divider/title page (+0), then Day1 = divider+1/+2, Day2 = +3/+4, Day3 = +5/+6, Day4 = +7/+8, Day5 = +9/+10, Day6 = +11/+12, Day7 (実戦問題 test, 3 pages) = +13 to +15. Verified exactly against Week 1 (divider p.11, Day1 p.12–13, ..., Day7 p.24–26) via both the main content pages and the answer booklet's own day labels.
- Book teaches 739 kanji total / ~2,200 words over 8 weeks, 14–15 kanji/day.

## 2. ANSWER KEY — GREAT NEWS, fully present in this scan (unlike N1 Kanji and unlike N2 Vocabulary's test days)

- The book's [別冊] 解答・解説 (separate detachable answer/explanation booklet) **is included in this PDF scan**, starting at **PDF index 161** (its own internal page "1"). Formula: **booklet's own page number = PDF index − 160**.
- The booklet is organized by week/day exactly like the main book (「第N週」headers, then 「M日目　左 (p.X)」/「M日目　右 (p.Y)」 sub-sections for the printed left/right page of that day, each showing 練習 answers ①②③④ plus any callout vocab). Day 7 test answers show as 「7日目 (p.X〜Y)」 with 問題1/2/3/4 sections, each fully answered (e.g. 問題1 ①4②4③4④2...).
- Each week's answers span roughly 2 booklet pages (some weeks compress to less) — **estimate the booklet page for week N starts at PDF index `161 + 2×(N-1)`**, but render a small window (that index and the next 2-3 pages) and search for the actual 「第N週」header to confirm before citing — the estimate can drift by ±1-2 pages toward the back of the book. Confirmed anchors: Week1 → index 161 ("第1週 みる①"), Week8 → index 175 ("第8週", ending with 7日目 test answers on booklet p.15).
- **Always cite the confirmed answer from the booklet — never reason out or guess any answer in this book**, regular day or test day alike. This is a stronger guarantee than N1 Kanji (no key at all) or N2 Vocabulary (test days unconfirmable) — use it.

## 3. Symbols used in this book — CONFIRMED (legend page, printed p.10, "本書で使用しているマーク")

| Symbol | Meaning |
|---|---|
| ☞ [number] | Cross-reference to another kanji's ID number in this book (e.g. ☞恋308 = "see kanji #308") — informational only, no need to build cross-links on the site, just reproduce the note |
| ❶ (filled circle with exclamation) | 特に注意してほしい読み — a reading requiring particular attention (usage caution) |
| ⊙-style special-reading mark (small circled dot icon, distinct from ❶) | 特別な読み — an unusual/irregular reading, e.g. 一日 read as ついたち |
| 《 》 around a reading | Reading not in the official Jōyō kanji list but commonly/idiomatically used (e.g. 等《など》) |
| Katakana reading | 音読み (on-yomi) |
| Hiragana reading | 訓読み (kun-yomi) |
| ⇔ | Antonym (seen paired with related kanji, e.g. 内側⇔外側) |
| S / ● badges (in the back-matter index only) | S = elementary-level kanji, ● = advanced-level kanji (informational, from the appendix index — not needed on day pages) |

Each numbered kanji entry (numbered 1–14/15 per day, book-wide serial ID shown as a small number badge like `480`) shows: the kanji character (large), stroke count (画), on/kun readings, then several compound words built from it with furigana + EN/CN/KR meaning (book's own languages) — translate EN meaning to also add Hindi + Gujarati per site convention, keep romaji on every Japanese string.

## 4. Structural format — situational, closer to N2 Vocabulary than N1 Kanji

Each day opens with an illustrated real-life scene (a sign, a receipt, an ad, a form, a headline, etc. — matching that day's theme) captioned with the kanji it contains, then lists the day's kanji entries (numbered, as above) grouped exactly as the book groups them (usually by the illustrated realia item, e.mid several kanji per picture) — do NOT flatten into one undifferentiated list; preserve the book's own visual/thematic grouping as separate `.kd-kanji-table` blocks under an `<h3>` matching the book's own sub-label (or the realia caption if no explicit sub-label is given).

Each day ends with a single unified `練習` (practice) exercise — usually 4 items, "choose the correct reading/kanji and mark ○" — not split into 練習Ⅰ/Ⅱ like N2 Vocabulary. Day 7 (実戦問題) is a full JLPT-style test: 問題1 (reading, ~10 items), 問題2 (kanji selection, ~5 items), 問題3 (usage/context, ~5-6 items), 問題4 (fill in with correct kanji word, ~3-4 items) — 制限時間15分, 25問/100点, matching N1 Kanji's test format.

Each week also has a [コラム] (column/sidebar) at the end with a memorization tip or related-kanji trivia (e.g. Week1's コラム: 看板・立て札・表示 sign vocabulary; Week3's コラム: 記号的な漢字 未⇔済) — include this as a `.bp-callout` at the end of Day 7's page.

## 5. Delivery — a real page on the site

- Build each day at `n2/kanji/week-{N}/day-{D}.html`, using `assets/css/style.css` + shared `assets/css/day-page.css`. Reuse the Kanji-specific classes already defined for N1 Kanji (`.kd-legend`, `.kd-group-head`, `.kd-kanji-table`) plus the standard `.bp-header`, `.bp-meta-grid`, `.bp-section-title`, `.bp-quiz`, `.bp-options` (for Day 7's multiple-choice test), `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`. Use `n2/vocabulary/week-1/day-1.html` and `n1/kanji/week-1/day-1.html` as structural references; body class `level-page n2`, N2 breadcrumb/nav.
- Update `n2/kanji.html` (hub) so each day's chip flips from `day-chip soon` to a linked `day-chip ready`, and each week's title gets the real Japanese title + romaji. This is consolidated separately after all build agents finish — individual day-builders should NOT touch the hub page.
- Header block: week/day title, source + page range used, kanji covered (list), where the confirmed answer was found (booklet page number).

## 6. Confusion Pairs / Nuance Notes — required every day

A `.bp-confusion` table comparing same-reading or visually-similar kanji taught that day (this book already clusters kanji thematically by scene rather than by shared reading, so pull genuine confusion pairs from the day's own kanji list — e.g. 危ない vs 危うい, same kanji different reading/nuance — rather than inventing unrelated ones), plus a `.bp-callout` for any ❶/special-reading trap.

## 7. Learner level & language rules

Same site-wide rule: English + Hindi + Gujarati meanings (book only gives EN/Chinese/Korean — add Hindi/Gujarati yourself), romaji under every Japanese word/sentence/option.

---

**Reference implementation:** none yet — Week 1 Day 1 (立て札・注意書き) is the first day to be built under this spec.
