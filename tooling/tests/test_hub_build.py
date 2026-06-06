"""Tests for the `wrap hub-build` hosted-layout builder."""

import json
import pathlib as pl
from typing import Any

import pytest

from wrap.apps.hub_build import (
    DEFAULT_COMPILER,
    _compiler_object,
    _summary,
    build_hub_layout,
)


def _write(path: pl.Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data), encoding="utf-8")


@pytest.fixture
def catalog_root(tmp_path: pl.Path, monkeypatch: pytest.MonkeyPatch) -> pl.Path:
    """A minimal niwrap catalog with a wrapped boutiques tool, a workbench tool,
    and a listed-but-unwrapped app; cwd is set to its root."""
    src = tmp_path / "src" / "niwrap"
    _write(
        src / "project.json",
        {
            "name": "niwrap",
            "version": "9.9.9",
            "license": "MIT",
            "packages": ["demo"],
            "docs": {"title": "Demo", "description": "Demo project."},
        },
    )
    _write(
        src / "demo" / "package.json",
        {
            "name": "demo",
            "neurodeskId": "demo",
            "versions": ["1.0"],
            "default": "1.0",
            "docs": {"title": "Demo Pkg", "description": "A demo package."},
        },
    )
    _write(
        src / "demo" / "1.0" / "version.json",
        {"name": "1.0", "container": "demo/img:1.0", "apps": ["tool", "wbtool", "bare"]},
    )
    _write(
        src / "demo" / "1.0" / "tool" / "app.json",
        {
            "name": "tool",
            "source": {"type": "boutiques", "path": "boutiques.json"},
            "docs": {"description": "A boutiques tool.\n\nA long second paragraph."},
        },
    )
    _write(src / "demo" / "1.0" / "tool" / "boutiques.json", {"name": "tool", "x": 1})
    _write(
        src / "demo" / "1.0" / "wbtool" / "app.json",
        {
            "name": "wbtool",
            "source": {"type": "workbench", "path": "workbench.json"},
            "docs": {"description": "A workbench tool."},
        },
    )
    _write(src / "demo" / "1.0" / "wbtool" / "workbench.json", {"name": "wbtool"})
    # Listed in version.apps but never wrapped (no source).
    _write(src / "demo" / "1.0" / "bare" / "app.json", {"name": "bare"})

    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_build_hub_layout(catalog_root: pl.Path) -> None:
    out = catalog_root / "out"
    stats = build_hub_layout(out, DEFAULT_COMPILER)

    assert stats == {"packages": 1, "apps": 3, "descriptors": 2}

    index = json.loads((out / "index.json").read_text(encoding="utf-8"))
    assert index["latest"] == "9.9.9"
    assert index["versions"][0]["catalog"] == "9.9.9/catalog.json"
    assert index["versions"][0]["compiler"] == DEFAULT_COMPILER

    catalog = json.loads((out / "9.9.9" / "catalog.json").read_text(encoding="utf-8"))
    assert catalog["schemaVersion"] == 1
    assert catalog["project"] == "niwrap"
    assert catalog["version"] == "9.9.9"
    assert catalog["compiler"] == {"name": "@styx-api/core", "version": "0.2.0"}
    assert catalog["descriptorBase"] == "descriptors"
    assert catalog["docs"]["title"] == "Demo"
    assert len(catalog["packages"]) == 1

    pkg = catalog["packages"][0]
    assert pkg["name"] == "demo"
    assert pkg["version"] == "1.0"
    assert pkg["container"] == "demo/img:1.0"
    assert pkg["neurodeskId"] == "demo"
    assert pkg["docs"]["title"] == "Demo Pkg"

    apps = {a["name"]: a for a in pkg["apps"]}
    # No compiled `@type` in the manifest: the compiler owns name scrubbing, so the
    # hub derives @type by compiling the descriptor (see module docstring).
    assert apps["tool"] == {
        "name": "tool",
        "description": "A boutiques tool.",  # first line only
        "descriptor": "descriptors/demo/tool.json",
        "format": "boutiques",
    }
    assert apps["wbtool"]["format"] == "workbench"
    assert apps["wbtool"]["descriptor"] == "descriptors/demo/wbtool.json"
    # Unwrapped app: name only, no descriptor / format / description.
    assert apps["bare"] == {"name": "bare"}


def test_descriptors_copied_verbatim(catalog_root: pl.Path) -> None:
    out = catalog_root / "out"
    build_hub_layout(out, DEFAULT_COMPILER)

    src = catalog_root / "src" / "niwrap" / "demo" / "1.0" / "tool" / "boutiques.json"
    dst = out / "9.9.9" / "descriptors" / "demo" / "tool.json"
    assert dst.read_bytes() == src.read_bytes()


def test_clean_rebuild_drops_stale_descriptors(catalog_root: pl.Path) -> None:
    out = catalog_root / "out"
    build_hub_layout(out, DEFAULT_COMPILER)
    stale = out / "9.9.9" / "descriptors" / "demo" / "removed.json"
    stale.write_text("{}", encoding="utf-8")

    build_hub_layout(out, DEFAULT_COMPILER)
    assert not stale.exists()


def test_summary_first_line_and_cap() -> None:
    assert _summary(None) is None
    assert _summary({}) is None
    assert _summary({"description": "One line.\nSecond."}) == "One line."
    long = "x" * 300
    out = _summary({"description": long})
    assert out is not None and out.endswith("...") and len(out) <= 243


def test_compiler_object_keeps_scope() -> None:
    assert _compiler_object("@styx-api/core@0.2.0") == {
        "name": "@styx-api/core",
        "version": "0.2.0",
    }
    assert _compiler_object("styx@1.2.3") == {"name": "styx", "version": "1.2.3"}
    with pytest.raises(ValueError):
        _compiler_object("noversion")
