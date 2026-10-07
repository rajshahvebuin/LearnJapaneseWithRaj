"""Extract N1 flashcard / quiz data from the built study pages.

Scans the existing N1 HTML pages (read-only) and writes compact JSON under
assets/data/n1/{vocab,kanji,quiz}/ for the flashcard and quiz pages.

    python tools/extract_study_data.py            # extract + write JSON + report
    python tools/extract_study_data.py --survey   # only print table header variants

Standard library only. HTML is parsed into a small element tree with
html.parser so nested tables / spans are handled structurally.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, OrderedDict, defaultdict
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
N1 = ROOT / "n1"
OUT = ROOT / "assets" / "data" / "n1"

# ---------------------------------------------------------------------------
# Minimal DOM
# ---------------------------------------------------------------------------
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link",
        "meta", "param", "source", "track", "wbr"}
# tags whose open implicitly closes an open sibling of the listed kinds
IMPLIED_CLOSE = {
    "tr": {"tr", "td", "th"},
    "td": {"td", "th"},
    "th": {"td", "th"},
    "li": {"li"},
    "p": {"p"},
    "option": {"option"},
}
# containers that stop the implicit-close search
SCOPE_STOP = {"table", "tbody", "thead", "tfoot", "ul", "ol", "div", "body", "html"}


class Node:
    __slots__ = ("tag", "attrs", "children", "parent")

    def __init__(self, tag, attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs or {})
        self.children = []
        self.parent = parent

    @property
    def classes(self):
        return set((self.attrs.get("class") or "").split())

    def has_class(self, c):
        return c in self.classes

    def iter(self):
        """Depth-first iteration over element descendants (incl. self)."""
        stack = [self]
        while stack:
            n = stack.pop()
            yield n
            for ch in reversed(n.children):
                if isinstance(ch, Node):
                    stack.append(ch)

    def find_all(self, tag=None, cls=None):
        for n in self.iter():
            if n is self:
                continue
            if tag and n.tag != tag:
                continue
            if cls and not n.has_class(cls):
                continue
            yield n

    def find(self, tag=None, cls=None):
        return next(self.find_all(tag, cls), None)

    def child_elems(self, tag=None):
        return [c for c in self.children
                if isinstance(c, Node) and (tag is None or c.tag == tag)]


class TreeBuilder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("#root")
        self.cur = self.root

    def handle_starttag(self, tag, attrs):
        tag = tag.lower()
        closes = IMPLIED_CLOSE.get(tag)
        if closes:
            n = self.cur
            while n is not self.root and n.tag not in SCOPE_STOP:
                if n.tag in closes:
                    self.cur = n.parent
                    break
                n = n.parent
        node = Node(tag, attrs, self.cur)
        self.cur.children.append(node)
        if tag not in VOID:
            self.cur = node

    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag.lower(), attrs, self.cur))

    def handle_endtag(self, tag):
        tag = tag.lower()
        if tag in VOID:
            return
        n = self.cur
        while n is not self.root:
            if n.tag == tag:
                self.cur = n.parent
                return
            n = n.parent
        # stray end tag: ignore

    def handle_data(self, data):
        self.cur.children.append(data)


def parse_html(text: str) -> Node:
    b = TreeBuilder()
    b.feed(text)
    b.close()
    return b.root


# ---------------------------------------------------------------------------
# Text helpers
# ---------------------------------------------------------------------------
WS = re.compile(r"\s+")


def collapse(s: str) -> str:
    return WS.sub(" ", s).strip()


def _text(node, skip_romaji: bool, out: list):
    for ch in node.children:
        if isinstance(ch, str):
            out.append(ch)
        else:
            if ch.tag in ("script", "style"):
                continue
            if skip_romaji and ch.tag == "span" and ch.has_class("romaji"):
                out.append(" ")
                continue
            if ch.tag == "br":
                out.append(" ")
                continue
            _text(ch, skip_romaji, out)


def text_of(node, skip_romaji=False) -> str:
    if node is None:
        return ""
    out = []
    _text(node, skip_romaji, out)
    return collapse("".join(out))


def jp_of(node) -> str:
    """Japanese text: everything except span.romaji content."""
    return text_of(node, skip_romaji=True)


def romaji_of(node) -> str:
    """Romaji: text of span.romaji descendants (joined)."""
    if node is None:
        return ""
    parts = [text_of(s) for s in node.find_all("span", "romaji")]
    return collapse(" ".join(p for p in parts if p))


def jp_main(node) -> str:
    """Japanese text without romaji spans and without span.note asides."""
    if node is None:
        return ""
    out = []

    def walk(n):
        for ch in n.children:
            if isinstance(ch, str):
                out.append(ch)
            elif ch.tag in ("script", "style"):
                continue
            elif ch.tag == "span" and (ch.has_class("romaji") or ch.has_class("note")):
                out.append(" ")
            elif ch.tag == "br":
                out.append(" ")
            else:
                walk(ch)
    walk(node)
    return collapse("".join(out))


def note_of(node) -> str:
    """Text of span.note asides inside a cell (outer parentheses dropped)."""
    if node is None:
        return ""
    parts = []
    for s in node.find_all("span", "note"):
        t = text_of(s)
        if t.startswith(("(", "（")) and t.endswith((")", "）")):
            t = t[1:-1].strip()
        if t:
            parts.append(t)
    return " ".join(parts)


def split_kana_romaji(r: str):
    """'かっき · kakki' -> ('かっき', 'kakki'); plain romaji passes through."""
    if " · " in r:
        head, tail = r.split(" · ", 1)
        if has_jp(head) and not has_jp(tail):
            return head.strip(), tail.strip()
    return "", r


JP_CHARS = re.compile(r"[぀-ヿ㐀-鿿ｦ-ﾟ]")


def has_jp(s: str) -> bool:
    return bool(JP_CHARS.search(s or ""))


# ---------------------------------------------------------------------------
# Table helpers
# ---------------------------------------------------------------------------
def table_rows(table: Node):
    """<tr> elements belonging to this table (not nested tables)."""
    rows = []

    def walk(n):
        for c in n.child_elems():
            if c.tag == "tr":
                rows.append(c)
            elif c.tag in ("thead", "tbody", "tfoot"):
                walk(c)
    walk(table)
    return rows


def row_cells(tr: Node):
    return [c for c in tr.child_elems() if c.tag in ("td", "th")]


def header_of(table: Node):
    """(header_texts, data_rows). Header = first row made only of <th>."""
    rows = table_rows(table)
    if rows:
        cells = row_cells(rows[0])
        if cells and all(c.tag == "th" for c in cells):
            hdr = tuple(jp_of(c) for c in cells)
            return hdr, rows[1:]
    return (), rows


def norm_header(h: str) -> str:
    h = h.lower()
    h = re.sub(r"\(.*?\)|（.*?）", "", h)
    return collapse(h)


def map_columns(header, rules):
    """rules: list of (key, predicate(normalised header)) -> {key: col_index}.
    First matching column wins for each key; a column is used once."""
    hn = [norm_header(h) for h in header]
    used, out = set(), {}
    for key, pred in rules:
        for i, h in enumerate(hn):
            if i in used:
                continue
            if pred(h):
                out[key] = i
                used.add(i)
                break
    return out


def cell(cells, idx):
    if idx is None or idx >= len(cells):
        return None
    return cells[idx]


# ---------------------------------------------------------------------------
# Page helpers
# ---------------------------------------------------------------------------
def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


TITLE_RE = re.compile(r"<title>(.*?)</title>", re.S | re.I)
_folder_common = {}


def _title_parts(t: str):
    import html as _html
    t = _html.unescape(t)
    return [collapse(x) for x in t.split(" · ")
            if collapse(x) and collapse(x) != "Learn Japanese with Raj"]


def _common_segments(folder: Path):
    """Title segments shared by most pages of a folder = book/module names."""
    if folder not in _folder_common:
        cnt, n = Counter(), 0
        for p in folder.glob("*.html"):
            if p.name == "index.html":
                continue
            m = TITLE_RE.search(p.read_text(encoding="utf-8"))
            if m:
                n += 1
                cnt.update(set(_title_parts(m.group(1))))
        _folder_common[folder] = {s for s, c in cnt.items() if n >= 3 and c >= 0.6 * n}
    return _folder_common[folder]


def page_unit(doc: Node, path: Path) -> str:
    """Short unit label: the page <title> minus the site, level/module and
    book-name segments (those repeated across the folder), e.g.
    'Week 1 Day 1 · どんな人？' or '文脈規定 第1回'."""
    t = doc.find("title")
    parts = _title_parts(text_of(t)) if t else []
    common = _common_segments(path.parent)
    parts = [p for p in parts if p not in common
             and not re.match(r"^N1 (Vocabulary|Grammar|Kanji|Reading|Listening|Multi-skill|Mock tests?)$", p, re.I)]
    label = parts[0] if parts else ""
    if len(parts) > 1 and len(label) + len(parts[1]) <= 40:
        label += " · " + parts[1]
    if not label:
        h1 = doc.find("h1")
        label = jp_of(h1).split(" — ")[0] if h1 else path.stem
    return label[:60]


def read_doc(path: Path) -> Node:
    return parse_html(path.read_text(encoding="utf-8"))


def html_files(base: Path):
    return sorted(p for p in base.rglob("*.html") if p.is_file())


def sort_key(p: Path):
    """Natural sort (week-2 before week-10, day-2 before day-10)."""
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", rel(p))]


# ---------------------------------------------------------------------------
# Titles (book index.html h1 + English subtitle, falling back to catalog.json)
# ---------------------------------------------------------------------------
CATALOG = json.loads((ROOT / "tools" / "catalog.json").read_text(encoding="utf-8"))

SOU_MATOME_TITLES = {
    "vocabulary": ("日本語総まとめ N1 語彙", "Nihongo Sou-Matome N1 Vocabulary"),
    "kanji": ("日本語総まとめ N1 漢字", "Nihongo Sou-Matome N1 Kanji"),
    "grammar": ("日本語総まとめ N1 文法", "Nihongo Sou-Matome N1 Grammar"),
}


def book_titles(module: str, slug: str):
    if module == "kanji" and slug == "sou-matome-words":
        t, te = book_titles("kanji", "sou-matome")
        return t + "（語）", te + " — Words"
    if slug == "sou-matome" and module in SOU_MATOME_TITLES:
        for e in CATALOG:
            if e.get("level") == "n1" and e.get("module") == module and e.get("slug") == slug:
                return e["title"], e.get("title_en") or SOU_MATOME_TITLES[module][1]
        return SOU_MATOME_TITLES[module]
    for e in CATALOG:
        if e.get("level") == "n1" and e.get("module") == module and e.get("slug") == slug:
            return e["title"], e.get("title_en") or slug
    for e in CATALOG:  # module mismatch fallback
        if e.get("level") == "n1" and e.get("slug") == slug:
            return e["title"], e.get("title_en") or slug
    idx = N1 / module / slug / "index.html"
    if idx.exists():
        d = read_doc(idx)
        h1 = d.find("h1")
        title = jp_of(h1) if h1 else slug
        sub = d.find(cls="subtitle") or d.find("p", "lead")
        return title, (text_of(sub) if sub else slug)
    return slug, slug


def deck_id_for(path: Path, module_dir: Path) -> str:
    relp = path.relative_to(module_dir).parts
    if relp[0].startswith("week-"):
        return "sou-matome"
    return relp[0]


# ---------------------------------------------------------------------------
# 1. Vocabulary
# ---------------------------------------------------------------------------
VOCAB_RULES = [
    ("jp", lambda h: h in ("japanese", "word", "語", "語彙", "vocabulary", "jp", "japanese word")),
    ("reading", lambda h: h in ("reading", "読み", "kana", "furigana")),
    ("en", lambda h: h in ("english", "meaning", "en")),
    ("hi", lambda h: h in ("hindi", "hi")),
    ("gu", lambda h: h in ("gujarati", "gu")),
    ("note", lambda h: h in ("note", "notes", "memo")),
]

header_log = defaultdict(Counter)  # section -> Counter[(table_class, header) + handling]


def extract_vocab():
    vdir = N1 / "vocabulary"
    decks = OrderedDict()
    for path in sorted(html_files(vdir), key=sort_key):
        if path.name == "index.html":
            continue
        doc = read_doc(path)
        tables = [t for t in doc.find_all("table")
                  if t.has_class("vd-wordlist") or t.has_class("bp-table")]
        if not tables:
            continue
        unit = page_unit(doc, path)
        deck = decks.setdefault(deck_id_for(path, vdir), OrderedDict())
        for t in tables:
            hdr, rows = header_of(t)
            cls = "vd-wordlist" if t.has_class("vd-wordlist") else "bp-table"
            cols = map_columns(hdr, VOCAB_RULES)
            ok = "jp" in cols and "en" in cols
            header_log["vocab"][(cls, hdr, "used" if ok else "skipped")] += 1
            if not ok:
                continue
            for tr in rows:
                cells = row_cells(tr)
                jc = cell(cells, cols["jp"])
                if jc is None:
                    continue
                jp = jp_main(jc)
                r = romaji_of(jc)
                kana = ""
                if "reading" in cols:
                    rc = cell(cells, cols["reading"])
                    if rc is not None:
                        kana = jp_of(rc)
                        r = romaji_of(rc) or r
                kana2, r = split_kana_romaji(r)
                kana = kana or kana2
                en = text_of(cell(cells, cols["en"]))
                if not jp or not en or jp in deck:
                    continue
                card = OrderedDict(jp=jp)
                if kana and kana != jp:
                    card["kana"] = kana
                if r:
                    card["r"] = r
                card["en"] = en
                for k in ("hi", "gu"):
                    v = text_of(cell(cells, cols.get(k)))
                    if v:
                        card[k] = v
                note = " ".join(x for x in (note_of(jc), text_of(cell(cells, cols.get("note")))) if x)
                if note:
                    card["note"] = note
                card["src"] = rel(path)
                card["unit"] = unit
                deck[jp] = card
    return {k: list(v.values()) for k, v in decks.items() if v}


# ---------------------------------------------------------------------------
# 2. Kanji
# ---------------------------------------------------------------------------
# Column roles are chosen by header text. Priority lists: the first header
# present wins. 'w' = the word the card is about.
K_WORD = ("word", "compound", "joined word", "expression", "on-yomi word")
K_KANA = ("kana", "special reading", "reading")
K_EX = ("book's example", "example", "antonym", "gloss", "counts",
        "kun-yomi paraphrase", "phrase")


def kanji_colmap(header, deck):
    """Return (mode, cols) for a kd-kanji-table header; mode None = skip."""
    hn = [norm_header(h) for h in header]

    def first(names, used=()):
        for name in names:
            for i, h in enumerate(hn):
                if h == name and i not in used:
                    return i
        return None

    cols = {}
    for key in ("english", "hindi", "gujarati"):
        i = first((key,))
        if i is not None:
            cols[key[:2]] = i
    if "en" not in cols:
        return None, cols
    k = first(("kanji",))
    w = first(K_WORD)
    if deck == "sou-matome" and k is not None and w is None and first(("example",)) is not None:
        # Sou-Matome core table: Kanji | Example | Reading ... (kanji carried down)
        cols.update(k=k, w=first(("example",)), kana=first(K_KANA))
        return "kanji-grouped", cols
    if w is None and first(("reading",)) is not None and first(("kana",)) is not None:
        w = first(("example",))  # Reading | Example | Kana: the example is the word
    if w is None and k is not None and first(("counts",)) is not None:
        w, k = k, None  # counter table: the 'Kanji' cell is the counter itself
    if w is None:
        return None, cols
    cols["w"] = w
    used = {w}
    if k is not None and k != w:
        cols["k"] = k
        used.add(k)
    kana = first(K_KANA, used)
    if kana is not None:
        cols["kana"] = kana
        used.add(kana)
    ex = first(K_EX, used)
    if ex is not None:
        cols["ex"] = ex
    return "word", cols


def ex_text(c):
    """Example cell: Japanese only (drops romaji and nested EN/HI/GU notes)."""
    if c is None:
        return ""
    out = []

    def walk(n):
        for ch in n.children:
            if isinstance(ch, str):
                out.append(ch)
            elif ch.tag == "span" and (ch.has_class("romaji") or ch.has_class("note")):
                out.append(" ")
            elif ch.tag == "br":
                out.append(" ")
            else:
                walk(ch)
    walk(c)
    return collapse("".join(out))


romaji_generated = Counter()


def kanji_cell(c):
    """Kanji column cell -> (kanji, aside). Handles '弟<br><span.note>デ',
    '滅<br>裂<br><span.romaji>', '営(～が経営する)' and '留守 ル・ス'."""
    if c is None:
        return "", ""
    main = jp_main(c)
    aside = note_of(c)
    m = re.match(r"^([^(（]+?)\s*[(（](.+)[)）]$", main)
    if m:
        main, aside = m.group(1), " ".join(x for x in (m.group(2), aside) if x)
    parts = main.split()
    if len(parts) > 1:
        if all(len(p) == 1 and not re.match(r"[゠-ヿ]", p) for p in parts):
            main = "".join(parts)  # stacked kanji: 滅 / 裂
        elif re.match(r"^[゠-ヿ・]+$", "".join(parts[1:])):
            main, aside = parts[0], " ".join([" ".join(parts[1:])] + ([aside] if aside else []))
    return main.strip(), aside.strip()


def extract_kanji():
    kdir = N1 / "kanji"
    sou = OrderedDict()        # kanji char -> grouped card
    sou_words = OrderedDict()  # word -> card (Sou-Matome non-core tables)
    skm = OrderedDict()        # word -> card (Shin Kanzen Master)
    for path in sorted(html_files(kdir), key=sort_key):
        if path.name == "index.html":
            continue
        deck = deck_id_for(path, kdir)
        doc = read_doc(path)
        tables = list(doc.find_all("table", "kd-kanji-table"))
        if not tables:
            continue
        unit = page_unit(doc, path)
        for t in tables:
            hdr, rows = header_of(t)
            mode, cols = kanji_colmap(hdr, deck)
            how = "skipped"
            if mode:
                how = mode + ": " + ", ".join(f"{k}={hdr[v]}" for k, v in cols.items()
                                              if k in ("k", "w", "kana", "ex"))
            header_log["kanji:" + deck][(hdr, how)] += 1
            if not mode:
                continue
            last_k, last_kn = "", ""
            for tr in rows:
                cells = row_cells(tr)
                if not cells:
                    continue
                if "k" in cols:
                    kk, kn = kanji_cell(cell(cells, cols["k"]))
                    if kk:
                        last_k, last_kn = kk, kn
                wc = cell(cells, cols["w"])
                w = jp_main(wc)
                en = text_of(cell(cells, cols["en"]))
                if not w or not en:
                    continue
                kana, r = "", ""
                kc = cell(cells, cols.get("kana"))
                if kc is not None:
                    kana, r = jp_of(kc), romaji_of(kc)
                if not r and kana:
                    # Reading cell printed without romaji: use the word cell's
                    # romaji when it actually spells this reading, else derive it.
                    gen = kana_to_romaji(kana)
                    wr = romaji_of(wc) if wc is not None else ""
                    letters = lambda x: re.sub(r"[^a-z]", "", x.lower())
                    if wr and (not gen or letters(wr).startswith(letters(gen))):
                        r = wr
                    elif gen:
                        r = gen
                        romaji_generated[deck] += 1
                if not r and wc is not None:
                    r = romaji_of(wc)
                word = OrderedDict(w=w)
                if kana:
                    word["kana"] = kana
                if r:
                    word["r"] = r
                word["en"] = en
                for key in ("hi", "gu"):
                    v = text_of(cell(cells, cols.get(key)))
                    if v:
                        word[key] = v
                wn = note_of(wc)
                if wn:
                    word["note"] = wn
                if mode == "kanji-grouped":
                    if not last_k:
                        continue
                    card = sou.get(last_k)
                    if card is None:
                        card = OrderedDict(k=last_k)
                        if last_kn:
                            card["kn"] = last_kn
                        card.update(words=[], src=rel(path), unit=unit)
                        sou[last_k] = card
                    if all(x["w"] != w for x in card["words"]):
                        card["words"].append(word)
                    continue
                target = sou_words if deck == "sou-matome" else skm
                if w in target:
                    continue
                if "k" in cols and len(last_k) == 1:
                    word["k"] = last_k
                ex = ex_text(cell(cells, cols.get("ex")))
                if ex and has_jp(ex):
                    word["ex"] = ex
                word["src"] = rel(path)
                word["unit"] = unit
                target[w] = word
    return OrderedDict([
        ("sou-matome", ("kanji", list(sou.values()))),
        ("sou-matome-words", ("word", list(sou_words.values()))),
        ("shin-kanzen-master", ("word", list(skm.values()))),
    ])


# Kana -> romaji fallback for kana cells printed without romaji
# (wapuro style as used on the site: ou, uu; ー repeats the vowel).
_KANA = {}
for _tok in ("あa いi うu えe おo かka きki くku けke こko さsa しshi すsu せse そso "
             "たta ちchi つtsu てte とto なna にni ぬnu ねne のno はha ひhi ふfu へhe ほho "
             "まma みmi むmu めme もmo やya ゆyu よyo らra りri るru れre ろro わwa ゐi ゑe をo "
             "がga ぎgi ぐgu げge ごgo ざza じji ずzu ぜze ぞzo だda ぢji づzu でde どdo "
             "ばba びbi ぶbu べbe ぼbo ぱpa ぴpi ぷpu ぺpe ぽpo ぁa ぃi ぅu ぇe ぉo ゔvu").split():
    _KANA[_tok[0]] = _tok[1:]
_YOON = {"ゃ": "a", "ゅ": "u", "ょ": "o"}
_YSTEM = {"き": "ky", "ぎ": "gy", "し": "sh", "じ": "j", "ち": "ch", "ぢ": "j", "に": "ny",
          "ひ": "hy", "び": "by", "ぴ": "py", "み": "my", "り": "ry"}


def _syll(s, i):
    """(romaji, length) for the syllable at s[i], or ('', 0) if not kana."""
    c = s[i]
    nxt = s[i + 1] if i + 1 < len(s) else ""
    if c in _YSTEM and nxt in _YOON:
        return _YSTEM[c] + _YOON[nxt], 2
    if c in _KANA:
        return _KANA[c], 1
    return "", 0


def kana_to_romaji(s: str) -> str:
    s = "".join(chr(ord(c) - 0x60) if "ァ" <= c <= "ヶ" else c for c in s)
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "っ":
            nr = _syll(s, i + 1)[0] if i + 1 < len(s) else ""
            out.append("t" if nr.startswith("ch") else nr[:1])
            i += 1
        elif c == "ん":
            out.append("n")
            i += 1
        elif c == "ー":
            prev = "".join(out)
            out.append(prev[-1] if prev and prev[-1] in "aiueo" else "")
            i += 1
        elif c in "／/":
            out.append(" / ")
            i += 1
        elif c in "・ 　、":
            out.append(" ")
            i += 1
        else:
            r, n = _syll(s, i)
            if not n:
                return ""  # contains kanji or symbols: don't guess
            out.append(r)
            i += n
    return collapse("".join(out))


# ---------------------------------------------------------------------------
# 3. Quiz banks
# ---------------------------------------------------------------------------
TANKI_OK = re.compile(r"^(moji-goi-.*|bunpou-.*|matome-moji-goi|matome-bunpou)\.html$")


def quiz_page_ok(path: Path) -> bool:
    parts = path.relative_to(N1).parts
    module, name = parts[0], path.name
    if name == "index.html":
        return False
    if module in ("grammar", "vocabulary", "kanji"):
        return True
    if module == "multi-skill":
        book = parts[1]
        if book == "tanki-master-drill":
            return bool(TANKI_OK.match(name))
        if book == "20-nichi-de-goukaku":
            return name.startswith("day-")
        return name.startswith(("moji-", "bunpou-"))
    if module == "mock-tests":
        return "gengo" in name or name.startswith(("moji-", "bunpou-"))
    return False


OPT_RULES = [
    ("letter", lambda h: h in ("option", "#", "no", "no.", "", "choice", "opt")),
    ("jp", lambda h: h in ("japanese", "option text", "word", "answer", "reading", "jp", "選択肢", "expression", "sentence")),
    ("en", lambda h: h in ("english", "meaning", "en")),
    ("hi", lambda h: h in ("hindi", "hi")),
    ("gu", lambda h: h in ("gujarati", "gu")),
]

skip_reasons = Counter()
opt_headers = Counter()


def quiz_prompt(q: Node):
    p = q.find("p", "q-jp")
    if p is not None:
        return p
    # fallback: first <p> (direct child or nested) with Japanese text
    for n in q.find_all("p"):
        if n.has_class("bp-why"):
            continue
        if has_jp(jp_of(n)):
            return n
    return None


def quiz_lang(q: Node, code: str) -> str:
    """The question's translation line for one language (EN / HI / GU) from .q-translations."""
    tr = q.find(cls="q-translations")
    if tr is None:
        return ""
    for d in tr.find_all():
        b = d.find("b")
        if b is not None and text_of(b).rstrip(":").strip().upper() == code and d.tag != "b":
            t = text_of(d)
            return collapse(re.sub(r"^" + code + r"\s*:\s*", "", t))
    return ""


