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
 compile ── Styx frontends ──────▶  IR → bindings (mrtrix / argdump)
```

Only the **dump** stage touches Docker and tool versions. It is fully described
by [`Dockerfile`](Dockerfile) + [`patches/`](patches) + [`versions.json`](versions.json).

## Dump (this directory)

The pipeline builds from an **official** MRtrix3 tag plus two small patches
applied at build time — no fork branch to rebase:

- [`patches/cpp-json-usage.patch`](patches/cpp-json-usage.patch) — adds the
  `__print_usage_json__` hook to `core/app.cpp` (pure addition). Per argument it
  also serializes the constraints MRtrix keeps in `Argument::limits`: `choices`
  for enum arguments and `min`/`max` for bounded integers/floats (the unbounded
  sentinels are omitted) — data even MRtrix's own readthedocs docs throw away.
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

## Compile

The dumps are compiled to IR by styx2's `mrtrix` / `argdump` frontends (in
[`@styx-api/core`](https://github.com/styx-api/styx)), selected per command by
`app.json`'s `source.type`. `argdump` (argparse JSON → IR) is reusable for any
argparse-based CLI. A few commands whose flat dump can't express paired
input/output positionals (`dwi2fod`, `mtnormalise`) are split in
`process_metadata.py`, which also folds the Python `mrtrix` metadata block into
the argdump descriptor's `description`.

[argdump]: https://github.com/styx-api/argdump
