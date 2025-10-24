import json
import pathlib as pl
from typing import Any


def read_json(p: pl.Path) -> Any:
    with p.open(encoding="utf-8") as f:
        return json.load(f)
