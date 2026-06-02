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
 process ── process_metadata.py ─▶  descriptors (src/niwrap/mrtrix/<version>/...)   [TODO]
 compile ── Styx frontends ──────▶  IR → bindings                                   [TODO]
```

Only the **dump** stage touches Docker and tool versions. It is fully described
by [`Dockerfile`](Dockerfile) + [`patches/`](patches) + [`versions.json`](versions.json).

## Dump (this directory)

Everything builds from an **official** MRtrix3 tag plus two small patches — there
is no fork to maintain:

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
  --output type=local,dest=dump/3.0.4 \
  .
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

## Process & compile (next steps — not yet implemented)

- `process_metadata.py` — turn `dump/<version>/` into the repo descriptor layout
  (`src/niwrap/mrtrix/<version>/<cmd>/{app.json, mrtrix.json | argparse.json}`),
  mirroring [`../workbench/process_workbench_metadata.py`](../workbench/process_workbench_metadata.py).
- `load_mrtrix` / `load_argparse` — Styx frontends in
  `tooling/src/wrap/apps/build/loaders/` that compile the native dumps directly to
  IR, replacing the Boutiques conversion. `load_argparse` (argdump JSON → IR) is
  reusable for any argparse-based CLI.

## Legacy flow (superseded)

The previous pipeline — `buildenv.Dockerfile` + `generate_json_docs.sh` +
`mrt2bt.js` (Node → Boutiques) + the committed `source/` submodule and
`json_docs/` — is kept for reference until the frontends above land. It only
handled C++ commands; the Python descriptors under `src/niwrap/mrtrix` were
hand-authored.

[argdump]: https://github.com/styx-api/argdump
