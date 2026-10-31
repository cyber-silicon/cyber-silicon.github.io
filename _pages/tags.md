---
layout: page
title: الوسوم
description: ابحث في Cyber Silicon حسب الموضوع أو الأداة أو التقنية.
permalink: /tags/
---

<div class="taxonomy-intro">
  <p>الوسوم تساعدك عندما تبحث عن موضوع أدق من القسم: أداة معينة، نظام تشغيل، لغة برمجة، نوع عطل أو تقنية محددة. اختر وسمًا للوصول إلى كل المقالات المرتبطة به.</p>
</div>

<div class="tag-cloud-pro">
{% assign tags = site.tags | sort %}
{% for tag in tags %}
  <a href="#{{ tag[0] | slugify }}">#{{ tag[0] }} <span>{{ tag[1].size }}</span></a>
{% endfor %}
</div>

<div class="taxonomy-list">
{% for tag in tags %}
<section class="taxonomy-group" id="{{ tag[0] | slugify }}">
  <div class="taxonomy-head">
    <div><span class="eyebrow">TAG</span><h2>#{{ tag[0] }}</h2></div>
    <span class="taxonomy-count">{{ tag[1].size }} مقال</span>
  </div>
  <div class="compact-list">
    {% for post in tag[1] %}
    <a class="compact-row" href="{{ post.url | relative_url }}">
      <div><strong>{{ post.title }}</strong><small>{{ post.description | default: post.excerpt | strip_html | truncate: 100 }}</small></div>
      <span>{{ post.date | date: "%Y-%m-%d" }}</span>
    </a>
    {% endfor %}
  </div>
</section>
{% endfor %}
</div>
