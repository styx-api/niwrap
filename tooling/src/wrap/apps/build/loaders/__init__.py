import json
import pathlib as pl

from styx.frontend.boutiques import from_boutiques
from styx.ir import core as ir

from wrap.apps.build.loaders.workbench import load_workbench
from wrap.catalog import DescriptorSourceType


def load_source(source: DescriptorSourceType, app_path: pl.Path) -> ir.App:
    source_type = source["type"]
    if source_type == "boutiques":
        with (app_path.parent / source["path"]).open(encoding="utf-8") as f:
            return from_boutiques(json.load(f))
    if source_type == "workbench":
        with (app_path.parent / source["path"]).open(encoding="utf-8") as f:
            return load_workbench(json.load(f))

    raise Exception(f"Unknown source type '{source_type}'")
