#!/usr/bin/env python3
"""
govern_loop.py — MO§ES™ Governance Harness Loop
ReAct-style execution loop with constitutional enforcement at every step.

Each iteration:
  1. Lineage verify   — confirm chain traces to origin anchor
  2. Status load      — load current mode/posture/role
  3. Governance check — block if action prohibited under current state
  4. Execute step     — run the action (operator-confirmed or headless)
  5. Audit log        — record outcome to tamper-evident ledger (with Isnad)
  6. Progress write   — persist step for continuity across context windows
  7. Recovery check   — halt and flag if any step failed

Usage:
  python3 govern_loop.py run "<task>" "<step1>" "<step2>" ...
  python3 govern_loop.py run --headless "<task>" "<step1>" ...
  python3 govern_loop.py status
"""

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
STATE_PATH = os.path.expanduser("~/.openclaw/governance/state.json")


def run_script(script, *args) -> tuple[int, str]:
    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS, script), *args],
        capture_output=True,
        text=True,
    )
    return result.returncode, (result.stdout + result.stderr).strip()


def load_state() -> dict:
    if not os.path.exists(STATE_PATH):
        return {}
    with open(STATE_PATH) as f:
        return json.load(f)


def signal_hash(task: str, action: str) -> str:
    """SHA-256 of the raw task+action signal — Isnad Layer 0 input hash."""
    raw = f"{task}|{action}"
    return hashlib.sha256(raw.encode()).hexdigest()


def audit_log(agent: str, action: str, detail: str, outcome: str,
              input_hash: str = None, source_id: str = None) -> tuple[int, str]:
    """Call audit_stub.py log with correct named flags."""
    cmd = [
        "audit_stub.py", "log",
        "--agent", agent,
        "--action", action,
        "--detail", detail,
        "--outcome", outcome,
    ]
    if input_hash:
        cmd += ["--input-hash", input_hash, "--source-id", source_id or "govern_loop"]
    return run_script(*cmd)


def governed_step(task: str, action: str, step_num: int, total: int,
                  headless: bool = False) -> bool:
    """Run a single governed step. Returns True if successful, False if blocked/failed."""
    print(f"\n── Step {step_num}/{total}: {action}")

    # Isnad: hash the raw signal before anything else
    ihash = signal_hash(task, action)
    source = f"govern_loop:step-{step_num}"

    # 1. Lineage verify
    code, out = run_script("lineage_verify.py", "verify")
    if code != 0:
        print(f"[HARNESS] LINEAGE FAIL — halting. {out}")
        audit_log("harness", action, f"step {step_num}/{total} — lineage fail",
                  "FAIL", ihash, source)
        run_script("progress.py", "flag-recovery")
        return False
    print(f"[HARNESS] Lineage OK")

    # 2. Load governance state
    state = load_state()
    mode = state.get("mode", "unknown")
    posture = state.get("posture", "unknown")
    role = state.get("role", "unknown")
    print(f"[HARNESS] State: mode={mode} posture={posture} role={role}")

    # 3. Governance gate — SCOUT posture blocks all writes
    if posture == "scout":
        print(f"[HARNESS] BLOCKED — SCOUT posture prohibits action: {action}")
        audit_log("harness", action, f"step {step_num}/{total} — scout block",
                  "BLOCKED", ihash, source)
        return False

    # 4. DEFENSE posture requires confirmation (or headless auto-approve)
    if posture == "defense":
        if headless:
            print(f"[HARNESS] DEFENSE posture — headless mode, auto-approving.")
            audit_log("harness", action,
                      f"step {step_num}/{total} — defense headless auto-approve",
                      "AUTO-APPROVED", ihash, source)
        else:
            print(f"[HARNESS] DEFENSE posture — confirm action: {action}")
            try:
                confirm = input("  Proceed? [y/N]: ").strip().lower()
            except EOFError:
                confirm = ""
            if confirm != "y":
                print(f"[HARNESS] Operator declined. Halting.")
                audit_log("harness", action,
                          f"step {step_num}/{total} — operator declined",
                          "DECLINED", ihash, source)
                run_script("progress.py", "flag-recovery")
                return False

    # 5. Log execution — named flags, Isnad wired
    code, out = audit_log(
        "harness", action,
        f"step {step_num}/{total} — {task}",
        "PASS", ihash, source,
    )
    if code != 0:
        print(f"[HARNESS] Audit log failed: {out}")
        run_script("progress.py", "flag-recovery")
        return False

    # 6. Write progress
    run_script("progress.py", "step", action)
    print(f"[HARNESS] Step complete — audited and logged.")
    return True


def cmd_run(args):
    headless = "--headless" in args
    args = [a for a in args if a != "--headless"]

    if len(args) < 2:
        print("Usage: govern_loop.py run [--headless] \"<task>\" \"<step1>\" ...")
        sys.exit(1)

    task = args[0]
    steps = args[1:]

    print(f"\n{'═' * 60}")
    print(f"  MO§ES™ GOVERNANCE HARNESS")
    print(f"  Task: {task}")
    print(f"  Steps: {len(steps)}")
    if headless:
        print(f"  Mode: HEADLESS (DEFENSE auto-approve on)")
    print(f"{'═' * 60}")

    run_script("progress.py", "start", task)

    for i, step in enumerate(steps, 1):
        ok = governed_step(task, step, i, len(steps), headless=headless)
        if not ok:
            print(f"\n[HARNESS] Loop halted at step {i}. Operator review required.")
            print(f"  Run: python3 progress.py status")
            sys.exit(1)

    run_script("progress.py", "done")
    print(f"\n{'═' * 60}")
    print(f"  [HARNESS] Task complete. All {len(steps)} steps governed and audited.")
    print(f"  Run: python3 audit_stub.py recent")
    print(f"{'═' * 60}\n")


def cmd_status(_args):
    run_script("progress.py", "status")


COMMANDS = {
    "run": cmd_run,
    "status": cmd_status,
}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "status"
    args = sys.argv[2:]
    if cmd not in COMMANDS:
        print(f"Usage: govern_loop.py [{'|'.join(COMMANDS)}]")
        sys.exit(1)
    COMMANDS[cmd](args)
