# Learn Japanese with Raj

A simple, static JLPT study site — vocabulary, kanji, grammar, reading, and listening for N1 and N2 — built to work on phone, tablet, and laptop, and hosted for free on GitHub Pages.

No build step: plain HTML/CSS/JS, so any page can be opened directly or deployed as-is.

## Structure

```
index.html              Home page — links into JLPT N1 / N2
n1/, n2/                One page per module (Vocabulary, Kanji, Grammar, Reading, Listening)
n1/grammar/week-{N}/day-{D}.html       Day-by-day grammar pages
n1/vocabulary/week-{N}/day-{D}.html    Day-by-day vocabulary pages
assets/css/style.css     Shared site styling (layout, nav, cards, responsive/dark-mode)
assets/css/day-page.css  Shared styling for week/day study pages (grammar, vocabulary, …)
assets/js/main.js        Nav toggle, search filter, quiz interactions
book-source/             Staging area for source textbook material (see below)
```

## Content source

Day pages are built from the 日本語総まとめ (Nihongo Sou-Matome) JLPT prep series. Each module under `book-source/` has its own `PROCESSING-GUIDE.md` describing exactly how that book's content is located and turned into a page — see `book-source/n1/grammar/PROCESSING-GUIDE.md` and `book-source/n1/vocabulary/PROCESSING-GUIDE.md`.

The scanned textbook PDFs themselves are **not** included in this repository (copyrighted material) — only the derived study pages are published.

## Deploying

Enable GitHub Pages for this repo (Settings → Pages → Deploy from branch → `master` / root), and the site will be live at `https://<username>.github.io/LearnJapaneseWithRaj/`.
