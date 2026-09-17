# N1 Listening (聴解) — chapter-by-chapter processing guide

Standing instructions for turning `Nihongo_SouMatome_N1-Choukai.pdf` (新日语能力考试考前对策 N1 聴解, by Sasaki Hitoko &amp; Matsumoto Noriko, ASK Publishing / 世界图书出版公司) into the site's lesson-by-lesson listening pages. Give a chapter + lesson number (e.g. "Chapter 2, Lesson 3") and this is the process to follow.

The PDF is scanned/image-only (no text layer) — render pages to PNG (e.g. with PyMuPDF/`fitz`) and read them visually.

**This book is structurally different from Grammar/Vocabulary/Kanji** — it has no 週/日目 (week/day) structure at all. It's organized into 5 chapters (章), each with several numbered lessons, plus an answer/script appendix at the back. Treat **chapter + numbered lesson** as the unit of work (the "day" equivalent), not week/day.

## 1. Unit location & verification

- PDF page offset: **printed page = PDF index − 1** (index 4 = printed page 3 「はじめに」, index 6 = printed page 5 「目次」, etc. — confirmed by cross-checking printed page numbers in the scan).
- Full chapter/lesson map (from the TOC, PDF index 5–6, printed p.4–5):
  - **第1章 準備しよう** (p.11–22): 1 発音に関する聞き取り (p.12) · 2 文法に関する聞き取り① (p.14) · 3 文法に関する聞き取り② (p.16) · 4 会話表現 (p.18) · 5 まとめ問題 (p.20)
  - **第2章 問題のパターンに慣れよう** (p.23–38): 1 どんな返事をしますか－即時応答－ (p.24) · 2 このあと何をしますか－課題理解－ (p.26) · 3 どうしてですか－ポイント理解－ (p.28) · 4 どんな内容ですか－概要理解－ (p.30) · 5 どうすることにしますか－統合理解①－ (p.32) · 6 どれにしますか－統合理解②－ (p.34) · 7 まとめ問題 (p.36)
  - **第3章 いろいろなタイプの話を聞こう** (p.39–50): 1 情報を聞こう (p.40) · 2 指示を聞こう (p.42) · 3 説明を聞こう (p.44) · 4 テーマや言いたいことを聞こう (p.46) · 5 まとめ問題 (p.48)
  - **第4章 いろいろな語彙や表現を覚えよう** (p.51–62): 1 よく聞くカタカナを覚えよう① (p.52) · 2 よく聞くカタカナを覚えよう② (p.54) · 3 言い換えの言葉を覚えよう (p.56) · 4 よく聞く表現を覚えよう (p.58) · 5 まとめ問題 (p.60)
  - **第5章 総まとめ問題** (p.63–70): one comprehensive practice test, not broken into numbered lessons — treat as a single unit (may need splitting into parts when reached).
  - **付録 解答・スクリプト・訳文** (p.71 onward): answers + full script + translations for every lesson, **all consolidated in one place at the back** — NOT printed near each lesson like the other three books. Each lesson's exercise page prints "（答えは p.X）" telling you exactly which appendix page to fetch.
- 1レッスン2ページ (2 printed pages per lesson), matching the other books' cadence even though the organizing principle is different.
- Always fetch the cited appendix page (「答えは p.X」) and confirm answers from there — don't guess. Unlike Grammar (works, mostly) and Kanji (no key at all), this book's answer key is complete and present in the scan for every lesson, just centralized in the back.

## 2. Book characteristics specific to this edition

- This is a **Chinese-localized edition** (bilingual JP/Chinese, with some English/Korean glosses on harder items), not the Hindi/Gujarati-facing SouMatome originals. Reuse the book's own English glosses where given, but still add Hindi + Gujarati yourself per the site-wide rule ([[feedback-romaji-required]] and the site's EN/HI/GU convention).
- Audio: the book ships with real CD audio (`book-source/n1/listening/audio/…AudioCD1/`, `…AudioCD2/`), already extracted to individual track mp3s. **This audio is copyrighted purchased material and must never be published to the site** — it's already covered by the repo's `.gitignore` (`book-source/**/audio/`). Reference tracks by disc + track number only (e.g. "CD1, Track 2") using the `.ld-track` badge, so the user can play the matching file from their own local copy alongside the page. Do not embed a real `<audio>` player pointing at a real file.
- Small icon by each exercise (e.g. "①-02") gives the track number directly — cross-check against the actual audio filenames in the CD folder (e.g. `02 Track 2.mp3`) rather than assuming a 1:1 offset with exercise numbering.

## 3. Delivery — a real page on the site

- Build each lesson at `n1/listening/chapter-{N}/lesson-{M}.html`, using `assets/css/style.css` + the shared `assets/css/day-page.css`. Reuse `.bp-header`, `.bp-meta-grid`, `.bp-note`, `.bp-section-title`, `.bp-quiz`, `.bp-options` (mark the answer cell with `class="jp answer"`, not `tr.correct` — these are answer-key tables, not multiple-choice-with-distractors), `.bp-why`, `.bp-confusion`, `.bp-callout`, `.bp-day-nav`, plus listening-specific `.ld-track` (the CD/track badge).
- Update `n1/listening.html` (the chapter/lesson hub) so that lesson's chip flips from `day-chip soon` (a `<span>`, not yet a link) to a linked `day-chip ready`.
- Header block (`bp-header`) should note: chapter/lesson title, source + printed/PDF page range, skill(s) covered, where the confirmed answer key was found (which appendix page), and the standing audio-copyright note.

## 4. Content sections per lesson

Content shape varies a lot more than Grammar/Vocab/Kanji since each chapter teaches a different skill — don't force every lesson into the same three-section template. Adapt to what the lesson actually contains, e.g.:

- **Chapter 1** lessons are ear-training drills (pronunciation minimal pairs, grammar-in-fast-speech, colloquial contractions, conversational set phrases) — format as a "sound/pattern reference table" section followed by a "listening practice" section of drills, as built for Lesson 1.
- **Chapter 2** lessons introduce the 5 actual JLPT N1 聴解 question types (即時応答, 課題理解, ポイント理解, 概要理解, 統合理解) — format each as: question-type explanation, a worked example with full script + questions + options + answer, then practice items.
- **Chapter 3** lessons are about listening strategy for different talk types (informational, instructional, explanatory, thematic) — format as strategy notes + example scripts + comprehension questions, closer to the Reading module's `.rd-strategy` pattern.
- **Chapter 4** lessons are vocabulary/expression lists (katakana loanwords commonly heard, paraphrase pairs, set expressions) — format similar to the Vocabulary module's wordlist tables.
- **Chapter 5** is a full mock test — format as a sequence of `.bp-quiz` blocks grouped by question type, no separate "lesson" theme.

Always still close with a **Confusion Pairs / Nuance Notes** section (§3 pattern from Grammar/Vocab/Kanji/Reading) — for chapters where the lesson's own content already IS the confusion cluster (as in Lesson 1's minimal pairs / contraction table), it's fine to reuse that content as this section rather than inventing new pairs, the same adaptation the Kanji spec made.

## 5. Language rules

Same site-wide rules as every other module: English + Hindi + Gujarati meanings, romaji under every Japanese line — see [[feedback-romaji-required]].

**Reference implementation:** `n1/listening/chapter-1/lesson-1.html` (第1章-1 発音に関する聞き取り) is the first lesson built under this spec (2026-09-17).
