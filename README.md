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
- --apply ينشئ/يحدّث ملفات Blogger التي تحمل blogger_id المطابق، ولا يستبدل المقالات اليدوية.
- --sync-deletions يقرأ الحالات الثلاث (منشور/مسودة/مجدول) بصلاحية OAuth إدارية؛ المسودة والمجدول لا يُحذفان، أما المحذوف نهائياً أو المنقول إلى المهملات فيُحذف ملفه المستورد فقط بعد إعادة التحقق من معرّفه.
- لا تُحذف الملفات اليدوية أو الملفات التي لا تحمل علامة الاستيراد الخاصة بالمستورد. وعند تعذر قراءة أي حالة أو التحقق من معرّف، تتوقف المزامنة دون تنفيذ الحذف.
- يحاول الحفاظ على مسار Blogger الأصلي (/YYYY/MM/post.html) كـ permalink.
- يزيل عناصر script وسمات أحداث HTML، ويسمح بإطارات YouTube وVimeo، وبمشغّل TikTok الرسمي على المسار `/player/v1/{video_id}` فقط.

بعد دمج الإعدادات إلى `main`، أضف أسرار OAuth الأربعة في إعدادات المستودع: `BLOGGER_API_KEY` و`BLOGGER_OAUTH_CLIENT_ID` و`BLOGGER_OAUTH_CLIENT_SECRET` و`BLOGGER_OAUTH_REFRESH_TOKEN`. يجب أن يكون رمز التحديث صادراً عن حساب يملك صلاحية إدارة المدونة وبنطاق `https://www.googleapis.com/auth/blogger.readonly`. استخدم `Sync Blogger preview` للمعاينة من فرع `feature/blogger-lifecycle-sync-20261115`، ثم استخدم `Import Blogger posts to development branch` من `main` للتطبيق. يكتب سير العمل إلى فرع التطوير المحدد فقط؛ وبعد المراجعة يُدمج طلب السحب إلى `main` لنشر الموقع.

مثال تشغيل محلي:
```bash
export BLOGGER_API_KEY="YOUR_RESTRICTED_API_KEY"
export BLOGGER_URL="https://cyber-silicon.blogspot.com/"
export BLOGGER_OAUTH_CLIENT_ID="YOUR_OAUTH_CLIENT_ID"
export BLOGGER_OAUTH_CLIENT_SECRET="YOUR_OAUTH_CLIENT_SECRET"
export BLOGGER_OAUTH_REFRESH_TOKEN="YOUR_OAUTH_REFRESH_TOKEN"
python3 scripts/sync_blogger_posts.py --sync-deletions
# راجع خطة الإضافة والتعديل والحذف قبل الكتابة
python3 scripts/sync_blogger_posts.py --apply --sync-deletions
```

تتطلب مزامنة الحذف قراءة حالات المسودات والمنشورات المجدولة بصلاحية OAuth إدارية؛ لذلك يستخدم المستورد Refresh Token لتوليد Access Token مؤقت لكل تشغيل. لا تُحفظ الرموز في المستودع، بل في GitHub Secrets. لا يرفع هذا المستورد أي شيء إلى Blogger؛ اتجاهه Blogger إلى Jekyll فقط.

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

- The repository includes the Blogger v3 importer and controlled GitHub Actions workflows.
- Any sample articles currently under `_posts/` are temporary test fixtures, not approved production content; they may be removed without changing the theme or importer.
- The importer supports stable Blogger IDs, source aliases, permalink preservation, HTML sanitization, and protection for hand-maintained posts.
- Preview is read-only and includes a safe deletion plan. The separate import workflow is manual-only and writes only to the dedicated development branch.
- Deletion sync requires Blogger OAuth refresh credentials; it checks all three API-visible post states and re-fetches each deletion candidate before removing an importer-managed local file.
- The importer is one-way (Blogger → Jekyll); it never writes to Blogger.
