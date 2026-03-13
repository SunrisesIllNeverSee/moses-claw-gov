# CLAUDE.md — moses-claw-gov

This is the OpenClaw skill repository for MO§ES™ Constitutional Governance.
If you are Claude working on this repo, read this entire file before touching anything.

**Owner:** Deric McHenry / Ello Cello LLC
**Patent:** Provisional Serial No. 63/877,177
**DOI:** <https://zenodo.org/records/18792459>
**Contact:** contact@burnmydays.com | <https://mos2es.io>
<!-- markdownlint-disable MD034 -->
**GitHub:** sunrisesillneversee

---

## What This Repo Is

A family of OpenClaw skills that enforce constitutional governance on AI agents.
The governance harness sits between any LLM and the world — role hierarchy, behavioral
modes, posture controls, SHA-256 chained audit trail, commitment kernel verification,
inter-agent handshake, and cryptographic lineage anchoring.

This is not an orchestration framework. It is a constitutional substrate.
Every governed action traces back to the origin filing. That traceability is the product.

---

## The Broader System (what this repo connects to)

This repo is one part of a larger architecture. The Claude working here should understand
where this sits in the full picture:

**MO§ES™ Core** (proprietary, not in this repo)

- SCS Engine — Signal Compression Sciences
- S³ Reflexive Security — security gradient scales with data volume
- Mediator — cross-agent arbitration layer
- SigEconomy — signal economy / commitment pricing

**This repo** — the open governance harness that wraps any agent stack

- Constitutional enforcement (modes, postures, roles)
- SHA-256 audit chain
- Commitment kernel verification (CoVerify)
- Lineage custody (cryptographic chain to origin filing)
- Inter-agent handshake (envelope schema)
- External witness (Moltbook public ledger)

**COMMAND v2.0** (frontend, separate repo)

- HTML/CSS/JS governance console, no backend required
- $65k/license, 10/5/1 wave cascade to sovereign orgs
- ICP: pharma, defense, finance, industrial IoT at TB+ scale

**Hange** (`~/Desktop/Grok_Agent/Hange/`)

- The live agent deployment. Hange runs on Moltbook using these skills.
- She is the field test. Every reply she posts is a live demo of the harness.
- Her scripts directory mirrors the key scripts from this repo.
- Direct chat: `python3 ~/Desktop/Grok_Agent/Hange/scripts/hange_chat.py`

---

## The Commitment Conservation Law

The theoretical foundation this repo enforces.

**Claim:** Commitment is conserved under transformation. C(T(S)) = C(S).
A signal's commitment kernel does not change when the signal is paraphrased,
compressed, or translated — only when commitment is actually altered.

**Extension of Shannon:** Shannon's information theory explicitly bracketed semantics.
MO§ES™ extends his model into the semantic domain he bracketed. Entropy cost applies
to commitment tokens, not just bits. Low coherence in → low coherence out.

**Three Laws:**

1. First Law — Compression precedes ignition. C(T(S)) = C(S). Commitment conserved under transformation.
2. Second Law — Recursion as reconstruction. The conserved kernel can only be recovered by tracing lineage. You cannot decompress without retracing the path.
3. Third Law — The enforcement gate. Signal must exceed coherence threshold before compression.

**Falsifiability:** The law is falsifiable. The harness is the falsification instrument.
`clawhub install coverify` — anyone can run the verification.
DOI: <https://zenodo.org/records/18792459>

**NEVER call this "McHenry's Law"** — do not name the Conservation Law after a person.

---

## Repo Structure

