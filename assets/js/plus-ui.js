/* Plus UI Pro - JavaScript - Professional Features */

(function() {
  'use strict';

  // === Theme & Color Management Like Plus UI ===
  const STORAGE_KEY = 'plus-ui-pro-settings';
  
  function getSettings() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {
        theme: 'auto',
        primaryColor: '#2962ff',
        layout: 'grid',
        fontSize: 100
      };
    } catch {
      return { theme: 'auto', primaryColor: '#2962ff', layout: 'grid', fontSize: 100 };
    }
  }
  
  function saveSettings(settings) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(settings));
  }

  // Initialize theme
  function initTheme() {
    const settings = getSettings();
    
    // Primary color
    setPrimaryColor(settings.primaryColor, false);
    
    // Theme mode
    setThemeMode(settings.theme, false);
    
    // Layout
    setLayout(settings.layout, false);
    
    // Font size
    document.documentElement.style.fontSize = settings.fontSize + '%';
    const fontValue = document.getElementById('fontSizeValue');
    if (fontValue) fontValue.textContent = settings.fontSize + '%';
  }

  // === Color Switcher ===
  window.setPrimaryColor = function(color, save = true) {
    document.documentElement.style.setProperty('--primary', color);
    // Calculate RGB for rgba usage
    const r = parseInt(color.slice(1,3), 16);
    const g = parseInt(color.slice(3,5), 16);
    const b = parseInt(color.slice(5,7), 16);
    document.documentElement.style.setProperty('--primary-rgb', `${r}, ${g}, ${b}`);
    
    // Update meta theme-color
    const metaTheme = document.querySelector('meta[name="theme-color"]');
    if (metaTheme) metaTheme.setAttribute('content', color);
    
    // Update active state
    document.querySelectorAll('.color-preset').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.color === color);
    });
    
    // Update picker
    const picker = document.getElementById('customColorPicker');
    if (picker) picker.value = color;
    
    if (save) {
      const s = getSettings();
      s.primaryColor = color;
      saveSettings(s);
    }
  };

  window.setThemeMode = function(mode, save = true) {
    let effective = mode;
    if (mode === 'auto') {
      effective = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    document.documentElement.setAttribute('data-theme', effective);
    document.documentElement.setAttribute('data-theme-mode', mode);
    
    document.querySelectorAll('.theme-option').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.theme === mode);
    });
    
    // Update Giscus theme if exists
    const giscusFrame = document.querySelector('iframe.giscus-frame');
    if (giscusFrame) {
      giscusFrame.contentWindow.postMessage({
        giscus: { setConfig: { theme: effective === 'dark' ? 'dark' : 'light' } }
      }, 'https://giscus.app');
    }
    
    if (save) {
      const s = getSettings();
      s.theme = mode;
      saveSettings(s);
    }
  };

  window.toggleTheme = function() {
    const current = document.documentElement.getAttribute('data-theme');
    const newMode = current === 'dark' ? 'light' : 'dark';
    setThemeMode(newMode);
  };

  window.setLayout = function(layout, save = true) {
    const grid = document.getElementById('postsGrid');
    if (grid) {
      grid.className = grid.className.replace(/\b(list|grid)\b/g, '').trim() + ' ' + layout;
      // Ensure posts-grid class remains
      if (!grid.classList.contains('posts-grid')) grid.classList.add('posts-grid');
    }
    document.querySelectorAll('.layout-option').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.layout === layout);
    });
    if (save) {
      const s = getSettings();
      s.layout = layout;
      saveSettings(s);
    }
  };

  window.changeFontSize = function(delta) {
    const s = getSettings();
    let newSize = s.fontSize + (delta * 10);
    newSize = Math.max(80, Math.min(140, newSize));
    document.documentElement.style.fontSize = newSize + '%';
    const el = document.getElementById('fontSizeValue');
    if (el) el.textContent = newSize + '%';
    s.fontSize = newSize;
    saveSettings(s);
  };

  window.resetTheme = function() {
    localStorage.removeItem(STORAGE_KEY);
    setPrimaryColor('#2962ff', false);
    setThemeMode('auto', false);
    setLayout('grid', false);
    document.documentElement.style.fontSize = '100%';
    alert('✅ تم إعادة تعيين المظهر إلى الافتراضي');
    location.reload();
  };

  // === Color Switcher Panel ===
  window.openColorSwitcher = function() {
    document.getElementById('colorSwitcher')?.classList.add('active');
    document.getElementById('switcherOverlay')?.classList.add('active');
    document.body.style.overflow = 'hidden';
  };
  window.closeColorSwitcher = function() {
    document.getElementById('colorSwitcher')?.classList.remove('active');
    document.getElementById('switcherOverlay')?.classList.remove('active');
    document.body.style.overflow = '';
  };

  // === Search Modal ===
  window.openSearch = function() {
    document.getElementById('searchModal')?.classList.add('active');
    document.getElementById('searchOverlay')?.classList.add('active');
    document.body.style.overflow = 'hidden';
    setTimeout(() => document.getElementById('searchInput')?.focus(), 100);
  };
  window.closeSearch = function() {
    document.getElementById('searchModal')?.classList.remove('active');
    document.getElementById('searchOverlay')?.classList.remove('active');
    document.body.style.overflow = '';
  };

  // === Mobile Menu ===
  window.toggleMobileMenu = function() {
    document.getElementById('mobileMenu')?.classList.toggle('active');
  };

  // === Post Actions ===
  window.sharePost = function() {
    if (navigator.share) {
      navigator.share({ title: document.title, url: location.href });
    } else {
      navigator.clipboard.writeText(location.href).then(() => alert('✅ تم نسخ رابط المقال'));
    }
  };
  window.toggleBookmark = function() {
    // Simple bookmark via localStorage
    const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
    const url = location.href;
    const idx = bookmarks.indexOf(url);
    if (idx > -1) {
      bookmarks.splice(idx, 1);
      alert('❌ تم إزالة المقال من المحفوظات');
    } else {
      bookmarks.push(url);
      alert('🔖 تم حفظ المقال');
    }
    localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
  };
  window.increaseFont = function() { changeFontSize(1); };

  window.subscribeNewsletter = function(e) {
    e.preventDefault();
    const email = e.target.querySelector('input[type="email"]').value;
    // For GitHub Pages, we can use Formspree or similar
    alert(`✅ شكراً! تم تسجيل ${email} في النشرة البريدية (تحتاج ربط Formspree أو Mailchimp)`);
    e.target.reset();
  };

  // === Progress Bar Like Plus UI ===
  function initProgressBar() {
    const bar = document.getElementById('progress-bar');
    if (!bar) return;
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      bar.style.width = scrolled + '%';
    });
  }

  // === TOC Toggle ===
  function initTOC() {
    document.querySelectorAll('.toc-toggle').forEach(btn => {
      btn.addEventListener('click', () => {
        const content = btn.closest('.toc-container')?.querySelector('.toc-content');
        if (content) {
          content.style.display = content.style.display === 'none' ? 'block' : 'none';
          btn.textContent = content.style.display === 'none' ? '+' : '−';
        }
      });
    });
  }

  // === Keyboard Shortcuts ===
  function initShortcuts() {
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        openSearch();
      }
      if (e.key === 'Escape') {
        closeSearch();
        closeColorSwitcher();
        document.getElementById('mobileMenu')?.classList.remove('active');
      }
    });
  }

  // === Init ===
  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initProgressBar();
    initTOC();
    initShortcuts();
    
    // Auto theme listener
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
      const s = getSettings();
      if (s.theme === 'auto') setThemeMode('auto', false);
    });
    
    // View toggle
    document.querySelectorAll('.toggle-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        setLayout(btn.dataset.view);
      });
    });
  });

})();
