# Metadata extraction

Reproducible, container-driven generation of NiWrap metadata. Two distinct
concerns live here:

1. **Descriptor metadata** — the *contents* of each tool's Boutiques descriptor.
2. **Application lists** — *which* of a release's programs we wrap, recorded in
   each `src/niwrap/<pkg>/<ver>/version.json`.

## Descriptor metadata

Some packages use shared internal data structures which store command line parsing information. By serializing these data structures, we can extract it and subsequently generate Boutiques descriptors from it which will always be correct and can be automatically updated whenever the packages change.

The rough steps to extract metadata are as follows:

1. Add JSON serialization code to the package.
2. Instead of emitting a help message, emit a JSON object.
3. Write a script to run all the commands and extract the JSON objects.
4. Write a script to generate Boutiques descriptors from the JSON objects.

Packages where this is viable:

- Connectome Workbench
- MRTrix3

## Application lists (`apps` / `executables`)

Each `src/niwrap/<pkg>/<ver>/version.json` carries the inventory of programs a
release ships:

- `apps` — every program we intend to wrap (the denominator of the README
  coverage bar);
- `executables.required` — kept identical to `apps`; CI (`wrap check-container`)
  asserts each one resolves on the container's `PATH`;
- `executables.ignored` — programs present in the container that we deliberately
  do **not** wrap.

These lists are **generated from the pinned container**, not hand-maintained.
`<pkg>/app_list.py` reads the `container` field from the manifest, enumerates
the tool's programs, splits them into wrapped vs. ignored, and rewrites only
those keys.

### Usage

```sh
python extraction/<pkg>/app_list.py                 # rewrite version.json
python extraction/<pkg>/app_list.py --check         # CI: non-zero exit if stale
python extraction/<pkg>/app_list.py --prune-orphans # also delete dropped descriptor dirs
```

Requires Docker on `PATH` (the image is pulled on first run).

### Layout

[`applist_common.py`](applist_common.py) holds everything package-independent —
the container read, the manifest rewrite, and two consistency guards:

- `--check` fails if the manifest is stale **or** if a descriptor dir under
  `src/niwrap/<pkg>/<ver>/` is no longer in `apps`;
- `--prune-orphans` deletes those orphaned descriptor dirs.

Together these keep the invariant **descriptor dirs == `apps`**: an ignored
program must also lose its descriptor, or Styx keeps emitting a wrapper for it.

Each package supplies only the two parts that genuinely differ — how to list
programs, and how to split them:

| Package | Program source | Ignore rule |
| --- | --- | --- |
| ANTs | files in `/opt/ants/bin` | `.R` / `.pl` helper scripts |
| AFNI | `apsearch -list_all_afni_progs` | `@Install_*` / `uber_*` / `plugout_*` prefixes, plus an explicit list (GUIs, installers, dev/test, internal helpers) |
| FreeSurfer | executables in `$FREESURFER_HOME/bin` | `.fsl` / `.afni` / `.example` / `.sch` suffixes, plus an explicit list (GUIs incl. Tcl/Tk, tests, MCR installer, internal helpers) |

### What we don't wrap

A program is left out when it isn't a scriptable data-processing command:
interactive GUIs and viewer-launchers, programs that drive a running GUI,
demo/dependency installers, developer test binaries, bundled copies of other
packages' tools (wrapped under their own package), data files that merely live
in `bin`, and internal helper/plumbing scripts. Where a whole family shares a
safe pattern (e.g. AFNI `@Install_*`) it becomes a rule; otherwise the names are
listed explicitly, grouped by reason, in the package's `app_list.py`.

Be conservative — a name that *looks* like a test or GUI but is real analysis
stays wrapped (`3dNormalityTest`, `mri_nu_correct.mni`, `tkregister2_cmdl`).

### Adding a package

Create `extraction/<pkg>/app_list.py` defining `list_programs(container)` and
`partition(names) -> (apps, ignored)`, then call `run_cli(...)` from
`applist_common.py`. See [`ants/app_list.py`](ants/app_list.py) for the simplest
example.