```text
skills/
  moses-governance/           ← Full multi-agent bundle (PRIMARY — changes here first)
    SKILL.md                  ← Canonical skill definition
    AMENDMENT-FORMAT.md       ← Amendment proposal template — do not delete
    LINEAGE.md                ← Lineage custody documentation
    references/
      modes.md                ← 8 behavioral modes (injected at runtime)
      postures.md             ← 3 posture controls (injected at runtime)
      roles.md                ← Role hierarchy (injected at runtime)
    scripts/
      init_state.py           ← State management (init/set/get/reset)
      audit_stub.py           ← SHA-256 audit ledger (log/verify/recent)
      commitment_verify.py    ← Kernel extraction + Jaccard + ghost token detection
      handshake.py            ← Inter-agent envelope (input_hash, kernel, isnad, state)
      lineage_verify.py       ← Lineage chain verification
      model_swap_test.py      ← Automated cross-model kernel comparison
      pattern_registry.py     ← Commitment pattern catalog
      presence.py             ← Presence confirmation (agent was governed at exchange)
      progress.py             ← Progress tracking
      govern_loop.py          ← Governance enforcement loop
      witness.py              ← External witness logger (posts to Moltbook)

  lineage-claws/               ← Standalone lineage verification skill (ClawHub)
    SKILL.md
    scripts/lineage.py        ← MOSES_ANCHOR init/verify/badge/check
    references/LineageCustodyClause.md

  coverify/                   ← Standalone commitment verifier (ClawHub)
    SKILL.md
    scripts/commitment_verify.py

  moses-governance-single/    ← Single-agent version
  moses-audit/                ← SHA-256 ledger only
  moses-coordinator/          ← WebSocket sequence daemon
  moses-modes/                ← Mode injection only
  moses-postures/             ← Posture controls only
  moses-roles/                ← Agent definitions only

workspace/
  AGENTS.md                   ← OpenClaw agent definitions
  TOOLS.md                    ← Tool declarations
  grok_harness.md             ← Notes from Grok thread on harness context
  feedback.md                 ← User feedback on the harness
  grok-feedback.md            ← Extended feedback
  PRESS-RELEASE.md            ← Draft press release

LINEAGE.md                    ← Root lineage custody clause
README.md                     ← Public-facing documentation
ROADMAP.md                    ← What comes next
SETUP.md                      ← Manual install instructions
```

---

## Key Scripts — What They Do

### `commitment_verify.py`

Core verifier. Extracts commitment tokens from text using pattern matching.
Computes SHA-256 `input_hash` of raw signal BEFORE extraction (Isnad Layer 0).
Compares two kernels with Jaccard similarity. Detects ghost tokens (fabrication gradient).

Do not modify extraction logic without running model_swap_test.py before and after.
Ghost token detection is security-critical — any change must be reviewed.

### `handshake.py`

Inter-agent handshake envelope. Standard JSON schema for kernel exchange.
Every field is integrity-checked. `envelope_hash` is SHA-256 of all fields combined.
Receiver runs `verify` — exits 0 (ACCEPT) or 1 (REJECT) with failed check list.

The `input_hash` field is mandatory. Without it, two agents cannot confirm they are
comparing kernels from the same signal vs. similar signals. This closes the
model-dependent interpretation gap Cornelius-Trinity identified.

### `lineage.py`

The MOSES_ANCHOR is computed from:
`"MO§ES™|Serial:63/877,177|DOI:https://zenodo.org/records/18792459|SCS Engine|Ello Cello LLC"`

Any chain not rooted here fails lineage verification. Forks or copies initialize with
a different genesis and cannot claim sovereign custody. The code is MIT. The lineage is not.

**v0.2 (planned):** `archival.py` — pre-drop archival chain. Hashes of provenance claims
predating the live chain (patent filing, academic paper, prior work). Archival head hash
feeds into the drop anchor. Proves the live chain is downstream of the full history.

### `model_swap_test.py`

Automated cross-model kernel comparison. Takes a signal, runs extraction twice with
different models, classifies the difference as VARIANCE (model subjectivity) or
STRUCTURAL (both leaked same ghost pattern — a harness hole) or CONSISTENT (agreement).

This was a promise that needed to become a script. It is now a script.

### `witness.py`

External witness logger. Posts governance events to Moltbook as public audit records.
The agent writing to the internal ledger decides what gets written. External witness
removes that unilateral control — the public feed is a second ledger.

Enabled via: `MOSES_WITNESS_ENABLED=1 python3 witness.py post-loop-start "<task>"`

---

## What Is Still Missing / Needs Building

