from typing import Any
from wrap.apps.test.test import test_boutiques, ok, error

import pathlib as pl
from boutiques_schema_pydantic.v_styx_1.descriptor import Descriptor
from pydantic import ValidationError


@test_boutiques
def test_descriptor_validation(path: pl.Path, data: Any):
    """Test that descriptors can be loaded and validated with the Pydantic schema."""

    try:
        _descriptor_model = Descriptor.model_validate(data)
    except ValidationError as e:
        # You might want to include some validation error details if your framework supports it
        return error(f"Descriptor failed Pydantic validation")

    return ok()
