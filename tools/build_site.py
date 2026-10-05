#!/usr/bin/env python3
"""
Learn Japanese with Raj — site skeleton generator.

Plain static site (GitHub Pages, no build step needed to *serve* it). This
script only (re)generates the structural pages and keeps every page's shared
header/footer in sync. Run it from the repo root whenever a book is added or a
course is completed:

    python tools/build_site.py            # rebuild pages from tools/catalog.json
    python tools/build_site.py --scan     # refresh catalog.json from book-source/ first

What it writes
  index.html, library.html, about.html, 404.html, .nojekyll
  nX/index.html                      level overview (N1–N5)
  nX/<module>.html                   module hub (generated ones only — the
                                     hand-built Sou-Matome course hubs are kept and
                                     get a generated "books" block appended)
  nX/<module>/<slug>/index.html      placeholder for every book not built yet
What it edits in place
  every other .html page: the <header>, <footer>, skip link and <main id>
  (the page content itself is never touched)
"""
import json, os, re, sys, glob, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, 'tools', 'catalog.json')
SRC = os.path.join(ROOT, 'book-source')
AUDIO_EXT = ('.mp3', '.wma', '.m4a', '.wav')

LEVELS = {
    'n1': dict(name='N1', en='Advanced', jp='上級', blurb='The top level — nuanced grammar, abstract vocabulary and native-speed reading and listening.'),
    'n2': dict(name='N2', en='Upper-intermediate', jp='中上級', blurb='Everyday and workplace Japanese across a wide range of topics — the level most jobs ask for.'),
    'n3': dict(name='N3', en='Intermediate', jp='中級', blurb='The bridge from textbook Japanese to real-world Japanese: longer texts and natural conversation.'),
    'n4': dict(name='N4', en='Elementary', jp='初中級', blurb='Basic grammar and vocabulary for daily situations, read and heard at a slower pace.'),
    'n5': dict(name='N5', en='Beginner', jp='初級', blurb='Hiragana, katakana, the first kanji and the core sentence patterns of Japanese.'),
}
CORE = ['vocabulary', 'kanji', 'grammar', 'reading', 'listening']
MODULES = {
    'vocabulary': dict(name='Vocabulary', jp='語彙', icon='語', desc='Word lists with readings, meanings and confusable pairs.'),
    'kanji': dict(name='Kanji', jp='漢字', icon='漢', desc='Readings, meanings and compound words, day by day.'),
    'grammar': dict(name='Grammar', jp='文法', icon='文', desc='Patterns, formation rules, examples and drills.'),
    'reading': dict(name='Reading', jp='読解', icon='読', desc='Passages with strategies and comprehension questions.'),
    'listening': dict(name='Listening', jp='聴解', icon='聴', desc='Lesson-by-lesson listening practice with track references.'),
    'mock-tests': dict(name='Mock tests', jp='模擬試験', icon='模', desc='Full practice exams in the real JLPT format.'),
    'multi-skill': dict(name='All-in-one', jp='総合', icon='総', desc='Books that cover several test sections in one course.'),
    'textbooks': dict(name='Textbooks', jp='教科書', icon='本', desc='General course books for building foundations.'),
}
MODULE_ORDER = CORE + ['mock-tests', 'multi-skill', 'textbooks']

