---
title: "[سلسلة Kali Linux - الدرس 6] أهم الخطوات الأساسية بعد تثبيت كالي لينكس"
date: 2026-10-27 04:24:31 +0200
image: https://p19-common-sign.tiktokcdn.com/tos-alisg-p-0037/ogaNcFDuVCB6qQKZKtEIWBBAoCcgSifSbqf461~tplv-tiktokx-cropcenter-q:300:400:q70.webp?dr=14782&refresh_token=b28b81fa&x-expires=1792094400&x-signature=4Hu0HPdGjtlWo%2FgPxGjEr%2FHj%2Fy4%3D&t=bacd0480&ps=933b5bde&shp=d05b14bd&shcp=8aecc5ac&idc=my2&biz_tag=tt_video&s=TIKTOK_FOR_DEVELOPER&sc=cover
description: "[سلسلة Kali Linux - الدرس 6] أهم الخطوات الأساسية بعد تثبيت كالي لينكس"
summary: "[سلسلة Kali Linux - الدرس 6] أهم الخطوات الأساسية بعد تثبيت كالي لينكس"
lang: ar
direction: rtl
comments: true
toc: true
tiktok_url: "https://www.tiktok.com/@cyber_silicon/video/7668964574950952212?utm_campaign=tt4d_open_api&utm_source=sbawotogm6mg76anhw"
---

