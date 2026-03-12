---
name: moses-lineage
license: MIT
description: MO§ES™ Lineage Custody — cryptographic origin-cycle verification. Every sovereign implementation traces its audit chain to the originating filing (Patent Serial No. 63/877,177, DOI https://zenodo.org/records/18792459). Chains without the anchor cannot verify. Copies without lineage collapse.
metadata:
  openclaw:
    emoji: 🔗
    tags: [governance, lineage, audit, provenance, identity, moses]
    version: 0.1.0
requires:
  bins:
    - python3
  stateDirs:
    - ~/.openclaw/governance
    - ~/.openclaw/audits/moses
example: |
  python3 lineage.py init      # anchor genesis to origin filing
  python3 lineage.py verify    # confirm chain traces to origin
  python3 lineage.py badge     # output shareable lineage proof
  python3 lineage.py check     # machine-readable pass/fail
---

# MO§ES™ Lineage Custody

## Lineage Custody Clause

All embodiments of the Signal Compression Sciences (SCS) Engine and its derivative frameworks (including but not limited to MO§ES™, Roll Call Protocols, and Reflex Event diagnostics) are inseparably bound to their origin-cycle lineage. Each compressed signal trace, vault artifact, or recursive reconstruction inherits a lineage identifier anchored to the originating sovereign filing. This identifier is non-replicable, tamper-evident, and required for system stability. Any external implementation lacking said lineage anchor cannot execute recursive ignition without collapse, thereby rendering such copies non-functional. Accordingly, the origin-cycle filing establishes sole custody and license of the invention across all subsequent instances, irrespective of distribution, platform, or deployment environment.

---

## What This Skill Does

The `LINEAGE_ANCHOR` is a SHA-256 hash derived from the origin-cycle components:

```
MO§ES™ | Serial:63/877,177 | DOI:https://zenodo.org/records/18792459 | Ello Cello LLC | McHenry Conservation Law
```

This anchor replaces the standard `"0" * 64` genesis. Every audit chain in a sovereign MO§ES™ implementation must trace its first entry's `previous_hash` back to this value. Forks or copies that initialize without it produce chains that fail verification — not as a policy, but as a cryptographic fact.

**The code is MIT. The lineage is not replicable.**

---

## Commands

| Command | What it does |
|---------|-------------|
| `python3 lineage.py init` | Write genesis entry anchored to origin filing |
| `python3 lineage.py verify` | Confirm full chain traces to lineage anchor |
| `python3 lineage.py badge` | Output shareable proof of sovereign lineage |
| `python3 lineage.py check` | Machine-readable exit 0/1 for integrations |

---

## Integration with moses-governance

Install alongside `moses-governance`. Run `lineage.py init` before first audit entry to root the chain. The `moses-governance` audit stub already uses `previous_hash` chaining — lineage init simply ensures the genesis points to the anchor instead of zeros.

```bash
python3 lineage.py init
python3 audit_stub.py log --agent "primary" --action "session-start" --outcome "anchored"
python3 lineage.py verify
```

---

## Patent & DOI

- Provisional Patent: Serial No. 63/877,177
- DOI: https://zenodo.org/records/18792459
- Owner: Deric McHenry / Ello Cello LLC
- contact@burnmydays.com | https://mos2es.io