# series key (regex on folder name) -> (jp, en, slug)
SERIES = [
    (r'Soumatome|SouMatome', '日本語総まとめ', 'Nihongo Sou-Matome', 'sou-matome'),
    (r'Shin_Kanzen_Mas', '新完全マスター', 'Shin Kanzen Master', 'shin-kanzen-master'),
    (r'Speed_Master', 'スピードマスター', 'Speed Master', 'speed-master'),
    (r'Mimi_Kara_Oboeru', '耳から覚える', 'Mimi kara Oboeru', 'mimi-kara-oboeru'),
    (r'Drill_(&|and)_Drill', 'ドリル&ドリル', 'Drill & Drill', 'drill-and-drill'),
    (r'Power_Drill', '日本語パワードリル', 'Nihongo Power Drill', 'power-drill'),
    (r'Pattern_Betsu', 'パターン別徹底ドリル', 'Pattern-betsu Tettei Drill', 'pattern-betsu-tettei-drill'),
    (r'Pattern_de_Manabu', 'パターンで学ぶ', 'Pattern de Manabu', 'pattern-de-manabu'),
    (r'Shiken_ni_Deru', '試験に出る', 'Shiken ni Deru', 'shiken-ni-deru'),
    (r'Jitsuryoku_Appu', '実力アップ！', 'Jitsuryoku Appu', 'jitsuryoku-appu'),
    (r'Super_Moshi', 'スーパー模試', 'Super Moshi', 'super-moshi'),
    (r'Kanzen_Moshi', '完全模試', 'Kanzen Moshi', 'kanzen-moshi'),
    (r'Yosou_Mondaishu', '予想問題集', 'Yosou Mondaishuu', 'yosou-mondaishuu'),
    (r'Moshi_to_Taisaku', '模試と対策', 'Moshi to Taisaku', 'moshi-to-taisaku'),
    (r'20_Nichi', '20日で合格', '20-nichi de Goukaku', '20-nichi-de-goukaku'),
    (r'Tanki_Master', '短期マスター', 'Tanki Master Drill', 'tanki-master-drill'),
    (r'Goukaku_Dekiru', '合格できる', 'Goukaku Dekiru', 'goukaku-dekiru'),
    (r'Koushiki_Mondaishuu', '公式問題集', 'Official Workbook', 'official-workbook'),
    (r'Official_Guide', '公式ガイドブック', 'Official Guide Book', 'official-guide-book'),
    (r'Kirari', 'きらり日本語', 'Kirari Nihongo', 'kirari-nihongo'),
    (r'Nihongo_Challenge', '日本語チャレンジ', 'Nihongo Challenge', 'nihongo-challenge'),
    (r'Kanji_Master', '漢字マスター', 'Kanji Master', 'kanji-master'),
    (r'Taisaku_Mondai', '対策問題＆要点整理', 'Taisaku Mondai & Youten Seiri', 'taisaku-mondai'),
    (r'JLPT_Taisaku', 'JLPT対策', 'JLPT Taisaku', 'jlpt-taisaku'),
    (r'55_Reading', '55 Reading Comprehension', '55 Reading Comprehension', '55-reading-comprehension'),
    (r'Bunka_Chukyu', '文化中級日本語 1', 'Bunka Chuukyuu Nihongo 1', 'bunka-chukyu-nihongo'),
    (r'Anata_no_Jakuten', 'あなたの弱点がわかる 2級模擬試験', 'Anata no Jakuten ga Wakaru (old Level 2)', 'anata-no-jakuten'),
    (r'Shochukyu_Honsatsu', '初中級 本冊', 'Pre-intermediate textbook', 'shochukyu-honsatsu'),
    (r'Shokyu_Honsatsu', '初級 本冊', 'Beginner textbook', 'shokyu-honsatsu'),
    (r'Chukyu_Honsatsu', '中級 本冊', 'Intermediate textbook', 'chukyu-honsatsu'),
    (r'N3_Mondai', 'N3 問題', 'N3 practice problems', 'n3-mondai'),
]
SUBJECT = [  # longest first
    (r'Moji\.Goi\.Bunpou', '文字・語彙・文法', 'Vocabulary & Grammar'),
    (r'Bunpou-Goi-Kanji', '文法・語彙・漢字', 'Grammar, Vocabulary & Kanji'),
    (r'Choukai[_-]Dokkai', '聴解・読解', 'Listening & Reading'),
    (r'Bunpo_to_Yomu', '文法と読む', 'Grammar & Reading'),
    (r'Moji[._]Goi', '文字・語彙', 'Vocabulary'),
    (r'Bu[nm]pou?', '文法', 'Grammar'), (r'Goi', '語彙', 'Vocabulary'), (r'Kanji', '漢字', 'Kanji'),
    (r'Dokkai', '読解', 'Reading'), (r'Choukai', '聴解', 'Listening'), (r'Yomu', '読む', 'Reading'),
    (r'Kiku', '聞く', 'Listening'), (r'Kotoba', 'ことば', 'Vocabulary'), (r'Reading', '', ''),
]
# books already built as site courses: (level, module, folder) -> href (relative to root)
BUILT = {
    ('n1', 'vocabulary', 'Nihongo_SouMatome_N1-Goi'): 'n1/vocabulary.html',
    ('n1', 'kanji', 'Nihongo_SouMatome_N1-Kanji'): 'n1/kanji.html',
    ('n1', 'grammar', 'Nihongo_Soumatome_N1-Bunpou'): 'n1/grammar.html',
    ('n1', 'reading', 'Nihongo_Soumatome_N1-Dokkai'): 'n1/reading.html',
    ('n1', 'listening', 'Nihongo_SouMatome_N1-Choukai'): 'n1/listening.html',
    ('n2', 'vocabulary', 'Nihongo_SouMatome_N2-Goi'): 'n2/vocabulary.html',
    ('n2', 'kanji', 'Nihongo_SouMatome_N2-Kanji'): 'n2/kanji.html',
    ('n2', 'grammar', 'Nihongo_SouMatome_N2-Bumpou'): 'n2/grammar.html',
    ('n2', 'reading', 'Nihongo_SouMatome_N2-Dokkai'): 'n2/reading.html',
    ('n1', 'grammar', 'Shin_Kanzen_Master_N1-Bunpou'): 'n1/grammar/shin-kanzen-master/index.html',
    ('n1', 'grammar', 'Shiken_ni_Deru_N1_N2-Bunpou'): 'n1/grammar/shiken-ni-deru/index.html',
    ('n1', 'grammar', 'Drill_&_Drill_N1-Bunpou'): 'n1/grammar/drill-and-drill/index.html',
    ('n1', 'grammar', 'Nihongo_Power_Drill_N1-Bunpou'): 'n1/grammar/power-drill/index.html',
    ('n1', 'kanji', 'Shin_Kanzen_Master_N1-Kanji'): 'n1/kanji/shin-kanzen-master/index.html',
    ('n1', 'multi-skill', 'Pattern_Betsu_Tettei_Drill_JLPT_N1'): 'n1/multi-skill/pattern-betsu-tettei-drill/index.html',
    ('n1', 'multi-skill', 'Tanki_Master_Drill_N1'): 'n1/multi-skill/tanki-master-drill/index.html',
    ('n1', 'multi-skill', '20_Nichi_Goukaku_N1-Moji.Goi.Bunpou'): 'n1/multi-skill/20-nichi-de-goukaku/index.html',
    ('n1', 'multi-skill', 'Drill_&_Drill_N1-Choukai_Dokkai'): 'n1/multi-skill/drill-and-drill/index.html',
    ('n1', 'reading', 'Shiken_ni_Deru_N1_N2-Dokkai'): 'n1/reading/shiken-ni-deru/index.html',
    ('n1', 'reading', 'Speed_Master_N1-Dokkai'): 'n1/reading/speed-master/index.html',
    ('n1', 'reading', 'Jitsuryoku_Appu_JLPT_N1-Yomu'): 'n1/reading/jitsuryoku-appu/index.html',
}
# hand-built module hubs that keep their own content (a books block is appended)
HANDBUILT_HUBS = {'n1/vocabulary.html', 'n1/kanji.html', 'n1/grammar.html', 'n1/reading.html', 'n1/listening.html',
                  'n2/vocabulary.html', 'n2/kanji.html', 'n2/grammar.html', 'n2/reading.html'}

