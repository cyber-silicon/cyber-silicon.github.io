(() => {
  const root=document.documentElement;
  const saved=localStorage.getItem('cs-theme');
  if(saved) root.dataset.theme=saved;
  else root.dataset.theme=matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';

  const q=(s,p=document)=>p.querySelector(s), qa=(s,p=document)=>[...p.querySelectorAll(s)];
  qa('[data-theme-toggle]').forEach(b=>b.addEventListener('click',()=>{const n=root.dataset.theme==='dark'?'light':'dark';root.dataset.theme=n;localStorage.setItem('cs-theme',n)}));
  const nav=q('[data-mobile-nav]');
  qa('[data-menu-toggle]').forEach(b=>b.addEventListener('click',()=>nav?.classList.toggle('open')));

  const dialog=q('[data-search-dialog]'), backdrop=q('[data-search-backdrop]'), input=q('#searchInput');
  const setSearch=(open)=>{if(!dialog||!backdrop)return;dialog.hidden=!open;backdrop.hidden=!open;document.body.classList.toggle('modal-open',open);if(open)setTimeout(()=>input?.focus(),20)};
  qa('[data-search-open]').forEach(b=>b.addEventListener('click',()=>setSearch(true)));
  qa('[data-search-close]').forEach(b=>b.addEventListener('click',()=>setSearch(false)));
  backdrop?.addEventListener('click',()=>setSearch(false));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')setSearch(false);if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();setSearch(true)}});

  input?.addEventListener('input',()=>{const term=input.value.trim().toLowerCase();qa('.search-item').forEach(a=>a.hidden=!!term&&!a.dataset.searchText.includes(term))});

  qa('[data-share]').forEach(b=>b.addEventListener('click',async()=>{try{if(navigator.share)await navigator.share({title:document.title,url:location.href});else{await navigator.clipboard.writeText(location.href);b.textContent='تم النسخ'}}catch{}}));
  qa('[data-bookmark]').forEach(b=>{const key='cs-bookmarks';const url=b.dataset.url;const read=()=>JSON.parse(localStorage.getItem(key)||'[]');const paint=()=>b.classList.toggle('saved',read().includes(url));paint();b.addEventListener('click',()=>{let x=read();x=x.includes(url)?x.filter(v=>v!==url):[...x,url];localStorage.setItem(key,JSON.stringify(x));paint();b.textContent=x.includes(url)?'محفوظ':'حفظ'})});

  qa('.prose pre').forEach(pre=>{const wrap=document.createElement('div');wrap.className='code-wrap';pre.parentNode.insertBefore(wrap,pre);wrap.appendChild(pre);const btn=document.createElement('button');btn.className='copy-code';btn.textContent='نسخ';wrap.appendChild(btn);btn.addEventListener('click',async()=>{await navigator.clipboard.writeText(pre.innerText);btn.textContent='تم ✓';setTimeout(()=>btn.textContent='نسخ',1400)})});
})();