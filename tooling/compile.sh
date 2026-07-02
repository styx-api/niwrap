#!/usr/bin/env bash
#
# Compile the NiWrap catalog into per-language distributions with styx2 (the
# styx-ts compiler), then reshape the output into the dist/ layout that the
# compile + publish workflows push to the styx-api/niwrap-* repos.
#
# This replaces the v1 `wrap build` command: compilation is now owned by the
# styx2 Node CLI, while the Python `wrap` tool keeps `sync` / `test` /
# `check_container`.
#
# Usage:   tooling/compile.sh [targets]
#   targets  comma-separated styx2 backends (default: python,typescript,json-schema)
#
# Env overrides:
#   STYX2_REF   styx-ts git ref to build (default: pinned SHA below)
#   STYX2_REPO  styx-ts repo URL (default: the public repo)
#
# Run from the niwrap repo root.
set -euo pipefail

# -----------------------------------------------------------------------------
# Pin: the styx-ts commit the catalog is compiled with. Kept at a fixed SHA so
# releases are reproducible; bump deliberately and coordinate with the hub's
# bundled @styx/core version (see the styx2 v1-replacement plan).
#
# Pinned to styx-ts main at styx-ts#28 (per-suite wrapper packages carry the
# project/catalog version, not the wrapped tool version - so every niwrap_<pkg>
# stays in lockstep with the niwrap meta release). That built on #27 (per-tool
# json-schema file names) and #26 (Phase A codegen gaps). Bump deliberately when
# adopting newer styx2 behavior.
# -----------------------------------------------------------------------------
STYX2_REPO="${STYX2_REPO:-https://github.com/styx-api/styx-ts.git}"
STYX2_REF="${STYX2_REF:-b47a179bf610c28db12980c707d1075695f505db}"

TARGETS="${1:-python,typescript,json-schema}"

NIWRAP_ROOT="$(pwd)"
CATALOG_DIR="$NIWRAP_ROOT/src/niwrap"
DIST_DIR="$NIWRAP_ROOT/dist"

if [ ! -d "$CATALOG_DIR" ]; then
  echo "error: catalog not found at $CATALOG_DIR (run from the niwrap repo root)" >&2
  exit 1
fi

# Temp dirs for the styx2 checkout and the raw build output; cleaned on exit.
STYX2_DIR="$(mktemp -d)"
BUILD_OUT="$(mktemp -d)"
trap 'rm -rf "${STYX2_DIR:-}" "${BUILD_OUT:-}"' EXIT

# -----------------------------------------------------------------------------
# Build the styx2 compiler at the pinned ref.
# -----------------------------------------------------------------------------
echo "==> Cloning styx-ts @ ${STYX2_REF}"
git clone --quiet "$STYX2_REPO" "$STYX2_DIR"
git -C "$STYX2_DIR" checkout --quiet "$STYX2_REF"

echo "==> Building @styx/core + @styx/cli"
(
  cd "$STYX2_DIR"
  npm ci
  npm run build -w @styx/core -w @styx/cli
)

STYX_CLI="$STYX2_DIR/packages/cli/dist/bin.mjs"

# -----------------------------------------------------------------------------
# Compile the full catalog. `--mode multi` emits the per-tool files plus the
# suite (__init__/index) and project (root pyproject/package.json) tiers.
# -----------------------------------------------------------------------------
echo "==> Compiling catalog (targets: ${TARGETS})"
node "$STYX_CLI" build --catalog "$CATALOG_DIR" -o "$BUILD_OUT" --mode multi -b "$TARGETS"

# -----------------------------------------------------------------------------
# Reshape the raw styx2 output (one dir per backend) into the dist/ layout the
# workflows push: dist/niwrap-python, dist/niwrap-js, dist/niwrap-json-schema.
# -----------------------------------------------------------------------------
echo "==> Reshaping into ${DIST_DIR}"
rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

IFS=',' read -ra TARGET_ARR <<< "$TARGETS"
for target in "${TARGET_ARR[@]}"; do
  case "$target" in
    python)
      src="$BUILD_OUT/python"
      out="$DIST_DIR/niwrap-python"
      mkdir -p "$out/niwrap"
      # The root meta package (deps on every niwrap_<pkg> + the container
      # runners) goes in a `niwrap/` subdir. Drop requirements.txt - it is an
      # editable-install convenience the wheel build does not consume.
      mv "$src/pyproject.toml" "$out/niwrap/pyproject.toml"
      mv "$src/README.md" "$out/niwrap/README.md"
      rm -f "$src/requirements.txt"
      # Determine the sub-package version (all share the same one) so we can
      # pin the meta-package dependencies with a compatible-release (~=) spec.
      # Read from $src before the move loop below consumes the directories.
      first_pkg="$(dirname "$(ls -1 "$src"/*/pyproject.toml | head -1)" | xargs basename)"
      sub_ver="$(grep '^version' "$src/$first_pkg/pyproject.toml" | head -1 \
                | sed 's/.*"\([^"]*\)".*/\1/')"
      major="${sub_ver%%.*}"
      minor="${sub_ver#*.}"; minor="${minor%%.*}"
      sed -i "s/\"niwrap_\([a-z0-9_]*\)\"/\"niwrap_\1~=${major}.${minor}\"/g" \
            "$out/niwrap/pyproject.toml"
      # Each remaining sub-package dir (afni, fsl, ...) becomes a sibling of
      # niwrap/, so `for d in dist/niwrap-python/*/` builds meta + every package.
      for d in "$src"/*/; do
        mv "$d" "$out/$(basename "$d")"
      done
      ;;
    typescript)
      mv "$BUILD_OUT/typescript" "$DIST_DIR/niwrap-js"
      ;;
    json-schema)
      mv "$BUILD_OUT/json-schema" "$DIST_DIR/niwrap-json-schema"
      ;;
    *)
      echo "warning: no reshape rule for target '${target}'; keeping as dist/${target}" >&2
      mv "$BUILD_OUT/$target" "$DIST_DIR/$target"
      ;;
  esac
done

echo "==> Done. dist/ contains:"
ls -1 "$DIST_DIR"