esc = html.escape


# ---------------------------------------------------------------- catalog

def scan():
    """Build catalog.json from the folders in book-source/."""
    try:
        import pymupdf
    except ImportError:
        pymupdf = None
    old = {}
    if os.path.exists(CATALOG):
        old = {b['id']: b for b in json.load(open(CATALOG, encoding='utf-8'))}
    books = []
    for lvl in LEVELS:
        for mod in MODULE_ORDER:
            d = os.path.join(SRC, lvl, mod)
            if not os.path.isdir(d):
                continue
            entries = []
            for e in sorted(os.listdir(d)):
                p = os.path.join(d, e)
                if os.path.isdir(p) and e != 'audio':
                    entries.append((e, p, True))
                elif e.lower().endswith('.pdf'):  # flat Sou-Matome course PDFs
                    entries.append((e[:-4], p, False))
            for folder, path, is_dir in entries:
                bid = f'{lvl}/{mod}/{folder}'
                b = dict(id=bid, level=lvl, module=mod, folder=folder)
                b.update(describe(folder, lvl))
                files = [os.path.join(r, f) for r, _, fs in os.walk(path) for f in fs] if is_dir else [path]
                if not is_dir:  # flat course: its audio lives in <module>/audio/
                    ad = os.path.join(d, 'audio')
                    files += [os.path.join(r, f) for r, _, fs in os.walk(ad) for f in fs] if os.path.isdir(ad) else []
                pdfs = [f for f in files if f.lower().endswith('.pdf')]
                b['audio_tracks'] = sum(f.lower().endswith(AUDIO_EXT) for f in files)
                b['has_pdf'] = bool(pdfs)
                if pymupdf and pdfs:
                    try:
                        b['pdf_pages'] = sum(pymupdf.open(f).page_count for f in pdfs)
                    except Exception:
                        pass
                for k in ('pdf_pages', 'note'):
                    if k not in b and k in old.get(bid, {}):
                        b[k] = old[bid][k]
                books.append(b)
    json.dump(books, open(CATALOG, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(f'catalog: {len(books)} books written to tools/catalog.json')


def describe(folder, lvl):
    jp = en = slug = None
    for pat, sjp, sen, sslug in SERIES:
        if re.search(pat, folder):
            jp, en, slug = sjp, sen, sslug
            break
    if not jp:
        jp = en = folder.replace('_', ' ')
        slug = re.sub(r'[^a-z0-9]+', '-', folder.lower()).strip('-')
    sub_jp = sub_en = ''
    for pat, a, b in SUBJECT:
        if re.search(pat, folder):
            sub_jp, sub_en = a, b
            break
    if sub_jp and sub_jp in jp:
        sub_jp = sub_en = ''
    if re.search(r'N1_N2', folder):
        lv = 'N1・N2'
    elif re.search(r'N4[-.]N5|N4\.5', folder):
        lv = 'N4・N5'
    else:
        lv = LEVELS[lvl]['name']
    covers = lv
    if 'Anata_no_Jakuten' in folder or 'Honsatsu' in folder or 'Bunka' in folder or 'N3_Mondai' in folder:
        lv = ''
    title = ' '.join(x for x in (jp, lv, sub_jp) if x)
    title_en = ' '.join(x for x in (en, lv.replace('・', '–') if lv else '', sub_en) if x)
    return dict(title=title, title_en=title_en, slug=slug, covers=covers)


def load():
    books = json.load(open(CATALOG, encoding='utf-8'))
    for b in books:
        key = (b['level'], b['module'], b['folder'])
        if key in BUILT:
            b['status'] = 'ready'
            b['href'] = BUILT[key]
        elif not b.get('has_pdf', True):
            b['status'] = 'audio-only'
            b['href'] = f"{b['level']}/{b['module']}/{b['slug']}/index.html"
        else:
            b['href'] = f"{b['level']}/{b['module']}/{b['slug']}/index.html"
            b['status'] = 'ready' if is_complete(b['href']) else 'soon'
        b['units'] = count_units(b['href']) if b['status'] == 'ready' else 0
    # slug collisions inside one module folder
    seen = {}
    for b in books:
        k = b['href']
        if k in seen and b['status'] != 'ready':
            raise SystemExit(f'slug collision: {b["id"]} vs {seen[k]} -> {k}')
        seen[k] = b['id']
    order = {m: i for i, m in enumerate(MODULE_ORDER)}
    books.sort(key=lambda b: (b['level'], order[b['module']], b['status'] != 'ready', b['title']))
    return books


def is_complete(href):
    """A hand-built course index with ready chips and no 'soon' chips left counts as ready."""
    p = os.path.join(ROOT, href)
    if not os.path.exists(p):
        return False
    t = open(p, encoding='utf-8').read()
    return 'class="day-chip ready"' in t and 'class="day-chip soon"' not in t


def count_units(href):
    p = os.path.join(ROOT, href)
    if not os.path.exists(p):
        return 0
    return open(p, encoding='utf-8').read().count('class="day-chip ready"')


def study_pages(level):
    n = 0
    for f in glob.glob(os.path.join(ROOT, level, '**', '*.html'), recursive=True):
        if os.path.basename(f) == 'index.html':
            continue
        s = open(f, encoding='utf-8', errors='ignore').read()
        if 'class="bp-day-nav"' in s or 'class="bp-header"' in s:
            n += 1
    return n


# ---------------------------------------------------------------- chrome

FAVICON = ('data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22>'
           '<rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%23c8102e%22/><text x=%2250%22 y=%2268%22 '
           'font-size=%2260%22 text-anchor=%22middle%22 fill=%22white%22 font-family=%22sans-serif%22>日</text></svg>')


def depth_prefix(relpath):
    return '../' * relpath.replace('\\', '/').count('/')


def section_of(relpath):
    first = relpath.replace('\\', '/').split('/')[0]
    if first in LEVELS:
        return first
    return {'index.html': 'home', 'library.html': 'library', 'about.html': 'about'}.get(first, '')


def header(relpath):
    d = depth_prefix(relpath)
    act = section_of(relpath)
    def a(href, label, key, extra=''):
        cls = ' class="active" aria-current="page"' if key == act else ''
        return f'<a href="{d}{href}"{cls}{extra}>{label}</a>'
    links = [a('index.html', 'Home', 'home')]
    links += [a(f'{k}/index.html', v['name'], k, f' data-level="{k}"') for k, v in LEVELS.items()]
    links += [a('library.html', 'Library', 'library'), a('about.html', 'About', 'about')]
    nav = '\n        '.join(links)
    return f'''<header class="site-header">
    <div class="container">
      <a class="brand" href="{d}index.html">
        <span class="brand-mark">日</span>
        <span class="brand-text">Learn Japanese with Raj</span>
      </a>
      <nav class="nav-links" aria-label="Main">
        {nav}
      </nav>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false">☰</button>
    </div>
  </header>'''


def footer(relpath):
    d = depth_prefix(relpath)
    lv = '\n            '.join(f'<li><a href="{d}{k}/index.html">JLPT {v["name"]} · {v["en"]}</a></li>' for k, v in LEVELS.items())
    return f'''<footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a class="brand" href="{d}index.html"><span class="brand-mark">日</span><span class="brand-text">Learn Japanese with Raj</span></a>
          <p>Self-paced JLPT study pages — grammar, vocabulary, kanji, reading and listening — explained in English, Hindi and Gujarati with romaji.</p>
        </div>
        <div>
          <h4>Levels</h4>
          <ul>
            {lv}
          </ul>
        </div>
        <div>
          <h4>Site</h4>
          <ul>
            <li><a href="{d}index.html">Home</a></li>
            <li><a href="{d}library.html">Book library</a></li>
            <li><a href="{d}about.html">How to use this site</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <span>Built by Raj · Hosted on GitHub Pages</span>
        <span>Study notes based on published JLPT workbooks. The books themselves are not hosted here.</span>
      </div>
    </div>
  </footer>'''


def page(relpath, title, body, desc='', body_class='', extra_css=(), extra_js=(), auth=True):
    d = depth_prefix(relpath)
    css = ''.join(f'\n  <link rel="stylesheet" href="{d}assets/css/{c}" />' for c in ('style.css',) + tuple(extra_css))
    js = ''.join(f'\n  <script src="{d}assets/js/{j}"></script>' for j in extra_js)
    auth_js = f'\n  <script src="{d}assets/js/auth.js"></script>' if auth else ''
    bc = f' class="{body_class}"' if body_class else ''
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />{auth_js}
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc or 'JLPT N1–N5 study pages in English, Hindi and Gujarati with romaji.')}" />
  <link rel="icon" href="{FAVICON}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;600;700&display=swap" rel="stylesheet" />{css}
