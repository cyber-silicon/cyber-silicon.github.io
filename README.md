# Cyber Silicon — Arabic Technology Blog

موقع Cyber Silicon مبني باستخدام Jekyll ويُنشر عبر GitHub Pages. تركيز المحتوى: **البرمجة، Linux، والأمن السيبراني**.

## واجهة الموقع
- واجهة عربية RTL مستوحاة من بنية مدونة Blogger: رأس تنقل ثابت، مساحة محتوى رئيسية، شريط جانبي، بطاقات المقالات، ومعلومات المقال.
- ألوان وهوية Cyber Silicon باللون الكحلي والسماوي.
- وضع فاتح وداكن مع حفظ اختيار الزائر.
- بحث فوري مع اختصار Ctrl+K.
- فهرس عناوين تلقائي داخل المقالات.
- أزرار نسخ الأكواد ومشاركة المقال وحفظه.
- وضع قراءة ومؤشر تقدم القراءة.
- تصميم متجاوب للهاتف واللوحي والحاسوب.

## التشغيل المحلي
\`\`\`bash
gem install bundler jekyll
bundle install
bundle exec jekyll serve
\`\`\`
ثم افتح http://localhost:4000

## إضافة مقال
أنشئ ملفاً داخل \`_posts/YYYY-MM-DD-title.md\`:
\`\`\`yaml
---
title: "عنوان المقال"
date: 2026-11-12
categories: [Kali Linux]
tags: [Linux, أمن سيبراني]
image: /assets/images/cover.webp
description: "وصف مختصر للمقال"
---
\`\`\`

## إعدادات الهوية
- العنوان والوصف والروابط في \`_config.yml\`.
- الرأس في \`_includes/header.html\`.
- الشريط الجانبي في \`_includes/sidebar.html\`.
- التذييل في \`_includes/footer.html\`.
- الألوان وتخطيط الشاشات في \`assets/css/cyber-silicon.css\`.
- البحث والوضع الداكن والقراءة والنسخ في \`assets/js/main.js\`.

## النشر
يُبنى الموقع بواسطة GitHub Actions ثم يُنشر عبر GitHub Pages. لا تضع رموز OAuth أو مفاتيح API أو كلمات مرور داخل المستودع.