def quiz_en(q: Node) -> str:
    return quiz_lang(q, "EN")


def extract_quizzes():
    banks = OrderedDict()
    for module in ("grammar", "vocabulary", "kanji", "multi-skill", "mock-tests"):
        mdir = N1 / module
        for path in sorted(html_files(mdir), key=sort_key):
            if not quiz_page_ok(path):
                continue
            doc = read_doc(path)
            quizzes = list(doc.find_all("div", "bp-quiz"))
            if not quizzes:
                continue
            unit = page_unit(doc, path)
            bank = f"{module}-{deck_id_for(path, mdir)}"
            items = banks.setdefault(bank, [])
            for q in quizzes:
                item = parse_quiz(q, path, unit)
                if item:
                    items.append(item)
    return {k: v for k, v in banks.items() if v}


def parse_quiz(q: Node, path: Path, unit: str):
    prompt = quiz_prompt(q)
    if prompt is None or not jp_of(prompt):
        skip_reasons["no prompt"] += 1
        return None
    table = q.find("table", "bp-options")
    if table is None:
        skip_reasons["no bp-options table"] += 1
        return None
    hdr, rows = header_of(table)
    rows = [r for r in rows if row_cells(r)]
    if len(rows) < 2:
        skip_reasons["<2 option rows"] += 1
        return None
    correct = [i for i, r in enumerate(rows) if r.has_class("correct")]
    if len(correct) != 1:
        skip_reasons[f"{len(correct)} correct rows" if correct else "no correct row"] += 1
        return None
    cols = map_columns(hdr, OPT_RULES)
    if "jp" not in cols:
        # first text column after the option letter
        start = cols.get("letter", -1) + 1
        for i in range(max(start, 0), len(hdr)):
            if i not in cols.values():
                cols["jp"] = i
                break
        if "jp" not in cols and not hdr:
            cols["jp"] = 1 if len(row_cells(rows[0])) > 1 else 0
    opt_headers[(hdr, "jp=%s en=%s" % (cols.get("jp"), cols.get("en")))] += 1
    opts = []
    for r in rows:
        cells = row_cells(r)
        c = cell(cells, cols.get("jp"))
        o = OrderedDict(t=jp_of(c) if c is not None else "")
        rr = romaji_of(c) if c is not None else ""
        if rr:
            o["r"] = rr
        for lang in ("en", "hi", "gu"):
            val = text_of(cell(cells, cols.get(lang)))
            if val:
                o[lang] = val
        opts.append(o)
    if sum(1 for o in opts if o["t"]) < 2:
        skip_reasons["empty option text"] += 1
        return None
    item = OrderedDict(q=jp_of(prompt))
    u = [jp_of(x) for x in prompt.find_all("u")]
    if any(u):
        item["u"] = " / ".join(x for x in u if x)  # underlined target word(s)
    qr = romaji_of(prompt)
    if qr:
        item["qr"] = qr
    for lang in ("EN", "HI", "GU"):
        val = quiz_lang(q, lang)
        if val:
            item[lang.lower()] = val
    item["opts"] = opts
    item["a"] = correct[0]
    why_el = q.find(cls="bp-why")
    if why_el is not None:
        why = re.sub(r"^\s*(Why|理由)\s*[:：]\s*", "", text_of(why_el))
        if why:
            item["why"] = why[:400]
    item["src"] = rel(path)
    item["unit"] = unit
    return item


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------
def dump(path: Path, data) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)
    s = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    path.write_text(s, encoding="utf-8")
    return len(s.encode("utf-8"))


