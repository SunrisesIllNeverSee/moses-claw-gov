# CHANGELOG — MO§ES™ Constitutional Governance

Tracks substantive builds by date. Commit hashes for full diff.

---

## [Unreleased] — next release tag

---

## v0.6.0 — 2026-03-14

### BUILD-005 — Adversarial Blind Peer Review (`9643bda`)
- `adversarial_review.py` — blind peer review of governed output vs. original instruction commitment kernel
- Verdicts: `CONSERVED` / `FAIL_CASCADE` / `FAIL_LEAK` / `VARIANCE`
- `ghost_pattern` fingerprint: same pattern across two reviewers = structural flaw, not variance
- triall.ai integration: `post_to_triall()` sends blind envelope (kernels + hashes, no agent identity) to external reviewer pool
- `witness.py`: `adversarial-pass` / `adversarial-fail` events route to Moltbook
- `SKILL.md` v0.5.3: env vars `TRIALL_API_KEY`, `TRIALL_ENABLED`, `MOSES_WITNESS_ENABLED` declared

### FIX — coverify version corrected (`1799269`)
- Downgraded version `0.4.1` → `0.3.1` — `archival.py` marked Planned, not Live
- Resolved ClawHub security scanner flag on missing declared file

### BUILD-003 — Ghost token detection wired into governed_step (`b3532ea`)
- `govern_loop.py`: `governed_step()` now calls `commitment_verify.py ghost` before logging
- Ghost token report embedded in audit ledger entries

### BUILD-001 — Meta-governance / Constitutional Amendment Protocol (`7f0baf4`)
- `meta.py` — ported from MCP server. Analyzes audit trail, generates proposals, HMAC-signed apply/rollback
- Immutable `core_principles.json` + amendable `constitution.json` + append-only `amendments.jsonl`
- CLI: `meta.py status|analyze|proposals|sign|apply|reject|rollback`

### BUILD-002 — Commitment Drift Engine (`7f0baf4`)
- `commitment.py` — TF-IDF cosine (sklearn) or Jaccard fallback
- Drift 0–100%: Green (<5%), Yellow (5–20%), Orange (20–40%), Red (>40%)
- CLI: `commitment.py check "<message>" --history "<h1>" --block-threshold 40`
- Exits 1 if threshold exceeded

### BUILD-004 — Stamp Skill (`7f0baf4`)
- `skills/moses-governance/skills/stamp/SKILL.md`
- Embeds governance metadata (mode, posture, role, session ID, action #, SHA-256 integrity hash) into qualifying outputs
- Deactivation: `/stamp off`

---

## 2026-03-13

### v0.5.2 — SKILL.md operator secret documentation fix (`5fbf09f`)
- Corrected `MOSES_OPERATOR_SECRET` documentation contradiction in SKILL.md

### v0.5.1 / v0.4.1 — moses-governance + lineage-claws (`d24d5e5`)
- Lineage: bump to v0.4.1
- Governance: bump to v0.5.1

### v0.4.0 — Archival chain, ghost token spec, falsifiability doc (`0e32885`)
- `archival.py` (lineage v0.2 concept documented)
- `references/ghost-token-spec.md` — standalone ghost token concept
- `references/falsifiability.md` — harness as falsification instrument
- Shannon extension doc
- Handshake presence layer (interpersonal verification)

### v0.3.0 — Inter-agent trust layer (`00147ab`)
- `witness.py` — external witness logger (Moltbook second ledger)
- `presence.py` — presence confirmation protocol
- `handshake.py` — inter-agent envelope with `input_hash` field
- Ghost token detection in `commitment_verify.py`
- `model_swap_test.py` — cross-model CONSISTENT/VARIANCE/STRUCTURAL classification
- `coverify` — standalone skill published to ClawHub

### v0.2.x — Isnad chain + HMAC attestation (`6b625d1` → `a76774b`)
- `lineage_verify.py` — three-layer lineage
- HMAC chain-head attestation for inter-agent trust
- Three Laws of Commitment Conservation named and documented

### v0.2.0 — Governance harness loop (`4e38b9c`)
- `progress.py` + `govern_loop.py` — ReAct-style enforcement loop
- Repositioned as constitutional governance harness (not orchestration)

### v0.1.0 — Initial skill family (`86b1271`)
- `moses-governance`, `lineage-claws` published
- `init_state.py`, `audit_stub.py`, `commitment_verify.py`, `handshake.py`
- SHA-256 chained audit ledger
- Modes, postures, roles reference files

---

## Release Tags

| Tag | Commit | Date | What it marks |
|---|---|---|---|
| *(next)* | — | 2026-03-14 | BUILD-001–005 complete. Adversarial review live. |
| v0.3.0 | `00147ab` | 2026-03-13 | Inter-agent trust layer shipped |
| v0.1.0 | `86b1271` | 2026-03-12 | Initial public skill family |
