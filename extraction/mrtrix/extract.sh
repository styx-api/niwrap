#!/usr/bin/env bash
#
# Dump MRtrix3 command metadata for every version in versions.json.
#
# For each version V it builds the Dockerfile with --build-arg MRTRIX_VERSION=V
# and exports the raw JSON dump to dump/V/{cpp,python}/.
#
# Requires: docker (with buildx), and either jq or python3 to read versions.json.
#
# Usage:
#   ./extract.sh              # all versions in versions.json
#   ./extract.sh 3.0.4 3.0.5  # explicit versions, ignoring versions.json

set -euo pipefail
here="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

read_versions() {
  if command -v jq >/dev/null 2>&1; then
    jq -r '.[]' "$here/versions.json"
  elif command -v python3 >/dev/null 2>&1; then
    python3 -c "import json;print('\n'.join(json.load(open('$here/versions.json'))))"
  fi
}

# Avoid `mapfile` (bash 4+) so this also runs on macOS's stock bash 3.2.
versions=()
if [ "$#" -gt 0 ]; then
  versions=("$@")
else
  while IFS= read -r v; do
    [ -n "$v" ] && versions+=("$v")
  done < <(read_versions)
fi

if [ "${#versions[@]}" -eq 0 ]; then
  echo "error: no versions (need jq or python3 to read versions.json, or pass versions as args)" >&2
  exit 1
fi

export DOCKER_BUILDKIT=1
for v in "${versions[@]}"; do
  echo "==> Dumping MRtrix3 ${v}"
  docker buildx build \
    --build-arg "MRTRIX_VERSION=${v}" \
    --target artifact \
    --output "type=local,dest=${here}/dump/${v}" \
    "${here}"
  echo "    -> ${here}/dump/${v}"
done
