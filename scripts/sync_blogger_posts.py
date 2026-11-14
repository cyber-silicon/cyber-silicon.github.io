#!/usr/bin/env python3
"""Safely import published posts from a public Blogger blog into Jekyll.

Dry-run is the default. Use --apply to write files. Existing hand-written
Jekyll posts are never overwritten; only files carrying this importer's
blogger_id front matter can be updated.
"""
from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import sys
from datetime import datetime
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen


API_ROOT = "https://www.googleapis.com/blogger/v3"
DEFAULT_BLOG_URL = "https://cyber-silicon.blogspot.com/"
PERMALINK_RE = re.compile(r"^/\d{4}/\d{2}/[A-Za-z0-9._~!$&'()*+,;=:@%-]+\.html$")
BLOGGER_MARKER_RE = re.compile(r'^blogger_id:\s*["\']?([0-9]+)', re.MULTILINE)
BLOCKED_TAGS = {"script", "style", "object", "embed", "form", "input", "button",
                "textarea", "select", "option", "meta", "link", "base"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
             "link", "meta", "param", "source", "track", "wbr"}
ALLOWED_IFRAME_HOSTS = {"www.youtube.com", "youtube.com", "www.youtube-nocookie.com",
                        "youtube-nocookie.com", "player.vimeo.com"}


class SyncError(RuntimeError):
    pass


