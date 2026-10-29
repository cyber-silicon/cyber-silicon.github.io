/* Fix code copy button - Plus UI Pro */
document.addEventListener('DOMContentLoaded', function() {
  // Fix all code blocks
  document.querySelectorAll('.post-content .highlight').forEach(function(block) {
    // Skip if already fixed
    if (block.querySelector('.code-header')) return;
    
    // Detect language
    let lang = 'bash';
    const pre = block.querySelector('pre');
    if (pre) {
      const classes = pre.className + ' ' + block.className;
      if (classes.includes('python')) lang = 'python';
      else if (classes.includes('javascript') || classes.includes('js')) lang = 'javascript';
      else if (classes.includes('html')) lang = 'html';
      else if (classes.includes('css')) lang = 'css';
      else if (classes.includes('bash') || classes.includes('shell')) lang = 'bash';
    }
    
    // Create header
    const header = document.createElement('div');
    header.className = 'code-header';
    header.innerHTML = `<span class="code-lang">${lang}</span><button class="copy-btn" onclick="copyCode(this)"><span>📋</span> نسخ</button>`;
    
    // Insert header before pre
    block.insertBefore(header, block.firstChild);
  });
});

function copyCode(btn) {
  const block = btn.closest('.highlight');
  const code = block.querySelector('pre code') || block.querySelector('pre');
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
    // Fallback
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    btn.innerHTML = '<span>✅</span> تم النسخ';
    setTimeout(() => btn.innerHTML = '<span>📋</span> نسخ', 2000);
  });
}
