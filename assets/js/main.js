(() => {
  const root=document.documentElement;
  const q=(s,p=document)=>p.querySelector(s), qa=(s,p=document)=>[...p.querySelectorAll(s)];
  const storage={
    get:(k,fallback=null)=>{try{const v=localStorage.getItem(k);return v===null?fallback:v}catch{return fallback}},
    set:(k,v)=>{try{localStorage.setItem(k,v);return true}catch{return false}}
  };
  const parseJSON=(s,fallback=[])=>{try{return JSON.parse(s)}catch{return fallback}};
  const copyText=async text=>{
    if(navigator.clipboard?.writeText){try{await navigator.clipboard.writeText(text);return true}catch{}}
    try{
      const area=document.createElement('textarea');
      area.value=text;area.setAttribute('readonly','');area.style.position='fixed';area.style.opacity='0';
      document.body.appendChild(area);area.select();
      const ok=document.execCommand('copy');area.remove();return ok;
    }catch{return false}
  };

  const savedTheme=storage.get('cs-theme');
  if(savedTheme)root.dataset.theme=savedTheme;
  else root.dataset.theme=matchMedia('(prefers-color-scheme: light)').matches?'light':'dark';

  const syncThemeUI=()=>{
    const light=root.dataset.theme==='light';
    q('meta[name="theme-color"]')?.setAttribute('content',light?'#edf2f7':'#071827');
    qa('[data-theme-toggle]').forEach(b=>{
      b.setAttribute('aria-pressed',String(light));
      b.setAttribute('aria-label',light?'المظهر: فاتح':'المظهر: داكن');
      b.setAttribute('title',light?'المظهر الفاتح':'المظهر الداكن');
    });
  };
  syncThemeUI();

  const syncGiscusTheme=()=>{
    const frame=q('.giscus-frame');
    if(!frame?.contentWindow)return;
    const theme=root.dataset.theme==='dark'?'dark_dimmed':'light';
    frame.contentWindow.postMessage({giscus:{setConfig:{theme}}},'https://giscus.app');
  };
  const bindGiscusTheme=()=>{
    const frame=q('.giscus-frame');
    if(!frame||frame.dataset.csThemeBound)return;
    frame.dataset.csThemeBound='true';
    frame.addEventListener('load',syncGiscusTheme);
    syncGiscusTheme();
  };
  const giscusRoot=q('.giscus');
  if(giscusRoot&&'MutationObserver' in window){
    new MutationObserver(bindGiscusTheme).observe(giscusRoot,{childList:true,subtree:true});
    bindGiscusTheme();
  }
  qa('[data-theme-toggle]').forEach(b=>b.addEventListener('click',()=>{
    const next=root.dataset.theme==='dark'?'light':'dark';
    root.dataset.theme=next;storage.set('cs-theme',next);syncThemeUI();syncGiscusTheme();
  }));

  const nav=q('[data-mobile-nav]');
  const menuButtons=qa('[data-menu-toggle]');
  let menuOpener=null;
  const closeMenu=(restoreFocus=false)=>{
    const wasOpen=!!nav?.classList.contains('open');
    nav?.classList.remove('open');
    menuButtons.forEach(b=>b.setAttribute('aria-expanded','false'));
    if(wasOpen&&restoreFocus)menuOpener?.focus();
    if(wasOpen)menuOpener=null;
  };
  menuButtons.forEach(b=>b.addEventListener('click',()=>{
    const open=!nav?.classList.contains('open');
    if(open)menuOpener=b;
    else menuOpener=null;
    nav?.classList.toggle('open',open);
    b.setAttribute('aria-expanded',String(open));
  }));
  qa('[data-mobile-nav] a').forEach(a=>a.addEventListener('click',()=>closeMenu()));

  const dialog=q('[data-search-dialog]'),backdrop=q('[data-search-backdrop]'),input=q('#searchInput'),count=q('#searchCount'),noSearchResults=q('#searchNoResults'),searchEmptyState=q('.search-empty-state');
  const searchItems=qa('.search-item');
  const searchOpeners=qa('[data-search-open]');
  let searchOpener=null;
  const setSearch=open=>{
    if(!dialog||!backdrop)return;
    const isOpen=!dialog.hidden;
    if(open===isOpen)return;
    if(open){
      const active=document.activeElement;
      searchOpener=active instanceof HTMLElement&&active!==document.body?active:null;
      dialog.hidden=false;
      backdrop.hidden=false;
      document.body.classList.add('modal-open');
      searchOpeners.forEach(b=>b.setAttribute('aria-expanded','true'));
      requestAnimationFrame(()=>input?.focus());
    }else{
      dialog.hidden=true;
      backdrop.hidden=true;
      document.body.classList.remove('modal-open');
      searchOpeners.forEach(b=>b.setAttribute('aria-expanded','false'));
      const opener=searchOpener;
      searchOpener=null;
      if(opener?.isConnected)opener.focus();
    }
  };
  searchOpeners.forEach(b=>{
    b.setAttribute('aria-expanded','false');
    b.addEventListener('click',()=>setSearch(true));
  });
  qa('[data-search-close]').forEach(b=>b.addEventListener('click',()=>setSearch(false)));
  backdrop?.addEventListener('click',()=>setSearch(false));
  document.addEventListener('keydown',e=>{
    if(e.key==='Escape'){
      if(dialog&&!dialog.hidden)setSearch(false);
      if(nav?.classList.contains('open'))closeMenu(true);
    }
    if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){
      e.preventDefault();
      setSearch(true);
    }
    if(e.key==='Tab'&&dialog&&!dialog.hidden){
      const focusable=qa('button:not([disabled]),a[href],input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])',dialog)
        .filter(el=>!el.hidden&&!el.closest('[hidden]')&&el.getAttribute('aria-hidden')!=='true'&&el.getClientRects().length);
      if(!focusable.length)return;
      const first=focusable[0],last=focusable[focusable.length-1];
      if(!dialog.contains(document.activeElement)){
        e.preventDefault();
        (e.shiftKey?last:first).focus();
      }else if(e.shiftKey&&document.activeElement===first){
        e.preventDefault();
        last.focus();
      }else if(!e.shiftKey&&document.activeElement===last){
        e.preventDefault();
        first.focus();
      }
    }
  });
  input?.addEventListener('input',()=>{
    const term=input.value.trim().toLowerCase();
    let visible=0;
    searchItems.forEach(a=>{const show=!term||a.dataset.searchText.includes(term);a.hidden=!show;if(show)visible++});
    if(count)count.textContent=visible;
    if(noSearchResults)noSearchResults.hidden=!term||visible>0;
    if(searchEmptyState)searchEmptyState.hidden=!!term;
  });

  qa('[data-share]').forEach(b=>b.addEventListener('click',async()=>{
    const original=b.textContent;
    try{
      if(navigator.share){await navigator.share({title:document.title,url:location.href});return}
      const ok=await copyText(location.href);
      b.textContent=ok?'تم النسخ':'تعذر النسخ';
      setTimeout(()=>b.textContent=original,1600);
    }catch{}
  }));

  const bookmarkKey='cs-bookmarks';
  const readBookmarks=()=>parseJSON(storage.get(bookmarkKey,'[]'),[]);
  const saveBookmarks=v=>storage.set(bookmarkKey,JSON.stringify(v));
  qa('[data-bookmark]').forEach(b=>{
    const url=b.dataset.url;
    const paint=()=>{const on=readBookmarks().includes(url);b.classList.toggle('saved',on);b.textContent=on?'محفوظ':'حفظ'};
    paint();
    b.addEventListener('click',()=>{let x=readBookmarks();x=x.includes(url)?x.filter(v=>v!==url):[...x,url];saveBookmarks(x);paint()});
  });
  const bookmarkCards=qa('[data-bookmark-url]'),bookmarkGrid=q('#bookmarksGrid'),bookmarkEmpty=q('#bookmarksEmpty');
  const renderBookmarks=()=>{
    if(!bookmarkCards.length)return;
    const saved=readBookmarks();let visible=0;
    bookmarkCards.forEach(card=>{const show=saved.includes(card.dataset.bookmarkUrl);card.hidden=!show;if(show)visible++});
    if(bookmarkGrid)bookmarkGrid.hidden=visible===0;
    if(bookmarkEmpty)bookmarkEmpty.hidden=visible>0;
  };
  qa('[data-remove-bookmark]').forEach(b=>b.addEventListener('click',()=>{saveBookmarks(readBookmarks().filter(v=>v!==b.dataset.removeBookmark));renderBookmarks()}));
  renderBookmarks();

  qa('.prose pre').forEach(pre=>{
    const wrap=document.createElement('div');wrap.className='code-wrap';
    pre.parentNode.insertBefore(wrap,pre);wrap.appendChild(pre);
    const btn=document.createElement('button');btn.className='copy-code';btn.type='button';btn.textContent='نسخ';wrap.appendChild(btn);
    btn.addEventListener('click',async()=>{
      const original=btn.textContent,ok=await copyText(pre.innerText);
      btn.textContent=ok?'تم ✓':'تعذر النسخ';
      setTimeout(()=>btn.textContent=original,1400);
    });
  });

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
      const io=new IntersectionObserver(entries=>entries.forEach(e=>{
        if(e.isIntersecting){links.forEach(a=>a.classList.remove('active'));map.get(e.target.id)?.classList.add('active')}
      }),{rootMargin:'-20% 0px -65% 0px'});
      headings.forEach(h=>io.observe(h));
    }
  }
})();



