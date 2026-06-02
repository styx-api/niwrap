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

if [ "$#" -gt 0 ]; then
  versions=("$@")
elif command -v jq >/dev/null 2>&1; then
  mapfile -t versions < <(jq -r '.[]' "$here/versions.json")
elif command -v python3 >/dev/null 2>&1; then
  mapfile -t versions < <(python3 -c "import json;print('\n'.join(json.load(open('$here/versions.json'))))")
else
  echo "error: need jq or python3 to read versions.json (or pass versions as args)" >&2
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
