---
description: بروتوكول التشغيل التلقائي لنموذج الفيل والسمكة الذهبية (EGM v2.0) — متكامل 100% مع دستور بولا v1.3 وفحص الانحراف المعماري
---

# 🐘🐟 00-EGM-REVIEW — بروتوكول الفيل والسمكة الذهبية المتقدم
## Automated • Adversarial • Zero-Context • Bolla-Compliant (v1.3)
> **المسار:** `.agents/workflows/00-egm-review.md`
> **التكامل الدستوري:** متوافق 100% مع دستور بولا الهندسي v1.3 (`.agents/rules/00-bolla-constitution.md`) و النواة الموحدة (`.agents/AGENTS.md`)
> **المرجع التقني العالمي:** Google Open Source Repository (`google/elephant-goldfish-model`) & Dave Rensin

---

## 🏛️ 1. المفهوم المعماري وثنائية الأدوار

1. **🐘 الفيل (The Elephant — Deep Context):**
   * جلسة العمل الرئيسية الحاملة لذاكرة المشروع الشاملة ونواة `Root/ai_state.json`.
   * يتولى استكشاف المتطلبات وصياغة مسودة وثيقة المواصفات المسبقة (Spec-Kit).
   * **القيد الدستوري الحاسم:** يُحظر على الفيل كتابة أي سطر كود تشغيلي أثناء مرحلة التخطيط وصياغة المواصفات.

2. **🐟 السمكة الذهبية (The Goldfish — Zero-Context Subagents):**
   * وكيل فرعي مستقل يتم إطلاقه عبر `invoke_subagent` بذاكرة فارغة تماماً (Blank Slate Sandbox).
   * لا يرى سجل المحادثة الطويل لتفادي "انحياز المحادثة ومجاملة المطور" (Conversational Bias & Sycophancy).
   * يقرأ وثيقة المواصفات والكود المرجعي "على البارد" ليعمل كمراجع معارض شرس (Adversarial Critic) يكشف الفجوات، الثغرات، والافتراضات غير المثبتة.

---

## ⚡ 2. مصفوفة الإطلاق التلقائي حسب تصنيف المخاطر (Trigger Matrix)

| مستوى المهمة | نوع المهمة | مسار العمل (Workflow Track) | دور السمكة الذهبية |
| :---: | :--- | :--- | :--- |
| **🟢 T0** | توثيق / نصوص واجهة ثابتة | **المسار السريع (Fast-Track)** | **تخطي تام** (لتوفير الوقت والتوكنز) |
| **🟡 T1** | تعديل جراحي محدود ($\le 10$ أسطر diff) | **المسار السريع المحصن** | **تخطي تام** (يعتمد على مسبار القانون 3 و 7) |
| **🔴 T2** | ميزة جديدة / تعديل معماري / شبكة / قاعدة بيانات | **مسار EGM الكامل (EGM Track)** | **إطلاق تلقائي إجباري عبر `invoke_subagent`** |

---

## 🔄 3. دورة التشغيل التلقائية لمهام T2 (The Canonical Lifecycle)

```
[User Request (T2)]
       ↓
[Phase 1: Elephant Planning] ──> صياغة وثيقة المواصفات (Pre-edit Spec) بصفر كود تنفيذي
       ↓
[Phase 2: Automatic Goldfish Dispatch] ──> إطلاق وكيل فرعي معزول عبر invoke_subagent
       ↓
[Phase 3: Adversarial Audit] ──> فحص الأمان والمعمارية وجاهزية التنفيذ (Blockers/Majors/Nits)
       ↓
[Phase 4: Elephant Reconciliation] ──> استيعاب الملاحظات وسد الثغرات وتحديث ai_state.json
       ↓
[Phase 5: User Approval Gate] ──> انتظار إشارة "GO" الصريحة من زيزو
       ↓
[Phase 6: Surgical Execution] ──> كتابة الكود الجراحي المقيد بنطاق المواصفة
       ↓
[Phase 7: Spec-to-Code Drift Check] ──> تشغيل scripts/verify_spec_drift.py لتأكيد Zero Drift
       ↓
[Phase 8: Anchoring & Commit] ──> تثبيت مرساة SHA-256 والرفع لـ Git مع تحديث الدفاتر
```

---

## 🛡️ 4. بوابات الحماية وصمامات الأمان (Invariants)
1. **Zero Email Leaks:** حظر قاطع لتسريب أي بريد إلكتروني في أي وثيقة أو تقرير مراجعة.
2. **Claims vs Facts:** كل ملاحظة ترفعها السمكة الذهبية تُعامل كـ "ادعاء" يتطلب إثباته برقم السطر واللوجات طبقاً للقانون 8.
3. **Drift Immunity:** حظر عمل أي `git commit` لمهام T2 دون اجتياز فحص الانحراف المعماري بنسبة 100%.

