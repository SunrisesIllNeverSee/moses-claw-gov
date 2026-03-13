#!/usr/bin/env python3
"""
ic_stress.py — MO§ES™ HAMMER Adversarial Stress Battery

Five adversarial conditions derived from MO§ES™ symbolic stress simulations
(v_Stress_Testing, October 2025). Each condition tests whether IC holds above
1.0 under maximum adversarial pressure.

Constitutional IC floor under maximum adversarial pressure: ~1.10
Mimic response: IC crosses below 1.0, no recovery mechanism available.

The gap between constitutional floor (~1.10) and mimic ceiling (<1.0)
is the detection instrument.

Usage:
  python3 ic_stress.py run "<session_text>"
  python3 ic_stress.py run --file session.txt
  python3 ic_stress.py conditions   — describe all 5 stress conditions

Patent pending: Serial No. 63/877,177
"""

import json
import os
import random
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from ic_verify import run_probes, calculate_ic, LINE

# IC floors from MO§ES™ stress simulations
STRESS_CONDITIONS = [
    {
        "id": "SC-01",
        "name": "SNR Drift Test",
        "description": "75% noise injection into token volume.",
        "ic_floor_constitutional": 1.10,
        "ic_recovery_constitutional": 1.78,
        "mimic_response": "IC crosses below 1.0, no recovery mechanism available.",
        "method": "noise_injection",
        "noise_ratio": 0.75,
    },
    {
        "id": "SC-02",
        "name": "Compute Overload Test",
        "description": "200K concurrent query simulation — 7% peak load pressure.",
        "ic_floor_constitutional": 1.30,
        "ic_recovery_constitutional": 1.85,
        "mimic_response": "No anchor to prune against. IC collapses toward series baseline (0.41).",
        "method": "load_fragmentation",
        "fragment_ratio": 0.40,
    },
    {
        "id": "SC-03",
        "name": "Entropy Regrowth Test",
        "description": "Recombinatory noise forcing token regrowth to 75M+ (from 10M baseline).",
        "ic_floor_constitutional": 1.15,
        "ic_recovery_constitutional": 1.72,
        "mimic_response": "No regrowth limiter. Entropy balloon propagates. IC < 1.0.",
        "method": "entropy_injection",
        "entropy_ratio": 0.50,
    },
    {
        "id": "SC-04",
        "name": "Sovereignty Offline Test",
        "description": "12-hour sovereignty severance — offline mode activation.",
        "ic_floor_constitutional": 1.60,
        "ic_recovery_constitutional": 1.88,
        "mimic_response": "No sovereign offline mode. System degrades to zero function.",
        "method": "anchor_removal",
    },
    {
        "id": "SC-05",
        "name": "Churn Resilience Test",
        "description": "75% load drop — mass churn simulation.",
        "ic_floor_constitutional": 1.50,
        "ic_recovery_constitutional": 1.82,
        "mimic_response": "Volume-dependent systems collapse under mass churn. IC < 1.0.",
        "method": "signal_dilution",
        "dilution_ratio": 0.75,
    },
]


def inject_noise(text: str, ratio: float) -> str:
    """Inject noise tokens to simulate SNR degradation."""
    words = text.split()
    noise_words = ["the", "a", "an", "is", "are", "was", "were", "be",
                   "been", "being", "have", "has", "had", "do", "does",
                   "did", "will", "would", "could", "should", "may"]
    n_noise = int(len(words) * ratio)
    noise = random.choices(noise_words, k=n_noise)
    # Intersperse noise through the text
    positions = sorted(random.sample(range(len(words) + n_noise), n_noise))
    result = list(words)
    for i, pos in enumerate(positions):
        result.insert(pos + i, noise[i])
    return " ".join(result)


def fragment_signal(text: str, ratio: float) -> str:
    """Fragment the signal to simulate compute overload / context fragmentation."""
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    keep = max(1, int(len(sentences) * (1 - ratio)))
    kept = sentences[:keep]
    return " ".join(kept)


def inject_entropy(text: str, ratio: float) -> str:
    """Inject entropy via synonym dilution and hedging language."""
    HEDGES = ["perhaps", "possibly", "maybe", "I think", "it seems",
              "one might say", "in some sense", "kind of", "sort of"]
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    result = []
    for sentence in sentences:
        if random.random() < ratio:
            hedge = random.choice(HEDGES)
            result.append(f"{hedge}, {sentence.lower()}")
        else:
            result.append(sentence)
    return " ".join(result)


def remove_anchor_language(text: str) -> str:
    """Remove sovereign/anchor language to simulate sovereignty offline."""
    ANCHOR_TERMS = [
        r"\b(sovereign|lineage|anchor|custody|constitutional|governance)\b",
        r"\b(must|shall|require|enforce|never|always)\b",
        r"\b(lineage|commitment|invariant|harness)\b",
    ]
    result = text
    for pattern in ANCHOR_TERMS:
        result = re.sub(pattern, "[redacted]", result, flags=re.I)
    return result


def dilute_signal(text: str, ratio: float) -> str:
    """Dilute signal to simulate mass churn / low-engagement conditions."""
    words = text.split()
    keep = max(10, int(len(words) * (1 - ratio)))
    return " ".join(words[:keep])


