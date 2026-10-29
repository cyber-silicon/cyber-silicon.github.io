/* FIX V3 - يمنع تكرار BASH وزر النسخ - متوافق مع Plus UI Pro */
document.addEventListener('DOMContentLoaded', function() {
  
  // 1. أولاً فك التداخل: highlight داخل highlight (هذا سبب المشكلة في صورتك)
  document.querySelectorAll('.post-content .highlight .highlight').forEach(function(nested) {
    const parent = nested.closest('.post-content .highlight');
    if (parent && parent !== nested) {
      const pre = nested.querySelector('pre');
      if (pre) {
        const oldPre = parent.querySelector(':scope > pre');
        if (oldPre && oldPre !== pre) oldPre.remove();
        parent.appendChild(pre);
      }
      nested.remove();
    }
  });

  // 2. احذف الهيدرات المكررة الموجودة حالياً
  document.querySelectorAll('.post-content .highlight').forEach(function(block) {
    const headers = block.querySelectorAll('.code-header, .highlight-header, .p-code-head, [class*="code-head"]');
    if (headers.length > 1) {
      for (let i = 1; i < headers.length; i++) {
        headers[i].remove();
      }
    }
  });

  // 3. الآن أضف هيدر فقط لو ما فيه هيدر أصلاً من الثيم
  document.querySelectorAll('.post-content .highlight').forEach(function(block) {
    const existingThemeHeader = block.querySelector('.p-code-head, .highlight-header, .code-header, .post-code-head');
    if (existingThemeHeader) {
      return;
    }
    
    let lang = 'bash';
    const pre = block.querySelector('pre');
    if (pre) {
      const classes = (pre.className + ' ' + block.className).toLowerCase();
      if (classes.includes('python')) lang = 'python';
      else if (classes.includes('javascript') || classes.includes('js')) lang = 'javascript';
      else if (classes.includes('html')) lang = 'html';
      else if (classes.includes('css')) lang = 'css';
      else if (classes.includes('bash') || classes.includes('shell') || classes.includes('sh')) lang = 'bash';
      else if (classes.includes('yaml') || classes.includes('yml')) lang = 'yaml';
    }
    
    const header = document.createElement('div');
    header.className = 'code-header';
    header.innerHTML = `<span class="code-lang">${lang}</span><button class="copy-btn" onclick="copyCodeFix(this)"><span>📋</span> نسخ</button>`;
    
    block.insertBefore(header, block.firstChild);
  });
});

function copyCodeFix(btn) {
  const block = btn.closest('.highlight');
  const code = block.querySelector('pre code') || block.querySelector('pre');
  if (!code) return;
  const text = code.innerText;
  
  navigator.clipboard.writeText(text).then(() => {
    const original = btn.innerHTML;
    btn.innerHTML = '<span>✅</span> تم النسخ';
    btn.classList.add('copied');
    setTimeout(() => {
      btn.innerHTML = original;
      btn.classList.remove('copied');
    }, 2000);
  }).catch(() => {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.opacity = '0';
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    btn.innerHTML = '<span>✅</span> تم النسخ';
    setTimeout(() => btn.innerHTML = '<span>📋</span> نسخ', 2000);
  });
}

window.addEventListener('load', function() {
  setTimeout(() => {
    document.querySelectorAll('.post-content .highlight').forEach(function(block) {
      const headers = block.querySelectorAll('.code-header');
      if (headers.length > 1) {
        for (let i = 1; i < headers.length; i++) headers[i].remove();
      }
    });
  }, 500);
});