/* Cyber Silicon reading experience */
(() => {
  const q=(s,p=document)=>p.querySelector(s);
  const progressFill=q('[data-reading-progress] span');
  const article=q('#articleContent');
  let ticking=false;
  const paintProgress=()=>{
    if(!progressFill||!article)return;
    const rect=article.getBoundingClientRect();
    const start=window.scrollY+rect.top;
    const total=Math.max(1,article.scrollHeight-window.innerHeight);
    const done=Math.min(total,Math.max(0,window.scrollY-start+window.innerHeight*.18));
    progressFill.style.width=(done/total*100).toFixed(2)+'%';
  };
  if(progressFill&&article){
    paintProgress();
    window.addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(()=>{paintProgress();ticking=false});ticking=true}},{passive:true});
    window.addEventListener('resize',paintProgress,{passive:true});
  }
  document.querySelectorAll('[data-reading-toggle]').forEach(button=>{
    button.addEventListener('click',()=>{
      const active=document.body.classList.toggle('reading-mode');
      button.setAttribute('aria-pressed',String(active));
      button.textContent=active?'إنهاء وضع القراءة':'وضع القراءة';
      window.scrollTo({top:0,behavior:'smooth'});
    });
  });
  const topButton=q('[data-back-to-top]');
  if(topButton){
    const show=()=>topButton.classList.toggle('visible',window.scrollY>420);
    show();
    window.addEventListener('scroll',show,{passive:true});
    topButton.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));
  }
})();
