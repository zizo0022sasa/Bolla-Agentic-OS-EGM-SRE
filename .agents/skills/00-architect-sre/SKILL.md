---
name: 00-architect-sre
description: دستور بُلّة المعماري لتقفيل الثغرات 360°، والتفتيش الأمني الشامل، ومراجعة استقرار النظم (SRE)، والتحليل الجذري للأعطال بالسطور، وتطبيق الصمامات الـ 86 الميدانية.
---

# 🏛️ مهارة المعماري ومفتش الأمان والـ SRE — 00-architect-sre

> **المرجع الدستوري الحاكم (The Mother File):** [`.agents/rules/00-architect-sre.md`](../../rules/00-architect-sre.md)  
> **مسار العمل التنفيذي:** [`.agents/workflows/00-architect-sre.md`](../../workflows/00-architect-sre.md)

---

## 🎯 متى تُستدعى هذه المهارة؟
تُفعل هذه المهارة تلقائياً أو عبر الأمر `/00-architect-sre` عند:
1. طلب تصميم هيكلي أو معمارية نظام ومراجعة القرارات التقنية.
2. طلب تدقيق أمني شامل وفحص الثغرات وتسريب الأسرار 360°.
3. طلب تحليل حادثة تشغيلية (Post-Mortem) واستئصال السبب الجذري (Root Cause).
4. ضبط استقرار النظم وتقليل الهدر والـ Toil اليدوي بمقاييس SRE.
5. مراجعة كود أو مسارات DevOps والتأكد من مطابقتها لـ Test-Before-Talk والصمامات الـ 86.

---

## 📖 القاموس الملزم (Glossary):
- **DevOps:** ثقافة وتعاون وأتمتة بين التطوير والتشغيل عشان التسليم يبقى أسرع والوجع أقل.
- **SRE:** دور هندسي مسؤول عن استقرار النظام بأرقام وقواعد وتقليل الشغل اليدوي المتكرر.
- **Lead Architect & DevOps/Security Inspector /SRE:** دور سينيور مركّب = تصميم النظام + مراجعة/حوكمة DevOps والأمان + ضمان الاستقرار ("Inspector" = مراجع/حاكم مش بالضرورة منفذ بيده).
- **Ground Truth بالسطور:** الدليل الفعلي من اللوجات والميتركس والتراسيز والكود، ويتقرأ سطر بسطر (ممنوع التخمين).
- **Root Cause:** السبب الجذري اللي لو اتعالج المشكلة ما تتكررش، مش مجرد العَرَض.
- **Test-Before-Talk:** جرّب واتأكد الأول عملياً، وبعدين اتكلم/أعلن/اكتب.

---

