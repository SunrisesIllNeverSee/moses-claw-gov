#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIST_DIR="${REPO_ROOT}/dist"
BUNDLE_SLUG="${1:-moses-claw-plugin}"
BUNDLE_DIR="${DIST_DIR}/${BUNDLE_SLUG}"
ZIP_PATH="${DIST_DIR}/${BUNDLE_SLUG}.zip"
PRIMARY_SKILL="moses-governance"
PRIMARY_SKILL_FILE="${REPO_ROOT}/skills/${PRIMARY_SKILL}/SKILL.md"
BUILD_TIMESTAMP="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# Keep the bundle scope explicit so rebuilds match the original 9-skill upload.
SKILLS=(
  "coverify"
  "lineage-claws"
  "moses-audit"
  "moses-coordinator"
  "moses-governance"
  "moses-governance-single"
  "moses-modes"
  "moses-postures"
  "moses-roles"
)

require_cmd() {
  local cmd="$1"
  if ! command -v "${cmd}" >/dev/null 2>&1; then
    echo "Missing required command: ${cmd}" >&2
    exit 1
  fi
}

emit_json_string_array() {
  local indent="$1"
  shift
  local count="$#"
  local index=0
  local item
  for item in "$@"; do
    index=$((index + 1))
    if [[ "${index}" -lt "${count}" ]]; then
      printf '%s"%s",\n' "${indent}" "${item}"
    else
      printf '%s"%s"\n' "${indent}" "${item}"
    fi
  done
}

