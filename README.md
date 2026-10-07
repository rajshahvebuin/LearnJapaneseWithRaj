# Learn Japanese with Raj

A static JLPT study site for N1–N5: vocabulary, kanji, grammar, reading and listening. Every page is explained in English, Hindi and Gujarati, with romaji under each Japanese line. It works on phone, tablet and laptop, and is hosted for free on GitHub Pages.

The site is plain HTML, CSS and JavaScript. There is no build step to serve it: every page can be opened directly or deployed as-is.

## Site structure

```
index.html                     Home: levels, progress, N1 study tools, complete courses
library.html                   Every uploaded book, searchable, with its status
about.html                     How the site and its study pages work
404.html, .nojekyll            GitHub Pages support files

n1/ … n5/
  index.html                   Level page: every book first (filter by module), then study tools and modules
  vocab-cards.html             N1 only: vocabulary flashcards
  kanji-cards.html             N1 only: kanji flashcards
  quiz.html                    N1 only: practice quiz
  vocabulary.html  kanji.html  grammar.html  reading.html  listening.html
  mock-tests.html  multi-skill.html  textbooks.html   (where the level has those books)
  <module>/week-N/day-D.html   Sou-Matome course pages (N1, N2)
  <module>/<book-slug>/        One folder per book: index.html is its contents page
                               (a "coming soon" placeholder until the book is built)

assets/css/style.css           Design tokens, layout, navigation, shared components
assets/css/day-page.css        Study-page components (.bp-*, day chips, tables)
assets/css/tools.css           Flashcard and quiz components
assets/js/flashcards.js        Flashcard app (vocab + kanji pages)
assets/js/quiz.js              Quiz app
assets/data/n1/                Flashcard and quiz data (vocab/, kanji/, quiz/), generated
assets/js/main.js              Theme toggle, logout, mobile menu, tooltips
assets/js/library.js           Library search and filters
assets/js/auth.js, login.js    Simple client-side sign-in gate (not real security)

tools/build_site.py            Generator for the structural pages (see below)
tools/extract_study_data.py    Builds assets/data/n1/ from the N1 study pages
tools/catalog.json             Book catalog the generator reads
book-source/                   Local source books and processing guides; only .md files are committed
```

Every page shares one skeleton: a header with the level switcher, a level bar inside a level (overview, every module, and the study tools), the page content, and a footer. The generator writes this skeleton into every page.

Each level has its own accent colour: N1 red, N2 indigo, N3 green, N4 ochre, N5 purple. Dark mode follows the system setting, and the 🌙 button overrides it.

## Adding or finishing a book

1. Put the book under `book-source/<level>/<module>/<Book_Name>/` (see `book-source/README.md`).
2. Run `python tools/build_site.py --scan`. The book appears in the library, its module hub and its level page, and gets a placeholder page at `<level>/<module>/<slug>/index.html`.
3. Build the course pages into that same folder, replacing the placeholder `index.html` with the book's contents page.
4. Run `python tools/build_site.py` again. A book whose contents page has no grey "soon" chips left is marked "Ready" everywhere automatically. Books outside a `<level>/<module>/<slug>/` folder still go in the `BUILT` table.
5. For N1, run `python tools/extract_study_data.py` so the new words, kanji and exercises reach the flashcards and quiz, then run `python tools/build_site.py` once more to refresh the card counts.

The generator rewrites only the structural pages, plus the shared header and footer of every other page. Study-page content is never touched. You can run it any number of times: when nothing has changed, it changes nothing. `--scan` needs the local `book-source/` files. Without `--scan`, it uses `tools/catalog.json`, so it works on any machine.

## Content source

The course pages are built from published JLPT workbook series such as 日本語総まとめ, 新完全マスター, ドリル&ドリル and others. Each built book has a `PROCESSING-GUIDE.md` under `book-source/` describing exactly how its pages are made.

The scanned books and audio are **not** part of this repository. `.gitignore` excludes everything in `book-source/` except the guides. Only the derived study pages are published.

## Releasing on GitHub Pages

1. Commit and push to GitHub, on the `master` or `main` branch.
2. In the repository, open **Settings → Pages**. Choose **Deploy from a branch**, then select your branch and the **/ (root)** folder, and save.
3. After a minute or two the site is live at `https://<username>.github.io/LearnJapaneseWithRaj/`.

All links are relative, so the site works under the `/LearnJapaneseWithRaj/` project path, at a custom domain, or opened locally. `.nojekyll` makes GitHub serve the files exactly as they are. `404.html` works out the site root at runtime, so it shows correctly at any missing URL.

## Running it locally

```
python -m http.server 8000
```

Then open http://localhost:8000/. Sign in with the username and password set in `assets/js/login.js`.
