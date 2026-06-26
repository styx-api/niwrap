"""Shared plumbing for the per-package ``app_list.py`` generators.

The wrapped-program lists in ``src/niwrap/<pkg>/<ver>/version.json`` are derived
from the release container, not hand-maintained. Each package differs in *how*
its programs are enumerated and *how* they are split into wrapped vs. ignored
(ANTs lists a bin dir; AFNI asks ``apsearch``; ...), so every package keeps its
own small ``app_list.py`` that supplies two callables:

    list_programs(container) -> list[str]      # enumerate the tool's programs
    partition(names)         -> (apps, ignored) # split wrapped vs. ignored

and hands them to :func:`run_cli`, which owns everything package-independent:
reading the container from the manifest, rewriting only the derived keys, and
two consistency guards --

    --check          exit non-zero if the manifest (or descriptor tree) is stale
    --prune-orphans  delete descriptor dirs no longer in ``apps`` before writing

The descriptor-tree guard matters because an ignored program must also lose its
``src/niwrap/<pkg>/<ver>/<prog>/`` descriptor, or Styx keeps generating a
wrapper for it. The invariant the guard enforces is simply: the set of
descriptor dirs equals the ``apps`` list.
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Callable

# extraction/applist_common.py -> repo root is two levels up.
PROJECT_DIR = Path(__file__).resolve().parent.parent


def docker_capture(container: str, snippet: str) -> list[str]:
    """Run a POSIX ``sh`` snippet in ``container``; return non-empty output lines.

    Uses ``--entrypoint sh`` the same way ``check-container`` does, so nothing is
    assumed about the image's default entrypoint.
    """
    try:
        result = subprocess.run(
            ["docker", "run", "--rm", "--entrypoint", "sh", container, "-c", snippet],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
    except FileNotFoundError:
        raise SystemExit("error: docker is not installed or not on PATH")
    except subprocess.CalledProcessError as exc:
        raise SystemExit(
            f"error: 'docker run {container}' failed (exit {exc.returncode}):\n"
            f"{exc.stderr.strip()}"
        )
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def build_manifest(manifest: dict, apps: list[str], ignored: list[str]) -> dict:
    """Return a copy of ``manifest`` with the derived lists applied in place.

    Only the derived keys are touched; key order and every other field are
    preserved so the diff stays minimal. ``required`` is kept identical to
    ``apps`` -- the two are the same surface for these packages.
    """
    updated = dict(manifest)
    updated["apps"] = apps
    executables = dict(updated.get("executables", {}))
    executables["required"] = apps
    executables["ignored"] = ignored
    updated["executables"] = executables
    return updated


def dumps(manifest: dict) -> str:
    """Serialize matching the repo convention: 2-space indent, trailing newline."""
    return json.dumps(manifest, indent=2) + "\n"


def find_orphan_descriptors(version_file: Path, apps: list[str]) -> list[str]:
    """Descriptor dirs beside ``version_file`` that are not in ``apps``.

    These generate (or leave behind) wrappers for programs no longer wrapped,
    so they should be pruned to keep ``dirs == apps``.
    """
    appset = set(apps)
    return sorted(
        p.name
        for p in version_file.parent.iterdir()
        if p.is_dir() and p.name not in appset
    )


def run_cli(
    *,
    default_version_file: Path,
    list_programs: Callable[[str], list[str]],
    partition: Callable[[list[str]], tuple[list[str], list[str]]],
    description: str | None = None,
) -> int:
    """Drive a package generator. Returns a process exit code."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "--version-file",
        type=Path,
        default=default_version_file,
        help=f"version manifest to update (default: {default_version_file})",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write; exit non-zero if the manifest or descriptor tree is "
        "out of date (for CI)",
    )
    parser.add_argument(
        "--prune-orphans",
        action="store_true",
        help="delete descriptor dirs no longer in 'apps' before writing",
    )
    args = parser.parse_args()

    manifest = json.loads(args.version_file.read_text())
    container = manifest.get("container")
    if not container:
        raise SystemExit(f"error: {args.version_file} has no 'container' field")

    print(f"Reading programs from {container} ...", file=sys.stderr)
    names = list_programs(container)
    apps, ignored = partition(names)
    extra = f" ({', '.join(ignored)})" if len(ignored) <= 12 else ""
    print(
        f"  {len(names)} programs -> {len(apps)} wrapped, {len(ignored)} ignored{extra}",
        file=sys.stderr,
    )

    new_text = dumps(build_manifest(manifest, apps, ignored))
    orphans = find_orphan_descriptors(args.version_file, apps)

    if args.check:
        manifest_ok = new_text == args.version_file.read_text()
        if manifest_ok and not orphans:
            print(f"OK: {args.version_file} is up to date")
            return 0
        if not manifest_ok:
            print(
                f"STALE: {args.version_file} does not match {container}.",
                file=sys.stderr,
            )
        if orphans:
            print(
                f"ORPHANS: {len(orphans)} descriptor dir(s) not in 'apps': "
                f"{', '.join(orphans)}",
                file=sys.stderr,
            )
        print("re-run without --check (add --prune-orphans) to update.", file=sys.stderr)
        return 1

    if orphans:
        if args.prune_orphans:
            for name in orphans:
                shutil.rmtree(args.version_file.parent / name)
            print(f"Pruned {len(orphans)} orphan descriptor dir(s)")
        else:
            print(
                f"warning: {len(orphans)} descriptor dir(s) no longer in 'apps' "
                f"(re-run with --prune-orphans to delete): {', '.join(orphans)}",
                file=sys.stderr,
            )

    args.version_file.write_text(new_text)
    print(f"Wrote {args.version_file}")
    return 0
