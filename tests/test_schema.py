import glob
import json

import pytest
from boutiques_schema_pydantic.v_styx_1.descriptor import Descriptor
from pydantic import ValidationError


def load_descriptors():
    return glob.glob("descriptors/**/*.json", recursive=True)


class DescriptorValidationFailed(Exception):
    pass


@pytest.mark.parametrize("descriptor_path", load_descriptors())
class TestPydanticSchema:
    def test_descriptor_validation(self, descriptor_path):
        """Test that descriptors can be loaded and validated with the Pydantic schema."""

        with open(descriptor_path) as f:
            descriptor_data = json.load(f)

        try:
            _descriptor_model = Descriptor.model_validate(descriptor_data)

        except ValidationError:
            # For some reason pytest still prints a huge amount of errors when this fails
            # no idea how to solve this from here, but calling it with `--tb=no`, e.g. like this:
            #    pytest tests/test_schema.py::TestPydanticSchema --tb=no
            # supresses it.
            raise DescriptorValidationFailed(
                f"Descriptor {descriptor_path} failed Pydantic validation."
            )
