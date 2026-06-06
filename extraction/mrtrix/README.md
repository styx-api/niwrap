# MRtrix3 metadata extraction

Reproducible, version-parametrized extraction of MRtrix3 command interfaces.

MRtrix3 ships two kinds of commands:

| Kind   | Source            | How we dump it                                      |
| ------ | ----------------- | --------------------------------------------------- |
| C++    | `cmd/*.cpp`       | `<cmd> __print_usage_json__` (patched into `app.cpp`)|
| Python | `bin/*` (argparse)| `<cmd> __print_argdump__` → [argdump][argdump]      |

Both are obtained from the tool itself — no scraping, no text parsing — so the
descriptors track upstream exactly.

## Pipeline

```
 dump  ── Docker, per version ──▶  raw JSON   (dump/<version>/{cpp,python}/*.json)
 process ── process_metadata.py ─▶  descriptors (src/niwrap/mrtrix/<version>/...)
 compile ── Styx frontends ──────▶  IR → bindings                                   [TODO]
```

Only the **dump** stage touches Docker and tool versions. It is fully described
by [`Dockerfile`](Dockerfile) + [`patches/`](patches) + [`versions.json`](versions.json).

## Dump (this directory)

The new pipeline builds from an **official** MRtrix3 tag plus two small patches
applied at build time — no fork branch to rebase (the `source/` submodule
referenced under "Legacy flow" belongs to the old flow and retires with it):

- [`patches/cpp-json-usage.patch`](patches/cpp-json-usage.patch) — adds the
  `__print_usage_json__` hook to `core/app.cpp` (pure addition, ~190 lines).
- [`patches/python-argdump.patch`](patches/python-argdump.patch) — adds a
  `__print_argdump__` branch to `lib/mrtrix3/app.py` that serializes the live
  `argparse` parser (including all algorithm subparsers) with `argdump`, plus a
  `mrtrix` block carrying the descriptive metadata argparse doesn't hold
  (synopsis, description, author, citations, copyright, version) — recursed into
  each algorithm subparser. argparse-derived structure covers the interface;
  input/output file semantics are not present in the Python source and are
  recovered heuristically during processing.

### Run

One version:

```bash
docker buildx build \
  --build-arg MRTRIX_VERSION=3.0.4 \
  --target artifact \
  --output type=local,dest=extraction/mrtrix/dump/3.0.4 \
  extraction/mrtrix
```

The whole matrix in [`versions.json`](versions.json):

```bash
./extract.sh          # bash
./extract.ps1         # PowerShell (Windows)
```

Output lands in `dump/<version>/` (git-ignored):

```
dump/3.0.4/
├── VERSION
├── cpp/      5tt2gmwmi.json, mrconvert.json, ...
└── python/   5ttgen.json, dwi2response.json, ...
```

### Bump / add a version

Add the tag to [`versions.json`](versions.json) and re-run `extract.*`. The image
is tagged by version, so each dump is fully reproducible. If a patch ever fails to
apply on a newer release, the build stops loudly — refresh the patch against that
tag and commit it.

> **End-game:** if `__print_usage_json__` is upstreamed into MRtrix3, stage 1
> collapses to `FROM mrtrix3/mrtrix3:${MRTRIX_VERSION}` + `pip install argdump`,
> dropping the source build entirely.

## Process

[`process_metadata.py`](process_metadata.py) lays the raw dumps out into the
committed, build-consumable tree, mirroring
[`../workbench/process_workbench_metadata.py`](../workbench/process_workbench_metadata.py):

```bash
python extraction/mrtrix/process_metadata.py   # dump/<v>/ -> src/niwrap/mrtrix/<v>/
```

For each command it copies the dump verbatim as the descriptor
(`mrtrix.json` for C++ → `source.type: "mrtrix"`, `argdump.json` for Python →
`source.type: "argdump"`), writes an `app.json` (name + source pointer +
description), emits `<version>/version.json` (preserving the `executables`
required/ignored lists), and registers the version in `package.json`. Commands in
`executables.ignored` (e.g. `for_each`, `mrtrix_cleanup`) are skipped, and a stale
`boutiques.json` in a rewritten command directory is pruned. It does **not**
interpret the interface — that is the frontend's job; input/output file semantics
(absent from argparse) are recovered there too.

## Compile (next step — not yet implemented)

- `load_mrtrix` / `load_argdump` — Styx frontends in
  `tooling/src/wrap/apps/build/loaders/` that compile the dumps directly to IR,
  replacing the Boutiques conversion. `load_argdump` (argdump JSON → IR) is
  reusable for any argparse-based CLI. The `source.type` values are already
  registered in `catalog.py` and `schemas/app.schema.json`; only the `load_source`
  dispatch remains. Because `process_metadata.py` rewrites `app.json` to these
  types, run it against `src/niwrap` only **together with** this wiring — otherwise
  the mrtrix build fails for every command.

## Legacy flow (superseded)

The previous pipeline — `buildenv.Dockerfile` + `generate_json_docs.sh` +
`mrt2bt.js` (Node → Boutiques) + the committed `source/` submodule and
`json_docs/` — is kept for reference until the frontends above land. It generated
Boutiques only for the C++ commands; the Python commands' Boutiques descriptors
under `src/niwrap/mrtrix` were hand-authored.

[argdump]: https://github.com/styx-api/argdump
