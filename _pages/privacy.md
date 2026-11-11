---
layout: page
title: سياسة الخصوصية
description: سياسة الخصوصية لموقع Cyber Silicon وبرنامج Cyber Silicon Pro المكتبي، بما في ذلك البيانات المحلية وتكاملات المنصات والذكاء الاصطناعي وطلبات الحذف.
permalink: /privacy/
---

آخر تحديث: 12 نوفمبر 2026

تشرح هذه السياسة كيفية تعامل **Cyber Silicon** مع المعلومات عند زيارة الموقع، أو استخدام برنامج **Cyber Silicon Pro** المكتبي، أو ربط البرنامج بخدمات خارجية مثل Facebook وBlogger وTelegram وGitHub وTikTok ومزوّدي الذكاء الاصطناعي.

نحن نحاول تقليل البيانات التي نحتاج إليها، ونوضح متى تبقى البيانات على جهازك ومتى تُرسل إلى خدمة اخترت ربطها. تنطبق هذه السياسة على الإصدارات الحالية من الموقع والبرنامج، وقد تُحدّث إذا تغيرت الوظائف أو طرق معالجة البيانات.

**زوار الموقع:** الموقع صفحات ثابتة مستضافة عبر GitHub Pages ولا يتطلب حساباً لقراءة المحتوى. تحفظ بعض وظائف المتصفح تفضيلات مثل اختيار المظهر والمقالات المحفوظة في التخزين المحلي للمتصفح على جهازك. قد تعالج بنية استضافة GitHub بيانات تقنية لازمة لتقديم الصفحات وحمايتها، مثل عنوان IP وبيانات المتصفح والصفحة المطلوبة ووقت الطلب، وفق سياسة GitHub. وعند تحميل الخطوط من Google Fonts، يتصل المتصفح بخوادم Google وقد تتلقى Google بيانات الاتصال التقنية المعتادة لذلك الطلب. لا ننشئ حالياً قاعدة حسابات للزوار على الموقع.

## 1. من يدير الخدمة وكيف تعمل؟

Cyber Silicon موقع تقني، وCyber Silicon Pro برنامج مكتبي يعمل محلياً على جهاز المستخدم. البرنامج ليس خدمة حسابات سحابية مركزية؛ لا يحتاج استخدامه المعتاد إلى إنشاء حساب لدى خادم تديره Cyber Silicon، ولا توجد قاعدة بيانات مركزية لدى Cyber Silicon تُزامن إليها ملفات المستخدم ومفاتيح API تلقائياً.

تُحفظ ملفات العمل والإعدادات والبيانات التشغيلية محلياً، عادةً في مجلد البرنامج أو في المجلد الذي يحدده المستخدم عبر إعداد `CYBER_SILICON_HOME`. لكن البرنامج يتصل بخدمات خارجية عندما يفعّل المستخدم تكاملاً أو يطلب تنفيذ مهمة تحتاج تلك الخدمة. عندها تخضع البيانات المرسلة أيضاً لسياسة وشروط مزوّد الخدمة المعني.

## 2. المعلومات التي قد يعالجها البرنامج

بحسب الميزات التي يفعّلها المستخدم، قد يعالج Cyber Silicon Pro الفئات التالية:

- **بيانات الحسابات والاتصالات:** معرّفات صفحات Facebook، ومعرّف مدونة Blogger، ومعرّفات محادثات Telegram، ومعرّفات قنوات TikTok أو Buffer، واسم مستودع GitHub والفرع المحدد.
- **بيانات النشر والمحتوى:** عناوين المقالات ونصوصها ووصفها ووسومها وروابطها وصورها وفيديوهاتها والملفات التي يختار المستخدم استيرادها أو نشرها.
- **بيانات التعليقات والمحادثات:** نص التعليق أو السؤال، واسم العرض أو معرّف صاحبه عندما توفره المنصة، ومعرّف المنشور والتعليق الأب والرد، وبيانات الإشارة إلى الصفحة، وحالة الإرسال أو الإشراف. تُستخدم هذه البيانات لعرض صندوق الوارد وتحليل التعليقات وإعداد الردود عند تفعيل ذلك.
- **بيانات التحليلات والمزامنة:** الأرقام والحالات التي تعيدها المنصة، مثل حالة المنشور أو جدولته أو بيانات الفيديو المتاحة عبر التكامل.
- **بيانات مكتبة المعرفة:** الملفات التي يستوردها المستخدم، والنصوص المستخرجة منها، وبياناتها الوصفية، ومقاطع الفهرسة المحلية ونتائج الاسترجاع.
- **بيانات الإعدادات والتشخيص:** تفضيلات اللغة والمظهر والجدولة، وإعدادات المهام، وإصدار البرنامج وPython ونظام التشغيل والمعمارية، ومعرّفات المهام وأحداثها ومددها وأنواع الأخطاء وملخصاتها.