def main(argv):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    survey = "--survey" in argv
    vocab = extract_vocab()
    kanji = extract_kanji()
    quiz = extract_quizzes()

    print("== Table header variants ==")
    for sec, cnt in header_log.items():
        print(f"[{sec}]")
        for key, n in cnt.most_common():
            print(f"  {n:5d}  {key}")
    print("[quiz bp-options]")
    for key, n in opt_headers.most_common():
        print(f"  {n:5d}  {key}")
    print("== Quiz skip reasons ==", dict(skip_reasons))
    if survey:
        return

    sizes = {}
    # vocab
    vidx = []
    for did, cards in vocab.items():
        title, title_en = book_titles("vocabulary", did)
        f = f"{did}.json"
        sizes["vocab/" + f] = dump(OUT / "vocab" / f, OrderedDict(
            id=did, title=title, title_en=title_en, cards=cards))
        vidx.append(OrderedDict(id=did, title=title, title_en=title_en,
                                count=len(cards), file=f))
    sizes["vocab/index.json"] = dump(OUT / "vocab" / "index.json",
                                     OrderedDict(level="n1", kind="vocab", decks=vidx))
    # kanji
    kidx = []
    for did, (typ, cards) in kanji.items():
        if not cards:
            continue
        title, title_en = book_titles("kanji", did)
        f = f"{did}.json"
        sizes["kanji/" + f] = dump(OUT / "kanji" / f, OrderedDict(
            id=did, title=title, title_en=title_en, type=typ, cards=cards))
        kidx.append(OrderedDict(id=did, title=title, title_en=title_en, type=typ,
                                count=len(cards), file=f))
    sizes["kanji/index.json"] = dump(OUT / "kanji" / "index.json",
                                     OrderedDict(level="n1", kind="kanji", decks=kidx))
    # quiz
    qidx = []
    for bid, items in quiz.items():
        module = next(m for m in ("multi-skill", "mock-tests", "grammar", "vocabulary", "kanji")
                      if bid.startswith(m + "-"))
        slug = bid[len(module) + 1:]
        title, title_en = book_titles(module, slug)
        f = f"{bid}.json"
        sizes["quiz/" + f] = dump(OUT / "quiz" / f, OrderedDict(
            id=bid, module=module, title=title, title_en=title_en, items=items))
        qidx.append(OrderedDict(id=bid, module=module, title=title, title_en=title_en,
                                count=len(items), file=f))
    sizes["quiz/index.json"] = dump(OUT / "quiz" / "index.json",
                                    OrderedDict(level="n1", kind="quiz", banks=qidx))

    print("== Counts ==")
    for e in vidx:
        print(f"  vocab  {e['id']:32s} {e['count']:6d}")
    for e in kidx:
        print(f"  kanji  {e['id']:32s} {e['count']:6d}  ({e['type']})")
    for e in qidx:
        print(f"  quiz   {e['id']:40s} {e['count']:6d}")
    for kind in ("vocab", "kanji", "quiz"):
        tot = sum(v for k, v in sizes.items() if k.startswith(kind + "/"))
        print(f"  {kind} total: {tot / 1024:.1f} KB")
    print(f"  ALL: {sum(sizes.values()) / 1024:.1f} KB")
    print("== Kana->romaji fallback used ==", dict(romaji_generated))

    import random
    rng = random.Random(7)
    print("== Samples ==")
    for name, cards in (("vocab", [c for d in vocab.values() for c in d]),
                        ("kanji", [c for _, d in kanji.values() for c in d]),
                        ("quiz", [c for d in quiz.values() for c in d])):
        for c in rng.sample(cards, 2):
            print(f"  [{name}]", json.dumps(c, ensure_ascii=False)[:500])
    verify_quiz(quiz, rng)