</head>
<body{bc}>
  <a class="skip-link" href="#main">Skip to content</a>
  {header(relpath)}

  <main class="container" id="main">
{body}
  </main>

  {footer(relpath)}

  <script src="{d}assets/js/main.js"></script>{js}
</body>
</html>
'''


def write(relpath, text):
    p = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def crumbs(relpath, items):
    d = depth_prefix(relpath)
    out = []
    for i, (label, href) in enumerate(items):
        if href is None:
            out.append(f'<span class="current">{label}</span>')
        else:
            out.append(f'<a href="{d}{href}">{label}</a>')
    return '    <p class="breadcrumb">\n      ' + '<span class="sep">/</span>\n      '.join(out) + '\n    </p>'


# ---------------------------------------------------------------- components

def pill(b):
    if b['status'] == 'ready':
        return f'<span class="pill ready">✓ Ready · {b["units"]} units</span>' if b['units'] else '<span class="pill ready">✓ Ready</span>'
    if b['status'] == 'audio-only':
        return '<span class="pill partial">Audio only · PDF needed</span>'
    return '<span class="pill soon">Coming soon</span>'


def book_card(b, relpath, show_level=False, current_href=None):
    d = depth_prefix(relpath)
    meta = [pill(b)]
    if show_level:
        meta.insert(0, f'<span class="pill lvl">{LEVELS[b["level"]]["name"]} · {MODULES[b["module"]]["name"]}</span>')
    if b.get('audio_tracks'):
        meta.append(f'<span class="pill soon">🎧 {b["audio_tracks"]} tracks</span>')
    soon = '' if b['status'] == 'ready' else ' is-soon'
    here = b['href'] == current_href
    tag = 'div' if here else 'a'
    href = '' if here else f' href="{d}{b["href"]}"'
    label = ' <span class="pill lvl">This course</span>' if here else ''
    search = esc(f'{b["title"]} {b["title_en"]} {LEVELS[b["level"]]["name"]} {MODULES[b["module"]]["name"]}'.lower())
    return (f'      <{tag} class="book-card lv-{b["level"]}{soon}"{href} data-level="{b["level"]}" data-module="{b["module"]}" '
            f'data-status="{b["status"]}" data-search="{search}">\n'
            f'        <span class="bk-jp">{esc(b["title"])}{label}</span>\n'
            f'        <span class="bk-en">{esc(b["title_en"])}</span>\n'
            f'        <span class="bk-meta">{" ".join(meta)}</span>\n'
            f'      </{tag}>')


def module_card(level, mod, books, relpath):
    d = depth_prefix(relpath)
    m = MODULES[mod]
    ready = [b for b in books if b['status'] == 'ready']
    units = sum(b['units'] for b in ready)
    if not books:
        meta = '<span class="pill soon">No book uploaded yet</span>'
    elif ready:
        meta = f'<span class="pill ready">✓ {len(ready)} of {len(books)} books ready</span>' + (f' <span class="pill soon">{units} units</span>' if units else '')
    else:
        meta = f'<span class="pill soon">{len(books)} book{"s" if len(books) != 1 else ""} · coming soon</span>'
    return (f'      <a class="module-card" href="{d}{level}/{mod}.html">\n'
            f'        <span class="icon">{m["icon"]}</span>\n'
            f'        <div>\n          <h3>{m["name"]} <span style="color:var(--muted);font-weight:500;font-size:.85em">{m["jp"]}</span></h3>\n'
            f'          <p>{m["desc"]}</p>\n          <div class="meta">{meta}</div>\n        </div>\n      </a>')


def modules_for(level, books):
    have = {b['module'] for b in books if b['level'] == level}
    return CORE + [m for m in MODULE_ORDER if m not in CORE and m in have]


# ---------------------------------------------------------------- pages

def build_home(books):
    rel = 'index.html'
    total = len(books)
    ready = [b for b in books if b['status'] == 'ready']
    pages = sum(study_pages(l) for l in LEVELS)
    cards = []
    for k, v in LEVELS.items():
        lb = [b for b in books if b['level'] == k]
        lr = [b for b in lb if b['status'] == 'ready']
        pct = round(100 * len(lr) / len(lb)) if lb else 0
        mods = ''.join(f'<span>{MODULES[m]["name"]}</span>' for m in CORE)
        cards.append(f'''      <a class="level-card {k}" href="{k}/index.html">
        <span class="tag">{v["name"]}</span>
        <h2>{v["en"]} <span style="color:var(--muted);font-weight:500">{v["jp"]}</span></h2>
        <p>{v["blurb"]}</p>
        <div class="progress" aria-hidden="true"><i style="width:{max(pct, 0)}%"></i></div>
        <div class="progress-label">{len(lr)} of {len(lb)} books ready</div>
        <span class="cta">Open {v["name"]} →</span>
      </a>''')
    featured = '\n'.join(book_card(b, rel, show_level=True) for b in ready)
    body = f'''    <section class="hero-home">
      <div>
        <span class="eyebrow">JLPT N1 – N5 · self-paced</span>
        <h1>Learn Japanese,<br /><span class="jp-accent">one day at a time.</span></h1>
        <p>Day-by-day study pages built from the best JLPT workbooks — every grammar point, word and exercise explained in English, Hindi and Gujarati, with romaji under every Japanese line.</p>
        <div class="hero-actions">
          <a class="btn btn-primary" href="n1/index.html">Start with N1 →</a>
          <a class="btn" href="library.html">Browse the library</a>
        </div>
      </div>
      <div class="hero-art" aria-hidden="true"><span>日</span></div>
    </section>

    <div class="stats">
      <div class="stat"><b>{pages}</b><span>study pages</span></div>
      <div class="stat"><b>{len(ready)}</b><span>complete courses</span></div>
      <div class="stat"><b>{total}</b><span>books in the library</span></div>
      <div class="stat"><b>5</b><span>JLPT levels</span></div>
    </div>

    <div class="section-title"><h2>Choose your level</h2><p>Each level has vocabulary, kanji, grammar, reading and listening.</p></div>
    <section class="level-grid">
{chr(10).join(cards)}
    </section>

    <div class="section-title"><h2>How every study page works</h2></div>
    <div class="steps">
      <div class="step"><h3>Learn the points</h3><p>Each grammar point or word comes with meaning, connection rules, formation tables and every example from the book.</p></div>
      <div class="step"><h3>Do every exercise</h3><p>All questions from the book, with the correct answer marked and a short “why” for each option — checked against the book's own key.</p></div>
      <div class="step"><h3>Fix the confusions</h3><p>A confusion-pairs table and exam-trap notes close each page, so similar forms stop tripping you up.</p></div>
    </div>

    <div class="section-title"><h2>Complete courses</h2><p><a href="library.html">See all {total} books →</a></p></div>
    <div class="book-grid">
{featured}
    </div>'''
    write(rel, page(rel, 'Learn Japanese with Raj · JLPT N1–N5 study pages', body,
                    desc='Self-paced JLPT N1–N5 study pages: grammar, vocabulary, kanji, reading and listening in English, Hindi and Gujarati with romaji.'))


def build_level(level, books):
    rel = f'{level}/index.html'
    v = LEVELS[level]
    lb = [b for b in books if b['level'] == level]
    ready = [b for b in lb if b['status'] == 'ready']
    mods = modules_for(level, books)
    cards = '\n'.join(module_card(level, m, [b for b in lb if b['module'] == m], rel) for m in mods)
    featured = '\n'.join(book_card(b, rel) for b in ready) or '      <p style="color:var(--muted)">No course is complete at this level yet. Every uploaded book is listed in the modules above and in the <a href="../library.html">library</a>.</p>'
    body = f'''{crumbs(rel, [('Home', 'index.html'), (f'JLPT {v["name"]}', None)])}

    <section class="level-hero">
      <div class="lv-badge">{v["name"]}</div>
      <div>
        <span class="section-label">JLPT {v["name"]} · {v["jp"]}</span>
        <h1>{v["en"]} Japanese</h1>
        <p>{v["blurb"]}</p>
      </div>
    </section>

    <div class="stats" style="margin-top:18px">
      <div class="stat"><b>{study_pages(level)}</b><span>study pages</span></div>
      <div class="stat"><b>{len(ready)}</b><span>complete courses</span></div>
      <div class="stat"><b>{len(lb)}</b><span>books uploaded</span></div>
      <div class="stat"><b>{len(mods)}</b><span>modules</span></div>
    </div>

    <div class="section-title"><h2>Modules</h2><p>Pick a skill to see every book for it.</p></div>
    <div class="module-grid">
{cards}
    </div>

    <div class="section-title"><h2>Ready to study</h2></div>
    <div class="book-grid">
{featured}
    </div>'''
    write(rel, page(rel, f'JLPT {v["name"]} · Learn Japanese with Raj', body, body_class=f'level-page {level}',
                    desc=f'JLPT {v["name"]} ({v["en"]}) study pages: vocabulary, kanji, grammar, reading and listening.'))


def build_module_hub(level, mod, books):
    rel = f'{level}/{mod}.html'
    v, m = LEVELS[level], MODULES[mod]
    mb = [b for b in books if b['level'] == level and b['module'] == mod]
    grid = '\n'.join(book_card(b, rel) for b in mb)
    if mb:
        ready = sum(b['status'] == 'ready' for b in mb)
        note = (f'<strong>{ready} of {len(mb)} books ready</strong>Ready books link to their full course. '
                'The others have a placeholder page and will be built one by one, in the same format as the finished courses.')
        books_html = f'''    <div class="section-title"><h2>Books</h2><p>{len(mb)} uploaded for {v["name"]} {m["name"].lower()}</p></div>
    <div class="book-grid">
{grid}
    </div>'''
    else:
        note = ('<strong>No book uploaded yet</strong>Add a source book under '
                f'<code>book-source/{level}/{mod}/</code>, run <code>python tools/build_site.py --scan</code>, and it will appear here.')
        books_html = ''
    body = f'''{crumbs(rel, [('Home', 'index.html'), (f'JLPT {v["name"]}', f'{level}/index.html'), (m['name'], None)])}

    <div class="page-head">
      <span class="section-label">JLPT {v["name"]} · Module</span>
      <h1>{m["name"]} <span style="color:var(--muted);font-weight:600;font-size:.6em">{m["jp"]}</span></h1>
      <p>{m["desc"]}</p>
    </div>

    <div class="sample-note"><span>{'📚' if mb else '🗂️'}</span><div>{note}</div></div>