لا يحتاج البرنامج إلى كلمة مرور Facebook أو Google أو TikTok لقراءتها من المستخدم. يستخدم بيانات التفويض أو الرموز التي يضيفها المستخدم أو يحصل عليها من مسار التفويض المدعوم، ولا ينبغي إرسال كلمات المرور أو الرموز إلى فريق Cyber Silicon عبر البريد أو قنوات الدعم.

## 3. أين تُخزّن البيانات محلياً؟

قد ينشئ البرنامج أو يستخدم المجلدات والملفات التالية على جهازك:

- `.env` و`credentials/` لبيانات الاعتماد وملفات OAuth والرموز.
- `queue/` و`archived/` للمقالات والملفات التي يديرها المستخدم.
- `data/` للإعدادات التشغيلية وحالات النشر والتعليقات وفهرس مكتبة المعرفة.
- `logs/` لسجلات التشغيل والتشخيص.
- مجلدات أخرى للميديا المؤقتة أو الملفات التي يحددها المستخدم.

تُقيّد بعض ملفات الأسرار والرموز بصلاحيات نظام الملفات (مثل `0600` على الأنظمة التي تدعم ذلك). هذا إجراء لتقليل وصول المستخدمين الآخرين على الجهاز، وليس تشفيراً كاملاً للملفات. يجب حماية حساب نظام التشغيل والقرص والنسخ الاحتياطية.

تستبعد النسخ الاحتياطية التي ينشئها البرنامج ملفات `.env` و`credentials/` وجلسات المتصفح ورموز OAuth والمفاتيح الخاصة بحسب مسار النسخ الاحتياطي. احتفظ بهذه الأسرار بصورة منفصلة وآمنة، ولا تضعها في مستودع عام.

## 4. متى تُرسل البيانات إلى خدمات خارجية؟

لا تُرسل كل الملفات المحلية إلى الإنترنت تلقائياً. تُرسل البيانات التي تتطلبها الوظيفة عندما يفعّل المستخدم التكامل أو يطلب العملية، مثل:

| الخدمة أو المزوّد | أمثلة على البيانات والغرض |
|---|---|
| **Meta / Facebook Graph API** | معرّف الصفحة ورمز الوصول، والمحتوى أو الوسائط التي يختار المستخدم نشرها، والتعليقات والردود ومعرّفاتها وبيانات السلسلة اللازمة لإدارة صندوق الوارد والردود. |
| **Google Blogger API وGoogle OAuth** | معرّف المدونة وبيانات التفويض والمقالات والتعليقات والردود التي يطلب المستخدم إدارتها أو نشرها. |
| **Google Gemini API** | النصوص والأسئلة والمقالات أو التعليقات والسياق والملفات أو الصور/الفيديو التي يختار المستخدم معالجتها بميزات Gemini. |
| **OpenAI API** | المطالبات والنصوص والمحتوى الذي يختاره المستخدم لمهام ChatGPT عبر OpenAI Platform API. وفي مسار تحويل الفيديو إلى مقال المرئي عبر ChatGPT، تُستخرج إطارات مرئية وتُرسل إلى النموذج؛ لا يستخرج هذا المسار الصوت ولا يرسله. |
| **Ollama** | في الإعداد الافتراضي يتصل البرنامج بخدمة Ollama المحلية على `127.0.0.1`. تُرسل إليها المدخلات اللازمة للتوليد أو التضمين محلياً. لا تُرسل هذه المدخلات إلى مزوّد سحابي عبر Ollama ما دام الخادم والنموذج محليين. |
| **Telegram Bot API** | رسائل البوت وإجابات Q&A والرسائل التي يطلب المستخدم نشرها إلى معرّفات المحادثات المحددة. إذا اختير مزوّد ذكاء اصطناعي سحابي لسؤال Telegram، يُرسل نص السؤال والسياق اللازم لذلك المزوّد أيضاً. |
| **GitHub API** | ملفات المقالات أو المحتوى الذي يختار المستخدم نشره إلى المستودع، وبيانات المستودع والفرع، وطلبات التحقق من التحديثات عند تفعيلها. |
| **TikTok وBuffer** | بيانات التفويض، والوسائط والتعليقات والوصف وبيانات الجدولة أو المزامنة التي تتطلبها الميزة المختارة. |
| **Filebase / IPFS** | الملفات والبيانات الوصفية التي يختار المستخدم رفعها إلى خدمة التخزين هذه عند تفعيل التكامل. |
| **GitHub Pages وGoogle Fonts** | يستضيف GitHub صفحات الموقع؛ وقد يتصل متصفح الزائر بخدمة Google Fonts لتحميل الخطوط. |

