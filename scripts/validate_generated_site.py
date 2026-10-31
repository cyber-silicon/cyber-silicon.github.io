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