{books_html}'''
    write(rel, page(rel, f'{v["name"]} {m["name"]} · Learn Japanese with Raj', body, body_class=f'level-page {level}'))


WILL_CONTAIN = {
    'vocabulary': ['Day-by-day word lists with reading, part of speech and meaning in EN/HI/GU', 'Example sentences with romaji', 'Every exercise with answers', 'Confusable-word pairs'],
    'kanji': ['Each kanji with on/kun readings and meaning', 'Compound words with readings and EN/HI/GU meanings', 'Every exercise with answers'],
    'grammar': ['Each grammar point with meaning, connection and formation table', 'Every example sentence in EN/HI/GU with romaji', 'Every exercise with answers and a “why” for each option', 'Confusion pairs and exam traps'],
    'reading': ['Reading strategy notes for each passage type', 'Questions with the key sentences quoted and explained', 'Answers checked against the book key'],
    'listening': ['Lesson-by-lesson listening tasks with track references', 'Question types and listening strategies', 'Answers checked against the book key'],
    'mock-tests': ['Every section of each practice test', 'Answers with explanations', 'Review links back to the grammar and vocabulary pages'],
    'multi-skill': ['Unit-by-unit pages for every section the book covers', 'Answers with explanations'],
    'textbooks': ['Lesson-by-lesson notes, vocabulary and grammar', 'Exercises with answers'],
}


def build_placeholder(b):
    rel = b['href']
    v, m = LEVELS[b['level']], MODULES[b['module']]
    facts = [('Level', f'JLPT {b["covers"]}'), ('Module', f'{m["name"]} ({m["jp"]})')]
    if b.get('pdf_pages'):
        facts.append(('Book pages', str(b['pdf_pages'])))
    if b.get('audio_tracks'):
        facts.append(('Audio', f'{b["audio_tracks"]} tracks (kept locally, not published)'))
    rows = '\n'.join(f'          <tr><th>{k}</th><td>{esc(val)}</td></tr>' for k, val in facts)
    items = '\n'.join(f'        <li>{x}</li>' for x in WILL_CONTAIN[b['module']])
    status_note = ('<strong>Audio only — PDF needed</strong>This book was uploaded with its audio but without the PDF, so it cannot be built yet.'
                   if b['status'] == 'audio-only' else
                   '<strong>Coming soon</strong>This book is in the library and will be built into day-by-day study pages in the same format as the finished courses.')
    body = f'''{crumbs(rel, [('Home', 'index.html'), (f'JLPT {v["name"]}', f'{b["level"]}/index.html'), (m['name'], f'{b["level"]}/{b["module"]}.html'), (esc(b['title']), None)])}

    <div class="page-head">
      <span class="section-label">JLPT {v["name"]} · {m["name"]} · Book</span>
      <h1>{esc(b["title"])}</h1>
      <p>{esc(b["title_en"])}</p>
    </div>

    <div class="sample-note"><span>{'🎧' if b['status'] == 'audio-only' else '🛠️'}</span><div>{status_note}</div></div>

    <div class="bp-table-wrap" style="max-width:560px">
      <table class="bp-table">
{rows}
      </table>
    </div>

    <div class="prose">
      <h2>What this course will contain</h2>
      <ul>
{items}
      </ul>
      <p><a class="btn" href="{depth_prefix(rel)}{b["level"]}/{b["module"]}.html">← All {v["name"]} {m["name"].lower()} books</a></p>
    </div>'''
    write(rel, page(rel, f'{b["title"]} · Learn Japanese with Raj', body, body_class=f'level-page {b["level"]}', extra_css=('day-page.css',)))


def build_library(books):
    rel = 'library.html'
    lv_chips = ''.join(f'<button class="chip" type="button" data-filter-level="{k}" aria-pressed="false">{v["name"]}</button>' for k, v in LEVELS.items())
    sections = []
    for k, v in LEVELS.items():
        lb = [b for b in books if b['level'] == k]
        if not lb:
            continue
        mods = []
        for mod in MODULE_ORDER:
            mb = [b for b in lb if b['module'] == mod]
            if not mb:
                continue
            grid = '\n'.join(book_card(b, rel) for b in mb)
            mods.append(f'''      <div class="lib-module">
        <h3>{MODULES[mod]["name"]} · {MODULES[mod]["jp"]}</h3>
        <div class="book-grid">
{grid}
        </div>
      </div>''')
        sections.append(f'''    <section class="lib-level lv-{k}" data-level-section="{k}">
      <h2><span class="dot"></span>JLPT {v["name"]} <span style="color:var(--muted);font-size:.7em;font-weight:600">{v["en"]} · {len(lb)} books</span></h2>
{chr(10).join(mods)}
    </section>''')
    ready = sum(b['status'] == 'ready' for b in books)
    body = f'''{crumbs(rel, [('Home', 'index.html'), ('Library', None)])}

    <div class="page-head">
      <span class="section-label">Book library</span>
      <h1>Every book, every level</h1>
      <p>{len(books)} JLPT workbooks across N1–N5. {ready} are complete study courses; the rest are queued and have a placeholder page.</p>
    </div>

    <div class="filter-bar" role="search">
      <input type="search" placeholder="Search books — e.g. 新完全マスター, grammar, N3" aria-label="Search books" data-lib-search />
      <div class="chip-group" aria-label="Filter by level">{lv_chips}</div>
      <div class="chip-group" aria-label="Filter by status"><button class="chip" type="button" data-filter-status="ready" aria-pressed="false">Ready only</button></div>
    </div>
    <p class="empty-note" data-lib-empty>No books match your search.</p>

