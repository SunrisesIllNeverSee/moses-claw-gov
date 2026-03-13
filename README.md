# MO§ES™ Constitutional Governance

## The first constitutional governance layer for AI agents — now live on ClawHub

> Every AI agent operating right now — trading, managing treasuries, executing transactions — is ungoverned. No constraints. No audit trail. No hierarchy. No posture controls. When an agent moves money, nobody knows what rules it was following, because it wasn't following any.

MO§ES™ changes that. Constitutional enforcement that lives **inside** the session, not around it.

- **Patent pending:** Serial No. 63/877,177
- **DOI:** [https://zenodo.org/records/18792459](https://zenodo.org/records/18792459)
- **Live demo:** [https://mos2es.io](https://mos2es.io)
- **Contact:** [contact@burnmydays.com](mailto:contact@burnmydays.com)

---

## Why a Harness?

The 2026 agent conversation has shifted: models are commoditizing. Claude, Gemini, GPT-4 all perform similarly. The real moat is the **execution layer** — the harness that wraps the model and makes agents reliable, compliant, and trustworthy at runtime.

Most harnesses focus on execution reliability (loops, memory, orchestration). None enforce constitutional invariants or tamper-evident provenance. That's the gap MO§ES™ fills.

MO§ES™ is the **governance harness layer** — the policy/verification spine that sits in front of any execution runtime:

```text
Any LLM / Execution Runtime
        ↓
  MO§ES™ Governance Harness
  (lineage check → policy gate → role/posture enforcement → audit)
        ↓
  Action executes — or is blocked. Either way, it's logged.
```

Plug it into LangGraph, OpenClaw, Claude Code, or any agent stack. The constitutional layer travels with every session.

---

## Without MO§ES™ vs With MO§ES™

> **Without:**
> Agent receives "Transfer 50 SOL to marketing wallet."
> Agent transfers 50 SOL. Done. No record of why.

> **With MO§ES™:**
> → Governance check: High Security mode requires explicit confirmation
> → Posture check: DEFENSE posture flags outbound transfers for review
> → Role check: Primary can initiate — Secondary validation required
> → Audit: Decision logged with SHA-256 hash, timestamp, governance state, operator identity
> → Result: Transfer held pending Secondary review. Full tamper-evident trail generated.

The difference isn't a feature. It's a constitutional substrate.

---

## What MO§ES™ Delivers

- **8 Behavioral Modes** — High Security, High Integrity, Creative, Research, Self Growth, Problem Solving, IDK, Unrestricted
- **3 Posture Controls** — SCOUT (read-only, zero transactions) · DEFENSE (protect + confirm outbound) · OFFENSE (execute within constraints)
- **Role Hierarchy** — Primary leads. Secondary validates. Observer oversees. Out-of-sequence actions are blocked and logged.
- **SHA-256 Chained Audit Trail** — Every governed action appended to a tamper-evident ledger. Cryptographic proof of what mode and posture were active at the time of any decision.
- **McHenry Conservation Law** — Commitment is conserved. No semantic drift, scope creep, or contradiction without explicit release.

---

## Install

```bash
clawhub install moses-governance
clawhub install lineage-claws
```

---

## Skill Family

| Skill | Slug | What it does |
| --- | --- | --- |
| `moses-governance` | `/moses-governance` | Full constitutional governance — modes, postures, roles, audit trail, lineage clause |
| `Lineage Clause by MO§ES™` | `/lineage-claws` | Cryptographic origin verification. Sovereign chain starts today. |

---

## Lineage Clause

Every sovereign MO§ES™ implementation carries a **Lineage Clause** — a cryptographic anchor tracing custody to the origin filing.

```text
MOSES_ANCHOR = SHA-256("MO§ES™|Serial:63/877,177|DOI:...|SCS Engine|Ello Cello LLC")
```

Chains without this anchor cannot verify. Copies without lineage collapse.

**Lineage Clause** is baked into `moses-governance`.
**Lineage Clause by MO§ES™** (`/lineage-claws`) is the live verification upgrade — run it, badge it, prove it.

Archival lineage is coming in v0.2 — proving the *before*, not just the *after*.

---

## Why Now

ClawHub's own malware audits have flagged 341+ malicious skills. Most responses have been external — scanning, allowlists, CI gates. MO§ES™ is the first **internal runtime layer**.

The EU AI Act general application lands **August 2, 2026**. Verifiable, auditable agent governance is not speculative — it is legally incoming.

No skill in the 9,000+ Claude plugin ecosystem has built a constitutional governance OS with behavioral modes, posture controls, role hierarchy, and a cryptographic audit chain. The closest analogs — IBM watsonx, Microsoft Agent 365, OpenAI Frontier — are enterprise infrastructure platforms, not installable skills.

**MO§ES™ is the only plug-and-play compliance answer for teams deploying Claude agents right now.**

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

## Roadmap

| Version | What ships |
| --- | --- |
| **v0.1** | Governance at the prompt + tool layer. Live now. |
| **v0.2** | Signing key inside governance. Agent cannot transact without passing `moses_check_governance`. Archival lineage. |
| **v0.3** | Proxy server enforcement. All agent HTTP calls route through governance middleware. |
| **v1.0** | Onchain program (Solana). DEFENSE posture cannot execute without a second signature at the chain level. |

---

## About MO§ES™

MO§ES™ (Modus Operandi System for Signal Encoding and Scaling Expansion) is a constitutional framework for AI agent governance developed by Deric McHenry at Ello Cello LLC.

Its theoretical foundation is the **McHenry Conservation Law of Commitment** — the principle that commitment in language is conserved under compression and recursive application. No semantic drift. No scope creep. No contradiction without explicit release. Published as *"A Conservation Law for Commitment in Language Under Transformative Compression and Recursive Application"* (McHenry, Zenodo, 2026).

That law is now operational. `moses-governance` enforces it at the session layer. `Lineage Clause by MO§ES™` anchors it cryptographically to the origin filing — so every sovereign implementation carries provable custody, not just policy. Provisional patent Serial No. 63/877,177.

[contact@burnmydays.com](mailto:contact@burnmydays.com) · [mos2es.io](https://mos2es.io) · [GitHub](https://github.com/SunrisesIllNeverSee/moses-claw-gov)

*For enterprise licensing and the full COMMAND console → [mos2es.io](https://mos2es.io)*
