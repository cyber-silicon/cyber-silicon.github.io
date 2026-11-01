---
title: "[سلسلة Kali Linux - الدرس 5] التثبيت الكامل والتشغيل الأول لنظام Kali Linux"
date: 2026-11-01 14:35:43 +0200
image: /assets/images/tiktok-cover-سلسلة-kali-linux-الد.jpg
description: "image: "
summary: "image: "
lang: ar
direction: rtl
comments: true
toc: true
tiktok_url: "https://www.tiktok.com/@cyber_silicon/video/7667125195303357716?utm_campaign=tt4d_open_api&utm_source=sbawotogm6mg76anhw"
---

![[سلسلة Kali Linux - الدرس 5] التثبيت الكامل والتشغيل الأول لنظام Kali Linux](/assets/images/tiktok-cover-سلسلة-kali-linux-الد.jpg){: .center-image }

مرحباً بكم في الدرس الخامس من **سلسلة تعلم واحتراف نظام Kali Linux من الصفر** المقدمة من قناة **Cyber Silicon**! 💻🐉

نصل اليوم للخطوة المرتقبة التي نحصد فيها ثمرة الدروس السابقة، حيث نتعلم خطوة بخطوة كيفية بدء عملية التثبيت الرسومي الكامل لنظام Kali Linux داخل البيئة الوهمية VirtualBox والوصول لسطح المكتب بنجاح.

---

### 🚀 الخطوة 1: بدء التثبيت الرسومي (Graphical Install)

1. افتح برنامج **VirtualBox** وحدد الآلة الوهمية التي قمنا بإنشائها سابقاً (`Kali`).
2. اضغط على زر **Start** لتشغيل الآلة.
![[68.webp]]
3. من قائمة الإقلاع الخاصة بنظام Kali Linux، اختر **Graphical Install** واضغط على `Enter`.
![[623.webp]]
---

### 🌍 الخطوة 2: ضبط اللغة والمنطقة وتوزيع الكيبورد

1. **Select a language:** اختر لغة تثبيت النظام (يُفضل اختيار **English** لضمان استقرار الأسماء والمجلدات).
![[629.webp]]
2. **Select your location:** حدد منطقتك الجغرافية (مثل `United States` أو منطقتك المحلية).
![[628.webp]]
3. **Configure the keyboard:** اختر توزيع لوحة المفاتيح الافتراضي (**American English**).
![[67.webp]]
---

### 👤 الخطوة 3: إعداد اسم المستخدم وكلمة المرور (User & Password)

1. **Configure the network:** في خانة **Hostname** اكتب اسم الجهاز على الشبكة (مثلاً: `kali`)، وقم بتخطي خانة **Domain name** بالنقر على `Continue`.
![[619.webp]]
2. **Set up users and passwords:** 
   * اكتب اسمك الكامل أو اسم الحساب (**Full name for the new user**).
![[63.webp]]
   * اكتب اسم المستخدم الحركي (**Username for your account**) الذي ستستخدمه لتسجيل الدخول (مثلاً: `yusuf`).
   * أدخل كلمة المرور الخاصة بك وأعد كتابتها للتأكيد، ثم اضغط **Continue**.
![[65.webp]]
---

### 💾 الخطوة 4: تقسيم الهارد الوهمي (Partition Disks)

1. في شاشة **Partition disks**، اختر **Guided - use entire disk** لتقسيم القرص الوهمي تلقائياً.
![[618.webp]]
2. حدد الهارد الوهمي المتاح واضغط **Continue**.
![[625.webp]]
3. اختر الخيار الموصى به للمبتدئين: **All files in one partition (recommended for new users)**.
![[66.webp]]
4. اضغط على **Finish partitioning and write changes to disk**.
![[622.webp]]
5. تأكد من تحديد **Yes** للموافقة على كتابة التغييرات على القرص والشروع في تثبيت ملفات النظام.
![[614.webp]]
---

### 🖥️ الخطوة 5: اختيار الواجهة وتثبيت محمل الإقلاع (GRUB Boot Loader)

1. **Software selection:** اترُك خيارات الواجهة الرسومية الافتراضية كما هي (XFCE مع الأدوات الأساسية)، واضغط **Continue**.
![[613.webp]]
2. **Install the GRUB boot loader:** عند الوصول لشاشة تثبيت محمل الإقلاع GRUB، اختر **Yes**.
![[617.webp]]
3. حدد القرص الوهمي الرئيسي (مثل `/dev/sda`) ليتم تثبيت GRUB عليه بنجاح.
![[612.webp]]
4. عند ظهور رسالة **Installation complete**، اضغط على **Continue** ليتم إعادة تشغيل الآلة الوهمية تلقائياً.
![[621.webp]]
---

### 🎉 الخطوة 6: تسجيل الدخول والتشغيل الأول

1. بعد إعادة التشغيل، ستظهر لك واجهة الدخول الخاصة بـ Kali Linux.
2. أدخل اسم المستخدم وكلمة المرور اللذين قمت بإنشائهما في الخطوة 3.
![[611.webp]]
3. اضغط على **Log In**، ومبروك عليك! هكذا أصبحت بيئة المختبر الخاصة بك جاهزة تماماً للعمل والاستكشاف. 🚀✨
![[610.webp]]
---

🔔 **في الدرس القادم:** سنقوم باستكشاف أدوات النظام الأساسية، والتعرف على أهم الأوامر الأولى لتحديث وتجهيز بيئة العمل!

---

### 🔗 التنقل بين دروس السلسلة

- **الدرس السابق 👈:** جاري إعداد الدرس...
- **الدرس التالي 👈:** جاري إعداد الدرس السادس...

<div class='tiktok-embed-wrapper' style='display:flex;justify-content:center;margin:25px 0'>
<iframe src="https://www.tiktok.com/player/v1/7667125195303357716?autoplay=0" style="width:100%;max-width:340px;height:580px;border:none;border-radius:12px;" allow="fullscreen" loading="lazy"></iframe>
</div>

> 📹 **شاهد الشرح الكامل على TikTok:** [https://www.tiktok.com/@cyber_silicon/video/7667125195303357716?utm_campaign=tt4d_open_api&utm_source=sbawotogm6mg76anhw](https://www.tiktok.com/@cyber_silicon/video/7667125195303357716?utm_campaign=tt4d_open_api&utm_source=sbawotogm6mg76anhw)