{chr(10).join(sections)}'''
    write(rel, page(rel, 'Library · Learn Japanese with Raj', body, extra_js=('library.js',),
                    desc='All JLPT N1–N5 workbooks used on the site, with their study-course status.'))


def build_about(books):
    rel = 'about.html'
    body = f'''{crumbs(rel, [('Home', 'index.html'), ('About', None)])}

    <div class="page-head">
      <span class="section-label">About</span>
      <h1>How to use this site</h1>
      <p>A personal JLPT study site. Every page follows one of the popular JLPT workbooks, unit by unit, and explains it for learners whose native languages are Hindi and Gujarati.</p>
    </div>

    <div class="prose">
      <h2>Finding your way</h2>
      <ul>
        <li><b>Levels</b> — N1 (hardest) to N5 (beginner). Each level page lists its modules.</li>
        <li><b>Modules</b> — vocabulary, kanji, grammar, reading and listening, plus mock tests, all-in-one books and textbooks where available.</li>
        <li><b>Books</b> — a module can have several books. Each finished book has its own contents page with every week, day or lesson as a chip.</li>
        <li><b>Library</b> — every uploaded book in one searchable list, with its status.</li>
      </ul>

      <h2>Inside a study page</h2>
      <ul>
        <li><b>Header</b> — the book, the printed pages covered, the points on the page and where the answers come from.</li>
        <li><b>§1 Points</b> — meaning in English, Hindi and Gujarati, connection rules, formation tables and examples. Anything not in the book is marked <i>(added, not in book)</i>.</li>
        <li><b>§2 Exercises</b> — every question, with the correct option marked ✅ and a short “why”.</li>
        <li><b>§3 Confusion pairs</b> — similar forms side by side, plus the traps the exam likes to set.</li>
        <li>Romaji sits under every Japanese line. Use the 🌙 button for dark mode.</li>
      </ul>

      <h2>About the source books</h2>
      <p>The pages are study notes based on published JLPT workbooks. The books, scans and audio are not published here; listening pages refer to tracks by number so you can play them from your own copy. Long reading passages are summarised rather than reproduced.</p>
    </div>'''
    write(rel, page(rel, 'About · Learn Japanese with Raj', body))


def build_404():
    # Served by GitHub Pages for any missing URL at any depth, so links are
    # resolved at runtime against the site root instead of relative paths.
    write('404.html', '''<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Page not found · Learn Japanese with Raj</title>
  <meta name="robots" content="noindex" />
  <script>
    // Project sites live under /<repo>/ on github.io; user sites and local servers at /.
    (function () {
      var seg = location.pathname.split('/').filter(Boolean);
      var base = /\\.github\\.io$/.test(location.hostname) && seg.length ? '/' + seg[0] + '/' : '/';
      window.SITE_BASE = base;
      document.write('<base href="' + base + '">');
    })();
  </script>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="assets/css/style.css" />
