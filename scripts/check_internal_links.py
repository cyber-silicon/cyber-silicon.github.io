from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote
import sys

ROOT = Path("_site").resolve()
BROKEN = []

class Parser(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.source = source

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ("href", "src"):
            value = attrs.get(key)
            if not value:
                continue
            if value.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                continue
            parsed = urlparse(value)
            if parsed.scheme or parsed.netloc:
                continue
            path = unquote(parsed.path)
            if not path:
                continue
            if path.startswith("/"):
                target = ROOT / path.lstrip("/")
            else:
                target = (self.source.parent / path).resolve()
            candidates = [target]
            if target.suffix == "":
                candidates += [target / "index.html", Path(str(target) + ".html")]
            if not any(p.exists() for p in candidates):
                BROKEN.append((self.source.relative_to(ROOT), value))

for html in ROOT.rglob("*.html"):
    try:
        Parser(html).feed(html.read_text(encoding="utf-8"))
    except UnicodeDecodeError:
        pass

if BROKEN:
    print("Broken internal links/assets:")
    for source, value in BROKEN:
        print(f" - {source}: {value}")
    sys.exit(1)

print("Internal link check passed.")
