// FIX MINIMAL - يحذف الثاني فقط
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.post-content .highlight').forEach(function(block) {
    const headers = block.querySelectorAll('.code-header, .highlight-header');
    for (let i = 1; i < headers.length; i++) {
      headers[i].style.display = 'none';
    }
    
    const nested = block.querySelector('.highlight');
    if (nested && nested !== block) {
      nested.replaceWith(...nested.childNodes);
    }
  });
});
