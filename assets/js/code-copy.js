/* FIX V3.1 - إصلاح نهائي جذري */
(function() {
  function cleanCodeBlocks() {
    document.querySelectorAll('.post-content .highlight .highlight').forEach(function(nested) {
      const parent = nested.closest('.post-content .highlight');
      if (parent && parent !== nested) {
        const pres = nested.querySelectorAll('pre');
        pres.forEach(pre => {
          if (!parent.querySelector('pre')) parent.appendChild(pre.cloneNode(true));
        });
        nested.remove();
      }
    });

    document.querySelectorAll('.post-content .highlight').forEach(function(block) {
      const headers = block.querySelectorAll(':scope > .code-header, :scope > .highlight-header, :scope > .p-code-head');
      if (headers.length > 1) {
        for (let i = 1; i < headers.length; i++) headers[i].remove();
      }
      const allHeaders = block.querySelectorAll('.code-header, .highlight-header');
      if (allHeaders.length > 1) {
        for (let i = 1; i < allHeaders.length; i++) allHeaders[i].remove();
      }
    });

    document.querySelectorAll('.post-content .highlight').forEach(function(block) {
      if (block.querySelector('.code-header, .highlight-header, .p-code-head')) return;
      let lang = 'bash';
      const pre = block.querySelector('pre');
      if (pre) {
        const cls = (pre.className + ' ' + block.className).toLowerCase();
        if (cls.includes('python')) lang = 'python';
        else if (cls.includes('js')) lang = 'javascript';
      }
      const header = document.createElement('div');
      header.className = 'code-header';
      header.innerHTML = `<span class="code-lang">${lang}</span><button class="copy-btn" onclick="copyCodeFinal(this)"><span>📋</span> نسخ</button>`;
      block.insertBefore(header, block.firstChild);
    });
  }

  document.addEventListener('DOMContentLoaded', cleanCodeBlocks);
  window.addEventListener('load', () => {
    cleanCodeBlocks();
    setTimeout(cleanCodeBlocks, 300);
    setTimeout(cleanCodeBlocks, 1000);
    setTimeout(cleanCodeBlocks, 2500);
  });

  const observer = new MutationObserver(cleanCodeBlocks);
  document.addEventListener('DOMContentLoaded', () => {
    const content = document.querySelector('.post-content');
    if (content) observer.observe(content, { childList: true, subtree: true });
  });
})();

function copyCodeFinal(btn) {
  const block = btn.closest('.highlight');
  const code = block.querySelector('pre code') || block.querySelector('pre');
  const text = code.innerText;
  navigator.clipboard.writeText(text).then(() => {
    const orig = btn.innerHTML;
    btn.innerHTML = '<span>✅</span> تم النسخ';
    btn.classList.add('copied');
    setTimeout(() => { btn.innerHTML = orig; btn.classList.remove('copied'); }, 2000);
  });
}