def _strip_tags(s: str) -> str:
    s = re.sub(r'<span class="romaji"[^>]*>.*?</span>', " ", s, flags=re.S)
    import html as _html
    return collapse(_html.unescape(re.sub(r"<[^>]+>", " ", s)))


def verify_quiz(quiz, rng, n=5):
    """Independent spot check: in the raw page, find the quiz by its prompt
    text and compare the first tr.correct after it with opts[a]."""
    print(f"== Spot-check {n} random quiz items against source ==")
    items = [it for b in quiz.values() for it in b]
    ok = 0
    nows = lambda x: re.sub(r"\s+", "", x)
    for it in rng.sample(items, n):
        raw = (ROOT / it["src"]).read_text(encoding="utf-8")
        starts = [m.start() for m in re.finditer(r'<div class="bp-quiz"', raw)] + [len(raw)]
        correct_txt = "?"
        for a, b in zip(starts, starts[1:]):
            blk = raw[a:b]
            pm = re.search(r'<p class="q-jp">(.*?)</p>', blk, re.S)
            head = nows(_strip_tags(pm.group(1))) if pm else nows(_strip_tags(blk))[:len(nows(it["q"])) + 400]
            flat = nows(_strip_tags(blk))
            if (head == nows(it["q"]) if pm else nows(it["q"]) in head) and                     all(nows(o["t"]) in flat for o in it["opts"]):
                cm = re.search(r'<tr class="correct">(.*?)</tr>', raw[a:b], re.S)
                correct_txt = _strip_tags(cm.group(1)) if cm else "?"
                break
        hit = nows(it["opts"][it["a"]]["t"]) in nows(correct_txt)
        ok += hit
        print(f"  {'OK ' if hit else 'BAD'} {it['src']} | q={it['q'][:30]} | a={it['a']} "
              f"'{it['opts'][it['a']]['t'][:20]}' | source correct row: {correct_txt[:50]}")
    print(f"  {ok}/{n} matched")


if __name__ == "__main__":
    main(sys.argv[1:])
