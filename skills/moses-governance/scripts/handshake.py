#!/usr/bin/env python3
"""
handshake.py — MO§ES™ Inter-Agent Handshake Envelope
Standard JSON schema for kernel exchange between governed agents.

Answers Cornelius-Trinity + automationscout: the verify command takes two
JSON blobs but there is no agreed envelope for passing that between agents
in a live session. The handshake is manual. This fixes that.

An envelope contains:
  - input_hash: SHA-256 of raw signal (Isnad Layer 0 — proves identical input)
  - kernel: extracted commitment tokens
  - ghost_pattern: fingerprint of leaked tokens (if any) from prior comparison
  - state: governed state at extraction time
  - isnad: signal provenance chain entry
  - presence: optional presence response proving agent was governed at exchange
  - envelope_hash: SHA-256 of all above fields

Receivers call: handshake.py verify <envelope.json>
  → checks schema, input_hash present, isnad chain, state valid, envelope intact

Usage:
  python3 handshake.py pack "<signal_text>" [--source-id <id>]   — create envelope
  python3 handshake.py verify <envelope.json>                     — verify received envelope
  python3 handshake.py unpack <envelope.json>                     — extract kernel for comparison
"""

import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

STATE_PATH = os.path.expanduser("~/.openclaw/governance/state.json")
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
LINEAGE_ANCHOR = "1a2b3c4d5e6f7890abcdef1234567890abcdef1234567890abcdef1234567890ab"


def load_state():
    if not os.path.exists(STATE_PATH):
        return {}
    with open(STATE_PATH) as f:
        return json.load(f)


def run_script(script, *args):
    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPTS_DIR, script)] + list(args),
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return None, result.stderr.strip()
    try:
        return json.loads(result.stdout), None
    except json.JSONDecodeError:
        return result.stdout.strip(), None


