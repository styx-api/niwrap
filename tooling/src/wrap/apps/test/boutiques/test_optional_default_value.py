import pathlib as pl
from typing import Any

from wrap.apps.test.test import error, ok, skip, test_boutiques


def has_optional_with_default(obj):
    """Check if object contains optional inputs with default-value."""
    if isinstance(obj, dict):
        inputs = obj.get("inputs", [])
        for input_ in inputs:
            if input_.get("optional") and "default-value" in input_:
                return True
            if has_optional_with_default(input_.get("type")):
                return True
        return False
    elif isinstance(obj, list):
        return any(has_optional_with_default(item) for item in obj)
    return False


@test_boutiques
def test_descriptor_optional_default(path: pl.Path, data: Any):
    """Optional inputs should not use `default-value` (with extremely rare exceptions)."""
    # dcm2niix has an optional output param which if not set writes outputs to input file location
    if "workbench" in str(path) or "mrtrix" in str(path) or "dcm2niix" in str(path):
        return skip(f"Skipping excluded file: {path}")

    if has_optional_with_default(data):
        return error("Found optional input with default-value")

    return ok()
