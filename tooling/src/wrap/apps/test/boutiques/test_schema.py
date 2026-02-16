import pathlib as pl
from typing import Any

from boutiques_schema_pydantic.v_styx_1.descriptor import Descriptor
from pydantic import ValidationError

from wrap.apps.test.test import TestResult, error, ok, test_boutiques


@test_boutiques
def test_descriptor_validation(path: pl.Path, data: Any) -> TestResult:
    """Test that descriptors can be loaded and validated with the Pydantic schema."""
    try:
        _descriptor_model = Descriptor.model_validate(data)
    except ValidationError:
        # You might want to include some validation error details if your framework supports it
        return error("Descriptor failed Pydantic validation")

    return ok()
