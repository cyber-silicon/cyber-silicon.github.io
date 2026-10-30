
/* Cyber Silicon - Main JS - Clean & Functional */
(function() {
  'use strict';

  const STORAGE_KEY = 'cyber-silicon-theme';

  function getTheme() {
    try { return localStorage.getItem(STORAGE_KEY) || 'light'; }
    catch { return 'light'; }
  }
  function setTheme(theme) {
    try { localStorage.setItem(STORAGE_KEY, theme); } catch {}
    document.documentElement.setAttribute('data-theme', theme);
    document.documentElement.setAttribute('data-theme-mode', theme);
  }

  function initTheme() {
    const saved = getTheme();
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    const effective = saved === 'auto' ? (prefersDark ? 'dark' : 'light') : saved;
    setTheme(effective === 'dark' ? 'dark' : 'light');
  }

  window.toggleTheme = function() {
    const current = document.documentElement.getAttribute('data-theme') || 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    setTheme(next);
  };

  // Mobile menu
  window.toggleMobileMenu = function() {
    const menu = document.getElementById('mobileMenu');
    const overlay = document.getElementById('mobileOverlay');
    if (!menu) return;
    const isActive = menu.classList.contains('active');
    menu.classList.toggle('active', !isActive);
    if (overlay) overlay.classList.toggle('active', !isActive);
    document.body.style.overflow = !isActive ? 'hidden' : '';
  };

  // Search modal
  window.openSearch = function() {
    const modal = document.getElementById('searchModal');
    const overlay = document.getElementById('searchOverlay');
    if (!modal) return;
    modal.classList.add('active');
    if (overlay) overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
    setTimeout(() => document.getElementById('searchInput')?.focus(), 100);
  };
  window.closeSearch = function() {
    document.getElementById('searchModal')?.classList.remove('active');
    document.getElementById('searchOverlay')?.classList.remove('active');
    document.body.style.overflow = '';
  };

  // Share & bookmark
  window.sharePost = function() {
    if (navigator.share) {
      navigator.share({ title: document.title, url: location.href }).catch(()=>{});
    } else {
      navigator.clipboard.writeText(location.href).then(() => {
        showToast('✅ تم نسخ رابط المقال');
      });
    }
  };
  window.toggleBookmark = function() {
    try {
      const bookmarks = JSON.parse(localStorage.getItem('bookmarks') || '[]');
      const url = location.href;
      const idx = bookmarks.indexOf(url);
      if (idx > -1) { bookmarks.splice(idx,1); showToast('❌ تم إزالة المقال من المحفوظات'); }
      else { bookmarks.push(url); showToast('🔖 تم حفظ المقال'); }
      localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
    } catch { showToast('🔖 تم حفظ المقال'); }
  };
  window.subscribeNewsletter = function(e) {
    e.preventDefault();
    const email = e.target.querySelector('input[type="email"]')?.value || '';
    showToast(`✅ شكراً! تم تسجيل ${email} - سيتم تفعيل النشرة قريباً`);
    e.target.reset();
  };

  function showToast(msg) {
    let t = document.getElementById('toast');
    if (!t) {
      t = document.createElement('div');
      t.id = 'toast';
      t.style.cssText = 'position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#1e2128;color:white;padding:12px 20px;border-radius:10px;box-shadow:0 8px 24px rgba(0,0,0,0.3);z-index:9999;font-size:13px;font-weight:600;transition:all 0.3s;opacity:0;pointer-events:none;';
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.style.opacity = '1';
    t.style.transform = 'translateX(-50%) translateY(0)';
    setTimeout(()=>{ t.style.opacity='0'; t.style.transform='translateX(-50%) translateY(10px)'; }, 3000);
  }

  // Progress bar
  function initProgressBar() {
    const bar = document.getElementById('progress-bar');
    if (!bar) return;
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      bar.style.width = scrolled + '%';
    }, { passive: true });
  }

  // Beautiful code blocks with copy button
  function initCodeBlocks() {
    const blocks = document.querySelectorAll('.post-content .highlight, .post-content div.highlighter-rouge, .post-content figure.highlight');
    blocks.forEach((block) => {
      if (block.querySelector('.code-block-header')) return; // already processed
      
      // Find pre and code
      const pre = block.querySelector('pre');
      if (!pre) return;
      const code = pre.querySelector('code') || pre;
      
      // Detect language
      let lang = 'code';
      const classList = (block.className + ' ' + pre.className + ' ' + code.className).toLowerCase();
      if (classList.includes('bash') || classList.includes('shell') || classList.includes('sh')) lang = 'bash';
      else if (classList.includes('python') || classList.includes('py')) lang = 'python';
      else if (classList.includes('javascript') || classList.includes('js')) lang = 'javascript';
      else if (classList.includes('html')) lang = 'html';
      else if (classList.includes('css')) lang = 'css';
      else if (classList.includes('json')) lang = 'json';
      else if (classList.includes('yaml') || classList.includes('yml')) lang = 'yaml';
      else if (classList.includes('ruby')) lang = 'ruby';
      else if (classList.includes('go')) lang = 'go';
      else if (classList.includes('sql')) lang = 'sql';
      else if (classList.includes('docker')) lang = 'dockerfile';
      // Try data-lang
      const dataLang = block.getAttribute('data-lang') || pre.getAttribute('data-lang');
      if (dataLang) lang = dataLang.toLowerCase();

      // Create header
      const header = document.createElement('div');
      header.className = 'code-block-header';
      header.innerHTML = `
        <span class="code-lang ${lang}">${lang}</span>
        <button class="copy-btn" aria-label="نسخ الكود">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v3"/></svg>
          <span>نسخ</span>
        </button>
      `;

      const btn = header.querySelector('.copy-btn');
      btn.addEventListener('click', async () => {
        const text = code.innerText || code.textContent;
        try {
          await navigator.clipboard.writeText(text);
          const span = btn.querySelector('span');
          const original = span.textContent;
          btn.classList.add('copied');
          span.textContent = 'تم النسخ ✓';
          setTimeout(() => {
            btn.classList.remove('copied');
            span.textContent = original;
          }, 2000);
        } catch {
          // Fallback
          const range = document.createRange();
          range.selectNodeContents(code);
          const sel = window.getSelection();
          sel.removeAllRanges();
          sel.addRange(range);
          document.execCommand('copy');
          sel.removeAllRanges();
          const span = btn.querySelector('span');
          span.textContent = 'تم النسخ ✓';
          btn.classList.add('copied');
          setTimeout(()=>{ btn.classList.remove('copied'); span.textContent='نسخ'; }, 2000);
        }
      });

      block.insertBefore(header, block.firstChild);
    });
  }

  // Keyboard shortcuts
  function initShortcuts() {
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        openSearch();
      }
      if (e.key === 'Escape') {
        closeSearch();
        const menu = document.getElementById('mobileMenu');
        if (menu?.classList.contains('active')) toggleMobileMenu();
      }
    });
  }

  // View toggle grid/list
  function initViewToggle() {
    document.querySelectorAll('.toggle-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.toggle-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const grid = document.getElementById('postsGrid');
        if (!grid) return;
        const view = btn.dataset.view;
        grid.classList.remove('grid','list');
        grid.classList.add(view);
        try { localStorage.setItem('cyber-view', view); } catch {}
      });
    });
    try {
      const saved = localStorage.getItem('cyber-view');
      if (saved) {
        const btn = document.querySelector(`.toggle-btn[data-view="${saved}"]`);
        if (btn) btn.click();
      }
    } catch {}
  }

  document.addEventListener('DOMContentLoaded', () => {
    initTheme();
    initProgressBar();
    initCodeBlocks();
    initShortcuts();
    initViewToggle();
  });

})();