class SafeHTML(HTMLParser):
    """Conservative Blogger HTML sanitizer for imported static pages."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=False)
        self.parts: list[str] = []
        self.skip_depth = 0

    @staticmethod
    def _safe_url(value: str) -> bool:
        value = value.strip()
        lowered = value.lower()
        if lowered.startswith(("javascript:", "vbscript:", "data:", "file:")):
            return False
        return True

    @staticmethod
    def _safe_style(value: str) -> bool:
        lowered = value.lower()
        forbidden = ("javascript:", "expression(", "behavior:", "@import", "url(")
        return not any(token in lowered for token in forbidden)

    def _attrs(self, tag: str, attrs: list[tuple[str, str | None]]) -> str:
        safe: list[tuple[str, str]] = []
        for name, value in attrs:
            name = name.lower()
            if value is None or name.startswith("on") or name in {"srcdoc", "formaction"}:
                continue
            if name in {"href", "src", "poster"} and not self._safe_url(value):
                continue
            if name == "style" and not self._safe_style(value):
                continue
            if name not in {
                "href", "src", "poster", "alt", "title", "width", "height",
                "class", "id", "name", "target", "rel", "dir", "lang",
                "loading", "decoding", "colspan", "rowspan", "scope",
                "align", "border", "cellpadding", "cellspacing", "datetime",
                "type", "controls", "autoplay", "muted", "loop", "start",
                "reversed", "style", "role", "aria-label", "aria-hidden",
                "allow", "allowfullscreen", "frameborder", "referrerpolicy"
            } and not name.startswith("data-"):
                continue
            safe.append((name, value))
        if tag == "a":
            target_blank = any(k == "target" and v == "_blank" for k, v in safe)
            if target_blank and not any(k == "rel" for k, _ in safe):
                safe.append(("rel", "noopener noreferrer"))
        rendered = []
        for name, value in safe:
            rendered.append(f' {name}="{html.escape(value, quote=True)}"')
        return "".join(rendered)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if self.skip_depth:
            if tag in BLOCKED_TAGS:
                self.skip_depth += 1
            return
        if tag in BLOCKED_TAGS:
            self.skip_depth = 1
            return
        if tag == "iframe":
            src = next((v for k, v in attrs if k.lower() == "src" and v), "")
            host = urlparse(src or "").hostname or ""
            if host not in ALLOWED_IFRAME_HOSTS:
                self.skip_depth = 1
                return
        self.parts.append(f"<{tag}{self._attrs(tag, attrs)}>")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag.lower() not in VOID_TAGS and self.skip_depth == 0:
            self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.skip_depth:
            if tag in BLOCKED_TAGS:
                self.skip_depth = max(0, self.skip_depth - 1)
            return
        if tag not in VOID_TAGS and tag not in BLOCKED_TAGS:
            self.parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if not self.skip_depth:
            self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        if not self.skip_depth:
            self.parts.append(f"&#{name};")

    def handle_comment(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(f"<!--{data.replace('--', '—')}-->")

    def result(self) -> str:
        return "".join(self.parts).strip()


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)

    def text(self) -> str:
        return re.sub(r"\s+", " ", " ".join(self.parts)).strip()


def sanitize_html(source: str) -> str:
    parser = SafeHTML()
    parser.feed(source or "")
    parser.close()
    return parser.result()


def html_text(source: str) -> str:
    parser = TextExtractor()
    parser.feed(source or "")
    parser.close()
    return parser.text()


def api_get(path: str, params: dict[str, str]) -> dict:
    url = f"{API_ROOT}/{path.lstrip('/')}?{urlencode(params)}"
    request = Request(url, headers={"Accept": "application/json",
                                    "User-Agent": "CyberSilicon-Blogger-Sync/1.0"})
    try:
        with urlopen(request, timeout=25) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        # Never print the request URL: it contains the API key.
        body = exc.read(2048).decode("utf-8", errors="replace")
        try:
            message = json.loads(body).get("error", {}).get("message", "Blogger API error")
        except json.JSONDecodeError:
            message = "Blogger API request failed"
        raise SyncError(f"Blogger API returned HTTP {exc.code}: {message}") from None
    except (URLError, TimeoutError) as exc:
        raise SyncError(f"Could not reach Blogger API: {exc.reason if isinstance(exc, URLError) else exc}") from None
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise SyncError("Blogger API returned an invalid JSON response") from None
    if not isinstance(payload, dict):
        raise SyncError("Unexpected Blogger API response")
    return payload


def resolve_blog_id(api_key: str, blog_url: str, explicit_id: str | None) -> str:
    if explicit_id:
        return explicit_id
    payload = api_get("blogs/byurl", {"url": blog_url, "key": api_key})
    blog_id = payload.get("id")
    if not blog_id:
        raise SyncError("Blogger did not return a blog ID for the configured URL")
    return str(blog_id)


def fetch_live_posts(api_key: str, blog_id: str, limit: int | None = None) -> list[dict]:
    posts: list[dict] = []
    page_token = None
    seen_tokens: set[str] = set()
    while True:
        params = {
            "key": api_key,
            "status": "live",
            "fetchBodies": "true",
            "fetchImages": "true",
            "maxResults": "100",
        }
        if page_token:
            params["pageToken"] = page_token
        payload = api_get(f"blogs/{blog_id}/posts", params)
        items = payload.get("items", [])
        if not isinstance(items, list):
            raise SyncError("Blogger returned an invalid posts list")
        posts.extend(item for item in items if isinstance(item, dict))
        if limit is not None and len(posts) >= limit:
            return posts[:limit]
        next_token = payload.get("nextPageToken")
        if not next_token:
            break
        if next_token in seen_tokens:
            raise SyncError("Blogger returned a repeated pagination token")
        seen_tokens.add(next_token)
        page_token = str(next_token)
    return posts


def normalise_date(value: str) -> tuple[str, str]:
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        raise SyncError(f"Post has an invalid published date: {value!r}") from None
    date_only = parsed.date().isoformat()
    iso = parsed.isoformat(timespec="seconds")
    return date_only, iso


def safe_permalink(post_url: str | None) -> str | None:
    if not post_url:
        return None
    parsed = urlparse(post_url)
    if parsed.scheme != "https" or not parsed.netloc:
        return None
    path = parsed.path
    if PERMALINK_RE.fullmatch(path) and ".." not in path:
        return path
    return None


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_post(post: dict) -> tuple[str, str]:
    post_id = str(post.get("id", "")).strip()
    title = html_text(str(post.get("title", "")))
    content = str(post.get("content", "") or "")
    published = str(post.get("published", "") or "")
    if not post_id.isdigit():
        raise SyncError("A Blogger post is missing a numeric ID")
    if not title:
        title = f"Imported Blogger post {post_id}"
    if not published:
        raise SyncError(f"Blogger post {post_id} has no published date")
    date_only, iso_date = normalise_date(published)
    labels = post.get("labels", [])
    labels = [html_text(str(label)) for label in labels if str(label).strip()] if isinstance(labels, list) else []
    labels = list(dict.fromkeys(label for label in labels if label))
    categories = labels[:1] or ["Blogger"]
    safe_body = sanitize_html(content)
    description = html_text(safe_body)[:180]
    if len(html_text(safe_body)) > 180:
        description = description.rstrip() + "…"
    original_url = str(post.get("url", "")).strip()
    permalink = safe_permalink(original_url)

    lines = [
        "---",
        f"title: {yaml_string(title)}",
        f"date: {iso_date}",
        "categories: [" + ", ".join(yaml_string(x) for x in categories) + "]",
        "tags: [" + ", ".join(yaml_string(x) for x in labels) + "]",
        f"blogger_id: {yaml_string(post_id)}",
        f"blogger_url: {yaml_string(original_url)}",
        "comments: true",
    ]
    if description:
        lines.append(f"description: {yaml_string(description)}")
    if permalink:
        lines.append(f"permalink: {yaml_string(permalink)}")
    lines.extend(["---", "", f"<!-- Imported from Blogger; source post ID: {post_id} -->", safe_body, ""])
    filename = f"{date_only}-blogger-{post_id}.html"
    return filename, "\n".join(lines)


def existing_permalink_map(output_dir: Path) -> dict[str, Path]:
    result: dict[str, Path] = {}
    if not output_dir.exists():
        return result
    pattern = re.compile(r'^permalink:\s*["\']?([^"\']+)["\']?', re.MULTILINE)
    for path in output_dir.glob("*"):
        if path.suffix.lower() not in {".md", ".markdown", ".html"} or not path.is_file():
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        match = pattern.search(text[:12000])
        if match:
            result[match.group(1).strip()] = path
    return result


def apply_posts(posts: list[dict], output_dir: Path, apply: bool) -> dict[str, list[str]]:
    summary = {"create": [], "update": [], "unchanged": [], "conflict": [], "invalid": []}
    permalink_map = existing_permalink_map(output_dir)
    planned: dict[str, str] = {}
    for post in posts:
        try:
            filename, content = render_post(post)
        except SyncError as exc:
            summary["invalid"].append(str(exc))
            continue
        target = output_dir / filename
        post_id = str(post.get("id"))
        existing = target.read_text(encoding="utf-8") if target.exists() else None
        if existing is not None:
            marker = BLOGGER_MARKER_RE.search(existing[:4000])
            if not marker or marker.group(1) != post_id:
                summary["conflict"].append(f"{filename}: refusing to overwrite a non-imported file")
                continue
            if existing == content:
                summary["unchanged"].append(filename)
                continue
            action = "update"
        else:
            action = "create"

        perm_match = re.search(r'^permalink:\s*["\']?([^"\']+)["\']?', content, re.MULTILINE)
        if perm_match:
            path = perm_match.group(1).strip()
            owner = permalink_map.get(path)
            if owner and owner != target:
                summary["conflict"].append(f"{filename}: permalink {path} is already used by {owner.name}")
                continue
            if path in planned and planned[path] != filename:
                summary["conflict"].append(f"{filename}: permalink {path} collides with another Blogger post")
                continue
            planned[path] = filename

        summary[action].append(filename)
        if apply:
            output_dir.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            perm_match = re.search(r'^permalink:\s*["\']?([^"\']+)["\']?', content, re.MULTILINE)
            if perm_match:
                permalink_map[perm_match.group(1).strip()] = target
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Import public Blogger posts into Jekyll")
    parser.add_argument("--blog-url", default=os.getenv("BLOGGER_URL", DEFAULT_BLOG_URL))
    parser.add_argument("--output-dir", type=Path, default=Path("_posts"))
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--apply", action="store_true", help="write changes (default is dry-run)")
    args = parser.parse_args(argv)

    api_key = os.getenv("BLOGGER_API_KEY", "").strip()
    blog_id = os.getenv("BLOGGER_BLOG_ID", "").strip() or None
    if not api_key:
        print("Set BLOGGER_API_KEY in the environment; do not put it in source files.", file=sys.stderr)
        return 2
    if args.limit is not None and args.limit < 1:
        parser.error("--limit must be greater than zero")

    try:
        resolved_id = resolve_blog_id(api_key, args.blog_url, blog_id)
        posts = fetch_live_posts(api_key, resolved_id, args.limit)
        summary = apply_posts(posts, args.output_dir, args.apply)
    except SyncError as exc:
        print(f"Sync stopped safely: {exc}", file=sys.stderr)
        return 1

    mode = "APPLY" if args.apply else "DRY RUN"
    print(f"{mode}: Blogger blog ID {resolved_id}; {len(posts)} live posts inspected")
    for action in ("create", "update", "unchanged", "conflict", "invalid"):
        print(f"{action}: {len(summary[action])}")
        for item in summary[action][:10]:
            print(f"  - {item}")
        if len(summary[action]) > 10:
            print(f"  ... and {len(summary[action]) - 10} more")
    if summary["conflict"] or summary["invalid"]:
        return 3
    if not args.apply:
        print("No files were changed. Review the plan, then rerun with --apply.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