</head>
<body>
  <main class="container" id="main">
    <section class="hero">
      <div class="hero-art" aria-hidden="true" style="max-width:160px;margin:0 auto 24px"><span style="font-size:3.4rem">迷</span></div>
      <h1>Page not found</h1>
      <p>This page doesn't exist — it may not have been built yet, or the link has a typo.</p>
      <p style="margin-top:22px"><a class="btn btn-primary" href="index.html">Go to the home page</a> <a class="btn" href="library.html">Browse the library</a></p>
    </section>
  </main>
</body>
</html>
''')


# ---------------------------------------------------------------- existing pages

HDR_RE = re.compile(r'<header class="site-header">.*?</header>', re.S)
FTR_RE = re.compile(r'<footer class="site-footer">.*?</footer>', re.S)
BLOCK_START, BLOCK_END = '<!-- catalog:books:start -->', '<!-- catalog:books:end -->'


def refresh_chrome(rel, s):
    s = HDR_RE.sub(lambda m: header(rel), s, count=1)
    s = FTR_RE.sub(lambda m: footer(rel), s, count=1)
    if 'class="skip-link"' not in s:
        s = re.sub(r'(<body[^>]*>)', r'\1\n  <a class="skip-link" href="#main">Skip to content</a>', s, count=1)
    s = re.sub(r'<main class="container">', '<main class="container" id="main">', s, count=1)
    return s


def books_block(rel, level, mod, books):
    mb = [b for b in books if b['level'] == level and b['module'] == mod]
    others = [b for b in mb if b['href'] != rel]
    if not others:
        return ''
    grid = '\n'.join(book_card(b, rel, current_href=rel) for b in mb)
    v, m = LEVELS[level], MODULES[mod]
    return f'''    {BLOCK_START}
    <div class="section-title"><h2>All {v["name"]} {m["name"].lower()} books</h2><p>{len(mb)} books · this course is one of them</p></div>
    <div class="book-grid">
{grid}
    </div>
    {BLOCK_END}
