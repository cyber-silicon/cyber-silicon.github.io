# Cyber Silicon - Jekyll Theme

قالب احترافي لمنصة Cyber Silicon مبني بـ Jekyll ويعمل على GitHub Pages.

## ✨ المميزات بعد الإصلاح

- ✅ القائمة الجانبية تظهر في الصفحة الرئيسية وجميع الصفحات
- ✅ تخطيط كامل العرض (Full Width) بدون انحياز لليمين
- ✅ مربعات أكواد جميلة مع زر نسخ يعمل
- ✅ لا يوجد أي ذكر لـ Cyber Silicon - علامة تجارية نظيفة Cyber Silicon فقط
- ✅ دعم كامل للغة العربية RTL
- ✅ وضع ليلي / نهاري
- ✅ بحث فوري (Ctrl+K)
- ✅ متجاوب مع الجوال
- ✅ تحسين SEO وسرعة التحميل

## 🚀 التشغيل المحلي

```bash
# تثبيت Jekyll (مرة واحدة)
gem install bundler jekyll

# تثبيت الاعتماديات
bundle install

# تشغيل الموقع
bundle exec jekyll serve
```

ثم افتح http://localhost:4000

## 📦 الرفع على GitHub Pages

1. Fork هذا الريبو باسم USERNAME.github.io
2. عدل `_config.yml` (title, url, author)
3. فعل GitHub Pages: Settings > Pages > Branch: main
4. الموقع سيعمل تلقائياً على https://USERNAME.github.io

## 🎨 التخصيص

- الألوان في `_config.yml` -> `primary_color`
- الشعار في `_includes/header.html`
- القائمة الجانبية في `_includes/sidebar.html`
- الأكواد: تلقائياً يتم إضافة زر النسخ لكل كود

## 📝 إضافة مقال جديد

أنشئ ملف في `_posts/YYYY-MM-DD-title.md`:

```markdown
---
title: "عنوان المقال"
date: 2026-10-30
categories: [Kali Linux]
tags: [أمن سيبراني, كالي]
image: /assets/images/your-image.webp
description: "وصف قصير"
---

محتوى المقال هنا...
```

## 🔧 ما تم إصلاحه

- تم حل مشكلة `main-wrapper .container` التي كانت تسبب انحياز الصفحة
- تم إصلاح `default.html` ليعرض الـ Sidebar دائماً
- تمت إزالة كل مراجع `Cyber Silicon Pro` من Header/Footer/Config
- تم بناء نظام أكواد جديد `code.css` + `main.js` مع زر نسخ احترافي
- تم تحسين CSS ليكون Full Width و responsive

## 📄 الرخصة

مفتوح المصدر - Cyber Silicon 2026
