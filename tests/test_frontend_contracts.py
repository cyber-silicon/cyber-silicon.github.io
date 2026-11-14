from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FrontendContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.js = (ROOT / "assets/js/main.js").read_text(encoding="utf-8")
        cls.css = (ROOT / "assets/css/cyber-silicon.css").read_text(encoding="utf-8")
        cls.header = (ROOT / "_includes/header.html").read_text(encoding="utf-8")
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
        self.assertIn("event.key!==bookmarkKey", self.js)
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
        self.assertIn(r".replace(/[\\u064B-\\u065F\\u0670\\u0640]/g,'')", self.js)
        self.assertIn("replace(/[أإآٱ]/g,'ا')", self.js)
        self.assertIn("replace(/ى/g,'ي')", self.js)
        self.assertIn("const term=normalizeSearchText(input.value)", self.js)

    def test_bookmark_buttons_expose_state_and_handle_storage_failure(self):
        self.assertIn("b.setAttribute('aria-pressed',String(on))", self.js)
        self.assertIn("تعذر حفظ المقال في هذا المتصفح", self.js)
        self.assertIn("if(!saveBookmarks(next))", self.js)
        self.assertIn("if(!saveBookmarks(next))", self.js)

    def test_reading_progress_tracks_dynamic_content_height(self):
        self.assertIn("new ResizeObserver(paintProgress)", self.js)
        self.assertIn("articleResizeObserver.observe(article)", self.js)

    def test_ci_checks_frontend_javascript_syntax(self):
        self.assertIn("node --check assets/js/main.js", self.workflow)


if __name__ == "__main__":
    unittest.main()