قد تحتفظ هذه الجهات ببيانات الطلبات أو المحتوى وفق إعدادات الحساب وشروطها وسياسات الخصوصية الخاصة بها. لا يتحكم Cyber Silicon في مدد احتفاظها أو ممارساتها المستقلة.

## 5. مزوّدو الذكاء الاصطناعي ومكتبة المعرفة

يمكن للمستخدم اختيار Ollama المحلي أو مزوّد سحابي متاح في إعداداته، مثل Gemini أو OpenAI للمهام المدعومة. عندما يختار مزوّداً سحابياً، يُرسل إلى ذلك المزوّد نص المهمة والمحتوى الضروري لتنفيذها، مثل نص تعليق يراد تحليله أو مسودة يراد تحريرها أو مادة مرئية اختار المستخدم تحليلها.

يتضمن البرنامج إعدادات خصوصية تتحكم في إدراج سياق أو مقتطفات مسترجعة من مكتبة المعرفة المحلية ضمن بعض مهام الذكاء الاصطناعي السحابي. **القيم الافتراضية الحالية تسمح بهذا السياق**، ويمكن للمستخدم إيقاف السماح العام أو تعطيل مشاركة سياق المراجع لمهام محددة من إعدادات الخصوصية. تعطيل هذا الخيار لا يعني أن كل بيانات المهمة أصبحت محلية؛ يجب أيضاً اختيار Ollama المحلي بدلاً من مزوّد سحابي إذا كان المطلوب عدم إرسال نص المهمة إلى مزوّد خارجي.

يجب ألا يضيف المستخدم كلمات مرور أو رموز وصول أو معلومات شديدة الحساسية إلى المطالبات أو الملفات المرسلة إلى مزوّد ذكاء اصطناعي، إلا إذا كان لديه أساس وصلاحية واضحة لذلك. تخضع معالجة كل مزوّد سحابي لسياساته وشروط واجهة API التي يستخدمها المستخدم.

## 6. السجلات والتشخيص

ينشئ البرنامج سجلات تشخيص محلية لمساعدة المستخدم في تتبع المهام والأخطاء. قد تتضمن هذه السجلات وقت الحدث، وإصدار البرنامج، وإصدار Python، ونظام التشغيل، واسم الصفحة أو المهمة، ومعرّف المهمة، والحالة، والمدة، ونوع الخطأ وملخصه.

تستبعد آلية التشخيص حقولاً غير مسموح بها وتحاول تنقيح الرموز والأسرار المعروفة قبل تسجيل الملخصات. تُحفظ السجلات محلياً ولا يعني إنشاؤها إرسالها تلقائياً إلى Cyber Silicon. قد يختار المستخدم تصدير تقرير تشخيص ومشاركته مع فريق الدعم؛ راجع التقرير واحذف أي معلومات لا تريد مشاركتها قبل إرساله.

فترة الاحتفاظ الافتراضية لسجلات جلسات التشخيص هي 30 يوماً، ويمكن تعديلها من إعدادات التشخيص. ويمكن للمستخدم حذف السجلات المحلية يدوياً.

## 7. المشاركة والبيع والإعلانات

لا يبيع Cyber Silicon بيانات المستخدمين. ولا تُرسل ملفات المستخدم المحلية إلى Cyber Silicon لمجرد تشغيل البرنامج. تتم مشاركة البيانات مع مزوّدي الخدمات الخارجيين عندما تكون لازمة للتكامل الذي اختاره المستخدم أو لتنفيذ طلبه، أو عندما يشارك المستخدم بنفسه تقريراً أو محتوى مع فريق الدعم، أو عندما يفرض القانون ذلك.

قد يؤدي النشر أو الرد على تعليق إلى إظهار النص أو الوسائط للجمهور وفق إعدادات المنصة والحساب. راجع المحتوى والوجهة قبل تنفيذ أي إجراء عام.

## 8. الاحتفاظ والحذف