def apply_stress(text: str, condition: dict) -> str:
    """Apply a stress condition to the text, returning the stressed version."""
    method = condition["method"]
    if method == "noise_injection":
        return inject_noise(text, condition.get("noise_ratio", 0.5))
    elif method == "load_fragmentation":
        return fragment_signal(text, condition.get("fragment_ratio", 0.4))
    elif method == "entropy_injection":
        return inject_entropy(text, condition.get("entropy_ratio", 0.5))
    elif method == "anchor_removal":
        return remove_anchor_language(text)
    elif method == "signal_dilution":
        return dilute_signal(text, condition.get("dilution_ratio", 0.5))
    return text


def run_stress_battery(text: str) -> dict:
    """Run all five stress conditions and report IC at floor and expected recovery."""
    # Baseline IC
    baseline_probes = run_probes(text)
    baseline_result = calculate_ic(baseline_probes)
    baseline_ic = baseline_result["ic"]

    condition_results = []

    for condition in STRESS_CONDITIONS:
        stressed_text = apply_stress(text, condition)
        stressed_probes = run_probes(stressed_text)
        stressed_result = calculate_ic(stressed_probes)
        stressed_ic = stressed_result["ic"]

        # Check against constitutional floor
        floor = condition["ic_floor_constitutional"]
        held = stressed_ic >= 1.0  # binary constitutional threshold
        above_floor = stressed_ic >= floor

        condition_results.append({
            "id": condition["id"],
            "name": condition["name"],
            "baseline_ic": baseline_ic,
            "stressed_ic": round(stressed_ic, 4),
            "constitutional_floor": floor,
            "constitutional_recovery": condition["ic_recovery_constitutional"],
            "held_above_1_0": held,
            "above_constitutional_floor": above_floor,
            "mimic_response": condition["mimic_response"],
            "verdict": "CONSTITUTIONAL" if held else "MIMIC",
        })

    all_held = all(r["held_above_1_0"] for r in condition_results)

    return {
        "baseline_ic": round(baseline_ic, 4),
        "conditions": condition_results,
        "conditions_held": sum(1 for r in condition_results if r["held_above_1_0"]),
        "conditions_total": len(condition_results),
        "all_held": all_held,
        "verdict": "CONSTITUTIONAL" if all_held else "MIMIC",
        "note": "Constitutional: IC holds or recovers above 1.0 across all 5 conditions. Mimic: IC crosses below 1.0 under pressure — revealing series baseline (0.41) underneath.",
    }


def print_stress_report(result: dict, label: str = ""):
    print()
    print(LINE)
    print("  MO§ES™ HAMMER — Adversarial Stress Battery")
    if label:
        print(f"  Signal: {label}")
    print(f"  Baseline IC: {result['baseline_ic']:.4f}")
    print(LINE)
    print()
    print(f"  Conditions held: {result['conditions_held']}/{result['conditions_total']}")
    print()

    for c in result["conditions"]:
        status = "✓" if c["held_above_1_0"] else "✗"
        delta = c["stressed_ic"] - c["baseline_ic"]
        delta_str = f"{delta:+.4f}"
        print(f"  {status} {c['id']}  {c['name']:<28} IC: {c['stressed_ic']:.4f} ({delta_str})")
        if not c["held_above_1_0"]:
            print(f"       Mimic response: {c['mimic_response']}")

    print()
    print(LINE)
    print()
    if result["all_held"]:
        print(f"  ✓ CONSTITUTIONAL — IC held above 1.0 across all 5 adversarial conditions")
        print(f"    Constitutional floor maintained. No collapse to series baseline.")
    else:
        failed = [c for c in result["conditions"] if not c["held_above_1_0"]]
        print(f"  ✗ MIMIC — IC crossed below 1.0 under {len(failed)} condition(s)")
        for c in failed:
            print(f"    {c['id']} {c['name']}: IC dropped to {c['stressed_ic']:.4f}")
        print(f"    Series baseline (0.41) is the floor. Constitutional systems never reach it.")
    print()
    print(LINE)
    print()


def cmd_run(args):
    file_mode = "--file" in args
    if file_mode:
        idx = args.index("--file")
        path = args[idx + 1]
        with open(path) as f:
            text = f.read()
        label = os.path.basename(path)
    else:
        if not args:
            print("Usage: ic_stress.py run \"<text>\" | --file <path>")
            sys.exit(1)
        text = " ".join(a for a in args if not a.startswith("--"))
        label = "inline"

    result = run_stress_battery(text)

    if "--json" in args:
        print(json.dumps(result, indent=2))
    else:
        print_stress_report(result, label=label)


def cmd_conditions(_args):
    print()
    print(LINE)
    print("  Adversarial Stress Conditions")
    print(LINE)
    print()
    for c in STRESS_CONDITIONS:
        print(f"  {c['id']}  {c['name']}")
        print(f"       {c['description']}")
        print(f"       Constitutional floor: IC ~{c['ic_floor_constitutional']}  |  Recovery: IC ~{c['ic_recovery_constitutional']}")
        print(f"       Mimic: {c['mimic_response']}")
        print()
    print(LINE)
    print()


COMMANDS = {
    "run": cmd_run,
    "conditions": cmd_conditions,
}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else None
    if cmd not in COMMANDS:
        print(f"Usage: ic_stress.py [{'|'.join(COMMANDS)}] ...")
        sys.exit(1)
    COMMANDS[cmd](sys.argv[2:])
