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

## التعليقات عبر Giscus
التعليقات اختيارية ومعطلة افتراضياً. لتفعيلها:
1. فعّل Discussions في إعدادات مستودع GitHub العام.
2. ثبّت تطبيق Giscus على المستودع واختر تصنيف Discussions مناسباً.
3. استخدم مولّد الإعدادات في https://giscus.app/ للحصول على معرّفي المستودع والتصنيف.
4. أدخل القيم في إعدادات comments داخل _config.yml ثم غيّر enabled إلى true.

لا تضع رموز وصول أو أسراراً في القالب. يتطلب Giscus حساب GitHub للمشاركة. التعليقات القديمة في Blogger لا تُنقل تلقائياً إلى Discussions؛ هذه مساحة تعليقات جديدة مرتبطة بمسار المقال.

## مزامنة Blogger إلى Jekyll
يوجد مستورد آمن في scripts/sync_blogger_posts.py يستخدم Blogger API v3:
- يتطلب API key مقيّداً بـ Blogger API في متغير البيئة BLOGGER_API_KEY.
- يقرأ رابط المدونة من BLOGGER_URL (الافتراضي https://cyber-silicon.blogspot.com/).
- يمكن تمرير BLOGGER_BLOG_ID اختيارياً لتجاوز اكتشاف المدونة عبر URL.
- الوضع الافتراضي هو المعاينة فقط؛ لا يكتب ملفات.
- --apply ينشئ/يحدّث فقط الملفات التي يحمل رأسها blogger_id المطابق، ولا يستبدل المقالات اليدوية.
- يحاول الحفاظ على مسار Blogger الأصلي (/YYYY/MM/post.html) كـ permalink.
- يزيل عناصر script وسمات أحداث HTML، ويسمح بإطارات الفيديو من YouTube وVimeo فقط.

بعد دمج الإعدادات إلى الفرع الافتراضي، يمكن تشغيل GitHub Actions من تبويب Actions ثم Sync Blogger posts. اختر preview أولاً؛ اختر apply فقط بعد مراجعة الملخص. يلزم إضافة BLOGGER_API_KEY كـ Repository Secret، ويمكن ضبط BLOGGER_URL كـ Repository Variable. لا توجد جدولة تلقائية.

مثال تشغيل محلي:
```bash
export BLOGGER_API_KEY="YOUR_RESTRICTED_API_KEY"
export BLOGGER_URL="https://cyber-silicon.blogspot.com/"
python3 scripts/sync_blogger_posts.py
# راجع ملخص المعاينة قبل الكتابة
python3 scripts/sync_blogger_posts.py --apply
```

للمدونات العامة، تتيح Blogger API v3 قراءة المنشورات دون تفويض مستخدم، لكن يلزم API key. المدونات الخاصة تتطلب OAuth وصلاحيات مناسبة. لا يرفع هذا المستورد أي شيء إلى Blogger؛ اتجاهه الحالي Blogger إلى Jekyll فقط.

## التشغيل المحلي
```bash
gem install bundler jekyll
bundle install
bundle exec jekyll serve
```
ثم افتح http://localhost:4000

## إضافة مقال يدوي
أنشئ ملفاً داخل _posts/YYYY-MM-DD-title.md:
```yaml
---
title: "عنوان المقال"
date: 2026-11-14
categories: [Kali Linux]
tags: [Linux, أمن سيبراني]
image: /assets/images/cover.webp
description: "وصف مختصر للمقال"
---
```

## إعدادات الهوية
- العنوان والوصف والروابط في _config.yml.
- الرأس في _includes/header.html.
- التعليقات في _includes/comments.html.
- الشريط الجانبي في _includes/sidebar.html.
- التذييل في _includes/footer.html.
- الألوان وتخطيط الشاشات في assets/css/cyber-silicon.css.
- البحث والوضع الداكن والقراءة والنسخ في assets/js/main.js.

## النشر
يُبنى الموقع بواسطة GitHub Actions ثم يُنشر عبر GitHub Pages. لا تضع رموز OAuth أو مفاتيح API أو كلمات مرور داخل المستودع.

## Blogger import status

- Imported 7 published posts from `https://cyber-silicon.blogspot.com/` into `_posts/` on 2026-11-14.
- Blogger post IDs are retained in `blogger_id`; source URLs are retained in `blogger_url`.
- Original Blogger permalink paths are preserved for the imported posts where the path passed validation.
- The importer is idempotent and will update only files carrying the matching `blogger_id`; hand-authored posts are protected from overwrite.
- Imported article HTML is sanitized; JavaScript, event-handler attributes, forms, and untrusted embeds are removed.
- The import was performed on this development branch only. The default branch and the public site do not contain these seven imported posts yet.
