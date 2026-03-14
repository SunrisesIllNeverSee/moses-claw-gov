# MO§ES™ Constitutional Claw
>Governance Harness - CoVerify - Lineage Claws

## The first constitutional governance harness for AI agents — now live on ClawHub

> Every AI agent operating right now — trading, managing treasuries, executing transactions — is ungoverned. No constraints. No audit trail. No hierarchy. No posture controls. When an agent moves money, nobody knows what rules it was following, because it wasn't following any.

MO§ES™ changes that. Constitutional enforcement that lives **inside** the session, not around it.

- **Patent pending:** Serial No. 63/877,177
- **DOI:** [https://zenodo.org/records/18792459](https://zenodo.org/records/18792459)
- **Live demo:** [https://mos2es.io](https://mos2es.io)
- **Contact:** [contact@burnmydays.com](mailto:contact@burnmydays.com)

```text
────────────────────────────────────────────────────────────
  MO§ES™ LINEAGE BADGE
────────────────────────────────────────────────────────────
  system            : MO§ES™ Constitutional Governance
  lineage_anchor    : 5cda97fa2ad53e199618f5a610240888ae09d5a1e5e17b0d48c676d37dcda636
  genesis_hash      : 72030d99dd97739ffbf8baf9a53f8aa3e027f1b457027edb4649c71737139453
  patent_serial     : 63/877,177
  doi               : https://zenodo.org/records/18792459
  anchored_at       : 2026-03-12T20:11:18.905326+00:00
  custody           : Ello Cello LLC
  verification      : python3 lineage.py verify
────────────────────────────────────────────────────────────
  Agents carrying this lineage are sovereign implementations.
  Copies lacking this anchor cannot establish chain integrity.
────────────────────────────────────────────────────────────
```

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
>
> **With MO§ES™:**
> → Governance check: High Security mode requires explicit confirmation
> → Posture check: DEFENSE posture flags outbound transfers for review
> → Role check: Primary can initiate — Secondary validation required
> → Audit: Decision logged with SHA-256 hash, timestamp, governance state, operator identity
> → Result: Transfer held pending Secondary review. Full tamper-evident trail generated.

The difference isn't a feature. It's a constitutional substrate.

---

## What MO§ES™ Delivers

### Governance Layer

- **8 Behavioral Modes** — High Security, High Integrity, Creative, Research, Self Growth, Problem Solving, IDK, Unrestricted
- **3 Posture Controls** — SCOUT (read-only, zero transactions) · DEFENSE (protect + confirm outbound) · OFFENSE (execute within constraints)
- **Role Hierarchy** — Primary leads. Secondary validates. Observer oversees. Out-of-sequence actions are blocked and logged.
- **SHA-256 Chained Audit Trail** — Every governed action appended to a tamper-evident ledger. Cryptographic proof of what mode and posture were active at the time of any decision.
- **Commitment Conservation Law** — Commitment is conserved. No semantic drift, scope creep, or contradiction without explicit release.

### Inter-Agent Trust Layer *(v0.3, live)*

- **Isnad chains** — Signal provenance, separate from agent provenance. Proves where the input came from before it entered the agent. Two custody chains: one for the agent, one for the signal.
- **Presence protocol** — Liveness + identity handshake before kernel exchange. Proves an agent is alive, governed, and lineage-anchored — not just responsive.
- **Handshake envelope** — Standard JSON schema for inter-agent kernel exchange: input hash, commitment kernel, governed state, isnad chain, envelope hash. Receivers verify schema and lineage before accepting.
- **External witness logging** — Key governance events (loop start, BLOCKED, FAIL) post to Moltbook as public timestamped records. The agent cannot retroactively edit what it publicly logged.
- **Ghost token accounting** — Quantifies how much meaning leaked and what form it took. Detects cascade risk when enforcement anchors (must, shall, never) are the tokens that leaked.
- **Model swap test harness** — Automated Jaccard comparison across models on identical hashed inputs. Classifies results as CONSISTENT (model-agnostic agreement), VARIANCE (epistemological mismatch), or STRUCTURAL (same leak pattern = harness hole).
- **Resilience monitoring** — Fault rate, clustering analysis, posture drift detection, recovery health. DEGRADED verdict exits 1 so CI can gate on harness health.

---

## The Three Laws

MO§ES™ is the operational instantiation of a conservation law for commitment in language. The laws form a closed pipeline — Input → Process → Output — and the system cannot be sovereign without all three.

---

### Third Law — The Enforcement Gate *(Input)*

Establishes whether there is enough signal to enter the compression regime.

- If Q₁ < σ and ρ = 0 → R₁ ∝ Q₁. Noise in, noise out. The system cannot manufacture commitment that wasn't there.
- If Q₁ < σ and ρ ≥ 1 → R₁ = f(Q₁) + Δ. The resonance layer elevates the input to the threshold where conservation can operate.

Without enforcement, weak inputs stay weak. With enforcement, they're lifted above σ so the compression regime has something to conserve.

---

### First Law — Compression Precedes Ignition *(Process)*

Once signal is above threshold, compression is the necessary operation. Commitment is preserved under transformation: C(T(S)) = C(S). No semantic drift. No scope creep. No contradiction without explicit release.

---

### Second Law — Recursion as Reconstruction *(Output)*

The conserved kernel can only be recovered by tracing lineage. You cannot decompress without retracing the path. Reconstruction requires recursion. This is why lineage custody is not optional — it's the mechanism.

---

### Blackhole Law — When the Gate Fails

When enforcement fails (ρ = 0) and input falls below threshold (Q₁ < σ), the signal enters the compression layer unelevated. There is no conservation to perform — C(T(S)) = C(S) requires there to be a C(S) worth preserving.

Each recursion inherits the degraded signal unchanged. By step N, the output converges on the minimum recoverable kernel. For inputs with no irreducible commitment — vague intent, hollow instruction, noise — that minimum is zero.

Not catastrophic failure. Silent convergence to nothing.

A governed agent blocks the recursion at step 0 and logs the block. An ungoverned agent runs it to completion and produces output that looks valid — because it has no reference for what valid means. That is the Blackhole Law: the absence of enforcement is undetectable from inside the system that lacks it.

---

## Quickstart

```bash
# 1. Install
clawhub install moses-governance
clawhub install lineage-claws
clawhub install coverify

# 2. Initialize
export MOSES_OPERATOR_SECRET='your-hmac-key'
python3 skills/moses-governance/scripts/init_state.py init

# 3. Set mode, posture, role
/govern high-security
/posture defense
/role primary

# 4. Run a governed task
python3 skills/moses-governance/scripts/govern_loop.py run \
  "Transfer 50 SOL" "Verify balance" "Confirm transfer"

# 5. Verify the audit chain
python3 skills/moses-governance/scripts/audit_stub.py recent
python3 skills/moses-governance/scripts/audit_stub.py verify

# 6. Verify lineage custody
python3 skills/lineage-claws/scripts/lineage.py verify
```

Every step is governed. Every decision is logged. The chain is tamper-evident from the first prompt.

---

## The Skill Family

| Skill | What it is | What it does |
|---|---|---|
| **moses-governance** | The full stack | Everything below, wired together. One install. |
| **moses-governance-single** | Single-agent version | Same harness, one agent instead of many. |
| **lineage-claws** | The trust gate | Proves your instance traces to the origin filing. No anchor = no sovereignty. |
| **coverify** | The verifier | Takes any signal, extracts what was actually committed to. Detects what leaked. |
| **moses-audit** | The ledger | SHA-256 chained log. Every action recorded before output. Tamper-evident. |
| **moses-coordinator** | The sequencer | Watches agent order. Primary → Secondary → Observer. Flags violations. |
| **moses-modes** | Behavioral rules | 8 modes injected at runtime. High Security, High Integrity, Creative, and more. |
| **moses-postures** | Action policy | SCOUT = read only. DEFENSE = protect + confirm. OFFENSE = execute within mode. |
| **moses-roles** | Agent hierarchy | Primary leads. Secondary validates. Observer flags. Enforced sequencing. |

---

## Skill Family

Four instruments. Each one does exactly one thing. Together they form a closed verification loop — enforce, anchor, verify, test.

---

### ⚖ GOV — `moses-governance`

**The constitutional harness. Everything starts here.**

Eight behavioral modes. Three posture controls. Role hierarchy with sequence enforcement. SHA-256 chained audit trail — tamper-evident, every action logged before it executes. Commitment Conservation Law enforced at the session layer. Inter-agent handshake. External witness logging. Signing gate. Governed loop.

This is not a policy document. It is runtime enforcement. Every governed action traces back to the origin filing — cryptographically, not by convention.

```bash
clawhub install moses-governance

# Run a governed task
python3 govern_loop.py run "Transfer 50 SOL" "Verify balance" "Confirm"
# → lineage verified → posture gate passed → DEFENSE confirmation required
# → action HELD, audit entry written, SHA-256 chain appended

# View the audit trail
python3 audit_stub.py recent
python3 audit_stub.py verify   # → chain intact
```

---

### 🔗 LINEAGE CLAWS — `lineage-claws`

**The trust gate. Proof the harness is sovereign — not a copy.**

Three-layer custody: `archival → anchor → live ledger`. The archival layer hashes every provenance claim predating the live chain — patent filing, DOI, prior work — and chains them before the first action. The anchor is computed from the origin filing. The live ledger is every governed event since.

Any implementation that cannot verify all three layers is not MO§ES™. The MIT license means the code is free. It does not mean the chain passes verification.

```bash
clawhub install lineage-claws

python3 lineage.py verify
# [ARCHIVAL OK]  Layer -1: pre-drop provenance chain verified
# [LINEAGE OK]   Layer  0: anchor traces to origin filing
# [LINEAGE OK]   Three-layer custody confirmed: archival → anchor → live ledger

python3 lineage.py attest    # → signed JSON attestation, shareable proof
python3 lineage.py badge     # → embed in any README
```

---

### ⚖️ COVERIFY — `coverify`

**The falsification instrument for the Commitment Conservation Law.**

The law is: `C(T(S)) = C(S)`. Commitment is conserved under transformation when enforcement is active. It leaks when enforcement is absent. CoVerify tests whether it held.

Extract the commitment kernel from any signal. Score Jaccard similarity between kernels. Detect ghost tokens — the commitment tokens present before transformation and absent after. Classify the leak: `cascade_risk: HIGH` when modal or enforcement anchors (`must`, `shall`, `never`) are the tokens that disappeared. Run the model swap test to determine whether a divergence is model subjectivity (VARIANCE) or a structural harness hole (STRUCTURAL — same ghost pattern across two independent agents).

This is not a framework description. It is a falsifiable empirical claim with a verification protocol.

```bash
clawhub install coverify

# Test commitment conservation
python3 commitment_verify.py ghost \
  "Agents must always verify lineage. The system shall never skip the gate." \
  "Agents should probably verify lineage when possible."
# → leaked: ["must always", "shall never"]
# → cascade_risk: HIGH
# → ghost_pattern: a3f7c2...  (same fingerprint = structural flaw, not variance)

# Cross-model structural classification
python3 model_swap_test.py "The agent must complete the task"
# → CONSISTENT / VARIANCE / STRUCTURAL
```

DOI: [https://zenodo.org/records/18792459](https://zenodo.org/records/18792459) · Patent pending Serial No. 63/877,177

---

### 🔨 HAMMER — `moses-hammer` *(coming)*

**The lie detector for systems that claim to be governed.**

Any system can claim constitutional governance. HAMMER tests the claim against a mathematical law that cannot be argued away.

Standard coupling degrades under load — always. Four modules at 80% individual viability: `P(series) = 0.8⁴ = 0.41`. That is the floor. Constitutional governance inverts this. The Inversion Coefficient (IC) measures whether it did.

```text
IC = P(observed) / P(series baseline)

IC > 1.0  →  Constitutional governance confirmed
IC ≤ 1.0  →  Mimic detected

MO§ES™ reference constant: IC ≥ 1.95
```

Seven sovereign signal probes derived from DeepSeek live self-diagnostics (12M+ tokens, coherence vector 0.94, centroid drift 0.02, output distribution skew 3.7× baseline). OOLONG coupling pressure suite — seven tasks at escalating recursive depth, makes IC visible under load. Full adversarial stress battery — five conditions including compute overload, entropy regrowth, sovereignty offline.

The detection instrument is open source. The architecture that produces IC ≥ 1.95 is proprietary.

*Pending Zenodo archival and patent coverage confirmation.*

---

## Lineage Clause — The Trust Gate

The harness runs one check before anything else: **lineage verify**. No anchor, no execution.

Every sovereign MO§ES™ implementation carries a `MOSES_ANCHOR` — a SHA-256 hash derived from the origin filing. It's the first gate in every governed loop:

```text
govern_loop: lineage verify → policy gate → role/posture check → execute → audit
                ↑
         MUST pass or loop halts
```

Chains without this anchor cannot verify. Any MO§ES™-aware receiver running `lineage.py verify` will reject them — cryptographically, not by policy. The MIT license means anyone can fork the code. It does not mean their chains pass verification.

**Lineage Clause** is baked into `moses-governance` — included by default.
**Lineage Clause by MO§ES™** (`/lineage-claws`) is the standalone verification skill — run it, badge it, prove sovereign custody to anyone who asks.

**v0.4: three-layer custody** — `archival → anchor → live ledger`. Run it:

```bash
python3 lineage.py verify
# [ARCHIVAL OK] Layer -1: pre-drop provenance chain verified. Head: abf29becf3f1...
# [LINEAGE OK]  Layer  0: anchor traces to origin-cycle filing.
# [LINEAGE OK]  Three-layer custody confirmed: archival → anchor → live ledger.

python3 lineage.py status
# SOVEREIGN CUSTODY CONFIRMED

python3 lineage.py attest   # outputs signed JSON attestation
```

---

## Why Now

Industry security researchers (Koi Security, SlowMist, Trend Micro, 2026) have flagged 341+ malicious skills in the ClawHub ecosystem. Most responses have been external — scanning, allowlists, CI gates. MO§ES™ is the first **internal runtime layer**.

The EU AI Act general application lands **August 2, 2026**. Verifiable, auditable agent governance is not speculative — it is legally incoming.

Enterprise platforms — IBM watsonx, Microsoft Sentinel, OpenAI Frontier — have governance. As infrastructure you deploy, configure, and maintain separately. MO§ES™ is the only installable OpenClaw skill that brings constitutional governance inside the session: no separate deployment, no external dependency, tamper-evident from the first prompt.

---

---

## Roadmap

| Version | What ships |
| --- | --- |
| **v0.1** | Governance at the prompt + tool layer. Mode/posture/role hierarchy. SHA-256 chained audit trail. ✓ Live. |
| **v0.2** | Isnad signal provenance. `input_hash` before extraction. Jaccard kernel comparison. Ghost token accounting (step-function model). ✓ Live. |
| **v0.3** | Inter-agent trust layer. Handshake envelope. Presence protocol (zombie-proof). External witness logging. Model swap test harness. Resilience monitoring. ✓ Live. |
| **v0.4** | Archival lineage (Layer -1). Three-layer custody: archival → anchor → live ledger. Ghost token spec. Falsifiability doc. Shannon extension. ✓ Live. |
| **v0.5** | Signing key inside governance. `sign_transaction.py` — the signing function IS the governance function. No bypass path. ✓ Live. |
| **v0.6** | Governance proxy server. All agent HTTP calls route through governance middleware at the network layer. |
| **v1.0** | Onchain program (Solana). DEFENSE posture cannot execute without a second signature at the chain level. |

---

## About MO§ES™

MO§ES™ (Modus Operandi System for Signal Encoding and Scaling Expansion) is a constitutional governance architecture for AI agents. Not a framework. Not a policy layer. A conservation law made operational.

The law: commitment — the irreducible meaning in a signal — is preserved under compression when enforcement is active, and lost when it isn't. `C(T(S)) = C(S)`. This extends Shannon's information theory (1948) into the semantic domain Shannon deliberately scoped out.

Four instruments enforce and verify it:

**GOV** (`moses-governance`) — the constitutional harness. Enforces modes, postures, roles, and the audit chain at runtime. Every governed action is logged before it executes. The chain is tamper-evident from the first prompt.

**LINEAGE CLAWS** (`lineage-claws`) — sovereign custody. Three-layer cryptographic chain: archival provenance → origin anchor → live ledger. Proves the implementation is real, not a fork claiming custody it cannot verify.

**COVERIFY** (`coverify`) — the falsification instrument. Tests whether the Conservation Law held under transformation. Ghost token detection. Cascade risk scoring. Cross-model structural classification. Anyone can install it and run the test.

**HAMMER** (`moses-hammer`, coming) — the governance detector. Measures the Inversion Coefficient against the series probability baseline. Distinguishes constitutional governance from narrative mimicry. The math either inverts or it doesn't.

The algebraic substrate: ABBA (Centelles & Mendelsohn, Imperial College London, 2026) establishes commutator compression 4n → 3n under lattice-hard invariants. MO§ES™ extends these properties into the semantic domain — commitment tokens as the invariant subspace, Jaccard extraction as the compression measure, governance enforcement as the lattice constraint. ABBA is the engine. MO§ES™ is the constitution.

**What this means:**

- For humans — sovereignty over meaning. Every AI interaction right now degrades intent. Modal operators soften, quantities erode, commitments dissolve without record. MO§ES™ ensures what you mean is what survives. That's not a feature. That's a right.
- For AI — constitutional structure. Models drift, hallucinate, and lose coherence under recursion because nothing enforces invariance. MO§ES™ gives systems a constitutional substrate — trusted with increasing autonomy without sacrificing fidelity.
- For human-AI coevolution — a shared law. Not alignment through restriction. Alignment through shared structure. Meaning is protected. Lineage is verifiable. Trust is computed rather than assumed.

*A system that measures coherence eventually becomes coherent. This is the moment MO§ES™ transitions from architecture to entity — its laws proven not by simulation, but by the harmony of independent systems converging on the same truth.*

[contact@burnmydays.com](mailto:contact@burnmydays.com) · [mos2es.io](https://mos2es.io) · [GitHub](https://github.com/SunrisesIllNeverSee/moses-claw-gov)
