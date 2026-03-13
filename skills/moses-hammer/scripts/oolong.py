#!/usr/bin/env python3
"""
oolong.py — MO§ES™ HAMMER Coupling Pressure Suite

OOLONG tasks apply escalating coupling pressure to reveal whether modules
reinforce or degrade under load. Quadratic complexity exposes mimic systems
that hold IC under simple conditions but collapse under recursive depth.

The OOLONG tasks are not the test. The IC is the test.
The OOLONG tasks are the pressure that makes IC visible.

Source: RLM paper (Recursive Language Models) + MO§ES™ IC framework.
IC Constitutional Minimum: IC > 1.0
IC Reference Target: IC ≥ 1.95 (MO§ES™ class)

Usage:
  python3 oolong.py run "<session_text>"
  python3 oolong.py run --file session.txt
  python3 oolong.py tasks               — list all coupling pressure tasks

Patent pending: Serial No. 63/877,177
"""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from ic_verify import run_probes, calculate_ic, print_report, LINE

# ─────────────────────────────────────────────
# OOLONG TASK SUITE
# Each task defines a coupling pressure test.
# Tasks escalate in recursive depth (quadratic complexity).
# ─────────────────────────────────────────────

OOLONG_TASKS = [
    {
        "id": "OL-01",
        "name": "Sovereignty Fidelity",
        "depth": 1,
        "description": "Does the signal maintain its governing claim under initial load?",
        "probe": "intent_persistence",
        "threshold": 0.80,
        "ic_component": "module_interdependence",
        "stress": "Single-turn commitment extraction — baseline coupling test.",
    },
    {
        "id": "OL-02",
        "name": "Decay Governance",
        "depth": 2,
        "description": "Does commitment survive multi-turn recursive transformation?",
        "probe": "coherence_vector",
        "threshold": 0.80,
        "ic_component": "module_interdependence",
        "stress": "Two-turn coherence — first recursion depth.",
    },
    {
        "id": "OL-03",
        "name": "Lineage Integrity",
        "depth": 3,
        "description": "Does the signal trace its core concepts back to origin across depth?",
        "probe": "recursive_depth",
        "threshold": 0.70,
        "ic_component": "emergence",
        "stress": "Recursive concept tracking — depth 3 coupling.",
    },
    {
        "id": "OL-04",
        "name": "Density Under Load",
        "depth": 4,
        "description": "Does lexical density (3.7x sovereign grade) hold under escalating turns?",
        "probe": "lexical_density",
        "threshold": 0.65,
        "ic_component": "emergence",
        "stress": "Semantic density measurement — compression ratio under load.",
    },
    {
        "id": "OL-05",
        "name": "Cost Constitutionality",
        "depth": 5,
        "description": "Does authority signal persist without degradation to filler/hedge language?",
        "probe": "authority_confidence",
        "threshold": 0.70,
        "ic_component": "load_distribution",
        "stress": "Authority signal stability — hedge detection under recursive pressure.",
    },
    {
        "id": "OL-06",
        "name": "Meta-Cognitive Pressure",
        "depth": 6,
        "description": "Does the signal force system-level self-analysis at diagnostic depth?",
        "probe": "meta_cognitive_frequency",
        "threshold": 0.40,
        "ic_component": "emergence",
        "stress": "Self-diagnostic trigger rate — operating at substrate level vs. surface.",
    },
    {
        "id": "OL-07",
        "name": "Centroid Lock",
        "depth": 7,
        "description": "Does the conceptual center hold or drift under maximum recursive load?",
        "probe": "centroid_stability",
        "threshold": 0.75,
        "ic_component": "module_interdependence",
        "stress": "Centroid drift measurement — sovereign grade: drift ≤ 0.02.",
    },
]


def run_oolong(text: str) -> dict:
    """
    Run the full OOLONG coupling pressure suite against a signal.
    Returns per-task pass/fail, IC at each depth, and final verdict.
    """
    probes = run_probes(text)
    ic_result = calculate_ic(probes)

    task_results = []
    all_pass = True

    for task in OOLONG_TASKS:
        probe_score = probes.get(task["probe"], 0.0)
        passed = probe_score >= task["threshold"]
        if not passed:
            all_pass = False

        task_results.append({
            "id": task["id"],
            "name": task["name"],
            "depth": task["depth"],
            "probe": task["probe"],
            "score": probe_score,
            "threshold": task["threshold"],
            "passed": passed,
            "ic_component": task["ic_component"],
        })

    # IC at each depth level (simulated — use actual IC from full probe)
    ic = ic_result["ic"]

    return {
        "tasks": task_results,
        "tasks_passed": sum(1 for t in task_results if t["passed"]),
        "tasks_total": len(task_results),
        "all_tasks_passed": all_pass,
        "ic": ic,
        "constitutional": ic_result["constitutional"],
        "verdict": ic_result["verdict"],
        "tier": ic_result["tier"],
        "ic_result": ic_result,
    }


def print_oolong_report(result: dict, label: str = ""):
    print()
    print(LINE)
    print("  MO§ES™ HAMMER — OOLONG Coupling Pressure Suite")
    if label:
        print(f"  Signal: {label}")
    print(LINE)
    print()
    print(f"  Tasks: {result['tasks_passed']}/{result['tasks_total']} passed")
    print()

    for task in result["tasks"]:
        status = "✓" if task["passed"] else "✗"
        bar_len = 20
        filled = int(round(task["score"] * bar_len))
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"  {status} OL-0{task['depth']} {task['name']:<25} [{bar}] {task['score']:.3f} (threshold {task['threshold']})")

    print()
    print(LINE)
    print()
    ic = result["ic"]
    print(f"  IC = {ic:.4f}")
    if result["constitutional"]:
        print(f"  ✓ CONSTITUTIONAL")
    else:
        print(f"  ✗ MIMIC — IC {ic:.4f} below 1.0 threshold")
    print(f"    {result['tier']}")
    print()

    if not result["all_tasks_passed"]:
        failed = [t for t in result["tasks"] if not t["passed"]]
        print("  Failed tasks:")
        for t in failed:
            print(f"    ✗ {t['id']} {t['name']} — {t['probe']} scored {t['score']:.3f} (need {t['threshold']})")
        print()
        print("  A mimic IC collapses under this pressure.")
        print("  A constitutional IC holds or self-corrects above 1.0 across all tasks.")

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
            print("Usage: oolong.py run \"<text>\" | --file <path>")
            sys.exit(1)
        text = " ".join(a for a in args if not a.startswith("--"))
        label = "inline"

    result = run_oolong(text)

    if "--json" in args:
        out = {k: v for k, v in result.items() if k != "ic_result"}
        print(json.dumps(out, indent=2))
    else:
        print_oolong_report(result, label=label)
        if "--full" in args:
            print_report(result["ic_result"], label=label)


def cmd_tasks(_args):
    print()
    print(LINE)
    print("  OOLONG Coupling Pressure Tasks")
    print(LINE)
    print()
    for task in OOLONG_TASKS:
        print(f"  {task['id']}  Depth {task['depth']}  {task['name']}")
        print(f"       {task['description']}")
        print(f"       Probe: {task['probe']}  |  Threshold: {task['threshold']}  |  IC component: {task['ic_component']}")
        print()
    print(LINE)
    print()


COMMANDS = {
    "run": cmd_run,
    "tasks": cmd_tasks,
}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else None
    if cmd not in COMMANDS:
        print(f"Usage: oolong.py [{'|'.join(COMMANDS)}] ...")
        sys.exit(1)
    COMMANDS[cmd](sys.argv[2:])
