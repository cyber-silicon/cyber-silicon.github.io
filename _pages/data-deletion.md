---
layout: page
title: طلبات حذف البيانات
description: تعليمات حذف بيانات Cyber Silicon Pro المحلية وطلب حذف المعلومات المرسلة إلى Cyber Silicon أو إلغاء ربط الخدمات الخارجية.
permalink: /data-deletion/
---

آخر تحديث: 12 نوفمبر 2026

توضح هذه الصفحة كيفية طلب حذف البيانات المرتبطة بموقع Cyber Silicon وبرنامج Cyber Silicon Pro. يمكن الوصول إلى هذه التعليمات دون تسجيل الدخول، وهي مخصصة أيضاً لمن يحتاج إلى رابط تعليمات حذف البيانات في إعدادات تطبيق Meta.

## 1. حذف البيانات المحلية من Cyber Silicon Pro

Cyber Silicon Pro برنامج مكتبي يخزن معظم بياناته التشغيلية على جهاز المستخدم. لا يستطيع Cyber Silicon حذف ملفات جهازك عن بُعد؛ نفّذ الخطوات التالية على الجهاز الذي ثبّت عليه البرنامج:

1. أوقف البرنامج بالكامل.
2. افتح مجلد البرنامج أو مجلد البيانات الذي حددته عبر المتغير `CYBER_SILICON_HOME`. إذا لم تحدد هذا المتغير، فابحث في مجلد تثبيت/تشغيل البرنامج.
3. احذف البيانات التي تريد إزالتها. بحسب استخدامك، قد تشمل:
   - `.env` و`credentials/`: مفاتيح API وملفات OAuth ورموز الوصول وبيانات ربط الخدمات.
   - `data/`: حالات النشر والتعليقات والإعدادات التشغيلية وفهرس مكتبة المعرفة.
   - `logs/`: سجلات التشغيل والتشخيص.
   - `queue/` و`archived/`: المقالات والمسودات والملفات التي يديرها البرنامج.
   - مجلدات النسخ الاحتياطية أو الوسائط المؤقتة التي أنشأتها أو اخترت استخدامها.
4. إذا أردت حذف البرنامج وبياناته بالكامل، أزل التطبيق ومجلد بياناته بعد التأكد من أنك لا تحتاج إلى المقالات أو الوسائط أو النسخ الاحتياطية الموجودة فيه.

**تنبيه:** حذف `queue/` أو `archived/` أو `data/` قد يزيل مقالاتك وملفاتك وسجل النشر نهائياً. احتفظ بنسخة من المحتوى الذي تريد إبقاءه قبل الحذف. حذف ملفاتك المحلية لا يحذف المنشورات أو الرسائل أو التعليقات التي سبق إرسالها إلى المنصات الخارجية.

يمكنك أيضاً حذف مصادر مكتبة المعرفة من واجهة البرنامج حيث تتوفر وظيفة الحذف، أو فصل التكامل وحذف بيانات اعتماده المحلية من إعداداتك.

## 2. إلغاء ربط الخدمات الخارجية

إزالة بيانات الاعتماد من جهازك لا تلغي بالضرورة التفويض أو النسخ التي تحتفظ بها الخدمة الخارجية. راجع إعدادات كل مزوّد على حدة:

