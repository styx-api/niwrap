import json
import pathlib as pl
from typing import Any


def read_json(p: pl.Path) -> Any:
    with p.open(encoding="utf-8") as f:
        return json.load(f)


def write_json(p: pl.Path, data: Any) -> None:
    """Write `data` as pretty-printed JSON, creating parent dirs as needed."""
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
