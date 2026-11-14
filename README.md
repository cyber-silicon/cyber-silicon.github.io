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
Giscus مضبوط حالياً في `_config.yml` على المستودع `cyber-silicon/cyber-silicon.github.io` وتصنيف `General`، مع ربط المناقشات بمسار المقال (`pathname`) واللغة العربية. إعدادات المستودع تؤكد أن Discussions مفعّلة، وتطبيق Giscus مثبت على المستودع.

- تفعيل/تعطيل العرض يتم من `comments.enabled` في `_config.yml`.
- إعدادات المعرفات العامة والتصنيف ليست أسراراً؛ لا تضع رموز وصول أو مفاتيح خاصة في القالب.
- يحتاج الزائر إلى حساب GitHub للمشاركة.
- تعليقات Blogger القديمة لا تُنقل تلقائياً؛ Giscus ينشئ مناقشة جديدة لكل مسار مقال.

## مزامنة Blogger إلى Jekyll
يوجد مستورد آمن في scripts/sync_blogger_posts.py يستخدم Blogger API v3:
- يتطلب API key مقيّداً بـ Blogger API في متغير البيئة BLOGGER_API_KEY.
- يقرأ رابط المدونة من BLOGGER_URL (الافتراضي https://cyber-silicon.blogspot.com/).
- يمكن تمرير BLOGGER_BLOG_ID اختيارياً لتجاوز اكتشاف المدونة عبر URL.
- الوضع الافتراضي هو المعاينة فقط؛ لا يكتب ملفات.
- --apply ينشئ/يحدّث فقط الملفات التي يحمل رأسها blogger_id المطابق، ولا يستبدل المقالات اليدوية.
- يحاول الحفاظ على مسار Blogger الأصلي (/YYYY/MM/post.html) كـ permalink.
- يزيل عناصر script وسمات أحداث HTML، ويسمح بإطارات الفيديو من YouTube وVimeo فقط.

بعد دمج الإعدادات إلى الفرع الافتراضي، يمكن تشغيل GitHub Actions من تبويب Actions ثم Sync Blogger posts. وضع preview قراءة فقط ويعمل على الفرع المحدد. وضع apply مقيّد تقنياً بفرع التطوير `feature/blogger-parity-20261112`، كما أن صلاحية الكتابة ممنوحة لخطوة التطبيق فقط؛ لا يستطيع سير العمل تطبيق الاستيراد على `main`. يلزم إضافة BLOGGER_API_KEY كـ Repository Secret، ويمكن ضبط BLOGGER_URL كـ Repository Variable. لا توجد جدولة تلقائية.

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

- Retrieved 7 published source posts from `https://cyber-silicon.blogspot.com/`; consolidated the duplicated VirtualBox lesson into 1 canonical article, leaving 6 unique article pages in `_posts/`.
- All 7 Blogger source IDs and URLs are retained: the canonical lesson stores its primary ID plus the duplicate source ID in `blogger_alias_ids`.
- Original Blogger permalink paths are preserved; the November duplicate URL redirects to the canonical October article URL.
- The importer is idempotent and recognizes both primary and alias Blogger IDs; hand-maintained canonical posts are protected from overwrite and duplicate creation.
- Imported article HTML is sanitized; JavaScript, event-handler attributes, forms, and untrusted embeds are removed.
- The content consolidation and import remain on this development branch only. The default branch and public site have not been changed.
