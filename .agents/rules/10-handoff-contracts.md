# 📋 10-HANDOFF-CONTRACTS — قوالب التسليم والعقود الهندسية

## 1. مبدأ السياق عالي الإشارة (High-Signal Context Principle)
- دمج Rule 2 و Rule 15: يُمنع إرسال شجرة ملفات عمياء أو تفريغ عشوائي للمشروع.
- يُرسل لأوبوس: ملخص المشروع (10 سطور)، مقاطع الأكواد المعنية بدقة، رسائل الخطأ، مخرجات الاختبار، وحدود الملفات المسموحة والمحظورة فقط.

---

## 2. قالب تسليم الحافظة ([OPUS ENGINEERING HANDOFF])
```markdown
[OPUS ENGINEERING HANDOFF]
PROTOCOL LIVING GIST: <URL + VERSION>
SESSION CONTEXT ANCHOR: <COMMIT_HASH | TARGET_FILE_SHA256 | BASELINE_STATUS>

TASK: <المهمة المحددة>
CURRENT STATE: <الوضع الفعلي الحالي مدعوماً بالأدلة>
EXPECTED STATE: <الوضع المستهدف بعد الحل>
OBSERVED PROBLEM: <المشكلة الملاحظة وأرقام السطور المعنية>
EVIDENCE: <أدلة قاطعة، مخرجات فحص، أكواد مستهدفة>
ROOT CAUSE: <السبب الجذري المشخص>
CONSTRAINTS: <القيود المعمارية والتقنية>
ACCEPTANCE CRITERIA: <معايير القبول القابلة للاختبار>
REQUEST: <المطلوب من أوبوس تحديده مع خطة الـ Micro-Tasks>
```

---

## 3. قالب قرار أوبوس المعماري ([ARCHITECT DECISION])
```markdown
[ARCHITECT DECISION]
1. ROOT CAUSE          — تأكيد السبب الجذري
2. INTENDED BEHAVIOR   — السلوك المستهدف
3. FILES IN SCOPE      — الملفات المصرح بتعديلها (<= 3)
4. FILES OUT OF SCOPE  — الملفات المحظور لمسها
5. CHANGES & DIFFS     — الكود والـ Diffs الكاملة (Chat-Only)
6. TESTS & COMMANDS    — أمر التحقق الفردي
7. RISK & ROLLBACK     — مخاطر الكسر وخطة التراجع
```

---

## 4. قالب العقد التنفيذي ([OPUS EXECUTION CONTRACT])
```markdown
[OPUS EXECUTION CONTRACT]
OBJECTIVE: <الهدف>
APPROVED CHANGES: <التعديلات المعتمدة>
FILES IN SCOPE: <النطاق المسموح>
FILES OUT OF SCOPE: <المحظورات>
ACCEPTANCE CRITERIA: <معايير القبول>
VERIFICATION COMMANDS: <أوامر الفحص>
```

---

## 5. قالب التقرير النهائي ([ENGINEERING DELIVERY REPORT])
```markdown
[ENGINEERING DELIVERY REPORT]
TASK: <المهمة>
OPUS DECISION: <ملخص قرار أوبوس>
IMPLEMENTATION: <ما تم تنفيذه>
FILES CHANGED: <الملفات المعدلة وبصمة SHA-256 بعد التعديل>
TESTS RUN & RESULT: <PASS / FAIL>
PUBLIC SHARE LINK: <Genspark Viewer URL>
ACCOUNT EMAIL: <Email used>
FINAL STATUS: <COMPLETED 100%>
```
