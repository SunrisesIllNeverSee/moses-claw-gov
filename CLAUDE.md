# CLAUDE.md — moses-claw-gov

This is the OpenClaw skill repository for MO§ES™ Constitutional Governance.

## What This Repo Is
A family of OpenClaw skills that enforce constitutional governance on AI agents — role hierarchy, behavioral modes, posture controls, and SHA-256 chained audit trail. Built by Deric McHenry / Ello Cello LLC.

Patent pending: Serial No. 63/877,177
DOI: https://zenodo.org/records/18792459

---

## Repo Structure

```
skills/
  moses-governance/           ← Full multi-agent bundle (primary ClawHub listing)
  moses-governance-single/    ← Single-agent version (B option, ships fast)
  moses-audit/                ← SHA-256 ledger only
  moses-coordinator/          ← WebSocket sequence daemon
  moses-modes/                ← Mode constraint injection only
  moses-postures/             ← Posture controls only
  moses-roles/                ← Agent definitions + sequencing only
workspace/
  AGENTS.md                   ← OpenClaw agent definitions
  TOOLS.md                    ← Tool declarations for workspace
SETUP.md                      ← Manual install instructions
README.md                     ← Public-facing docs
```

---

## Active Development Rules

- Primary skill is `skills/moses-governance/` — changes here take priority
- `SKILL.md` frontmatter must always include `version:` — bump on every substantive change
- `scripts/audit_stub.py` and `scripts/init_state.py` must remain self-contained — no external dependencies beyond Python 3 stdlib
- `references/` folder (modes.md, postures.md, roles.md) must stay in sync with the SKILL.md body — these are injected at runtime
- Do NOT modify `workspace/AGENTS.md` or `workspace/TOOLS.md` without checking that all tool names match what's declared in SKILL.md

## File Naming
- SKILL.md = the canonical skill definition — top priority
- AMENDMENT-FORMAT.md = amendment proposal template — do not delete
- init_state.py = state management (init / set / get / reset)
- audit_stub.py = audit ledger (log / verify / recent)

## Testing
Before pushing, run:
```bash
export MOSES_OPERATOR_SECRET='test-key'
python3 skills/moses-governance/scripts/init_state.py init
python3 skills/moses-governance/scripts/audit_stub.py log "test" "test action" "pass" "High Security" "DEFENSE" "Primary"
python3 skills/moses-governance/scripts/audit_stub.py recent
python3 skills/moses-governance/scripts/audit_stub.py verify
```
All four should exit clean.

## Publishing
```bash
gh auth login
git init && git add . && git commit -m "initial"
gh repo create sunrisesillneversee/moses-claw-gov --public --source=. --push
clawhub publish skills/moses-governance
```

## Owner
Deric McHenry — Ello Cello LLC
contact@burnmydays.com | https://mos2es.io
GitHub: sunrisesillneversee
