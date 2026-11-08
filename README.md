# 🏛️ Bolla-Agentic OS (EGM & SRE Edition)

<div align="center">

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-green.svg)
![Architecture: Pure Standard Library](https://img.shields.io/badge/Dependencies-Zero%20pip%20(Pure%20StdLib)-brightgreen.svg)
![Governance: Bolla Protocol v1.3](https://img.shields.io/badge/Governance-Bolla%20v1.3-orange.svg)
![EGM: Elephant & Goldfish v2.0](https://img.shields.io/badge/EGM%20Swarm-10%2F10%20Zero--Context-blueviolet.svg)
![SRE: 360° Reliability](https://img.shields.io/badge/SRE-7%20Governing%20Gates-red.svg)

**Autonomous AI Agent Governance, SRE Resilience & Living Memory Operating System**  
*A hermetic, self-contained meta-framework for pair-programming AI agents, context persistence, Site Reliability Engineering (SRE), and Google's Elephant-Goldfish Model (EGM).*

</div>

---

> 🏷️ **Recommended GitHub Topics:**  
> `agentic-ai` • `ai-agents` • `sre` • `site-reliability-engineering` • `elephant-goldfish-model` • `egm` • `living-memory` • `agent-governance` • `antigravity` • `zero-leak` • `prompt-engineering`

---

## 🌟 Highlights & Key Capabilities

- 🧠 **Living Memory Engine (`Root/`):** Autonomous, persistent context across hundreds of sessions without hallucination or context loss via 6 synchronized ledgers (`ai_state.json`, `PROGRESS.md`, `tasks.md`, `memory.md`, `ANCHORS.md`, `HANDOFF.md`).
- 🛠️ **Architectural SRE & 360° Reliability (`/00-architect-sre`):** Site Reliability Engineering constitution featuring the 7 Governing Gates (Goal & Measurement, Ground Truth, Root Cause, Direct & Reverse Paths, Circuit Breakers, Red Line & Security, Test-Before-Talk).
- 🐘🐠 **Google's Elephant-Goldfish Model (EGM v2.0):** Built-in adversarial review swarm separating the Long-Horizon Contextual Planner (Elephant) from 10 specialized Zero-Context Reviewers (Goldfish).
- 🏛️ **Bolla Constitution v1.3:** 10 fundamental laws of agentic software engineering and 86 security valves enforcing zero-drift architecture.
- 🔒 **Ironclad Zero-Leak Perimeter:** Built-in regex scanners blocking API keys, personal tokens, phone numbers, and private emails before commit.
- ⚡ **Pure Standard Library:** Zero external `pip` dependencies. Runs anywhere Python 3.10+ is installed (Linux, macOS, Windows).

---

## 🐘🐠 The Elephant & Goldfish Model (EGM Swarm)

Bolla-Agentic OS natively integrates Google's **Elephant-Goldfish Model (EGM)** to eliminate cognitive bias, model exhaustion, and sycophancy:

```text
       ┌────────────────────────────────────────────────────────┐
       │             🐘 Elephant Orchestrator / Architect       │
       │     (Holds project memory, requirements & designs)     │
       └───────────────────────────┬────────────────────────────┘
                                   │ Spawns Zero-Context Swarm
       ┌───────────────────────────┴────────────────────────────┐
       │             🐠 10 Independent Goldfish Personas        │
       │  (Zero context memory — evaluate specs without bias)   │
       └───────────────────────────┬────────────────────────────┘
                                   │
 ┌─────────────────┬───────────────┼───────────────┬─────────────────┐
 │                 │               │               │                 │
▼                 ▼               ▼               ▼                 ▼
egm-design     egm-zoom-out   egm-codebase    egm-comprehend    egm-readiness
(Hostile      (Skeptical       (Pedantic       (Naive Reader     (Pragmatic
 Architect)    Simplicity)     Details)         Auditor)          Tech Lead)
 │                 │               │               │                 │
▼                 ▼               ▼               ▼                 ▼
egm-inventive   egm-structural  egm-style       egm-bootstrap   egm-synthesizer
(TRIZ Solver)  (Layout Eng)    (Copy Editor)   (Onboarding DX)  (Consolidator)
```

---

## 🛠️ Architectural SRE & The 7 Governing Gates (`/00-architect-sre`)

Every engineering task and architectural modification must pass through **Bolla's 7 Governing Gates**:

| # | Gate (البوابة) | Core Question | Mandatory Output |
|---|---|---|---|
| **1** | **Goal & Metric** | What exactly are we solving, and how do we measure success? | 1-sentence goal + quantitative/behavioral metric. |
| **2** | **Ground Truth** | What are the verified facts from source code and runtime logs? | Zero speculation. Direct line references and log evidence. |
| **3** | **Root Cause** | What is the underlying root cause vs surface symptoms? | Eliminates the deep trigger to prevent recurrence. |
| **4** | **Direct & Reverse** | What if it succeeds? What if it fails (Rollback Plan)? | Pre-verified happy path + instantaneous rollback path. |
| **5** | **Circuit Breaker** | What is the worst-case failure mode, and how is it isolated? | Blast radius containment to protect the rest of the OS. |
| **6** | **Red Line & Security** | Is there any secrets or credential leak risk? | 360° security scan, zero hardcoded keys, 1-year impact test. |
| **7** | **Test-Before-Talk** | How did we physically verify this before announcing it? | 100% test pass rate + decision ledger update. |

---

## 📂 Repository Architecture

```text
Bolla-Agentic-Operating-System/
├── README.md                            # Comprehensive global guide & Quickstart
├── GEMINI.md                            # Agentic OS AI constitutional guidelines
├── AGENTS.md                            # Unified SSOT operational reference
├── .gitignore                           # Hardened security exclusion filter
├── .env.example                         # Safe environment variables template
├── requirements.txt                     # Pure Python Standard Library declaration
├── LICENSE                              # MIT License
│
├── 🏛️ .agents/                             # Agent Mind & Governance Core
│   ├── rules/                           # Bolla Constitution v1.3, 86 valves, SRE rules
│   ├── workflows/                       # Workflows: /00-planning, /00-speckit, /00-egm-review, /00-architect-sre
│   ├── skills/                          # Core agent skills (SRE, Planning, Evidence Inspection)
│   ├── memory/                          # Architecture decision changelog & examples
│   └── AGENT.md                         # Antigravity agent identity & scope
│
├── 🧠 Root/                                # Living Memory Kernel (Genesis State)
│   ├── ai_state.json                    # Real-time state compass (Turn 0 baseline)
│   ├── PROGRESS.md                      # Cumulative milestones & session progress
│   ├── tasks.md                         # Interactive task decomposition ledger [x]
│   ├── memory.md                        # Architectural memory & forensic discoveries
│   ├── ANCHORS.md                       # Cryptographic SHA-256 state anchors
│   ├── HANDOFF.md                       # Standard resume & session handoff bridge
│   └── keys.example.txt                 # Safe API credentials template
│
├── 📜 docs/                                # Protocols & Specifications
│   └── BOLLA_PROTOCOL.md                # Full Bolla Protocol architectural documentation
│
├── 🛡️ .governance/                         # Automated Gatekeeper Tools
│   ├── AGENT_HARD_RULES.md              # Closure rules & invariants
│   ├── state_gate.py                    # 8-field state compass validator
│   ├── secret_scan.py                   # Multi-pattern secrets & leak scanner
│   ├── self_review.py                   # Automated self-critique gatekeeper
│   ├── attest.py                        # Cryptographic attestation engine
│   ├── claim_check.py                   # Line-anchored claim verification
│   └── path_scan.py                     # Absolute machine path detector
│
└── 🛠️ scripts/                             # Operational Tooling
    ├── init_project.py                  # One-click bootstrap script for new projects
    └── verify_spec_drift.py             # EGM drift prevention & spec verifier
```

---

## 🚀 Quickstart (Day 1 Workflow)

### 1. Clone the repository
```bash
git clone https://github.com/your-org/Bolla-Agentic-Operating-System.git
cd Bolla-Agentic-Operating-System
```

### 2. Verify Repository Health
Run the built-in drift verifier to confirm zero drift and zero leaks:
```bash
python scripts/verify_spec_drift.py
```

### 3. Initialize for a New Project
Bootstrap a clean living memory kernel for your target project:
```bash
python scripts/init_project.py --name "MyAmazingProject"
```

### 4. Pair-Program with Your Agent
Open the repository in **Google Antigravity**, **Cursor**, or **Windsurf**. Your agent will automatically read `GEMINI.md` and `AGENTS.md`, orient itself via `Root/ai_state.json`, and follow the 10 Laws of Bolla!

---

## 📜 The 10 Laws of Bolla (Constitution Summary)

1. **Law of Immunity:** Cryptographic Anchoring (SHA-256) of all core files.
2. **Law of the Scalpel:** Surgical, minimal diffs. Never wipe or destroy existing files.
3. **Law of the Laboratory:** Test-driven verification before and after all changes.
4. **Law of Proof:** Zero unverified assertions. Every claim must have explicit line evidence.
5. **Law of Truth:** State compass (`ai_state.json`) must accurately mirror reality.
6. **Law of Roles:** Strict separation between Planning (Elephant) and Adversarial Review (Goldfish).
7. **Law of Goal:** Relentless dedication to software excellence without shortcuts.
8. **Law of Reference:** Explicit file and line citations (`file.py#L10-L25`).
9. **Law of Continuity:** Every session ends with a clear handoff bridge (`Root/HANDOFF.md`).
10. **Law of Structural Isolation:** Meta-framework kernel strictly isolated from transient scrapers.

---

## 📄 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
