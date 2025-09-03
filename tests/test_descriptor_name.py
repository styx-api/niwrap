import pytest
import json
import pathlib


def load_descriptors():
    return pathlib.Path("descriptors").glob("**/*.json")


# The ids param makes sure the paths are logged in the pytest print output
@pytest.mark.parametrize("descriptor_path", load_descriptors(), ids=map(str, load_descriptors()))
class TestCommandLine:
    def test_descriptor_name(self, descriptor_path: pathlib.Path):
        """Descriptor name fields should be the same as their file stem."""

        with open(descriptor_path) as f:
            descriptor = json.load(f)

        name = descriptor["name"]
        filename = descriptor_path.name

        assert (name + ".json") == filename, (
            f"Descriptor name: '{name}' + '.json' != filename: '{filename}'"
        )
