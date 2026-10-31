---
layout: page
title: الأقسام
description: تصفح محتوى Cyber Silicon حسب المجال.
permalink: /categories/
---

<div class="taxonomy-intro">
  <p>اختر المجال الذي تريد استكشافه. يتم إنشاء هذه الصفحة تلقائيًا من تصنيفات المقالات.</p>
</div>

<div class="taxonomy-list">
{% assign categories = site.categories | sort %}
{% for category in categories %}
<section class="taxonomy-group" id="{{ category[0] | slugify }}">
  <div class="taxonomy-head">
    <div>
      <span class="eyebrow">CATEGORY</span>
      <h2>{{ category[0] }}</h2>
    </div>
    <span class="taxonomy-count">{{ category[1].size }} مقال</span>
  </div>
  <div class="post-grid taxonomy-grid">
    {% for post in category[1] %}
    <article class="post-card">
      <a class="card-media" href="{{ post.url | relative_url }}">
        {% if post.image %}<img src="{{ post.image | relative_url }}" alt="" loading="lazy">{% else %}<span>{{ forloop.index | prepend: '0' }}</span>{% endif %}
      </a>
      <div class="card-body">
        <span class="meta">{{ post.date | date: "%Y-%m-%d" }}</span>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.description | default: post.excerpt | strip_html | truncate: 110 }}</p>
        <div class="card-foot"><span>{{ post.content | number_of_words | divided_by: 180 | plus: 1 }} دقائق</span><a href="{{ post.url | relative_url }}">اقرأ ←</a></div>
      </div>
    </article>
    {% endfor %}
  </div>
</section>
{% endfor %}
</div>
