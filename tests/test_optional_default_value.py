import pytest
import json
import pathlib


def load_descriptors():
    return pathlib.Path("descriptors").glob("**/*.json")


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


# The ids param makes sure the paths are logged in the pytest print output
@pytest.mark.parametrize("descriptor_path", load_descriptors(), ids=map(str, load_descriptors()))
class TestOptionalDefaults:
    def test_descriptor_optional_default(self, descriptor_path: pathlib.Path):
        """Optional inputs should not use `default-value` (with extremely rare exceptions)."""
        
        # dcm2niix has an optional output param which if not set writes outputs to input file location
        if "workbench" in str(descriptor_path) or "mrtrix" in str(descriptor_path) or "dcm2niix" in str(descriptor_path):
            pytest.skip(f"Skipping excluded file: {descriptor_path}")

        with open(descriptor_path) as f:
            descriptor = json.load(f)

        assert not has_optional_with_default(descriptor), \
            f"Found optional input with default-value in {descriptor_path}"