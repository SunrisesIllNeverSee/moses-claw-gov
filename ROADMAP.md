# ROADMAP — moses-claw-gov

## Current: v0.4.0

Constitutional governance harness with full three-layer lineage custody,
inter-agent handshake envelope, commitment conservation verification,
ghost token accounting, model swap test, resilience monitoring, archival
provenance chain, and external witness logging.

---

## What Ships in Each Version

### v0.1 — Constitutional Substrate ✓ Live

Prompt-injected, tool-enforced governance. Mode/posture/role hierarchy.
SHA-256 chained audit trail. Works for any agent built to respect the protocol.

### v0.2 — Isnad + Commitment Verification ✓ Live

Signal provenance layer. `input_hash` before extraction. Jaccard kernel comparison.
Ghost token accounting (step-function leakage model). `commitment_verify.py`.

### v0.3 — Inter-Agent Trust Layer ✓ Live

Handshake envelope — standard JSON schema for kernel exchange between agents.
Presence protocol — zombie-proof, interpersonal verification.
Model swap test — CONSISTENT/VARIANCE/STRUCTURAL classification.
Resilience monitoring — fault rate, clustering, posture drift, recovery health.
External witness logging — Moltbook as second ledger.
Pattern registry — structural flaw detection across agents.

### v0.4 — Archival Lineage + Reference Layer ✓ Live

`archival.py` — pre-drop provenance chain (Layer -1). Hashes patent filing,
Zenodo DOI, prior work in chronological sequence. `lineage.py verify` now
reports three layers: `archival → anchor → live ledger`.

Formal reference documents:

- `references/ghost-token-spec.md` — standalone ghost token specification
- `references/falsifiability.md` — harness as falsification instrument
- `references/shannon-extension.md` — formal Shannon extension into semantic domain

Handshake `--with-presence` flag — zombie-proof interpersonal presence wired
into envelope schema. LINEAGE_ANCHOR fixed to real MOSES_ANCHOR.

---

## Next

### v0.5 — Signing Key Inside Governance

> *"The signing key never touches the agent. It only exists inside the governance tool.
> You cannot transfer without governance. That's not a rule — that's the architecture."*

`moses_sign_transaction()` — signing tool with governance gate.
The signing function IS the governance function. No bypass path.

```
Agent wants to transfer →
  calls moses_sign_transaction() →
    governance check runs inside the tool →
      blocked? returns error. permitted? signs + audits.
```

### v0.6 — Governance Proxy Server

Local proxy. All agent HTTP calls route through governance middleware before
hitting external APIs. Posture rules enforced at the network layer, not the
prompt layer.

```
Agent → governance proxy → external API
              ↓
         blocked? 403. permitted? forward + audit.
```

### v1.0 — Onchain Program

Solana program-controlled account. Transfers require a governance state proof.
DEFENSE posture cannot execute without a second signature. Smart contract
enforces it at the chain level — not the application layer.

---

## Feature Backlog

- [ ] `moses_sign_transaction()` — signing tool with governance gate (v0.5)
- [ ] Proxy server with posture enforcement (v0.6)
- [ ] Solana governance program (v1.0)
- [ ] WebSocket coordinator for real-time role sequence enforcement
- [ ] CoVerify ↔ moses-governance dependency declaration in SKILL.md frontmatter
- [ ] `model_swap_test.py` integration into CI
- [ ] ClawHub v2 listing with live demo link

---

*If you want to build on this or fund development: contact@burnmydays.com*
*Patent pending Serial No. 63/877,177 | DOI: https://zenodo.org/records/18792459*
