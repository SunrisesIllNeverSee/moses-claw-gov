# MO§ES™ → OpenClaw Setup Guide

*Deploy time: ~30 minutes from scratch*

---

## Prerequisites

- OpenClaw installed and running (`openclaw onboard --install-daemon`)
- Node.js + pnpm (for OpenClaw)
- Python 3.11+
- Anthropic API key configured in `~/.openclaw/openclaw.json`

---

## Step 1 — Clone OpenClaw (if not installed)

```bash
git clone https://github.com/openclaw/openclaw.git
cd openclaw && pnpm install && pnpm ui:build
openclaw onboard --install-daemon
```

---

## Step 2 — Install the MO§ES™ Skill

```bash
# Create skill directory in your OpenClaw workspace
mkdir -p ~/.openclaw/workspace/skills/moses-governance/scripts
mkdir -p ~/.openclaw/workspace/skills/moses-governance/references

# Copy skill files
cp skills/moses-governance/SKILL.md ~/.openclaw/workspace/skills/moses-governance/
cp skills/moses-governance/scripts/audit_stub.py ~/.openclaw/workspace/skills/moses-governance/scripts/
```

---

## Step 3 — Set Operator Secret

```bash
export MOSES_OPERATOR_SECRET='your-secure-hmac-key-here'
# Add to ~/.zshrc or ~/.bashrc to persist
```

---

## Step 4 — Initialize Governance State

```bash
mkdir -p ~/.openclaw/governance
cat > ~/.openclaw/governance/state.json << 'EOF'
{
  "mode": "high-integrity",
  "posture": "defense",
  "role": "primary",
  "vault": [],
  "session_hash": null
}
EOF

mkdir -p ~/.openclaw/audits/moses
```

---

## Step 5 — Install Workspace Overrides

```bash
# Merge or replace workspace files
# WARNING: If you have an existing AGENTS.md or TOOLS.md, merge manually

cp workspace/AGENTS.md ~/.openclaw/workspace/AGENTS.md
cp workspace/TOOLS.md ~/.openclaw/workspace/TOOLS.md
```

---

## Step 6 — Publish to ClawHub

```bash
clawhub login   # authenticate with GitHub/OpenClaw creds
clawhub publish ~/.openclaw/workspace/skills/moses-governance
# Slug: moses-governance
# Others install with: clawhub install moses-governance
```

---

## Step 7 — Test

```bash
# Verify audit chain (should return "Chain is empty" on first run)
python3 ~/.openclaw/workspace/skills/moses-governance/scripts/audit_stub.py verify

# Send a test message
openclaw message send --text "Test governance — evaluate a high-risk action under High Security mode"

# Check audit log
python3 ~/.openclaw/workspace/skills/moses-governance/scripts/audit_stub.py recent --n 5
```

---

## Step 8 — Post to X

```
Ported MO§ES™ to @openclaw as a multi-agent governance skill.
Primary → Secondary → Observer. SHA-256 audit trail. Constitutional constraints on every agent action.
DOI-cited + patent-pending. Now on ClawHub. [link]
@openclaw @steipete
```

---

## Governance Commands (once running)

| Command | What it does |
|---------|-------------|
| `/govern high-security` | Max constraints — verify all, confirm before acting |
| `/govern high-integrity` | Accuracy first — cite, flag uncertainty |
| `/govern research` | Depth first — document methodology |
| `/posture scout` | Read-only mode — no execution |
| `/posture defense` | Protect — confirm outbound actions |
| `/posture offense` | Execute within governance constraints |
| `/role primary` | You lead |
| `/role secondary` | You validate after primary |
| `/role observer` | Oversight only, flag risks |
| `/audit recent` | Last 10 audit entries |
| `/audit verify` | Verify chain integrity |
| `/status` | Current mode/posture/role |

---

## Directory Structure (Final)

```
~/.openclaw/
  workspace/
    AGENTS.md              ← Primary/Secondary/Observer definitions
    TOOLS.md               ← moses_check_governance + audit tools
    skills/
      moses-governance/
        SKILL.md           ← Core governance skill
        scripts/
          audit_stub.py    ← SHA-256 chained ledger
  governance/
    state.json             ← Active mode/posture/role
  audits/
    moses/
      audit_ledger.jsonl   ← Append-only audit chain
```
