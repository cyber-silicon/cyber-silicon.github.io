---
layout: page
title: الأقسام
description: تصفح جميع أقسام المدونة
permalink: /categories/
---

<div class="categories-page">
  <h2>📚 جميع الأقسام</h2>
  {% assign categories = site.categories | sort %}
  {% for category in categories %}
  <div class="category-group" id="{{ category[0] | slugify }}">
    <h3>{{ category[0] }} <span class="count">({{ category[1].size }})</span></h3>
    <div class="posts-grid mini">
      {% for post in category[1] %}
        {% include post-card.html post=post %}
      {% endfor %}
    </div>
  </div>
  {% endfor %}
</div>
