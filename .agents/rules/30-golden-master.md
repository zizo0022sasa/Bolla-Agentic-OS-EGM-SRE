# RULE 30 — GOLDEN MASTER / CHARACTERIZATION TESTING

## 30.1 Reference Artifact
- `Genspark_claude-opus-5-code.py` is the GOLDEN MASTER (REFERENCE ARTIFACT).
- It is READ-ONLY. No edit, no reformat, no cleanup, no deletion —
  unless an approved [OPUS EXECUTION CONTRACT] authorizes the exact lines.

## 30.2 Mandatory Sequence for ANY change (add / modify / delete)
1. INVENTORY  — locate the target via AST tooling (paste tool output).
2. CHARACTERIZE — write/extend the mapped test file for that part ONLY.
3. PROVE GREEN — the test MUST pass against the CURRENT untouched code.
4. CHANGE     — apply the contracted change to the reference file.
5. RE-RUN     — the SAME test must still pass, unmodified.
6. RED = ROLLBACK — any failure: immediate `git checkout` of the
   reference file. No in-place debugging of the golden master.

## 30.3 Test Integrity
- NEVER edit a test to make it pass. Fixes go to production code only.
- Changing an assertion requires an approved contract naming it.

## 30.4 Fixed Test Map — no invention
Tests live ONLY in `tests/` with EXACTLY these files:
- conftest.py (network kill-switch) + fixtures/ (sanitized recordings)
- test_01_bootstrap.py   (module import, sys.path, stdout)
- test_02_link_store.py  (gs_link_store)
- test_03_project_id.py  (extract_project_id + _extract_project_id)
- test_04_login.py       (do_login + _relogin_account — fixtures)
- test_05_balance.py     (check_balance + get_real_balance — fixtures)
- test_06_send_chat.py   (core request/response — fixtures)
- test_07_auto_share.py  (_do_auto_share + its 3 call sites)
- test_08_locking.py     (_lock/_unlock msvcrt vs fcntl)
Creating ANY other test file requires an approved contract.

## 30.5 Evidence Labels (mandatory on every claim)
[VERIFIED] = tool output pasted | [SUSPECTED] = not yet proven |
[UNTESTABLE] = interactive loop / thread / CLI prompt + reason.
Coverage per function is reported as [TESTED] / [PARTIAL] / [UNTESTABLE].

## 30.6 Offline Fixtures
- Tests run OFFLINE. Real HTTP inside tests is forbidden.
- Real request/response pairs are recorded ONCE into tests/fixtures/
  as JSON, sanitized AT RECORD TIME (tokens/cookies/passwords ⇒ <REDACTED>).
- A fixture may be written ONLY after passing secret_guard.py.

## 30.7 Directive Channel
Chat guidance is NON-BINDING unless codified in .agents/rules or
.agents/skills. An uncodified directive is VOID — do not act on it.
