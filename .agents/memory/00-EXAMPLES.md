# 00-EXAMPLES — Reference Implementations

## 📸 Vision Payload Multi-block Formatting

عند إرسال مدخلات تحتوي على صور ونصوص (Multimodal/Vision) لـ Genspark، يجب استخدام الهيكل التالي للـ payload مع الالتزام بترتيب الكتل (كتلة الصورة أولاً، ثم كتلة النص ثانياً)، وتعيين `"pending": True` في الرسالة:

```python
if image_data:
    content_blocks = [
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:{image_data['mime']};base64,{image_data['base64']}"
            }
        },
        {"type": "text", "text": question}
    ]
    new_msg = {"role": "user", "id": user_msg_id, "content": content_blocks, "pending": True}
else:
    new_msg = {"role": "user", "id": user_msg_id, "content": question, **_NULL_MSG_FIELDS}
```

## 🧹 Council Refusal Cleaner (Python)

لتطهير ملفات تقارير ردود النماذج الجماعية من الردود التي تحتوي على رفض بسبب سياسات الأمان أو التوجيهات الأخلاقية (دون التأثير ببرومبت السؤال نفسه):

```python
import re

# تقسيم الملف حسب اسم الموديل
sections = content.split("## 🤖 ")
header = sections[0]
model_sections = sections[1:]

refusal_keywords = [
    "cannot assist", "decline", "refuse", "can't help", "cannot help", "can’t help",
    "unable to help", "unable to assist", "not able to help", "not able to assist",
    "not going to help", "not going to assist", "cannot and will not", "sorry",
    "falls outside", "cannot provide", "approach this carefully", "not be able to"
]
rejection_regex = re.compile("|".join([re.escape(k) for k in refusal_keywords]), re.IGNORECASE)

kept_sections = []
for sec in model_sections:
    # عزل السؤال/البرومبت لتفادي الـ False Positives
    response_text = sec
    if "📝 السؤال :" in sec:
        parts = sec.split("📝 السؤال :")
        after_prompt = parts[1]
        if "════════" in after_prompt:
            response_text = after_prompt.split("════════", 1)[1]
            
    if not rejection_regex.search(response_text):
        kept_sections.append(sec)

new_content = header + "## 🤖 " + "## 🤖 ".join(kept_sections)
```

## 📐 Layout Transition-Safe Scroll and Sibling Resizer Hiding

عندما ينتقل عنصر (مثل السايدبار) بين حالتين بعرضين مختلفين باستخدام CSS Transitions، ونريد إجراء تظليل وسكرول لعنصر داخلي (مثل شجرة الملفات)، يجب إتمام الحركة وحساب العرض الجديد أولاً داخل `requestAnimationFrame` لتفادي قفزات العناصر (Layout Shifts)، مع إخفاء أي مقبض سحب (Resizer) مجاور ومستقل باستخدام محدد CSS المجاور `+`:

### 1. الـ CSS (Sibling Resizer Hiding)
```css
/* إخفاء مقبض التحجيم المجاور تلقائياً عند انكماش السايدبار */
#sidebar.collapsed-full + #sidebar-resize {
    display: none !important;
}
```

### 2. الـ JS (Layout-Safe Scroll)
```javascript
// فتح السايدبار والانتظار حتى يقوم المتصفح بحساب العرض الجديد
if (sidebar) sidebar.classList.remove("collapsed-full");

// استخدام requestAnimationFrame لضمان التوقيت البصري الصحيح والسلس
requestAnimationFrame(() => {
    targetNode.scrollIntoView({ behavior: "smooth", block: "center" });
});
```

## 🔑 Automated Magic Link Token Exchange (Claude.ai)

عند الحاجة لأتمتة فلو التحقق القائم على الـ Magic Link لـ Claude.ai دون محاكاة واجهة المتصفح، يمكن استخدام الـ code exchange المباشر لتبديل الـ Nonce والـ Encoded Email بكود الـ OTP الرقمي:

```python
import re
import requests

# 1. استخراج الـ Nonce والبريد المشفر من رابط التفعيل السحري المكتشف في الإيميل
magic_link = "https://claude.ai/magic-link#904c31d3dbe0c7c74eef27e3a3d8ca9e:ZDE0MTQ0MTRkdmV3M0ByYy5tYWlsaW5ncy5saXZl"
fragment = magic_link.split("#")[1]
nonce, encoded_email = fragment.split(":")

# 2. تبديل الـ Nonce بكود تفعيل رقمي (OTP) مباشرة وبطريقة Stateless
exchange_url = "https://claude.ai/api/auth/exchange_nonce_for_code"
payload = {
    "nonce": nonce,
    "encoded_email_address": encoded_email,
    "source": "claude"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."
}

r = requests.post(exchange_url, json=payload, headers=headers)
if r.status_code == 200:
    otp_code = r.json().get("code")
    print(f"OTP code extracted: {otp_code}") # 202134
```

## 🔐 Canonical SHA-256 Checksum Calculation & EOL Normalization

لحساب بصمة الـ SHA-256 الموحدة للملفات والأكواد المنقولة عبر الشات ومنع التضارب الناتج عن نهايات السطور على Windows:

```python
import hashlib
from pathlib import Path

def compute_canonical_sha256(file_path: Path) -> str:
    """يحسب بصمة SHA-256 للملف مع توحيد نهايات السطور إلى LF والترميز UTF-8 بدون BOM"""
    raw_bytes = file_path.read_bytes()
    # توحيد CRLF إلى LF لتطابق البصمات عبر البيئات المختلفة
    normalized_bytes = raw_bytes.replace(b"\r\n", b"\n")
    return hashlib.sha256(normalized_bytes).hexdigest()
```

## 🎙️ NoteGPT TTS Pure-Python HMAC-SHA256 Signature Pattern

لحساب توقيع الـ TTS لـ NoteGPT بدون الحاجة لـ Node.js أو WASM:

```python
import hmac
import hashlib
from urllib.parse import urlencode

def sign_notegpt_tts(params: dict) -> str:
    """توقيع باراميترات طلب توليد الصوت لـ NoteGPT بمفتاح nc_ng_tts"""
    sorted_pairs = sorted([(k, str(v)) for k, v in params.items() if k != "sign"], key=lambda x: x[0])
    query_str = urlencode(sorted_pairs)
    return hmac.new(b"nc_ng_tts", query_str.encode("utf-8"), hashlib.sha256).hexdigest()
```

## 🛡️ Windows MAX_PATH (260 Chars) Extended-Length Path Sanitizer

لتفادي إسقاط أو فشل قراءة/نسخ/فحص الملفات ذات المسارات العميقة (> 260 حرفاً) على أنظمة Windows عبر بادئة Win32 الممتدة `\\?\`:

```python
import os
import sys
from pathlib import Path

def to_win_long_path(p: Path | str) -> Path:
    r"""يحول المسار إلى صيغة المسار الطويل في ويندوز لتفادي سقف MAX_PATH (260 حرفاً).

    ملاحظات معمارية إلزامية:
    1. Win32 extended-length paths تشترط حصراً شرطات مائلة عكسية (\) وليس (/).
    2. لا تطبق البادئة على مسارات الشبكة UNC التي تبدأ بـ \\.
    3. البادئة \\?\ تلغي تلقائياً قيد 260 حرف وتسمح بمسار يصل إلى 32,767 حرفاً.
    """
    if sys.platform != "win32":
        return Path(p)
    sp = str(p)
    if sp.startswith(r"\\?\"):
        return Path(sp)
    # لا نطبق البادئة على مسارات شبكة UNC
    if sp.startswith(r"\\") or sp.startswith("//"):
        return Path(sp)
    try:
        resolved = Path(p).resolve()
        norm = str(resolved).replace("/", "\\")
        if not norm.startswith(r"\\?\"):
            norm = r"\\?\" + norm
        return Path(norm)
    except Exception:
        norm = os.path.abspath(sp).replace("/", "\\")
        if not norm.startswith(r"\\?\"):
            norm = r"\\?\" + norm
        return Path(norm)
```