تظل ملفات العمل والإعدادات والرموز والسجلات المحلية على جهاز المستخدم إلى أن يحذفها المستخدم أو يزيل البرنامج أو يغيّر موقع التخزين. أما البيانات التي أُرسلت إلى Meta أو Google أو Telegram أو GitHub أو TikTok أو Buffer أو مزوّد ذكاء اصطناعي فتخضع أيضاً لسجلات ونسخ واحتفاظ تلك الخدمات.

يمكن للمستخدم:
- حذف مصادر مكتبة المعرفة من داخل البرنامج حيث تتوفر وظيفة الحذف.
- فصل التكامل أو إلغاء التفويض وحذف بيانات الاعتماد المحلية.
- حذف السجلات والبيانات المحلية أو مجلدات المقالات بحسب ما يريد الاحتفاظ به.
- طلب حذف أي معلومات شخصية أرسلها إلى Cyber Silicon مباشرة عبر البريد الإلكتروني.

توجد تعليمات مفصلة للحذف المحلي وطلب الحذف من فريق Cyber Silicon في صفحة [طلبات حذف البيانات](/data-deletion/).

## 9. حقوق المستخدم وطلبات الخصوصية

يمكنك طلب معرفة ما إذا كنت قد أرسلت معلومات شخصية مباشرة إلى Cyber Silicon، أو طلب تصحيحها أو حذفها، عبر:

- البريد الإلكتروني: [mylif2021@gmail.com](mailto:mylif2021@gmail.com?subject=Cyber%20Silicon%20Privacy%20Request)
- صفحة التعليمات: [طلبات حذف البيانات](/data-deletion/)

اذكر الخدمة أو الحساب المعني، ونوع البيانات المطلوب التعامل معها، وأي تفاصيل تساعدنا على تحديدها. لا ترسل كلمات مرور أو رموز وصول أو مفاتيح API أو ملفات `.env`.

لأن البرنامج يخزن بياناته محلياً ولا يملك Cyber Silicon وصولاً عن بُعد إلى جهازك، لا نستطيع حذف الملفات من جهازك نيابة عنك. كما لا يمكننا حذف نسخة تحتفظ بها Meta أو Google أو أي مزوّد آخر نيابة عنه؛ يجب تقديم طلب الحذف إلى ذلك المزوّد وفق إجراءاته.

## 10. أمن المعلومات

نستخدم في البرنامج إجراءات مثل حفظ الملفات بصورة ذرية، وتقييد صلاحيات بعض ملفات الأسرار، وتنقيح بيانات الاعتماد من سجلات التشخيص. ومع ذلك، لا يوجد نظام تخزين أو نقل خالٍ تماماً من المخاطر. المستخدم مسؤول عن تحديث نظامه، وحماية جهازه، وتأمين النسخ الاحتياطية، وعدم مشاركة بيانات الاعتماد.

إذا اشتبهت في كشف رمز أو مفتاح، ألغِه أو دوّره من الخدمة التي أصدرته، ثم حدّث بيانات الاعتماد المحلية.

## 11. الأطفال

البرنامج أدوات مكتبية لإدارة المحتوى والحسابات والتكاملات التقنية، وليس موجهاً للأطفال. يجب على من يستخدمه الالتزام بشروط العمر والخدمات الخارجية والقوانين المنطبقة عليه.

## 12. التغييرات والتواصل

قد نحدّث هذه السياسة عند إضافة ميزات أو تغيير مزوّدي الخدمة أو طرق التخزين. سنغيّر تاريخ التحديث أعلى الصفحة عند نشر تعديل جوهري. النسخة المنشورة هنا هي المرجع الحالي.

للاستفسارات المتعلقة بالخصوصية: [mylif2021@gmail.com](mailto:mylif2021@gmail.com).

---

# English — Privacy Policy Summary and Key Disclosures

**Last updated: 12 November 2026**

This policy covers the Cyber Silicon website and the Cyber Silicon Pro desktop application.

**Website visitors:** The website is a static GitHub Pages site and does not require an account to read. Some browser features store preferences such as theme selection and saved articles in local browser storage on your device. GitHub's hosting infrastructure may process technical request data needed to serve and protect the site, such as IP address, browser information, requested page, and request time, under GitHub's policies. Loading fonts through Google Fonts causes the browser to connect to Google, which may receive the technical connection data normally associated with that request. The site does not currently operate a visitor account database.

## Product and storage model

