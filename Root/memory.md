# 🧠 Living Technical Memory Ledger (memory.md)

> **Persistent Engineering Insights, Forensic Analyses & System Invariants**

## 🔍 Core Architectural Principles
1. **Separation of Concerns:** Keep core governance isolated from operational scripts.
2. **Deterministic State:** All agent state must be explicitly tracked in `Root/ai_state.json`.
3. **Cryptographic Anchoring:** SHA-256 anchors in `Root/ANCHORS.md` detect any unauthorized file drift.
4. **Zero Email & Secrets Policy:** Strict regex gating prevents accidental credential or PII leaks.
