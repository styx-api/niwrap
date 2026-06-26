#!/usr/bin/env python3
"""Regenerate the FreeSurfer ``apps`` / ``executables`` lists in a version manifest.

FreeSurfer has no program index (unlike AFNI's ``apsearch``), so the program set
is the executable regular files in ``$FREESURFER_HOME/bin`` -- the same set the
manifest already tracks. The catch is that ``bin`` mixes real analysis programs
with GUIs, bundled third-party tools, data files, and dev scaffolding, and the
naming is inconsistent (``mri_nu_correct.mni`` is a real program while
``reg-mni305.2mm`` is a real script -- so a suffix like ``.mni`` is *not* a safe
signal). Partitioning therefore uses a mix:

* ``IGNORE_SUFFIXES`` -- suffixes that reliably mark a non-program: bundled
  copies of other packages' tools (``.fsl``, ``.afni`` -- niwrap wraps FSL and
  AFNI separately), config templates (``.example``), and FSL FLIRT schedule
  data files (``.sch``).
* ``IGNORE_EXPLICIT`` -- the rest, with no safe shared pattern: GUI viewers and
  viewer-launcher scripts (note ``tkregister2_cmdl`` and ``qdec_glmfit`` are the
  non-GUI variants and are *kept*), the MATLAB-runtime installer, developer test
  programs, and a few non-wrappable leftovers retained from prior curation.
* ``apps`` == ``executables.required`` -- everything else: the surface niwrap
  wraps and that ``check-container`` validates in CI.

Run it whenever the pinned container changes::

    python extraction/freesurfer/app_list.py                  # rewrite version.json
    python extraction/freesurfer/app_list.py --check          # CI: fail if stale
    python extraction/freesurfer/app_list.py --prune-orphans  # also delete dropped descriptors

Requires Docker on PATH and network access to pull the image on first run.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from applist_common import PROJECT_DIR, docker_capture, run_cli  # noqa: E402

DEFAULT_VERSION_FILE = PROJECT_DIR / "src/niwrap/freesurfer/7.4.1/version.json"

# Suffixes that mark a bin entry as not a FreeSurfer analysis program:
#   .fsl      bundled FSL tool copies (bet.fsl, flirt.fsl, ...) -- wrapped via fsl
#   .afni     bundled AFNI tool copy (3dvolreg.afni)            -- wrapped via afni
#   .example  dmrirc config templates
#   .sch      FSL FLIRT schedule data files (not executables in any real sense)
IGNORE_SUFFIXES = (".fsl", ".afni", ".example", ".sch")

# Programs to leave unwrapped that share no safe pattern. Grouped by reason.
IGNORE_EXPLICIT = {
    # GUI viewers and viewer-launcher scripts (no batch interface to wrap).
    # The non-GUI siblings tkregister2_cmdl / qdec_glmfit are deliberately kept.
    "freeview",
    "qdec",
    "rtview",
    "tkmedit",
    "tkmeditfv",
    "tkregister2",
    "tkregisterfv",
    "tksurfer",
    "tksurferfv",
    # legacy Tcl/Tk GUIs (identified by Tk-widget use; the non-GUI .tcl helpers
    # mkima_index.tcl / mkmnc_index.tcl are kept)
    "browse-minc-header.tcl",
    "plot_structure_stats.tcl",
    "unpack_ima.tcl",
    "unpack_ima1.tcl",
    "unpack_mnc.tcl",
    # MATLAB Compiler Runtime installer (setup, not analysis)
    "fs_install_mcr",
    # internal build-dependency helper (echoes whether a target is out of date)
    "UpdateNeeded",
    # developer test programs / scripts
    "Spline3_test",
    "mri_create_tests",
    "parc_atlas_jackknife_test",
    "rbftest",
    "testOrientationPlanesFromParcellation",
    "test_recon-all.csh",
    "test_tutorials.sh",
    # non-wrappable leftovers retained from prior curation (bundled Python
    # runtime, deprecated tool, Tcl widget include)
    "fspython",
    "mris_make_map_surfaces",
    "progressbar.tcl",
}


def list_programs(container: str) -> list[str]:
    """Names of every executable regular file in ``$FREESURFER_HOME/bin``."""
    # POSIX sh, guarded glob (see extraction/ants/app_list.py).
    snippet = (
        'for f in "$FREESURFER_HOME"/bin/*; do '
        '[ -f "$f" ] && [ -x "$f" ] && basename "$f"; '
        "done"
    )
    names = docker_capture(container, snippet)
    if not names:
        raise SystemExit(
            f"error: no executables found in $FREESURFER_HOME/bin of {container}"
        )
    return names


def partition(names: list[str]) -> tuple[list[str], list[str]]:
    """Split into (apps/required, ignored), sorted.

    Explicit-ignore names that no longer appear are reported -- the signal that
    curation has drifted from the image.
    """
    stale = sorted(IGNORE_EXPLICIT - set(names))
    if stale:
        print(
            "warning: explicit-ignore entries not in this image (renamed/removed?): "
            + ", ".join(stale),
            file=sys.stderr,
        )

    def is_ignored(name: str) -> bool:
        return name.endswith(IGNORE_SUFFIXES) or name in IGNORE_EXPLICIT

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
