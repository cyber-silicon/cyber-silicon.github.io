---
title: "[سلسلة Kali Linux - الدرس 2] تحميل برنامج VirtualBox و حزمة Extension Pack"
date: 2026-11-03 19:38:50 +0200
categories: ["Kali Linux", "VirtualBox", "Cyber Silicon"]
tags: ["Kali Linux", "VirtualBox", "Cyber Silicon", "دروس وتقنيات"]
labels: ["Kali Linux", "VirtualBox", "Cyber Silicon", "دروس وتقنيات"]
description: "في هذا الدرس نتعلم كيفية تحميل برنامج Oracle VM VirtualBox وحزمة Extension Pack لتجهيز البيئة الوهمية لتثبيت نظام Kali Linux."
summary: "في هذا الدرس نتعلم كيفية تحميل برنامج Oracle VM VirtualBox وحزمة Extension Pack لتجهيز البيئة الوهمية لتثبيت نظام Kali Linux."
lang: ar
direction: rtl
comments: true
toc: true
---

# [سلسلة Kali Linux - الدرس 2] كيفية تحميل برنامج VirtualBox وحزمة Extension Pack

مرحباً بكم في الدرس الثاني من **سلسلة تعلم واحتراف نظام Kali Linux من الصفر** المقدمة من قناة **Cyber Silicon**! 💻🚀

![IMG_20261005_052601.webp](/assets/images/IMG_20261005_052601.webp)

بعد أن تعرّفنا في الدرس الأول على كيفية اختيار وتحميل نسخة Kali Linux المناسبة، تأتي الخطوة الثانية وهي تجهيز البيئة الوهمية (Virtual Environment) التي سنقوم بتثبيت النظام عليها باستخدام برنامج **Oracle VM VirtualBox**.

---

### 📌 ما هو برنامج VirtualBox ولماذا نحتاجه؟

برنامج **VirtualBox** هو أداة مجانية ومفتوحة المصدر تتيح لك إنشاء حواسيب وهمية (Virtual Machines) داخل نظامك الحالي. تتيح لك هذه البيئة تشغيل نظام Kali Linux وتجربة أدواته بأمان تام ودون أي تأثير على ملفاتك أو نظام تشغيلك الأساسي.

---

### 📥 أولاً: التوجه إلى الصفحة الرسمية للتحميل

1. افتح المتصفح وتوجه إلى الموقع الرسمي: **`virtualbox.org`**

![IMG_20261005_052601 1.webp](/assets/images/IMG_20261005_052601 1.webp)

2. اضغط على زر **Download** في الصفحة الرئيسية أو قائمة **Downloads** العلوية.

---

### ⚙️ ثانياً: شرح النسخ والحزم المتاحة (VirtualBox Platform Packages)

![IMG_20261005_052655 1.webp](/assets/images/IMG_20261005_052655 1.webp)

عند فتح صفحة التنزيلات، ستجد قسم **VirtualBox Platform Packages** والذي يوفر ملف التثبيت المخصص لكل نظام تشغيل:

* **Windows hosts:** مخصصة لأجهزة الكمبيوتر التي تعمل بنظام **Windows** (مثل Windows 10 أو Windows 11).
* **macOS / Intel hosts:** مخصصة لأجهزة أبل ماك (MacBook / iMac) القديمة التي تعمل بمعالجات **Intel**.
* **macOS / Apple Silicon hosts:** مخصصة لأجهزة أبل ماك الحديثة المزودة بشرائح أبل **Apple Silicon** (M1, M2, M3, M4).
* **Linux distributions:** مخصصة لأنظمة لينكس المختلفة مثل Ubuntu, Debian, Fedora, RHEL, و openSUSE.
* **Solaris hosts / Solaris 11 IPS hosts:** مخصصة لأنظمة Oracle Solaris على بيئات الخوادم والمؤسسات.

---

### 🧩 ثالثاً: حزمة التوسعة (VirtualBox Extension Pack)

لضمان الأداء الأفضل ولتفعيل كامل خصائص البيئة الوهمية، يجب تحميل حزمة **Extension Pack**.

**مميزات حزمة Extension Pack:**
* دعم منافذ الأجهزة والأجهزة الموصولة عبر USB 2.0 و USB 3.0.
* دعم التشفير للأقراص الوهمية (Virtual Disk Encryption).
* دعم ميزة NVMe لتسريع أداء التخزين الوهمي.
* إمكانية التحكم عن بعد عبر RDP (VirtualBox Remote Desktop Protocol).

**طريقة التحميل:** من قسم **VirtualBox Extension Pack**، اضغط على زر **Accept and download** للموافقة على الترخيص وتنزيل الملف.

---

## 🔗 روابط التحميل المباشرة

* 🌐 **صفحة التحميل الرئيسية:** [virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)
* 💻 **تحميل VirtualBox لنظام Windows:** [VirtualBox Windows Installer](https://download.virtualbox.org/virtualbox/7.2.20/VirtualBox-7.2.20-175154-Win.exe)
* 🧩 **تحميل حزمة Extension Pack:** [VirtualBox Extension Pack All Platforms](https://download.virtualbox.org/virtualbox/7.2.20/Oracle_VirtualBox_Extension_Pack-7.2.20.vbox-extpack)

---

💡 **الخطوة القادمة:** في الدرس القادم سنقوم بشرح تثبيت برنامج VirtualBox وإضافة حزمة Extension Pack وضبط إعدادات البيئة الوهمية استعداداً لتثبيت نظام Kali Linux!

---

### 🔗 التنقل بين دروس السلسلة

* **الدرس السابق 👈:** [الدرس 1](https://cyber-silicon.github.io/Kali%20Linux/Cyber%20Silicon/%D8%AF%D8%B1%D9%88%D8%B3%20%D9%88%D8%AA%D9%82%D9%86%D9%8A%D8%A7%D8%AA/2026/11/03/lesson-1-سلسلة-kali-linux-الدرس-1-الشرح-الشامل-لاختيار-وتحميل-نسخة-ka.html)
* **الدرس التالي 👈:** سيُضاف عند نشر الدرس التالي