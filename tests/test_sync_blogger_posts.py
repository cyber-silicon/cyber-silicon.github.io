import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

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

    def test_non_self_closing_void_input_does_not_hide_following_content(self):
        source = '<p>before</p><input type="text"><p>after</p>'
        result = SYNC.sanitize_html(source)
        self.assertIn("before", result)
        self.assertIn("after", result)

    def test_void_embed_does_not_hide_following_content(self):
        source = '<p>before</p><embed src="movie.swf"><p>after</p>'
        result = SYNC.sanitize_html(source)
        self.assertIn("before", result)
        self.assertIn("after", result)

    def test_void_tag_inside_blocked_script_does_not_break_skip_depth(self):
        source = '<script><input></script><p>after</p>'
        result = SYNC.sanitize_html(source)
        self.assertNotIn("<script", result)
        self.assertIn("after", result)

    def test_sanitizer_keeps_safe_video_embed(self):
        source = '<iframe src="https://www.youtube-nocookie.com/embed/abc" title="Video"></iframe>'
        self.assertIn("youtube-nocookie.com/embed/abc", SYNC.sanitize_html(source))

    def test_sanitizer_keeps_official_tiktok_player_embed(self):
        source = '<iframe src="https://www.tiktok.com/player/v1/7667112940985715989?autoplay=0" title="Video"></iframe>'
        result = SYNC.sanitize_html(source)
        self.assertIn("www.tiktok.com/player/v1/7667112940985715989", result)

    def test_sanitizer_rejects_non_player_tiktok_pages(self):
        source = '<iframe src="https://www.tiktok.com/@creator/video/7667112940985715989"></iframe>'
        self.assertEqual("", SYNC.sanitize_html(source))

    def test_sanitizer_removes_untrusted_iframe(self):
        source = '<iframe src="https://attacker.example/embed/x"></iframe>'
        self.assertEqual("", SYNC.sanitize_html(source))

    def test_rejected_iframe_does_not_hide_following_article_content(self):
        source = '<p>before</p><iframe src="https://attacker.example/embed/x"></iframe><p>after</p>'
        result = SYNC.sanitize_html(source)
        self.assertIn("before", result)
        self.assertIn("after", result)

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

    def test_render_removes_only_a_duplicate_leading_h1(self):
        post = {
            "id": "222333444",
            "title": "عنوان المقال",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/heading.html",
            "labels": ["Kali Linux"],
            "content": "<h1>عنوان المقال</h1><p>يبقى المحتوى</p>",
        }
        _, content = SYNC.render_post(post)
        self.assertNotIn("<h1>عنوان المقال</h1>", content)
        self.assertIn("<p>يبقى المحتوى</p>", content)

    def test_render_keeps_non_duplicate_leading_h1(self):
        post = {
            "id": "222333445",
            "title": "عنوان الصفحة",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/another-heading.html",
            "labels": [],
            "content": "<h1>عنوان فرعي مختلف</h1><p>المحتوى</p>",
        }
        _, content = SYNC.render_post(post)
        self.assertIn("<h1>عنوان فرعي مختلف</h1>", content)
        self.assertIn('categories: ["General"]', content)

    def test_unlabeled_kali_posts_get_kali_category(self):
        post = {
            "id": "222333446",
            "title": "دليل Kali Linux للمبتدئين",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/kali.html",
            "labels": [],
            "content": "<p>محتوى الدليل</p>",
        }
        _, content = SYNC.render_post(post)
        self.assertIn('categories: ["Kali Linux"]', content)

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

    def test_manual_canonical_blogger_post_is_not_duplicated(self):
        post = {
            "id": "666777888",
            "title": "Manually maintained Blogger article",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/manual-canonical.html",
            "labels": ["Kali Linux"],
            "content": "<p>Source copy</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            manual = root / "2026-11-14-manual-canonical.md"
            manual.write_text(
                '---\ntitle: "Hand maintained"\nblogger_id: "666777888"\nblogger_sync: manual\n---\n# Editorial copy\n',
                encoding="utf-8",
            )
            summary = SYNC.apply_posts([post], root, apply=True)
            self.assertEqual(0, len(summary["create"]))
            self.assertEqual(1, len(summary["unchanged"]))
            self.assertIn("manually maintained canonical", summary["unchanged"][0])
            self.assertEqual([manual], list(root.glob("*.md")))
            self.assertFalse(list(root.glob("*blogger-666777888.html")))

    def test_manual_canonical_alias_blogger_id_is_not_duplicated(self):
        post = {
            "id": "888999000",
            "title": "Republished lesson",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/republished-lesson.html",
            "labels": ["Kali Linux"],
            "content": "<p>Second source copy</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            manual = root / "2026-10-08-canonical.md"
            manual.write_text(
                '---\ntitle: "Canonical lesson"\nblogger_id: "123456789"\n'
                'blogger_alias_ids: ["888999000"]\nblogger_sync: manual\n---\n',
                encoding="utf-8",
            )
            summary = SYNC.apply_posts([post], root, apply=True)
            self.assertEqual(0, len(summary["create"]))
            self.assertEqual(1, len(summary["unchanged"]))
            self.assertIn("888999000", summary["unchanged"][0])
            self.assertFalse(list(root.glob("*blogger-888999000.html")))

    def test_duplicate_blogger_id_without_manual_lock_is_a_conflict(self):
        post = {
            "id": "777888999",
            "title": "Already represented",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/already-represented.html",
            "labels": [],
            "content": "<p>Source copy</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            existing = root / "different-name.md"
            existing.write_text(
                '---\ntitle: "Existing article"\nblogger_id: "777888999"\n---\n',
                encoding="utf-8",
            )
            summary = SYNC.apply_posts([post], root, apply=True)
            self.assertEqual(0, len(summary["create"]))
            self.assertEqual(1, len(summary["conflict"]))
            self.assertFalse(list(root.glob("*blogger-777888999.html")))

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

    def test_post_inventory_collects_live_draft_and_scheduled_states(self):
        def fake_api_get(path, params, access_token=None):
            state = params["status"]
            self.assertEqual("ADMIN", params["view"])
            self.assertEqual("admin-token", access_token)
            return {"items": [{"id": {"live": "101", "draft": "202", "scheduled": "303"}[state],
                               "status": state.upper()}]}

        with patch.object(SYNC, "api_get", side_effect=fake_api_get):
            inventory = SYNC.fetch_post_inventory("key", "blog", "admin-token")

        self.assertEqual({"101", "202", "303"}, set(inventory))
        self.assertEqual("LIVE", inventory["101"]["status"])
        self.assertEqual("DRAFT", inventory["202"]["status"])
        self.assertEqual("SCHEDULED", inventory["303"]["status"])

    def test_post_inventory_fails_closed_when_admin_status_is_missing(self):
        def fake_api_get(path, params, access_token=None):
            state = params["status"]
            if state == "live":
                return {"items": [{"id": "404"}]}
            return {"items": []}

        with patch.object(SYNC, "api_get", side_effect=fake_api_get):
            with self.assertRaises(SYNC.SyncError):
                SYNC.fetch_post_inventory("key", "blog", "admin-token")

    def test_deletion_candidates_include_only_managed_non_manual_files(self):
        post = {
            "id": "121212121",
            "title": "Managed",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/managed.html",
            "labels": [],
            "content": "<p>Imported body</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            filename, imported_content = SYNC.render_post(post)
            managed = root / filename
            managed.write_text(imported_content, encoding="utf-8")
            manual = root / "manual.md"
            manual.write_text(
                '---\ntitle: "Manual"\nblogger_id: "232323232"\nblogger_sync: manual\n---\n'
                '<!-- Imported from Blogger; source post ID: 232323232 -->',
                encoding="utf-8",
            )
            unmanaged = root / "unmanaged.md"
            unmanaged.write_text(
                '---\ntitle: "Unmanaged"\nblogger_id: "343434343"\n---\n',
                encoding="utf-8",
            )

            candidates = SYNC.find_imported_deletion_candidates(root, set())

            self.assertEqual([(managed, "121212121")], candidates)

    def test_confirmed_delete_removes_only_importer_managed_copy(self):
        post = {
            "id": "454545454",
            "title": "Managed copy",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/managed-copy.html",
            "labels": [],
            "content": "<p>Imported body</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            filename, content = SYNC.render_post(post)
            managed = root / filename
            managed.write_text(content, encoding="utf-8")
            manual = root / "manual-copy.md"
            manual.write_text(
                '---\ntitle: "Manual copy"\nblogger_id: "565656565"\n'
                'blogger_sync: manual\n---\n',
                encoding="utf-8",
            )

            dry_run = SYNC.apply_posts([], root, apply=False, confirmed_deleted_ids={"454545454"})
            self.assertEqual([filename], dry_run["delete"])
            self.assertTrue(managed.exists())

            applied = SYNC.apply_posts([], root, apply=True, confirmed_deleted_ids={"454545454"})
            self.assertEqual([filename], applied["delete"])
            self.assertFalse(managed.exists())
            self.assertTrue(manual.exists())

    def test_live_or_draft_or_scheduled_source_id_prevents_prune_candidate(self):
        post = {
            "id": "676767676",
            "title": "Keep while source still exists",
            "published": "2026-11-14T10:15:00Z",
            "url": "https://cyber-silicon.blogspot.com/2026/11/keep.html",
            "labels": [],
            "content": "<p>Imported body</p>",
        }
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            filename, content = SYNC.render_post(post)
            path = root / filename
            path.write_text(content, encoding="utf-8")

            candidates = SYNC.find_imported_deletion_candidates(root, {"676767676"})

            self.assertEqual([], candidates)

    def test_alias_still_present_prevents_pruning_managed_file(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / "canonical.md"
            path.write_text(
                '---\ntitle: "Canonical"\nblogger_id: "787878787"\n'
                'blogger_alias_ids: ["898989898"]\n---\n'
                '<!-- Imported from Blogger; source post ID: 787878787 -->',
                encoding="utf-8",
            )
            candidates = SYNC.find_imported_deletion_candidates(root, {"898989898"})
            self.assertEqual([], candidates)

    def test_verify_removed_ids_retains_drafts_and_confirms_missing_or_trashed(self):
        candidates = [(Path("draft.html"), "111"), (Path("missing.html"), "222"),
                      (Path("trashed.html"), "333")]
        def fake_status(api_key, blog_id, post_id, access_token):
            return {"111": "draft", "222": None, "333": "soft_trashed"}[post_id]

        with patch.object(SYNC, "get_blogger_post_status", side_effect=fake_status):
            removed, retained = SYNC.verify_removed_post_ids("key", "blog", "token", candidates)
        self.assertEqual({"222", "333"}, removed)
        self.assertEqual({"111"}, retained)


if __name__ == "__main__":
    unittest.main()