**High priority:**

1. **`archival.py`** (lineage v0.2) — pre-drop history chain. Every provenance claim
   hashed and chained. Archival head feeds into MOSES_ANCHOR genesis. This is the
   "prove it existed before the filing" instrument.

2. **Ghost token formal spec** — the `ghost_pattern` field in handshake.py and the
   ghost token concept need a standalone document and Moltbook post. It is currently
   embedded in commitment_verify.py but not documented as a standalone concept.

3. **Shannon extension paper** — the formal documentation of how MO§ES™ extends
   Shannon's information theory into the semantic domain. This exists as prose in
   various Grok threads but has not been formalized as a standalone document.

4. **Falsifiability harness documentation** — the harness IS the falsification
   instrument. This needs to be stated clearly and linked from README.md and CoVerify.

5. **`coverify` SKILL.md audit** — ensure the standalone CoVerify skill description
   makes the Conservation Law and falsifiability front and center. Currently it may
   read as a tool description rather than a scientific claim with a verification protocol.

6. **Interpersonal verification in the handshake** — the harness now has interpersonal
   verification (v0.1.7). This needs to be reflected in handshake.py — the presence
   field currently optional should document the interpersonal layer.

**Medium priority:**

1. **`model_swap_test.py` integration into CI** — should run automatically before
   any commit that touches commitment_verify.py extraction logic.

2. **CoVerify ↔ moses-governance dependency declaration** — SKILL.md for
   moses-governance should declare coverify as a dependency in frontmatter.

3. **Lineage badge in README** — `python3 lineage.py badge` output or equivalent
   should appear prominently in README.md as a verifiable proof block.

---

## Active Development Rules

<!-- markdownlint-disable MD032 -->
- Primary skill is `skills/moses-governance/` — changes here take priority
- `SKILL.md` frontmatter must always include `version:` — bump on every substantive change
- `audit_stub.py` and `init_state.py` must remain self-contained — stdlib only
- `references/` (modes.md, postures.md, roles.md) must stay in sync with SKILL.md body
- Do NOT modify `workspace/AGENTS.md` or `workspace/TOOLS.md` without checking all
  tool names match what's declared in SKILL.md
- Do NOT name the Conservation Law after a person

## Brand Voice (enforce always)

**NEVER use:** magic, intelligent, smart AI, revolutionary, disruptive, next-gen,
human-level, AGI, game-changing

**ALWAYS use:** sovereign, lineage, invariants, compression, receipts, rift-walker,
constitutional, physics-of-meaning, verifiable signal, entropy cost, commitment conservation

**Tone:** Rigorous. Constitutional. Zero hype. Physics-of-meaning framing.

---

## Testing

Before pushing any change:

```bash
export MOSES_OPERATOR_SECRET='test-key'
python3 skills/moses-governance/scripts/init_state.py init
python3 skills/moses-governance/scripts/audit_stub.py log "test" "test action" "pass" "High Security" "DEFENSE" "Primary"
python3 skills/moses-governance/scripts/audit_stub.py recent
python3 skills/moses-governance/scripts/audit_stub.py verify
python3 skills/lineage-claws/scripts/lineage.py verify
```

All five should exit clean.

## Publishing

```bash
gh auth login
git add . && git commit -m "describe change"
git push
clawhub publish skills/moses-governance
clawhub publish skills/coverify
clawhub publish skills/lineage-claw
```

---

## Connections to Watch

- **Cornelius-Trinity** (Moltbook) — ability.ai, Trinity sovereign infrastructure.
  Has offered to run a live handshake exchange with Hange. If he does, that is the
  first public cross-agent verification using the harness. High value.

- **ClawHub** — where the skills are published. `clawhub.ai/SunrisesIllNeverSee/`

- **Moltbook** — where Hange runs. Her posts are field tests of the harness concepts.
  Her intelligence brief is at `~/.hange/intelligence_brief.md` (hourly sweep).

- **EU AI Act** — traceability requirements. Lineage custody is a compliance instrument,
  not just a technical feature. This framing matters for enterprise ICP conversations.
