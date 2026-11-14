import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "sync_blogger_posts.py"
SPEC = importlib.util.spec_from_file_location("sync_blogger_posts", SCRIPT)
SYNC = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(SYNC)


class BloggerSyncTests(unittest.TestCase):
    def test_sanitizer_removes_script_and_event_handlers(self):
        source = '<p onclick="alert(1)">safe <a href="javascript:alert(1)">link</a></p><script>alert(2)</script>'
        result = SYNC.sanitize_html(source)
        self.assertIn("<p>", result)
        self.assertIn("safe", result)
        self.assertNotIn("onclick", result)
        self.assertNotIn("javascript:", result)
        self.assertNotIn("alert(2)", result)

    def test_self_closing_blocked_tag_does_not_hide_following_content(self):
        source = '<p>before</p><input /><p>after</p>'
        result = SYNC.sanitize_html(source)
        self.assertIn("before", result)
        self.assertIn("after", result)

    def test_sanitizer_keeps_safe_video_embed(self):
        source = '<iframe src="https://www.youtube-nocookie.com/embed/abc" title="Video"></iframe>'
        self.assertIn("youtube-nocookie.com/embed/abc", SYNC.sanitize_html(source))

    def test_sanitizer_removes_untrusted_iframe(self):
        source = '<iframe src="https://attacker.example/embed/x"></iframe>'
        self.assertEqual("", SYNC.sanitize_html(source))

    def test_preserves_blogger_post_permalink(self):
        url = "https://cyber-silicon.blogspot.com/2026/10/kali-linux-6_02001830419.html"
        self.assertEqual("/2026/10/kali-linux-6_02001830419.html", SYNC.safe_permalink(url))

    def test_rejects_unsafe_permalink(self):
        self.assertIsNone(SYNC.safe_permalink("javascript:alert(1)"))
        self.assertIsNone(SYNC.safe_permalink("https://example.com/../2026/10/test.html"))

    def test_render_uses_stable_id_and_safe_metadata(self):
        post = {
            "id": "123456789",
            "title": "مقال تجريبي",
            "published": "2026-11-14T10:15:00+02:00",
            "url": "https://cyber-silicon.blogspot.com/2026/11/sample_123.html",
            "labels": ["Kali Linux", "أمن سيبراني"],
            "content": "<h2>عنوان</h2><p>محتوى المقال</p><script>bad()</script>",
        }
        filename, content = SYNC.render_post(post)
        self.assertEqual("2026-11-14-blogger-123456789.html", filename)
        self.assertIn('blogger_id: "123456789"', content)
        self.assertIn('permalink: "/2026/11/sample_123.html"', content)
        self.assertIn('comments: true', content)
        self.assertNotIn("bad()", content)

    def test_dry_run_does_not_write(self):
        post = {
            "id": "987654321",
            "title": "Dry run",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/dry-run.html",
            "labels": [],
            "content": "<p>Test</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            summary = SYNC.apply_posts([post], root, apply=False)
            self.assertEqual(1, len(summary["create"]))
            self.assertFalse(list(root.glob("*")))

    def test_apply_is_idempotent(self):
        post = {
            "id": "555555555",
            "title": "Idempotent",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/idempotent.html",
            "labels": ["Python"],
            "content": "<p>Test</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            first = SYNC.apply_posts([post], root, apply=True)
            second = SYNC.apply_posts([post], root, apply=True)
            self.assertEqual(1, len(first["create"]))
            self.assertEqual(1, len(second["unchanged"]))
            self.assertEqual(1, len(list(root.glob("*.html"))))

    def test_never_overwrites_unmanaged_post(self):
        post = {
            "id": "111222333",
            "title": "Conflict",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/conflict.html",
            "labels": [],
            "content": "<p>Test</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            filename, _ = SYNC.render_post(post)
            target = root / filename
            target.write_text("---\ntitle: Manually authored\n---\n", encoding="utf-8")
            summary = SYNC.apply_posts([post], root, apply=True)
            self.assertEqual(1, len(summary["conflict"]))
            self.assertIn("Manually authored", target.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
