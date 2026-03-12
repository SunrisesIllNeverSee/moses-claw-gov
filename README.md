# moses-claw-gov

MO§ES™ Constitutional Governance — OpenClaw skill family.

Constitutional control layer for AI agents. Role hierarchy, behavioral modes, posture controls, and SHA-256 chained audit trail. Built for [OpenClaw](https://github.com/openclaw/openclaw) and [ClawHub](https://clawhub.ai).

**Patent pending:** Serial No. 63/877,177
**DOI:** https://zenodo.org/records/18792459
**Live demo:** https://mos2es.io

---

## Install

```bash
clawhub install moses-governance
```

Or clone and install manually — see [SETUP.md](SETUP.md).

---

## Skill Family

| Skill | Purpose | Install |
|-------|---------|---------|
| `moses-governance` | Full multi-agent bundle (recommended) | `clawhub install moses-governance` |
| `moses-governance-single` | Single-agent, fastest install | `clawhub install moses-governance-single` |
| `moses-roles` | Agent definitions + sequencing only | `clawhub install moses-roles` |
| `moses-modes` | Mode constraint injection only | `clawhub install moses-modes` |
| `moses-postures` | Posture controls only | `clawhub install moses-postures` |
| `moses-audit` | SHA-256 ledger only | `clawhub install moses-audit` |
| `moses-coordinator` | Optional WebSocket sequence daemon | `clawhub install moses-coordinator` |

---

## What It Does

Every agent action is:
1. **Checked** against the active governance mode (High Security, High Integrity, Creative, Research, Self Growth, Problem Solving, IDK, Unrestricted)
2. **Filtered** through the active posture (SCOUT / DEFENSE / OFFENSE)
3. **Ordered** by role (Primary → Secondary → Observer)
4. **Logged** with SHA-256 hash to an append-only audit ledger

---

## Quick Start

```bash
export MOSES_OPERATOR_SECRET='your-hmac-key'
python3 skills/moses-governance/scripts/init_state.py init

/govern high-security
/posture defense
/role primary
/status
```

---

## © 2026 Ello Cello LLC
contact@burnmydays.com | https://mos2es.io