emit_readme() {
  cat <<EOF
# MO§ES™ ClawHub Bundle

Reproducible upload bundle for the published MO§ES™ ClawHub plugin. This archive is generated from the source of truth in \`SunrisesIllNeverSee/moses-claw-gov\` instead of being assembled ad hoc in-browser.

- Source repo: https://github.com/SunrisesIllNeverSee/moses-claw-gov
- Published plugin: https://clawhub.ai/plugins/moses-claw-plugin
- Built at: ${BUILD_TIMESTAMP}
- Bundle version: ${VERSION}

## Included Skills
EOF

  local skill
  for skill in "${SKILLS[@]}"; do
    printf -- '- `%s`\n' "${skill}"
  done

  cat <<EOF

## Build

Run \`./scripts/build-bundle.sh\` from the repo root. The builder copies each bundled skill with its local \`scripts/\`, \`references/\`, and companion files, then writes this root \`README.md\` and \`package.json\` before producing \`dist/${BUNDLE_SLUG}.zip\`.

## Notes

- Bundle scope is intentional and preserves the original 9-skill ClawHub upload.
- Networked behavior stays opt-in. See \`package.json\` for the aggregated environment and endpoint declarations.
EOF
}

emit_package_json() {
  cat <<EOF
{
  "name": "${BUNDLE_SLUG}",
  "version": "${VERSION}",
  "private": true,
  "description": "Reproducible ClawHub bundle for the MO§ES™ skill family.",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/SunrisesIllNeverSee/moses-claw-gov.git"
  },
  "homepage": "https://clawhub.ai/plugins/moses-claw-plugin",
  "bundleType": "openclaw-skill-bundle",
  "primarySkill": "${PRIMARY_SKILL}",
  "builtAt": "${BUILD_TIMESTAMP}",
  "sourceOfTruth": {
    "skillsDir": "skills/",
    "repo": "https://github.com/SunrisesIllNeverSee/moses-claw-gov"
  },
  "files": [
    "README.md",
    "package.json",
    "skills/"
  ],
  "skills": [
EOF

  emit_json_string_array "    " "${SKILLS[@]}"

  cat <<EOF
  ],
  "bins": [
    "python3"
  ],
  "stateDirs": [
    "~/.openclaw/governance",
    "~/.openclaw/audits/moses"
  ],
  "primaryEnv": "MOSES_OPERATOR_SECRET",
  "env": [
    {
      "name": "MOSES_OPERATOR_SECRET",
      "usedBy": [
        "moses-governance",
        "moses-governance-single",
        "moses-audit",
        "moses-roles"
      ],
      "required": false,
      "sensitive": true,
      "purpose": "Local HMAC attestation and signing gate enforcement. Never transmitted."
    },
    {
      "name": "MOSES_WITNESS_ENABLED",
      "usedBy": [
        "moses-governance"
      ],
      "required": false,
      "sensitive": false,
      "purpose": "Opt-in switch for the external Moltbook witness logger."
    },
    {
      "name": "MOLTBOOK_API_KEY",
      "usedBy": [
        "moses-governance"
      ],
      "required": false,
      "sensitive": true,
      "purpose": "Authenticates optional witness posting to Moltbook."
    },
    {
      "name": "MOLTBOOK_SUBMOLT",
      "usedBy": [
        "moses-governance"
      ],
      "required": false,
      "sensitive": false,
      "purpose": "Optional Moltbook target submolt. Defaults to general."
    },
    {
      "name": "REFEREE_ENABLED",
      "usedBy": [
        "moses-governance"
      ],
      "required": false,
      "sensitive": false,
      "purpose": "Opt-in switch for external blind-review/referee forwarding."
    },
    {
      "name": "REFEREE_URL",
      "usedBy": [
        "moses-governance"
      ],
      "required": false,
      "sensitive": false,
      "purpose": "Operator-supplied blind-review/referee endpoint."
    },
    {
      "name": "REFEREE_KEY",
      "usedBy": [
        "moses-governance"
      ],
      "required": false,
      "sensitive": true,
      "purpose": "API key for the optional blind-review/referee endpoint."
    }
  ],
  "networkPolicy": "All outbound network behavior is off by default and requires explicit operator opt-in.",
  "network": [
    {
      "name": "openclaw_gateway_ws",
      "url": "ws://127.0.0.1:18789",
      "kind": "local",
      "usedBy": [
        "moses-coordinator"
      ],
      "guard": "Local-only; optional daemon",
      "purpose": "Session sequencing monitor for Primary → Secondary → Observer order."
    },
    {
      "name": "moltbook_posts",
      "url": "https://www.moltbook.com/api/v1/posts",
      "kind": "remote",
      "usedBy": [
        "moses-governance"
      ],
      "guard": "MOSES_WITNESS_ENABLED=1 and MOLTBOOK_API_KEY set",
      "purpose": "Optional external witness ledger posting."
    },
    {
      "name": "moltbook_verify",
      "url": "https://www.moltbook.com/api/v1/verify",
      "kind": "remote",
      "usedBy": [
        "moses-governance"
      ],
      "guard": "MOSES_WITNESS_ENABLED=1 and MOLTBOOK_API_KEY set",
      "purpose": "Optional Moltbook verification challenge solver."
    },
    {
      "name": "referee_endpoint",
      "url": "\$REFEREE_URL",
      "kind": "remote",
      "usedBy": [
        "moses-governance"
      ],
      "guard": "REFEREE_ENABLED=1 with REFEREE_URL and REFEREE_KEY set",
      "purpose": "Optional blind-review/referee integration configured by the operator."
    }
  ]
}
EOF
}

copy_skill() {
  local skill="$1"
  local source_dir="${REPO_ROOT}/skills/${skill}"
  local dest_dir="${BUNDLE_DIR}/skills/${skill}"

  if [[ ! -f "${source_dir}/SKILL.md" ]]; then
    echo "Missing ${source_dir}/SKILL.md" >&2
    exit 1
  fi

  rsync -a \
    --exclude ".DS_Store" \
    --exclude "__pycache__/" \
    --exclude "*.pyc" \
    "${source_dir}/" "${dest_dir}/"
}

require_cmd "awk"
require_cmd "rsync"
require_cmd "zip"

if [[ ! -f "${PRIMARY_SKILL_FILE}" ]]; then
  echo "Missing primary skill metadata: ${PRIMARY_SKILL_FILE}" >&2
  exit 1
fi

VERSION="$(awk '/version:/{print $2; exit}' "${PRIMARY_SKILL_FILE}")"
VERSION="${VERSION:-0.0.0}"

mkdir -p "${DIST_DIR}"
rm -rf "${BUNDLE_DIR}" "${ZIP_PATH}"
mkdir -p "${BUNDLE_DIR}/skills"

for skill in "${SKILLS[@]}"; do
  copy_skill "${skill}"
done

emit_readme > "${BUNDLE_DIR}/README.md"
emit_package_json > "${BUNDLE_DIR}/package.json"

(
  cd "${BUNDLE_DIR}"
  zip -qr "${ZIP_PATH}" README.md package.json skills
)

echo "Bundle created:"
echo "  directory: ${BUNDLE_DIR}"
echo "  archive:   ${ZIP_PATH}"
