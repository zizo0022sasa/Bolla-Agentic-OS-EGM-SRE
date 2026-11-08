@.agents/rules/00-bolla-constitution.md
@.agents/rules/00-architect-sre.md
@.agents/rules/00-core-authority.md
@.agents/rules/20-governance-security.md
@.agents/rules/30-golden-master.md
@.agents/rules/90-glossary-limits.md

# 🤖 GEMINI.md — دستور حوكمة ونظام تشغيل الوكلاء (Bolla-Agentic OS)

> **📌 اقرأ الملف ده قبل ما تلمس أي سطر في المشروع.**
> بيخليك تفهم المشروع وتشتغل صح بأعلى معايير الحوكمة والذاكرة الحية.

---

## 🗣️ اللغة وأسلوب العمل

- **كلمني بالمصري دايماً** — لغة واضحة وودية وهندسية مباشرة.
- **استخدم Emojis** عشان الوضوح والمتعة والترتيب.
- **خليك مختصر ومباشر** — بلاش حشو ولا كلام مرسل.
- **كود → code blocks** مع اسم اللغة دايماً.

---

## 🏛️ معمارية المشروع — Bolla-Agentic OS

نظام تشغيل حوكمة الوكلاء والذاكرة الحية (`Bolla-Agentic OS`) هو إطار عمل مجرد وشامل لإدارة دورة حياة الوكلاء الأذكياء:

| المكون | الوظيفة |
|---|---|
| **`Root/ai_state.json`** | بوصلة الحالة اللحظية للوكيل (Turn count, Mode, Roles, Drift Status). |
| **`Root/` (النواة السداسية)** | دفاتر الذاكرة الحية: `PROGRESS.md`, `tasks.md`, `memory.md`, `ANCHORS.md`, `HANDOFF.md`. |
| **`.agents/rules/`** | دستور بولا v1.3 + الصمامات الـ 86 + قواعد الأمان والحوكمة. |
| **`.agents/workflows/`** | مسارات العمل التلقائية: `/00-planning`, `/00-speckit`, `/00-egm-review`. |
| **`.governance/`** | بوابات وصمامات الفحص الآلي للأسرار والمسارات والحالة اللحظية. |
| **`scripts/`** | أدوات كشف الانحراف المعماري وتهيئة المشاريع الجديدة. |

---

## 🔒 القواعد غير القابلة للتفاوض (Non-Negotiable)

1. **حظر تسريب الأسرار (Zero Secrets & Zero Leaks):** ممنوع منعاً باتاً ظهور أي بريد إلكتروني، رقم هاتف، أو مفتاح API في المحادثة أو الكود أو المستودع.
2. **فصل التخطيط عن المراجعة (EGM Protocol):** الفيل يخطط (`Elephant Architect`)، والسمكة الذهبية المستقلة (`Goldfish Critic`) تراجع بذاكرة صفرية قبل كتابة الكود.
3. **استمرارية الحالة:** تحديث `Root/ai_state.json` وسجل القرارات `CHANGELOG_DECISIONS.md` في نهاية كل مهمة.
