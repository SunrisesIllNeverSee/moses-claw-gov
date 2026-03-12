# ROADMAP — moses-claw-gov

## Current: v0.1.0
Prompt-injected, tool-enforced governance. Constitutional constraints via MCP server. Audit trail, posture controls, role hierarchy. Works for any agent built to respect the protocol.

---

## Requested / Coming Soon

### Level 1 — Signing Key Inside Governance (v0.2)
> *"The signing key never touches the agent. It only exists inside the governance tool. You cannot transfer without governance. That's not a rule — that's the architecture."*

Move the wallet/signing tool inside the MO§ES™ MCP server. Agent cannot sign a transaction without `moses_check_governance` running first — because the signing function IS the governance function. No bypass path.

```
Agent wants to transfer →
  calls moses_sign_transaction() →
    governance check runs inside the tool →
      blocked? returns error. permitted? signs + audits.
```

**Why it matters:** Converts governance from "laws" to "physics." Agent has no route to the keys without going through the constitution.

---

### Level 2 — Governance Proxy Server (v0.3)
Local proxy. All agent HTTP calls route through governance middleware before hitting external APIs. Posture rules enforced at the network layer, not the prompt layer.

```
Agent → governance proxy → external API
              ↓
         blocked? 403. permitted? forward + audit.
```

---

### Level 3 — Onchain Program (v1.0)
Solana program-controlled account. Transfers require a governance state proof. DEFENSE posture cannot execute without a second signature. Smart contract enforces it at the chain level — not the application layer.

---

## Feature Requests
- [ ] `moses_sign_transaction()` — signing tool with governance gate (Level 1)
- [ ] Proxy server with posture enforcement (Level 2)
- [ ] Solana governance program (Level 3)
- [ ] WebSocket coordinator for real-time role sequence enforcement
- [ ] ClawHub v2 listing with live demo link

---

*If you want to build on this or fund development: contact@burnmydays.com*
*Patent pending Serial No. 63/877,177 | DOI: https://zenodo.org/records/18792459*