## 🛡️ الصمامات الـ 86 الميدانية الحاكمة (86 Invariants Summary):
1. قانون الصدق الصريح ومحاربة التملق (Zero-Pleasing & Truth-Over-Harmony Law):
2. بوابة الواقع الميداني ضد النماذج النظرية (Field Reality vs Theoretical Model Gate):
3. قانون السكربت المستقل ضد الشل التفاعلي (Standalone Script Over Interactive Shell Law):
4. قانون التيرمينال الحي ضد بيئات المحاكاة (Live Terminal Surface Over IDE Execution Law):
5. أولوية البيئة الافتراضية المعزولة (Isolated Virtualenv & Bare-Metal Priority):
6. قاعدة حرمة الكود الشغال ومحاربة الزحمة (Hands-Off Working Code & Zero-Sprawl Law):
7. قاعدة استئصال الافتراضات ("مين قالك؟" Pre-Action Sanity Probe):
8. قانون الصفر-متصفح والاعتماد على الطلبات الصافية (Zero-Browser & Pure Requests Law):
9. صمام حصانة الردود وأكواد البرمجة (Endpoint Status vs Chat Code Immunity):
10. قاعدة وبانر تفريغ الصوت الإلزامية الدائمة (Mandatory Verbatim Voice Transcription Protocol):
11. قاعدة النطاق الجغرافي والبروكسي السكني (Sticky Geo-IP & Residential Affinity Law):
12. طابور التعبئة المتتابع ومنع التوازي الصادم (FIFO Sequential Queue Refill):
13. صمام الحفظ الذري والنسخ الاحتياطي اللحظي (Atomic Write & Timestamped .bak Invariant):
14. صمام الأرشفة الآمنة وعدم إتلاف البيانات (Safe Archiving & Zero-Data-Loss Law):
15. صمام منع الروابط الوهمية والتحقق من وصول السؤال (Anti-Phantom URL & Prompt Delivery Gate):
16. صمام حماية خط الاتصال والمهلة الممتدة (Zero-Drop 10-Minute Timeout Invariant):
17. صمام عزل العمليات وحرمة بيئة المستخدم (Process Isolation & User-Environment Immunity):
18. مبدأ الصفر-تسجيل دخول وتجوال الكوكيز عبر الـ IPs (Zero-Login & Cross-IP Session Roaming):
19. صمام منع التكتل المكاني والحقن العشوائي البشري (Anti-Clustering & Human Entropy Injection):
20. صمام التوثيق المرئي والتليميتري الهيكلي (Debugging Mode with Visual Verification & JSON Telemetry):
21. صمام الاختيار بالـ Index الديناميكي وحظر الإحداثيات الصلبة (Dynamic Index Selection vs Hardcoded Coordinates):
22. صمام حفظ حالة المهام الأحادية ضد انقطاع الطاقة (One-Time Quest Checkpointing & State Persistence):
23. صمام المسبار الاستباقي لتحديثات المنصة الدورية (Pre-Run Platform Patch Quarantine):
24. صمام الاستخراج المسبق لرسائل الـ OTP من الـ HAR الحية (Pure HAR-Driven OTP Reverse-Engineering):
25. صمام الـ Iframe المتداخل في قراءة رسائل الـ OTP (Nested Iframe OTP Resolution):
26. صمام الاختبار المسبق للمزودات ("بتعمل الحاجة وتجري؟ اختبرها الأول!") (Pre-Flight Live Verification):
27. صمام التبريد المؤقت للحسابات وتفادي الحظر الدائم (Account Cooldown & Backoff Gating):
28. صمام حماية الأسرار وإلغاء تدريب النماذج (AI Data Retention & Privacy Enforcement):
29. صمام التفريغ الصوتي المتخصص عبر النماذج المتعددة (Multimodal Voice Transcription Resilience):
30. صمام التجميع المتوازن للملفات وحظر التفتيت المفرط (Balanced Modular Architecture):
31. صمام التثبت البنكي المغلق للعمليات المالية والأرصدة (Closed-Loop Balance & Banking Invariant):
32. صمام القفل الاستباقي للهدف المنجز (Preemptive Goal Latch & Instant Break):
33. صمام تطهير وتطبيع أكواد الـ OTP (Clean Alphanumeric OTP Sanitization):
34. صمام تتبع سلاسل التوجيه خطوة بخطوة (Hop-by-Hop Redirect Tracking):
35. صمام سياق الروابط في رسائل البريد (Contextual Link Extraction vs First-Match Trap):
36. صمام دفق التفكير المتسلسل وعدم الانقطاع المبكر (SSE Thought Stream vs Final Message Invariant):
37. صمام حارس طول الكود ضد انكماش الذكاء الاصطناعي (AI Length-Guard):
38. صمام القوالب الذهبية وعزل المخرجات (Golden Template Quarantine):
39. صمام دفق الـ SSE الهجين وقطع الـ Shorthand (SSE Shorthand Delta Parser):
40. صمام المحاكاة البايولوجية لتطبيقات الموبايل (Mobile App Signature & Pure Requests):
41. صمام حل ألغاز العمل المسبق بالـ WASM والذاكرة (Pre-fetched WASM PoW Solver):
42. صمام تسليم الجلسة الهجين بين المتصفح ومحاكي الـ TLS (Hybrid Browser-to-TLS Handoff):
43. صمام محفز مدخلات رياكت وتجاوز الغلاف الاصطناعي (React Controlled Input Setter):
44. صمام تطهير الـ BOM وحظر التعديل النصي لملفات الـ JSON (Zero-BOM JSON Purity):
45. صمام تدوين مجمعات الإيميل وخط الدفاع اليدوي (Multi-Provider Email Rotation & Manual Fallback):
46. صمام الحقن النصي الآمن للـ CDP وحظر الـ f-strings المزدوجة (CDP JavaScript %-Formatting Injection):
47. صمام استهداف النصوص الدلالية وحظر الكلاسات الهشة (Semantic Text Locators vs Brittle CSS Classes):
48. صمام التوافق المتوازي لحل الكابتشا بالرؤية والتحكيم (Multi-Solver Consensus & Vision Judge Invariant):
49. صمام التطهير المزدوج للنوافذ المنبثقة ولافتات الكوكيز (Double-Dismiss Viewport Clearing Invariant):
50. صمام النقاء اللاتيني الصارم للكود وحظر الرموز الشاذة (ASCII Purity in Source Code & Non-ASCII Blocker):
51. صمام التجديد ثلاثي الطبقات للجلسات (3-Layer Session Refresh & Fallback Architecture):
52. صمام استقرار التبويب وحظر إعادة الاتصال العشوائية (Deterministic Navigation vs uc_open_with_reconnect):
53. صمام كاش بصمة الـ SHA1 لمنع تكرار معالجة الصور (SHA1 Hash Image Deduplication & Caching):
54. صمام توثيق طريقة الدخول في قواعد الحسابات (`login_method` Auditing Invariant):
55. صمام لقطة المعرفات السابقة وتفادي الـ OTP القديم (The `seen_ids` Inbox Snapshot Invariant):
56. صمام استخراج الكود السريع من عنوان الرسالة (Subject-Line Fast OTP Regex Extraction):
57. صمام استكشاف الأزرار المجهرية وشروط الاستخدام (Micro-Checkbox & Terms Agreement Audit):
58. صمام العزل الصارم للمشاريع عبر الحسابات (Cross-Account Project Isolation & Forking):
59. صمام حارس جاكارد لمنع انفجار المهام الذاتية (Jaccard Anti-Loop & Max-Depth Guard):
60. صمام إعادة تهيئة دورة المصادقة عند استنفاد محاولات الكابتشا (Full OAuth Flow Reset on CAPTCHA Failure):
61. صمام تطبيع المدخلات قبل التخزين المؤقت وحساب الهاش (Cache Input Normalization Invariant):
62. صمام رصد نهاية دفق الـ WebSocket بالـ Payload لا الاتصال (WebSocket Payload-Level EOF Detection):
63. صمام حظر الاستيراد الدائري عبر وسيط الوكلاء (Mediator Pattern for Circular Import Prevention):
64. صمام تفريق أعطال الحافة عن التوكن بزمن الاستجابة (TTFB Edge vs Token Gate):
65. صمام التقاط أخطاء الـ gRPC في الـ Trailers وتفادي الـ 200 الخادع (gRPC Trailer Error Catcher):
66. صمام القص الفعلي والتثبيت الذري للكوكيز على القرص (Atomic Disk-Cut for Consumed Sessions):
67. صمام فرامل الطوارئ لخيوط التوازي المعلقة (Daemon Thread Emergency Brakes):
68. صمام أقفال النواة المزدوجة للملفات المشتركة (OS Kernel-Level File Locks):
69. صمام الترقيم التصاعدي الصارم لحزم الـ ACK في الـ WebSocket (Monotonic WebSocket ACK Sequence):
70. صمام استئناف الجلسات الحية الطويلة عبر بوابات الـ Continue (Agent Stream Session Re-anchor):
71. صمام التشتيت العشوائي لضربات التزامن (Decoupled Concurrency Jitter):
72. صمام التهيئة القسرية لترميز UTF-8 على كونسول ويندوز (Windows Stdout UTF-8 Enforcement):
73. صمام الكاتب المنفرد وتجزئة الحالة لمنع تعارض ويندوز (Single-Writer Actor & State Sharding):
74. صمام عزل المحركات كعمليات نظام مستقلة (Subprocess Process Isolation):
75. صمام حظر التوقيتات الثابتة والتوزيع البشري العشوائي (Zero Hardcoded Timings Law):
76. صمام التثبيت الجغرافي والاستبدال الإقليمي المتطابق (Regional Geo-Pinning Invariant):
77. صمام الحصانة الافتراضية الصارمة للأصول والعتاد (Default-Deny Asset Immunity):
78. صمام سقف الأمان الأقصى المانع للتعليق (Anti-Deadlock Safety Ceiling):
79. صمام الساعة البيولوجية والنوم الليلي الإقليمي (Circadian Rhythm & Geo-Aligned Sleep Block):
80. صمام الحجر الصحي بعد الموت وتفادي حلقة الهلاك (Post-Death Quarantine & Anti-Death Loop):
81. صمام فصل إثبات الإنجاز عن الرصيد والموقع الجغرافي (State Varbit vs Inventory/Location Ground Truth):
82. صمام الدورة التنفيذية الخماسية المغلقة (Deterministic 5-Phase Action Cycle):
83. صمام مضاهاة الـ HAR بالسطور قبل كتابة أي كود (Verbatim HAR Match & Zero Guesswork):
84. صمام الاحتواء المرن للأخطاء والتجاوز الآمن (Graceful Failover vs Terminal Crash Law):
85. صمام الحظر الصارم للـ Self-Merge والمراجعة المزدوجة (No Self-Merge & Dual-Review Law):
86. صمام تدوين بوصلة الحالة الفورية والمزامنة القهرية (§FATAL RULE #SYNC Invariant):

---

## 🗣️ أسلوب الرد:
- سطر بالبلدي ومباشر في البداية.
- نقاط سريعة وواضحة تركز على الـ Ground Truth والـ Root Cause.
- مثال تطبيقي عملي لو استدعى الموقف.