![[سلسلة Kali Linux - الدرس 6] أهم الخطوات الأساسية بعد تثبيت كالي لينكس](https://p19-common-sign.tiktokcdn.com/tos-alisg-p-0037/ogaNcFDuVCB6qQKZKtEIWBBAoCcgSifSbqf461~tplv-tiktokx-cropcenter-q:300:400:q70.webp?dr=14782&refresh_token=b28b81fa&x-expires=1792094400&x-signature=4Hu0HPdGjtlWo%2FgPxGjEr%2FHj%2Fy4%3D&t=bacd0480&ps=933b5bde&shp=d05b14bd&shcp=8aecc5ac&idc=my2&biz_tag=tt_video&s=TIKTOK_FOR_DEVELOPER&sc=cover){: .center-image }

مرحباً بكم زوار ومتابعي **Cyber Silicon**. يُعد نظام **Kali Linux** التوزيعة القياسية الأكثر انتشاراً في اختبار الاختراق والأمن السيبراني، إلا أن الانتهاء من عملية التثبيت لا يعني أن النظام جاهز للعمل بشكل مثالي؛ حيث توجد مجموعة من الخطوات التقنية الحاسمة والتكوينات الأساسية التي يجب ضبطها لضمان استقرار النظام وتحديث مستودعاته وسلاسة بيئة سطر الأوامر (Terminal) والواجهة الرسومية (GUI).

نستعرض في هذا الدليل العملي الموسّع الخطوات الإلزامية التي تم تناولها في الدرس السادس، بدءاً من تحديث المستودعات وحل مشكلات الاتصال، وتهيئة لوحة المفاتيح، وصولاً إلى استعراض تصنيفات الأدوات وأهم الأوامر الأساسية للمبتدئين والمحترفين.

---

## 1. تحديث مستودعات النظام (Repository Update) 

أول أمر يجب تنفيذه في أي بيئة لينكس جديدة هو تحديث قواعد بيانات الحزم المتاحة. يتم ذلك عبر سطر الأوامر:
![627.webp](/assets/images/627.webp)

```bash
sudo apt update
```

سيطلب منك النظام إدخال كلمة مرور الحساب ذي الصلاحيات الإدارية (`sudo password`).

> ⚠️ **تنبيه ومعالجة مشكلة شائعة (403 Forbidden):**  
> في بعض الحالات أو النطاقات الجغرافية، قد يفشل التحديث وتظهر الرسالة التالية:  
> `403 Forbidden [IP: 104.17.254.239 80] - Failed to fetch http://http.kali.org/kali/dists/kali-rolling/InRelease`  
> هذا يعني وجود حجب أو تعذر في الوصول المباشر إلى خادم التوزيع الرسمي.

### حل مشكلة المستودعات بتغيير الخادم البديل (Mirror):
لحل هذا الخطأ، يتم توجيه النظام إلى مرآة مستودعات رسمية بديلة ومفتوحة (مثل خوادم dotsrc) عبر تنفيذ الأمر التالي دفعة واحدة:

```bash
echo "deb http://mirrors.dotsrc.org/kali kali-rolling main contrib non-free non-free-firmware" | sudo tee /etc/apt/sources.list
```

بعد تعديل ملف المستودعات بنجاح، أعد تنفيذ أمر التحديث مجدداً:

```bash
sudo apt update
```

ستلاحظ بدء تحميل فهارس الحزم  ودون أي عوائق.

---

## 2. ترقية حزم وأدوات النظام (Full System Upgrade)

بعد تحديث الفهرس، يجب ترقية كافة البرمجيات والمكتبات إلى أحدث إصداراتها لضمان سد الثغرات الأمنية واستقرار الأدوات:
![61.webp](/assets/images/61.webp)

```bash
sudo apt upgrade -y
```

```bash
# لأداء ترقية شاملة مع ضبط الحزم والاعتماديات الجديدة تلقائياً:
sudo apt dist-upgrade -y

# لحذف الحزم القديمة والمهملة التي لم يعد النظام بحاجة إليها:
sudo apt autoremove -y
```

> 💡 **ملاحظة:** تستغرق هذه العملية وقتاً يتفاوت حسب سرعة اتصالك بالإنترنت وسرعة قرص التخزين لديك؛ نظراً لأن حجم التحديثات بعد التثبيت الأولي قد يتجاوز عدة غيغابايت.

---

## 3. إعداد وتخصيص لوحة المفاتيح: إضافة اللغة العربية واختصار التبديل

تحتاج بيئة العمل إلى سهولة كتابة النصوص والملاحظات باللغة العربية، بالإضافة إلى اعتماد اختصار عالمي وسريع للتنقل بين اللغات (`Alt + Shift`).

### خطوات الإعداد من الواجهة الرسومية (XFCE Panel):
1. انقر بزر الفأرة الأيمن على الشريط العلوي (Panel) واختر **Panel** ثم **Add New Items**.
![69.webp](/assets/images/69.webp)
2. ابحث عن عنصر **Keyboard Layouts** وقم بإضافته إلى الشريط.
![616.webp](/assets/images/616.webp)
3. بالضغط بالزر الأيمن على الأيقونة المضافة واختيار **Properties**:
![615.webp](/assets/images/615.webp)
   - اضبط **Show layout as** على `system` أو `image`.
![64.webp](/assets/images/64.webp)
   - اضبط **Layout name** على `language`.
   - اضغط علي Close
4. اضغط على خيار **Keyboard settings**:
![62.webp](/assets/images/62.webp)
   - انتقل إلى تبويب **Layout**.
![626.webp](/assets/images/626.webp)
   - عطّل خيار **Use system defaults**.
   - من قائمة **Change layout option** اختر الاختصار المرغوب (مثال: `Alt + Shift`).
   - انقر على **+ Add** وابحث عن **Arabic** ثم اضغط **OK**.

الآن يمكنك التنقل بين اللغتين الإنجليزية والعربية بسلاسة عبر الضغط على `Alt + Shift`.

---

## 4. فهم تصنيفات قائمة أدوات كالي لينكس (Kali Tools Menu)

تمت إعادة هيكلة قائمة كالي لينكس لتتوافق مع مراحل اختبار الاختراق وأطر العمل التكتيكية مثل **MITRE ATT&CK**:
![624.webp](/assets/images/624.webp)

| التصنيف في القائمة | الوظيفة التقنية | أمثلة لأبرز الأدوات |
| :--- | :--- | :--- |
| **01 - Reconnaissance** | جمع المعلومات والاستطلاع | `Nmap`, `Masscan`, `theHarvester` |
| **02 - Resource Development** | إعداد الموارد وتطوير البنية التحتية | تجهيز الحمولات والشهادات |
| **03 - Initial Access** | الحصول على موطئ قدم أولي | `Social-Engineer Toolkit (SET)` |
| **04 - Execution** | تشغيل الأكواد والبرمجيات الخبيثة | `PowerShell-Empire`, `Metasploit` |
| **05 - Persistence** | الحفاظ على البقاء في النظام | `Backdoor-Factory`, `Netcat` |
| **06 - Privilege Escalation** | تصعيد الصلاحيات (PrivEsc) | `LinPEAS`, `WinPEAS` |
| **07 - Defense Evasion** | تجاوز آليات الحماية وجدران الحماية | برامج التشفير ومعدلات الحمولات |
| **08 - Credential Access** | استخراج كلمات المرور وكسر التجزئات | `Mimikatz`, `Hydra`, `John the Ripper` |
| **09 - Discovery** | استكشاف البيئة الداخلية والشبكة | أوامر الاستعلام الداخلي و `Netdiscover` |
| **10 - Lateral Movement** | التحرك الجانبي داخل الشبكة | `CrackMapExec`, `Impacket (psexec)` |
| **11 - Collection** | جمع ونهب البيانات الحساسة | أدوات استخراج قواعد البيانات و `Dumpzilla` |
| **12 - Command and Control** | إدارة قنوات الاتصال والتحكم (C2) | `Covenant`, `Sliver` |
| **13 - Exfiltration** | تهريب ونقل البيانات خارج النظام | `DNSExfiltrator` |
| **14 - Impact** | اختبار التأثير التشغيلي والتخريب المصرح | أدوات اختبار حجب الخدمة مثل `Slowloris` |
| **15/16 - Services & Other Tools** | إدارة الخدمات وقواعد البيانات المساعدة | خدمات `Apache2`, `MySQL/MariaDB` |

---

## 5. مرجع موسّع: أهم أوامر لينكس الأساسية مع أمثلة عملية

لإتقان التعامل مع النظام عبر الشاشة الطرفية (Terminal)، إليك جدولاً يضم الأوامر التي لا غنى عنها لكل ممارس أمن سيبراني:

### أولاً: إدارة الملفات والمجلدات (File Management)
```bash
# عرض الملفات مع كامل التفاصيل والملفات المخفية
ls -lah

# الانتقال إلى مسار معين
cd /var/www/html/

# إنشاء مجلد جديد
mkdir -p projects/cyber_silicon

# إنشاء ملف نصي فارغ
touch scan_results.txt

# قراءة محتوى ملف وعرضه في سطر الأوامر
cat /etc/passwd

# قراءة أول 10 أسطر من الملف
head -n 10 scan_results.txt

# مراقبة السجلات الحية لملف يتم التعديل عليه باستمرار
tail -f /var/log/auth.log

# البحث عن ملف بالاسم داخل كامل النظام
find / -name "id_rsa" 2>/dev/null
```

### ثانياً: إدارة المستخدمين والصلاحيات (Users & Permissions)
```bash
# إنشاء مستخدم جديد في النظام
sudo adduser analyst

# منح المستخدم الجديد صلاحيات المسؤول الكاملة (Sudo)
sudo usermod -aG sudo analyst

# معرفة اسم المستخدم الحالي
whoami

# تعديل صلاحيات ملف (قراءة، كتابة، تشغيل)
chmod 700 exploit.sh

# تغيير ملكية الملف لمستخدم محدد
sudo chown analyst:analyst exploit.sh
```

### ثالثاً: الشبكات والاستطلاع السريع (Networking & Recon)
```bash
# استعراض عناوين الـ IP لبطاقات الشبكة
ip a

# فحص المنافذ المفتوحة والخدمات المتصلة محلياً
ss -tulnp

# اختبار الاتصال بهدف محدد عبر بروتوكول ICMP
ping -c 4 192.168.1.1

# فحص المنافذ والخدمات لهدف محدد باستخدام Nmap
nmap -sV -sC 192.168.1.100

# تنزيل ملف أو أداة عبر الرابط مباشرة
wget https://example.com/tool.tar.gz

# فحص سجلات نطاق محدد عبر خوادم DNS
dig example.com ANY
```

### رابعاً: الأرشفة، والعمليات، وإدارة النظام (Processes & System)
```bash
# فحص استهلاك الذاكرة العشوائية (RAM) بشكل مفهوم
free -h

# فحص المساحة المتبقية على الأقراص
df -h

# عرض كافة العمليات النشطة واستهلاكها
ps aux | grep python

# إيقاف عملية معينة بالقوة باستخدام معرف العملية (PID)
kill -9 1234

# ضغط مجلد بصيغة tar.gz
tar -czvf backup.tar.gz /home/analyst/data/

# فك ضغط أرشيف tar.gz
tar -xzvf backup.tar.gz
```

---

## 6. روابط التحميل والمصادر المرفقة

للحصول على نسخة الـ PDF الشاملة من دليل أوامر كالي لينكس الأساسية والمقدمة من **Cyber Silicon Labs** كما عُرض في الفيديو، يمكنكم الوصول إلى ملف التحميل المباشر عبر الرابط التالي:

🔗 **رابط التحميل المباشر:** [مجلد ملفات كالي لينكس - MediaFire](https://www.mediafire.com/folder/o2mnxtdnno6an/kali)

---

## خلاصة وتوصيات ختامية

تثبيت Kali Linux هو مجرد خطوة تمهيدية؛ إن ضبط الخوادم السريعة والمستقرة، وتفعيل التحديثات الدورية، وتكوين بيئة الإدخال واللغات، وفهم هيكلية أدوات اختبار الاختراق المتوافقة مع أطر عمل الأمن السيبراني الحديثة يُمثل الأساس الصلب لبناء مهارات احترافية متقدمة. احرص دائماً على عدم تثبيت أدوات عشوائية غير موثوقة، واعتمد على الأوامر النظامية والتحديثات الرسمية للحفاظ على استقرار نظامك.

---
### 🔗 التنقل بين دروس السلسلة
* **الدرس السابق 👈:** تلقائي
* **الدرس التالي 👈:** جاري إعداد الدرس...

<div class='tiktok-embed-wrapper' style='display:flex;justify-content:center;margin:25px 0'>
<iframe src="https://www.tiktok.com/player/v1/7668964574950952212?autoplay=0" style="width:100%;max-width:340px;height:580px;border:none;border-radius:12px;" allow="fullscreen" loading="lazy"></iframe>
</div>

> 📹 **شاهد الشرح الكامل على TikTok:** [https://www.tiktok.com/@cyber_silicon/video/7668964574950952212?utm_campaign=tt4d_open_api&utm_source=sbawotogm6mg76anhw](https://www.tiktok.com/@cyber_silicon/video/7668964574950952212?utm_campaign=tt4d_open_api&utm_source=sbawotogm6mg76anhw)