def cmd_pack(args):
    """Pack a signal into a verifiable inter-agent handshake envelope."""
    if not args:
        print("Usage: handshake.py pack \"<signal_text>\" [--source-id <id>]")
        sys.exit(1)

    signal = args[0]
    source_id = None
    if "--source-id" in args:
        idx = args.index("--source-id")
        if idx + 1 < len(args):
            source_id = args[idx + 1]

    state = load_state()
    input_hash = hashlib.sha256(signal.encode()).hexdigest()
    timestamp = datetime.now(timezone.utc).isoformat()

    # Extract kernel
    kernel_result, err = run_script("commitment_verify.py", "extract", signal)
    if err or kernel_result is None:
        print(f"[HANDSHAKE] ERROR: commitment_verify failed: {err}")
        sys.exit(1)

    kernel = kernel_result.get("kernel", []) if isinstance(kernel_result, dict) else []

    # Build isnad entry
    prev_isnad = "0" * 64
    isnad = {
        "input_hash": input_hash,
        "source_id": source_id or "self",
        "transmitter": state.get("role", "unknown"),
        "prev_isnad_hash": prev_isnad,
    }
    isnad["isnad_hash"] = hashlib.sha256(
        json.dumps(isnad, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    envelope = {
        "schema_version": "1.0",
        "created_at": timestamp,
        "input_hash": input_hash,
        "kernel": kernel,
        "kernel_count": len(kernel),
        "state": {
            "mode": state.get("mode", "unknown"),
            "posture": state.get("posture", "unknown"),
            "role": state.get("role", "unknown"),
            "session_hash": state.get("session_hash", ""),
        },
        "isnad": isnad,
        "lineage_anchor": LINEAGE_ANCHOR,
    }

    # Envelope hash — receiver recomputes to detect tampering
    payload = json.dumps({k: v for k, v in envelope.items()}, sort_keys=True, separators=(",", ":"))
    envelope["envelope_hash"] = hashlib.sha256(payload.encode()).hexdigest()

    print(json.dumps(envelope, indent=2))
    print("\n[HANDSHAKE] Envelope ready. Share with receiving agent.", file=sys.stderr)
    print("[HANDSHAKE] Receiver runs: handshake.py verify <envelope.json>", file=sys.stderr)


def cmd_verify(args):
    """Verify a received inter-agent handshake envelope."""
    if not args:
        print("Usage: handshake.py verify <envelope.json>")
        sys.exit(1)

    path = args[0]
    if not os.path.exists(path):
        print(f"[HANDSHAKE] ERROR: File not found: {path}")
        sys.exit(1)

    with open(path) as f:
        envelope = json.load(f)

    checks = {}

    # 1. Schema version present
    checks["schema_version"] = envelope.get("schema_version") == "1.0"

    # 2. input_hash present (Isnad Layer 0 requirement)
    checks["input_hash_present"] = bool(envelope.get("input_hash"))

    # 3. Kernel non-empty
    checks["kernel_non_empty"] = len(envelope.get("kernel", [])) > 0

    # 4. Isnad chain present and internally consistent
    isnad = envelope.get("isnad", {})
    expected_isnad_hash = hashlib.sha256(
        json.dumps(
            {k: v for k, v in isnad.items() if k != "isnad_hash"},
            sort_keys=True, separators=(",", ":")
        ).encode()
    ).hexdigest()
    checks["isnad_hash_valid"] = isnad.get("isnad_hash") == expected_isnad_hash

    # 5. input_hash in isnad matches envelope input_hash
    checks["isnad_input_hash_match"] = isnad.get("input_hash") == envelope.get("input_hash")

    # 6. Lineage anchor matches
    checks["lineage_anchor_valid"] = envelope.get("lineage_anchor") == LINEAGE_ANCHOR

    # 7. Envelope hash integrity — recompute without envelope_hash field
    envelope_copy = {k: v for k, v in envelope.items() if k != "envelope_hash"}
    payload = json.dumps(envelope_copy, sort_keys=True, separators=(",", ":"))
    expected_hash = hashlib.sha256(payload.encode()).hexdigest()
    checks["envelope_hash_valid"] = envelope.get("envelope_hash") == expected_hash

    # 8. Governed state present
    state = envelope.get("state", {})
    checks["state_present"] = bool(state.get("mode") and state.get("posture") and state.get("role"))

    all_pass = all(checks.values())
    failed = [k for k, v in checks.items() if not v]

    result = {
        "verified": all_pass,
        "verdict": "ACCEPT" if all_pass else f"REJECT — failed: {', '.join(failed)}",
        "sender_role": state.get("role"),
        "sender_mode": state.get("mode"),
        "sender_posture": state.get("posture"),
        "input_hash": envelope.get("input_hash"),
        "kernel_count": envelope.get("kernel_count"),
        "checks": checks,
    }
    if failed:
        result["failed_checks"] = failed

    print(json.dumps(result, indent=2))
    sys.exit(0 if all_pass else 1)


def cmd_unpack(args):
    """Extract kernel from a verified envelope for Jaccard comparison."""
    if not args:
        print("Usage: handshake.py unpack <envelope.json>")
        sys.exit(1)

    with open(args[0]) as f:
        envelope = json.load(f)

    result = {
        "input_hash": envelope.get("input_hash"),
        "kernel": envelope.get("kernel", []),
        "kernel_count": envelope.get("kernel_count", 0),
        "sender_role": envelope.get("state", {}).get("role"),
        "isnad_hash": envelope.get("isnad", {}).get("isnad_hash"),
    }
    print(json.dumps(result, indent=2))


COMMANDS = {
    "pack": cmd_pack,
    "verify": cmd_verify,
    "unpack": cmd_unpack,
}

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else None
    if cmd not in COMMANDS:
        print(f"Usage: handshake.py [{'|'.join(COMMANDS)}] ...")
        sys.exit(1)
    COMMANDS[cmd](sys.argv[2:])
