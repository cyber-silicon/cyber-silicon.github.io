(() => {
  const root=document.documentElement;
  const safeJSON=(s,fallback=[])=>{try{return JSON.parse(s)}catch{return fallback}};
  const q=(s,p=document)=>p.querySelector(s), qa=(s,p=document)=>[...p.querySelectorAll(s)];
  const saved=localStorage.getItem('cs-theme');
  if(saved) root.dataset.theme=saved;
  else root.dataset.theme=matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';

  qa('[data-theme-toggle]').forEach(b=>b.addEventListener('click',()=>{const n=root.dataset.theme==='dark'?'light':'dark';root.dataset.theme=n;localStorage.setItem('cs-theme',n)}));
  const nav=q('[data-mobile-nav]');
  qa('[data-menu-toggle]').forEach(b=>b.addEventListener('click',()=>{
    const open=!nav?.classList.contains('open');
    nav?.classList.toggle('open',open);
    b.setAttribute('aria-expanded',String(open));
  }));
  qa('[data-mobile-nav] a').forEach(a=>a.addEventListener('click',()=>{
    nav?.classList.remove('open');
    qa('[data-menu-toggle]').forEach(b=>b.setAttribute('aria-expanded','false'));
  }));

  const dialog=q('[data-search-dialog]'),backdrop=q('[data-search-backdrop]'),input=q('#searchInput'),count=q('#searchCount');
  const searchItems=qa('.search-item');
  const setSearch=(open)=>{if(!dialog||!backdrop)return;dialog.hidden=!open;backdrop.hidden=!open;document.body.classList.toggle('modal-open',open);if(open)setTimeout(()=>input?.focus(),20)};
  qa('[data-search-open]').forEach(b=>b.addEventListener('click',()=>setSearch(true)));
  qa('[data-search-close]').forEach(b=>b.addEventListener('click',()=>setSearch(false)));
  backdrop?.addEventListener('click',()=>setSearch(false));
  document.addEventListener('keydown',e=>{if(e.key==='Escape')setSearch(false);if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();setSearch(true)}});
  input?.addEventListener('input',()=>{const term=input.value.trim().toLowerCase();let visible=0;searchItems.forEach(a=>{const show=!term||a.dataset.searchText.includes(term);a.hidden=!show;if(show)visible++});if(count)count.textContent=visible});

  qa('[data-share]').forEach(b=>b.addEventListener('click',async()=>{try{if(navigator.share)await navigator.share({title:document.title,url:location.href});else{await navigator.clipboard.writeText(location.href);b.textContent='تم النسخ'}}catch{}}));

  const bookmarkKey='cs-bookmarks';
  const readBookmarks=()=>safeJSON(localStorage.getItem(bookmarkKey)||'[]');
  const saveBookmarks=v=>localStorage.setItem(bookmarkKey,JSON.stringify(v));
  qa('[data-bookmark]').forEach(b=>{const url=b.dataset.url;const paint=()=>{const on=readBookmarks().includes(url);b.classList.toggle('saved',on);b.textContent=on?'محفوظ':'حفظ'};paint();b.addEventListener('click',()=>{let x=readBookmarks();x=x.includes(url)?x.filter(v=>v!==url):[...x,url];saveBookmarks(x);paint()})});
  const bookmarkCards=qa('[data-bookmark-url]'),bookmarkGrid=q('#bookmarksGrid'),bookmarkEmpty=q('#bookmarksEmpty');
  const renderBookmarks=()=>{if(!bookmarkCards.length)return;const saved=readBookmarks();let visible=0;bookmarkCards.forEach(card=>{const show=saved.includes(card.dataset.bookmarkUrl);card.hidden=!show;if(show)visible++});if(bookmarkGrid)bookmarkGrid.hidden=visible===0;if(bookmarkEmpty)bookmarkEmpty.hidden=visible>0};
  qa('[data-remove-bookmark]').forEach(b=>b.addEventListener('click',()=>{saveBookmarks(readBookmarks().filter(v=>v!==b.dataset.removeBookmark));renderBookmarks()}));
  renderBookmarks();

  qa('.prose pre').forEach(pre=>{const wrap=document.createElement('div');wrap.className='code-wrap';pre.parentNode.insertBefore(wrap,pre);wrap.appendChild(pre);const btn=document.createElement('button');btn.className='copy-code';btn.textContent='نسخ';wrap.appendChild(btn);btn.addEventListener('click',async()=>{await navigator.clipboard.writeText(pre.innerText);btn.textContent='تم ✓';setTimeout(()=>btn.textContent='نسخ',1400)})});

  const article=q('#articleContent'),toc=q('#articleToc');
  if(article&&toc){
    const headings=qa('h2,h3',article);
    const slug=s=>s.trim().toLowerCase().replace(/[^\p{L}\p{N}]+/gu,'-').replace(/^-|-$/g,'');
    const used=new Set();
    headings.forEach((h,i)=>{
      if(!h.id){let id=slug(h.textContent)||('section-'+(i+1)),base=id,n=2;while(used.has(id)||document.getElementById(id))id=base+'-'+n++;h.id=id}
      used.add(h.id);
      const a=document.createElement('a');a.href='#'+h.id;a.textContent=h.textContent;a.className=h.tagName==='H3'?'sub':'';
      toc.appendChild(a);
    });
    if(!headings.length)toc.closest('.article-aside')?.remove();
    else if('IntersectionObserver' in window){
      const links=qa('a',toc);
      const map=new Map(links.map(a=>[a.getAttribute('href').slice(1),a]));
      const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){links.forEach(a=>a.classList.remove('active'));map.get(e.target.id)?.classList.add('active')}}),{rootMargin:'-20% 0px -65% 0px'});
      headings.forEach(h=>io.observe(h));
    }
  }
})();