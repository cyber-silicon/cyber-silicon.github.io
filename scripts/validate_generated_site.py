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

# Validate the shared post-comments integration without depending on temporary sample posts.
POST_LAYOUT = Path("_layouts/post.html")
COMMENTS_INCLUDE = Path("_includes/comments.html")
if not POST_LAYOUT.exists():
    ERRORS.append(f"Missing post layout: {POST_LAYOUT}")
else:
    try:
        if "{% include comments.html %}" not in POST_LAYOUT.read_text(encoding="utf-8"):
            ERRORS.append(f"{POST_LAYOUT}: missing shared comments include")
    except OSError as exc:
        ERRORS.append(f"Could not inspect post layout: {exc}")

if not COMMENTS_INCLUDE.exists():
    ERRORS.append(f"Missing comments include: {COMMENTS_INCLUDE}")
else:
    try:
        comments_source = COMMENTS_INCLUDE.read_text(encoding="utf-8")
        if "https://giscus.app/client.js" not in comments_source or 'class="giscus"' not in comments_source:
            ERRORS.append(f"{COMMENTS_INCLUDE}: missing Giscus client integration")
    except OSError as exc:
        ERRORS.append(f"Could not inspect comments include: {exc}")

GISCUS_FRAGMENTS = [
    "https://giscus.app/client.js",
    'data-repo="cyber-silicon/cyber-silicon.github.io"',
    'data-repo-id="R_kgDOVXRHBA"',
    'data-category="General"',
    'data-category-id="DIC_kwDOVXRHBM4DJtF0"',
    'data-mapping="pathname"',
    'data-lang="ar"',
]
giscus_pages = 0
for html in ROOT.rglob("*.html"):
    parser = MetaParser()
    try:
        page_html = html.read_text(encoding="utf-8")
        parser.feed(page_html)
    except UnicodeDecodeError:
        continue

    rel = html.relative_to(ROOT)
    if "https://giscus.app/client.js" in page_html:
        giscus_pages += 1
        for fragment in GISCUS_FRAGMENTS:
            if fragment not in page_html:
                ERRORS.append(f"{rel}: missing Giscus config fragment {fragment!r}")
        if page_html.count("https://giscus.app/client.js") != 1:
            ERRORS.append(f"{rel}: expected exactly one Giscus script")
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
