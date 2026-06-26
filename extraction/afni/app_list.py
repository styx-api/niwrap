#!/usr/bin/env python3
"""Regenerate the AFNI ``apps`` / ``executables`` lists in a version manifest.

Unlike ANTs (see ``extraction/ants/app_list.py``), AFNI's install directory is
not a clean set of programs -- it mixes ~640 programs with hundreds of data and
support files. So instead of listing a directory, this script asks AFNI itself
for its authoritative program list via ``apsearch -list_all_afni_progs`` (the
same index AFNI uses for tab-completion and help search). That list is
deterministic and already sorted, and it excludes the ``*.R`` source files that
sit next to their wrapper programs (e.g. it lists ``3dMVM``, not ``3dMVM.R``).

Partitioning that list into wrapped vs. ignored is only *partly* mechanical:

* ``executables.ignored`` -- programs present in the image but deliberately not
  wrapped: GUIs, GUI drivers, demo/dependency installers, and internal/dev
  utilities. Whole families that are uniformly GUI/non-batch match a prefix
  rule (``IGNORE_PREFIXES``: ``@Install_``, ``uber_``, ``plugout_``); the rest
  have no safe shared pattern -- a bare ``@`` prefix or a ``test``/``Test``
  substring would wrongly catch real tools (``@auto_tlrc``, ``3dNormalityTest``,
  ``@GradFlipTest``) -- so they are listed explicitly in ``IGNORE_EXPLICIT``,
  grouped by reason.
* ``apps`` == ``executables.required`` -- everything else: the surface niwrap
  wraps and that ``check-container`` validates in CI.

Run it whenever the pinned container changes::

    python extraction/afni/app_list.py                  # rewrite version.json
    python extraction/afni/app_list.py --check          # CI: fail if stale
    python extraction/afni/app_list.py --prune-orphans  # also delete dropped descriptors

Requires Docker on PATH and network access to pull the image on first run.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from applist_common import PROJECT_DIR, docker_capture, run_cli  # noqa: E402

DEFAULT_VERSION_FILE = PROJECT_DIR / "src/niwrap/afni/24.2.06/version.json"

# Programs to leave unwrapped, by name prefix -- families where every member is
# a GUI / non-batch program, so the rule is safe and self-maintaining:
#   @Install_*  demo-dataset installers (@Install_NMT, @Install_MACAQUE_DEMO, ...)
#   uber_*      Tk "uber" GUIs that build processing scripts (uber_subject.py, ...)
#   plugout_*   helpers that drive a running afni GUI over its plugout port
IGNORE_PREFIXES = ("@Install_", "uber_", "plugout_")

# The non-mechanical remainder: real AFNI programs we choose not to wrap, with
# no safe shared pattern. Grouped by reason so the curation is auditable.
IGNORE_EXPLICIT = {
    # interactive GUI viewers / drivers (no batch interface to wrap)
    "afni",
    "aiv",
    "suma",
    "DriveSuma",
    "SUMA_paperplane",
    "HalloSuma",
    # @-prefixed internal helpers / drivers (not standalone analysis tools)
    "@DriveAfni",
    "@DriveSuma",
    "@FullPath",
    "@GetAfniBin",
    "@R_funclist",
    "@afni_refacer_make_master_addendum",
    "@clean_help_dir",
    "@escape-",
    "@global_parse",
    "@parse_name",
    # dependency installers (do not match the @Install_ prefix)
    "@afni_R_package_install",
    "rPkgsInstall",
    # internal wrappers, name-parsing helpers, dev/test utilities
    "ParseName",
    "afni_python_wrapper.py",
    "afni_skeleton.py",
    "afni_vcheck",
    "byteorder",
    "eg_main_chrono.py",
    "mycat",
    "python_module_test.py",
    "test_afni_prog_help.tcsh",
    "adjunct_tort_read_dp_align.py",
}


def list_programs(container: str) -> list[str]:
    """AFNI's authoritative program list via ``apsearch``."""
    names = docker_capture(container, "apsearch -list_all_afni_progs 2>/dev/null")
    if not names:
        raise SystemExit(
            f"error: 'apsearch -list_all_afni_progs' returned nothing in {container}"
        )
    return names


def partition(names: list[str]) -> tuple[list[str], list[str]]:
    """Split into (apps/required, ignored), sorted.

    Explicit-ignore names that no longer appear in the program list are reported
    -- the signal that curation has drifted from the image.
    """
    stale = sorted(IGNORE_EXPLICIT - set(names))
    if stale:
        print(
            "warning: explicit-ignore entries not in this image (renamed/removed?): "
            + ", ".join(stale),
            file=sys.stderr,
        )

    def is_ignored(name: str) -> bool:
        return name.startswith(IGNORE_PREFIXES) or name in IGNORE_EXPLICIT

    ignored = sorted(n for n in names if is_ignored(n))
    apps = sorted(n for n in names if not is_ignored(n))
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
