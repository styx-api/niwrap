#!/usr/bin/env python3
"""Regenerate the ANTs ``apps`` / ``executables`` lists in a version manifest.

The lists in ``src/niwrap/ants/<version>/version.json`` are derived, not
hand-curated: every program ANTs ships lives in ``/opt/ants/bin`` inside the
release container. This script makes that derivation reproducible -- it runs
the container named in the manifest, enumerates that directory, and partitions
the entries into:

* ``executables.ignored`` -- helper scripts we deliberately do not wrap
  (R network-analysis helpers and the Perl job-queue waiters), matched by the
  ``.R`` / ``.pl`` extensions in ``IGNORE_SUFFIXES``;
* ``apps`` == ``executables.required`` -- everything else (the bare C++ tools
  plus the ``.sh`` pipelines), i.e. the surface niwrap wraps and that
  ``check-container`` validates in CI.

Run it whenever the pinned container changes::

    python extraction/ants/app_list.py                  # rewrite version.json
    python extraction/ants/app_list.py --check          # CI: fail if stale
    python extraction/ants/app_list.py --prune-orphans  # also delete dropped descriptors

Requires Docker on PATH and network access to pull the image on first run.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from applist_common import PROJECT_DIR, docker_capture, run_cli  # noqa: E402

DEFAULT_VERSION_FILE = PROJECT_DIR / "src/niwrap/ants/2.5.3/version.json"

# Directory inside the antsx/ants image that holds every shipped executable.
BIN_DIR = "/opt/ants/bin"

# Extensions of programs present in the image but intentionally left unwrapped:
#   .R  -> antsBOLDNetworkAnalysis.R, antsLaplacianBoundaryCondition.R, ...
#   .pl -> waitForPBSQJobs.pl, waitForSGEQJobs.pl, ...
IGNORE_SUFFIXES = (".R", ".pl")


def list_programs(container: str) -> list[str]:
    """Names of every executable regular file in the ANTs bin dir."""
    # POSIX sh: print the basename of each regular, executable file. The glob is
    # guarded so an empty directory does not echo the literal pattern.
    snippet = (
        f'for f in "{BIN_DIR}"/*; do '
        '[ -f "$f" ] && [ -x "$f" ] && basename "$f"; '
        "done"
    )
    names = docker_capture(container, snippet)
    if not names:
        raise SystemExit(f"error: no executables found in {BIN_DIR} of {container}")
    return names


def partition(names: list[str]) -> tuple[list[str], list[str]]:
    """Split into (apps/required, ignored), sorted; ignore .R/.pl helpers."""
    ignored = sorted(n for n in names if n.endswith(IGNORE_SUFFIXES))
    apps = sorted(n for n in names if not n.endswith(IGNORE_SUFFIXES))
    return apps, ignored


if __name__ == "__main__":
    sys.exit(
        run_cli(
            default_version_file=DEFAULT_VERSION_FILE,
            list_programs=list_programs,
            partition=partition,
            description=__doc__.splitlines()[0],
        )
    )