- **Meta / Facebook:** أزل التطبيق أو التكامل التجاري من إعدادات الحساب أو الأعمال إذا كان ظاهراً ضمن التطبيقات المتصلة، وألغِ صلاحياته أو رموز الوصول من Meta. احذف أيضاً بيانات صفحة Facebook المحلية من البرنامج.
- **Google / Blogger:** أزل وصول التطبيق من صفحة [صلاحيات حساب Google](https://myaccount.google.com/permissions)، واحذف ملفات OAuth المحلية إذا لم تعد تريد استخدامها.
- **Telegram:** أوقف البوت أو أزله من المحادثة/المجموعة التي أضفته إليها، ودوّر Bot Token إذا لزم، ثم احذف الرمز المحلي.
- **GitHub:** ألغِ تفويض التطبيق أو الرمز من إعدادات Developer settings / Applications في حساب GitHub، واحذف الرمز المحلي.
- **TikTok وBuffer:** أزل التطبيق أو القناة من إعدادات التطبيقات المتصلة في الحساب المعني، ثم احذف رموز الوصول المحلية.
- **Gemini / Google وOpenAI:** راجع حساب الخدمة وسجل النشاط أو إعدادات البيانات لدى المزوّد، وقدّم طلب حذف إليه إذا كنت تريد إزالة طلبات أو ملفات سبق إرسالها.
- **Filebase / IPFS:** راجع حساب Filebase أو مزوّد التخزين الذي استخدمته لحذف الملفات أو إلغاء بيانات الاعتماد، مع الانتباه إلى أن البيانات المنشورة على IPFS قد تكون موزعة ولا يمكن ضمان إزالة كل نسخة من الشبكة بمجرد حذف الملف المحلي.

قد تختلف أسماء القوائم وخطوات الإلغاء باختلاف نوع الحساب وإصدار واجهة المزوّد.

## 3. طلب حذف معلومات أرسلتها مباشرة إلى Cyber Silicon

إذا أرسلت معلومات شخصية إلى Cyber Silicon عبر البريد أو الدعم، يمكنك طلب حذفها أو تصحيحها:

- البريد: [mylif2021@gmail.com](mailto:mylif2021@gmail.com?subject=Data%20Deletion%20Request%20-%20Cyber%20Silicon%20Pro)
- الموضوع المقترح: `Data Deletion Request - Cyber Silicon Pro`

اذكر:
- الخدمة أو التكامل المعني.
- الحساب أو الصفحة أو المدونة المعنية، باستخدام معرّف أو اسم عام عند الحاجة.
- نوع البيانات التي تريد حذفها.
- أي تفاصيل زمنية أو مرجع يساعد على العثور على المعلومات.

لا ترسل كلمة مرور أو Page Access Token أو OAuth Token أو API Key أو ملف `.env` أو أي سرّ آخر. قد نطلب معلومات محدودة للتحقق من أن الطلب صادر عن الشخص المعني.

بما أن البرنامج يعمل محلياً ولا يرسل ملفات المستخدم تلقائياً إلى خادم مركزي تديره Cyber Silicon، فإن طلب البريد لا يمنحنا وصولاً إلى جهازك ولا يمكنه حذف الملفات المحلية أو البيانات التي تحتفظ بها المنصات الخارجية. استخدم خطوات الحذف المحلية واطلب الحذف من المزوّد المعني أيضاً.

## 4. ماذا يحدث بعد تقديم الطلب؟

سنراجع الطلب ونوضح ما إذا كانت المعلومات المطلوبة موجودة لدينا مباشرة، أو ما إذا كان حذفها يتطلب إجراءً من المستخدم أو من مزوّد خارجي. لا نعد بحذف نسخة تحتفظ بها منصة أخرى نيابةً عنها، ولا نطلب منك مشاركة أسرار الدخول لإثبات ملكية الحساب.

للاطلاع على أنواع البيانات والمزوّدين وأغراض المعالجة، راجع [سياسة الخصوصية](/privacy/).

---

# English — Data Deletion Instructions

**Last updated: 12 November 2026**

These instructions explain how to remove Cyber Silicon Pro data and request deletion of information sent directly to Cyber Silicon.

## Delete local application data

1. Fully close Cyber Silicon Pro.
2. Locate the application directory or the data directory configured through `CYBER_SILICON_HOME`. If that variable is not set, use the application's installation/runtime directory.
3. Delete the categories you want to remove:
   - `.env` and `credentials/`: API keys, OAuth files, access tokens, and integration credentials.
   - `data/`: publishing/comment state, settings, and the local knowledge index.
   - `logs/`: local diagnostics and application logs.
   - `queue/` and `archived/`: drafts, articles, and managed media.
   - Any user-selected backup or temporary-media folders.
4. To remove all local application data, uninstall the application and remove its data directory after saving any articles, media, or backups you want to keep.

Deleting `queue/`, `archived/`, or `data/` may permanently remove your own content and publishing history. Local deletion does not remove posts, messages, comments, or files already sent to external platforms.

## Disconnect third-party services

Revoke or remove the integration with the relevant provider, then delete the corresponding local credentials:

- Meta / Facebook: remove the connected app/business integration or revoke its permissions/tokens in Meta settings.
- Google / Blogger: remove app access from [Google Account permissions](https://myaccount.google.com/permissions).
- Telegram: stop or remove the bot from chats/groups and rotate its bot token if needed.
- GitHub: revoke the relevant app authorization or token in GitHub Developer settings.
- TikTok / Buffer: disconnect the app or channel from the provider account.
- Gemini / OpenAI: review the relevant provider account's data controls and submit deletion requests there for prompts or files previously sent.
- Filebase / IPFS: delete hosted files and revoke credentials through the storage provider. Distributed IPFS copies may not be fully retractable once published.

Provider menus and retention practices may change. Follow the provider's current instructions.

## Request deletion from Cyber Silicon

To request deletion or correction of personal information you sent directly to Cyber Silicon, email **mylif2021@gmail.com** with the subject:

`Data Deletion Request - Cyber Silicon Pro`

Identify the relevant service/account and the information you want deleted. Do not send passwords, access tokens, API keys, OAuth secrets, or `.env` files.

Cyber Silicon Pro stores its operational data locally and does not automatically upload all user files to a Cyber Silicon-operated central server. Cyber Silicon cannot remotely delete files on your device or erase data held independently by Meta, Google, Telegram, GitHub, TikTok, Buffer, OpenAI, or another provider. You must also use the relevant provider's deletion process.

For details about data categories and processing, see the [Privacy Policy](/privacy/).
