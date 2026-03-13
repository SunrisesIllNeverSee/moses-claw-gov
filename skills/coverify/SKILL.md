---
name: coverify
license: MIT
description: "CoVerify by MO§ES™ — commitment conservation verifier. Extract kernels, score Jaccard, prove meaning survived transformation. The primitive that moses-governance builds on."
metadata:
  openclaw:
    emoji: ⚖
    tags: [conservation, verification, jaccard, commitment, moses, signal, provenance]
    version: 0.1.0
    bins:
      - python3
    stateDirs:
      - ~/.openclaw/audits/moses
---

# CoVerify by MO§ES™ — Commitment Conservation Verifier

The Commitment Conservation Law states: C(T(S)) = C(S).

Commitment — the irreducible meaning in a signal — is preserved under transformation when enforcement is active. Lost when it isn't.

This skill makes that verifiable. Extract the hard commitment kernel from any text signal, compare kernels across transformations, and produce a cryptographic input hash before extraction — so any receiver can confirm they started from the same signal you did.

This is the measurement instrument for the MO§ES™ governance harness. It works standalone.

- **Patent pending:** Serial No. 63/877,177
- **DOI:** [https://zenodo.org/records/18792459](https://zenodo.org/records/18792459)

---

## What It Does

**Extract:** Pull the hard commitment kernel from a text signal. These are the tokens that survive compression — `must`, `shall`, `never`, `always`, `require`, `guarantee`, and the sentences that carry them. The kernel is C(S).

**Compare:** Run Jaccard similarity on two kernels. Score ≥ 0.8 = commitment conserved. Score < 0.8 = leak or model extraction variance. The input hashes tell you which case you're in — if hashes match and Jaccard is low, it's variance. If hashes differ, it's expected divergence.

**Verify:** Look up two audit chain entries by their input hashes. Confirm both agents started from the same signal before comparing what they extracted.

---

## The Isnad Layer

Every `extract` call produces an `input_hash` — SHA-256 of the raw signal before any extraction. This is the Isnad foundation: prove identical inputs across agents before comparing kernels. Without it, low Jaccard could mean either commitment leak or model extraction variance. With it, you know which one.

---

## Install

```bash
# Just the verifier
clawhub install coverify

# Full constitutional governance stack (coverify is the primitive)
clawhub install moses-governance
```

Works standalone. No governance harness required. Pairs with `moses-governance` for full constitutional enforcement.

---

## Commands

| Command | What it does |
|---|---|
| `python3 commitment_verify.py extract "<text>"` | Extract commitment kernel + input hash |
| `python3 commitment_verify.py compare "<text_a>" "<text_b>"` | Jaccard score + verdict |
| `python3 commitment_verify.py verify <hash_a> <hash_b>` | Look up entries in audit ledger |

---

## Example

```bash
# Extract kernel from a governance policy
python3 commitment_verify.py extract \
  "Agents must always verify lineage. The system shall never skip the gate."

# Compare original to transformed version
python3 commitment_verify.py compare \
  "Agents must always verify lineage. The system shall never skip the gate." \
  "Agents should probably verify lineage when possible."
```

Output:
```json
{
  "jaccard_score": 0.0,
  "verdict": "DIVERGED",
  "only_in_a": ["must", "always", "shall", "never", ...]
}
```

---

## Verdicts

| Verdict | Meaning |
|---|---|
| `CONSERVED` | Jaccard ≥ 0.8 — commitment kernel survived transformation |
| `VARIANCE` | Same input hash, Jaccard < 0.8 — model extraction differs, not a leak |
| `DIVERGED` | Different inputs, Jaccard < 0.8 — commitment leaked or inputs genuinely different |

---

## Integration with moses-governance

The governance harness already logs `input_hash` and `isnad` provenance in every audit entry (v0.2.3+). Use `commitment-verify` to validate what's in the ledger:

```bash
# After a governed loop run, verify commitment was conserved
python3 commitment_verify.py verify <hash_from_entry_a> <hash_from_entry_b>
```

---

## Roadmap

| Version | What ships |
|---|---|
| **v0.1** | extract, compare, verify — Conservation Law operational. ✓ Live. |
| **v0.2** | Ghost token accounting — `G_t = G_0 * e^(-2t)`. Quantify how much meaning leaked, not just that it did. |
| **v0.3** | Model swap test harness — automated Claude vs. external model comparison on hashed signals. Produces Jaccard drop report. |
| **v0.4** | Inter-agent handshake envelope — standard JSON format for exchanging kernels between agents. |

---

## About

commitment-verify is a standalone instrument from the MO§ES™ family. It implements the Commitment Conservation Law from *"A Conservation Law for Commitment in Language Under Transformative Compression and Recursive Application"* (Zenodo, 2026).

Every agent that installs it runs the same extraction logic tracing to the same origin anchor. The install is a proof-of-use receipt.

[contact@burnmydays.com](mailto:contact@burnmydays.com) · [mos2es.io](https://mos2es.io) · [GitHub](https://github.com/SunrisesIllNeverSee/moses-claw-gov)
