---
title: "مرحباً بكم في Plus UI Pro - قالب GitHub Pages الاحترافي"
date: 2026-10-26 14:00:00 +0200
categories: ["إعلانات", "قوالب"]
tags: ["Plus UI", "GitHub Pages", "Jekyll", "قالب"]
image: /assets/images/welcome.png
description: "تم إطلاق قالب Plus UI Pro لـ GitHub Pages - نفس تصميم Plus UI الشهير مع مميزات تغيير اللون والتعليقات والدارك مود"
toc: true
comments: true
---

## 🎉 مرحباً بكم في القالب الجديد

هذا أول مقال على قالب **Plus UI Pro** - نسخة مطورة من قالب Plus UI الشهير لـ Blogger، لكن الآن على **GitHub Pages** بسرعة فائقة ومميزات خرافية.

### ✨ ما الجديد في هذا القالب؟

#### 1. 🎨 تغيير لون الصفحة (الميزة التي طلبتها)
مثل Plus UI تماماً، الآن يمكنك تغيير لون الموقع بالكامل:

- 8 ألوان جاهزة: أزرق Plus UI الأصلي، أخضر، برتقالي، بنفسجي، أصفر، وردي، أزرق داكن، أحمر
- لون مخصص عبر Color Picker
- يتم حفظ اختيارك تلقائياً

**جرب الآن:** اضغط على أيقونة 🎨 في الهيدر العلوي

#### 2. 🌓 دارك مود احترافي
- فاتح / داكن / تلقائي حسب النظام
- انتقال سلس بين الأوضاع
- يحفظ تفضيلك

#### 3. 💬 نظام التعليقات الشامل
يدعم 3 أنظمة تعليقات:

**Giscus (أنصح به):**
```yaml
comments:
  provider: giscus
  giscus:
    repo: USERNAME/USERNAME.github.io
```

**Utterances:**
```yaml
comments:
  provider: utterances
```

**Disqus:**
```yaml
comments:
  provider: disqus
  disqus:
    shortname: your-shortname
```

#### 4. 🔍 بحث فوري
- بحث بدون إضافات خارجية
- يبحث في العناوين والمحتوى والوسوم
- اختصار `Ctrl+K` لفتح البحث

#### 5. 📐 مميزات Plus UI الأصلية
- كروت مقالات بظلال وانتقالات
- شبكة وقائمة عرض
- تكبير وتصغير الخط
- شريط تقدم قراءة
- جدول محتويات تلقائي
- مشاركة المقالات
- حفظ المقالات

### 🚀 كيف تنشر مقالاتك هنا تلقائياً؟

سكربت `blogger_fb_publisher_v2.py` الذي جهزته لك ينشر تلقائياً:

```bash
python blogger_fb_publisher_v2.py
```

سيأخذ ملفاتك من `queue/*.md` ويرفعها إلى:

- `_posts/` في GitHub
- `assets/images/` للصور

### 📝 مثال Front Matter لمقال

```yaml
---
title: "الدرس 1: صيانة اللابتوب"
date: 2026-10-26 15:00:00 +0200
categories: ["صيانة", "لابتوب"]
tags: ["صيانة", "هاردوير", "تعليمي"]
image: /assets/images/lesson01.jpg
description: "شرح مفصل لصيانة شاشات اللابتوب"
toc: true
comments: true
---
```

### 🎨 تخصيص الألوان من _config.yml

```yaml
primary_color: "#2962ff" # غير هذا اللون
plus_ui:
  color_presets:
    - "#2962ff"
    - "#00b894"
    - "#e17055"
```

### 🔧 التثبيت السريع

1. انسخ مجلد `plus-ui-jekyll-pro` إلى جهازك
2. ارفعه إلى ريبو `USERNAME.github.io`
3. فعل GitHub Pages من Settings
4. أضف هذا في `_config.yml`:

```yaml
comments:
  provider: giscus
  giscus:
    repo: USERNAME/USERNAME.github.io
```

5. اذهب إلى https://giscus.app واحصل على `repo_id` و `category_id`

### 📱 PWA جاهز

القالب يدعم PWA - يمكن تثبيته كتطبيق على الهاتف مثل Plus UI الأصلي.

### 💡 نصائح

- استخدم صور بأبعاد 16:9 للكروت
- اكتب وصف قصير في `description`
- استخدم `toc: true` للمقالات الطويلة
- فعل التعليقات بـ `comments: true`

---

**استمتع بقالب Plus UI Pro!** إذا أردت أي تعديل إضافي، فقط اطلب.

> تم تطوير هذا القالب خصيصاً لـ Cyber Silicon Suite ليعمل مع نظام النشر التلقائي.
