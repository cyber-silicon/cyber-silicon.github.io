---
layout: page
title: الوسوم
description: جميع الوسوم والكلمات المفتاحية
permalink: /tags/
---

<div class="tags-page">
  <h2>🏷️ جميع الوسوم</h2>
  <div class="tags-cloud-large">
    {% assign tags = site.tags | sort %}
    {% for tag in tags %}
    <a href="#{{ tag[0] | slugify }}" class="tag-large">
      #{{ tag[0] }} <span>{{ tag[1].size }}</span>
    </a>
    {% endfor %}
  </div>

  {% for tag in tags %}
  <div class="tag-group" id="{{ tag[0] | slugify }}">
    <h3>#{{ tag[0] }}</h3>
    <div class="posts-grid mini">
      {% for post in tag[1] %}
        {% include post-card.html post=post %}
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>

<style>
.tags-cloud-large { display:flex; flex-wrap:wrap; gap:10px; margin:20px 0; }
.tag-large { background: var(--card-bg); border:1px solid var(--border); padding:8px 14px; border-radius:20px; font-size:13px; }
.tag-large span { background: var(--primary); color:white; padding:2px 8px; border-radius:10px; margin-right:6px; font-size:11px; }
.tag-group { margin-top:30px; padding-top:20px; border-top:1px solid var(--border); }
</style>
