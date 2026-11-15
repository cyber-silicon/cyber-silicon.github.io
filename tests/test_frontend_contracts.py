from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FrontendContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.js = (ROOT / "assets/js/main.js").read_text(encoding="utf-8")
        cls.css = (ROOT / "assets/css/cyber-silicon.css").read_text(encoding="utf-8")
        cls.header = (ROOT / "_includes/header.html").read_text(encoding="utf-8")
        cls.post = (ROOT / "_layouts/post.html").read_text(encoding="utf-8")
        cls.layout = (ROOT / "_layouts/default.html").read_text(encoding="utf-8")
        cls.bookmarks = (ROOT / "_pages/bookmarks.html").read_text(encoding="utf-8")
        cls.head = (ROOT / "_includes/head.html").read_text(encoding="utf-8")
        cls.home = (ROOT / "_layouts/home.html").read_text(encoding="utf-8")
        cls.search = (ROOT / "_includes/search-modal.html").read_text(encoding="utf-8")
        cls.workflow = (ROOT / ".github/workflows/jekyll-ci.yml").read_text(encoding="utf-8")

    def test_theme_rejects_invalid_saved_values_and_tracks_system_preference(self):
        self.assertIn("value==='light'||value==='dark'", self.js)
        self.assertIn("window.matchMedia?.('(prefers-color-scheme: light)')", self.js)
        self.assertIn("if(followsSystem)applyTheme(event.matches?'light':'dark')", self.js)
        self.assertIn("event.key!=='cs-theme'&&event.key!==null", self.js)
        self.assertIn("syncGiscusTheme()", self.js)
        self.assertIn("const validTheme=t==='light'||t==='dark'", self.head)
        self.assertIn("validTheme?t:", self.head)

    def test_bookmark_storage_is_validated_and_shared_between_tabs(self):
        self.assertIn("Array.isArray(stored)", self.js)
        self.assertIn("typeof value==='string'", self.js)
        self.assertIn("event.key!==bookmarkKey&&event.key!==null", self.js)
        self.assertIn("renderBookmarks()", self.js)

    def test_search_dialog_has_consistent_accessible_references(self):
        for source in (self.header, self.home):
            self.assertIn('aria-controls="searchDialog"', source)
            self.assertIn('aria-haspopup="dialog"', source)
        self.assertIn('id="searchDialog"', self.search)
        self.assertIn('role="dialog"', self.search)
        self.assertIn('aria-modal="true"', self.search)
        self.assertIn('aria-controls="searchResults"', self.search)
        self.assertIn('id="searchResults"', self.search)
        self.assertIn('aria-expanded="false"', self.header)

    def test_keyboard_focus_and_reduced_motion_contracts_are_present(self):
        self.assertIn(":focus-visible", self.css)
        self.assertIn("@media(prefers-reduced-motion:reduce)", self.css)
        self.assertIn("prefers-reduced-motion: reduce", self.js)
        self.assertIn("behavior});", self.js)
        self.assertIn("dialog.contains(document.activeElement)", self.js)

    def test_mobile_navigation_state_is_synchronized_and_dismissible(self):
        self.assertIn("paintMenuState(open)", self.js)
        self.assertIn("b.setAttribute('aria-label',open?'إغلاق القائمة':'فتح القائمة')", self.js)
        self.assertIn("nav.contains(event.target)", self.js)
        self.assertIn("closeMenuOnDesktop", self.js)

    def test_theme_toggle_keeps_a_stable_accessible_name(self):
        self.assertIn("b.setAttribute('aria-label','تبديل المظهر')", self.js)
        self.assertIn("b.setAttribute('aria-pressed',String(light))", self.js)

    def test_arabic_search_normalizes_diacritics_and_common_alif_forms(self):
        self.assertIn(".normalize('NFKC').toLowerCase()", self.js)
        self.assertIn(r".replace(/[\u064B-\u065F\u0670\u0640]/g,'')", self.js)
        self.assertIn("replace(/[أإآٱ]/g,'ا')", self.js)
        self.assertIn("replace(/ى/g,'ي')", self.js)
        self.assertIn("const term=normalizeSearchText(input.value)", self.js)

    def test_bookmark_buttons_expose_state_and_handle_storage_failure(self):
        self.assertIn("b.setAttribute('aria-pressed',String(on))", self.js)
        self.assertIn("تعذر حفظ المقال في هذا المتصفح", self.js)
        self.assertIn("if(!saveBookmarks(next))", self.js)

    def test_reading_progress_tracks_dynamic_content_height(self):
        self.assertIn("new ResizeObserver(paintProgress)", self.js)
        self.assertIn("articleResizeObserver.observe(article)", self.js)

    def test_current_navigation_and_toc_location_are_accessible(self):
        self.assertIn('class="active" aria-current="page"', self.header)
        self.assertIn("active?.setAttribute('aria-current','location')", self.js)
        self.assertIn("a.removeAttribute('aria-current')", self.js)
        self.assertIn("scroll-margin-top:88px", self.css)

    def test_bookmark_removal_buttons_include_the_article_title(self):
        self.assertIn('type="button" data-remove-bookmark=', self.bookmarks)
        self.assertIn('aria-label="إزالة {{ post.title | escape }} من المحفوظات"', self.bookmarks)

    def test_ci_checks_frontend_javascript_syntax(self):
        self.assertIn("node --check assets/js/main.js", self.workflow)


    def test_copy_and_share_feedback_is_announced_accessibly(self):
        self.assertIn("const announceAction=(element,message)=>", self.js)
        self.assertIn("status.setAttribute('role','status')", self.js)
        self.assertIn("status.setAttribute('aria-live','polite')", self.js)
        self.assertIn("announceAction(b,ok?'تم نسخ رابط الصفحة.':'تعذر نسخ رابط الصفحة.')", self.js)
        self.assertIn("announceAction(btn,ok?'تم نسخ الشيفرة.':'تعذر نسخ الشيفرة.')", self.js)
        self.assertIn("finally{area?.remove()}", self.js)
        self.assertIn(".visually-hidden{", self.css)

    def test_skip_link_target_can_receive_keyboard_focus(self):
        self.assertIn('href="#content"', self.layout)
        self.assertIn('<main id="content" tabindex="-1">', self.layout)

    def test_bookmark_removal_preserves_focus_and_announces_storage_errors(self):
        self.assertIn("const removeButtons=qa('[data-remove-bookmark]')", self.js)
        self.assertIn("const nextFocus=removeButtons.slice(currentIndex+1).find(isVisible)", self.js)
        self.assertIn("(nextFocus||q('#bookmarksEmpty h2'))?.focus()", self.js)
        self.assertIn('<h2 tabindex="-1">لا توجد مقالات محفوظة بعد</h2>', self.bookmarks)
        self.assertIn("announceAction(b,'تعذر حفظ المقال في هذا المتصفح.')", self.js)
        self.assertIn("announceAction(b,'تعذرت إزالة المقال من المحفوظات.')", self.js)

    def test_cross_tab_bookmark_updates_preserve_focus_and_are_announced(self):
        self.assertIn('id="bookmarksSyncStatus"', self.bookmarks)
        self.assertIn('role="status" aria-live="polite" aria-atomic="true"', self.bookmarks)
        self.assertIn("const activeCard=document.activeElement?.closest?.('[data-bookmark-url]')", self.js)
        self.assertIn("const saved=readBookmarks()", self.js)
        self.assertIn("const nextCard=bookmarkCards.slice(activeCardIndex+1).find(card=>!card.hidden)", self.js)
        self.assertIn("(nextTarget||q('#bookmarksEmpty h2'))?.focus()", self.js)
        self.assertIn("تم تحديث المحفوظات من علامة تبويب أخرى.", self.js)
        self.assertIn("event.key!==bookmarkKey&&event.key!==null", self.js)

if __name__ == "__main__":
    unittest.main()