'''


def refresh_existing(books, generated):
    n = 0
    for f in glob.glob(os.path.join(ROOT, '**', '*.html'), recursive=True):
        rel = os.path.relpath(f, ROOT).replace('\\', '/')
        if rel in generated or rel.startswith(('book-source/', 'tools/', 'node_modules/')) or rel in ('404.html', 'login.html'):
            continue
        s = open(f, encoding='utf-8').read()
        if '<header class="site-header">' not in s:
            continue
        new = refresh_chrome(rel, s)
        if rel in HANDBUILT_HUBS:
            level, mod = rel.split('/')[0], rel.split('/')[1][:-5]
            # one-time removal of the hand-written "Other workbooks" block on n1/grammar.html
            if BLOCK_START not in new and '<div class="page-head" style="margin-top:40px;">' in new:
                i = new.index('    <div class="page-head" style="margin-top:40px;">')
                j = new.index('  </main>', i)
                new = new[:i] + new[j:]
            new = re.sub(r'\s*' + re.escape(BLOCK_START) + r'.*?' + re.escape(BLOCK_END) + r'\n?', '\n', new, flags=re.S)
            blk = books_block(rel, level, mod, books)
            if blk:
                new = new.replace('  </main>', '\n' + blk + '  </main>', 1)
        if new != s:
            open(f, 'w', encoding='utf-8', newline='\n').write(new)
            n += 1
    return n


# ---------------------------------------------------------------- main

def main():
    if '--scan' in sys.argv or not os.path.exists(CATALOG):
        scan()
    books = load()
    generated = {'index.html', 'library.html', 'about.html'}
    build_home(books); build_library(books); build_about(books); build_404()
    open(os.path.join(ROOT, '.nojekyll'), 'w').close()
    for level in LEVELS:
        build_level(level, books); generated.add(f'{level}/index.html')
        for mod in modules_for(level, books):
            rel = f'{level}/{mod}.html'
            if rel not in HANDBUILT_HUBS:
                build_module_hub(level, mod, books); generated.add(rel)
    for b in books:
        if b['status'] != 'ready':
            p = os.path.join(ROOT, b['href'])
            if os.path.exists(p) and 'class="day-chip' in open(p, encoding='utf-8').read():
                continue  # course in progress: its hub is hand-built, keep it
            build_placeholder(b); generated.add(b['href'])
    changed = refresh_existing(books, generated)
    ready = sum(b['status'] == 'ready' for b in books)
    print(f'generated {len(generated)} structural pages; refreshed chrome on {changed} existing pages')
    print(f'books: {len(books)} total, {ready} ready, {sum(b["status"] == "soon" for b in books)} coming soon, '
          f'{sum(b["status"] == "audio-only" for b in books)} audio-only')


if __name__ == '__main__':
    main()
