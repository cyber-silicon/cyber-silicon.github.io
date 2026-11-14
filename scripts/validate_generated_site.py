from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path("_site")
ERRORS = []
REQUIRED = [
    ROOT / "index.html",
    ROOT / "404.html",
    ROOT / "about" / "index.html",
    ROOT / "categories" / "index.html",
    ROOT / "tags" / "index.html",
    ROOT / "bookmarks" / "index.html",
    ROOT / "privacy" / "index.html",
    ROOT / "terms" / "index.html",
    ROOT / "feed.xml",
    ROOT / "sitemap.xml",
    ROOT / "tiktoky3OKmXmwUNjswR7HZjSinb9EBScow5tj.txt",
]

class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.canonicals = 0
        self.json_ld = 0
        self.lang = None
        self.direction = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "html":
            self.lang = attrs.get("lang")
            self.direction = attrs.get("dir")
        elif tag == "link" and attrs.get("rel") == "canonical":
            self.canonicals += 1
        elif tag == "script" and attrs.get("type") == "application/ld+json":
            self.json_ld += 1

for path in REQUIRED:
    if not path.exists():
        ERRORS.append(f"Missing generated file: {path}")

# The canonical Blogger-backed Kali lesson must render exactly one Arabic Giscus instance.
COMMENTED_POST = ROOT / "2026" / "11" / "kali-linux-3-virtualbox-virtual-machine.html"
if not COMMENTED_POST.exists():
    ERRORS.append(f"Missing canonical Blogger-backed article: {COMMENTED_POST}")
else:
    try:
        article_html = COMMENTED_POST.read_text(encoding="utf-8")
        required_comment_fragments = [
            "https://giscus.app/client.js",
            'data-repo="cyber-silicon/cyber-silicon.github.io"',
            'data-repo-id="R_kgDOVXRHBA"',
            'data-category="General"',
            'data-category-id="DIC_kwDOVXRHBM4DJtF0"',
            'data-mapping="pathname"',
            'data-lang="ar"',
        ]
        for fragment in required_comment_fragments:
            if fragment not in article_html:
                ERRORS.append(f"{COMMENTED_POST}: missing Giscus config fragment {fragment!r}")
        if article_html.count("https://giscus.app/client.js") != 1:
            ERRORS.append(f"{COMMENTED_POST}: expected exactly one Giscus script")
    except OSError as exc:
        ERRORS.append(f"Could not inspect Giscus article output: {exc}")

for html in ROOT.rglob("*.html"):
    parser = MetaParser()
    try:
        parser.feed(html.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        continue

    rel = html.relative_to(ROOT)
    if parser.lang != "ar":
        ERRORS.append(f"{rel}: expected html lang=ar, found {parser.lang!r}")
    if parser.direction != "rtl":
        ERRORS.append(f"{rel}: expected html dir=rtl, found {parser.direction!r}")
    if parser.canonicals != 1:
        ERRORS.append(f"{rel}: expected exactly 1 canonical link, found {parser.canonicals}")
    if parser.json_ld > 1:
        ERRORS.append(f"{rel}: duplicate JSON-LD blocks ({parser.json_ld})")

if ERRORS:
    print("Generated site validation failed:")
    for error in ERRORS:
        print(f" - {error}")
    sys.exit(1)

print("Generated site structure and SEO checks passed.")