Cyber Silicon Pro is a local desktop application, not a centrally hosted user-account service. In normal use, drafts, media, settings, credentials, publishing state, knowledge-library files, and diagnostic logs are stored on the user's device, usually under the application directory or the directory configured through `CYBER_SILICON_HOME`.

The application does not automatically upload all local files to Cyber Silicon. It connects to third-party services when a user configures an integration or requests a feature that requires that service.

## Data categories

Depending on enabled features, the application may process:

- Account and destination identifiers, such as Facebook Page IDs, Blogger Blog IDs, Telegram chat IDs, TikTok/Buffer channel identifiers, and GitHub repository and branch names.
- Drafts, article text, titles, captions, links, images, videos, and files selected for import, analysis, or publishing.
- Comment and conversation text, display names or user identifiers supplied by a platform, post and parent-comment identifiers, mention metadata, reply identifiers, and moderation or delivery status.
- Platform synchronization and analytics information returned by connected services.
- User-imported knowledge documents, extracted text, metadata, local indexes, and retrieved passages.
- Application preferences and local diagnostic metadata, such as app/Python/OS versions, task IDs, event status, duration, error type, and sanitized error summaries.

## Third-party services and disclosures

When the relevant feature is used, data may be sent to:

- **Meta / Facebook Graph API** for Page publishing, media, comments, threaded replies, and Page-related metadata.
- **Google Blogger API and Google OAuth** for blog content, comments, replies, and authorization.
- **Google Gemini API** for prompts, selected text, comments, documents, images, or video material required by the selected Gemini feature.
- **OpenAI API** for prompts and user-selected content used by supported OpenAI features. The visual ChatGPT video-to-article route extracts and sends visual frames; it does not extract or send audio in that route.
- **Ollama**, which uses a local endpoint by default at `127.0.0.1`; model inputs remain on the local machine when the Ollama service and model are local.
- **Telegram Bot API** for messages, bot answers, and configured publishing destinations.
- **GitHub API** for content that the user chooses to publish, repository metadata, and update checks.
- **TikTok and Buffer** for authorization, selected media, captions, scheduling, synchronization, and available analytics.
- **Filebase / IPFS** for files and metadata the user chooses to upload when that integration is enabled.
- **GitHub Pages and Google Fonts** for hosting this website and loading its fonts.

Third-party services process data under their own terms, privacy policies, and account settings. Cyber Silicon does not control their independent retention practices.

## AI providers and knowledge context

Users can select a local or cloud AI provider for supported tasks. When a cloud provider is selected, the task prompt and the content needed for that task may be sent to that provider.

The application currently enables cloud reference context by default. This means relevant passages retrieved from the local knowledge library may be included in certain cloud AI requests. Users can disable the general cloud-reference setting or disable it for individual supported tasks in the application's privacy settings. Disabling reference context does not make a cloud-routed prompt local; select local Ollama for tasks that must remain on the device.

Do not submit passwords, access tokens, API keys, or highly sensitive information to an AI provider unless you have a clear lawful basis and authorization to do so.

## Local credentials and security

Credentials and tokens are stored locally in supported secret/configuration locations such as `.env` and `credentials/`. Some files are written with restrictive filesystem permissions (for example, `0600` on supported systems); this is not full-disk encryption. Application backups exclude key credential files and browser/OAuth secrets according to the backup implementation.

## Diagnostics and retention

Diagnostic logs are stored locally and may include timestamps, application and environment versions, task identifiers, event status, duration, error types, and sanitized error summaries. Their creation does not automatically send them to Cyber Silicon. Users may choose to export and share a report after reviewing it. The default diagnostic-session retention period is 30 days and can be changed in settings.

## Deletion and user requests

Users can remove local knowledge sources, disconnect integrations, revoke credentials with the relevant provider, and delete local application files. Full local deletion instructions are available at [Data Deletion Requests](/data-deletion/).

To request deletion or correction of information that you sent directly to Cyber Silicon, contact **mylif2021@gmail.com**. Include the relevant service/account and the data concerned, but never send passwords, access tokens, API keys, or `.env` files.

Cyber Silicon cannot remotely erase files from a user's device and cannot delete data held independently by Meta, Google, Telegram, GitHub, TikTok, Buffer, OpenAI, or other providers on the user's behalf. Such requests must also be made to the relevant provider.

## Contact and updates

Privacy requests: [mylif2021@gmail.com](mailto:mylif2021@gmail.com).

This policy may be updated when application features, providers, or data practices change. The published version is the current policy.
