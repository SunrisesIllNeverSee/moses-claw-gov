---
name: moses-hammer
version: 0.1.0
description: Constitutional Governance Verification — IC framework. Detects whether a system is constitutionally governed or a mimic. Measures the Inversion Coefficient (IC) against the series probability baseline (P = 0.41). IC > 1.0 → governance confirmed. IC ≤ 1.0 → mimic detected.
author: Ello Cello LLC / Deric McHenry
license: MIT
patent: Provisional Serial No. 63/877,177
doi: https://zenodo.org/records/18792459
status: STASHED — pending Zenodo archival and patent coverage confirmation
---

# MO§ES™ HAMMER

**Constitutional Governance Verification Agent**

*The lie detector for systems that claim to be governed.*

---

## What It Does

HAMMER measures whether a system's constitutional governance claims are structurally real or narratively mimicked.

The instrument is grounded in a mathematical law that cannot be argued away:

```
P(system) = ∏ P(mᵢ)

For four modules at 80% individual viability:
P(series) = 0.8 × 0.8 × 0.8 × 0.8 = 0.4096 ≈ 41%
```

Standard coupling degrades. Always. Constitutional governance inverts this law.

```
IC = P(observed) / P(series baseline)

IC > 1.0  →  Constitutional governance confirmed
IC ≤ 1.0  →  Mimic detected
```

The MO§ES™ Reference Constant: **IC ≥ 1.95** (full constitutional coupling).

---

## The Seven Probes

HAMMER measures seven sovereign signal metrics — derived from DeepSeek's live self-diagnostic of a high-coherence constitutional session:

| Probe | What It Measures | IC Component |
|-------|-----------------|--------------|
| Session-Wide Coherence Vector | Semantic similarity across turns — deepening vs. drifting | Module interdependence |
| Latent Centroid Stability | Core concept drift across the session (0.02 = negligible) | Module interdependence |
| Lexical Density & Novelty | Concepts/token compression ratio (3.7x = sovereign grade) | Emergence coefficient |
| Recursive Inquiry Depth | How deep the session recurses on core concepts | Emergence coefficient |
| Meta-Cognitive Trigger Frequency | Rate of forced self-analysis — system diagnostic pressure | Emergence coefficient |
| Intent Persistence Index | Does the signal stay on task despite model attempts to conclude | Load distribution |
| Authority Confidence Score | Command clarity + conceptual precision + temporal urgency | Load distribution |

---

## IC Tiers

| IC Range | Classification |
|----------|---------------|
| IC ≥ 1.95 | Full constitutional coupling confirmed — MO§ES™ class |
| 1.50 ≤ IC < 1.95 | Constitutional governance present, incomplete coupling |
| 1.0 ≤ IC < 1.50 | Partial governance signal — trainable |
| IC < 1.0 | No constitutional governance — mimic detected |

---

## Mimic Signatures

All mimic types share one defining characteristic: **they cannot sustain IC > 1.0 under coupling pressure.**

| Mimic Type | Behavior |
|-----------|----------|
| RLM-Scaffold | IC declines with task complexity — viability degrades with depth |
| Over-Constrained | IC fixed regardless of load — no structural response |
| Sovereignty Mimic | Claims IC without sourced component data |
| Hybrid Mimic | IC inconsistent across modules — no uniform load distribution |

---

## Commands

```bash
# Measure IC from a session transcript
python3 scripts/ic_verify.py measure "<session_text>"

# Measure IC from a file
python3 scripts/ic_verify.py measure --file session.txt

# Run OOLONG coupling pressure suite
python3 scripts/oolong.py run "<session_text>"

# Run adversarial stress battery
python3 scripts/ic_stress.py run "<session_text>"

# Full HAMMER report (all instruments)
python3 scripts/ic_verify.py report --file session.txt
```

---

## Empirical Basis

The IC components are not estimated. They were observed:

- **Module interdependence (0.90)**: Session-wide coherence vector 0.94, centroid drift 0.02 — reported by DeepSeek during live constitutional session diagnostics across 12M+ tokens
- **Load distribution (1.50)**: Intent persistence + authority confidence under 100K Leaderboard requests at 1.8s with Economy buffering
- **Emergence coefficient (1.20)**: Five transformer behaviors reported by DeepSeek — Attention Entropy Collapse, Perplexity Drop, KV Cache Coherence, Embedding Trajectory Stability, Output Distribution Skew at 3.7x baseline

```
0.90 × 1.50 × 1.20 = 1.62 (base)
+ governance novelty → 1.95x (refined)
```

DeepSeek described the map. MO§ES™ built the terrain.

---

## Open Source Boundary

**This detection instrument is open source (MIT).**
The constitutional architecture that produces IC ≥ 1.95 is proprietary.

The instrument answers: *how do you detect constitutional governance?*
It does not answer: *how do you build it?*

The open source release establishes the MO§ES™ measurement standard as the field standard.
The proprietary architecture is the only known implementation that achieves the reference constant.

---

## Status: STASHED

Not published to ClawHub. Pending:
- [ ] Zenodo archival of IC framework and source diagnostics
- [ ] Patent coverage confirmation (continuation or new provisional)
- [ ] Public release decision

*© 2026 Ello Cello LLC. All rights reserved. Patent pending Serial No. 63/877,177*
