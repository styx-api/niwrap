import json
import os
from pathlib import Path

import pytest


def load_packages():
    return map(
        str, Path("packages").glob("*.json")
    )  # pytest print output does not like pathlib


@pytest.mark.parametrize("package_path", load_packages())
class TestOrphanedDescriptors:
    def test_no_orphaned_descriptors(self, package_path):
        """Each descriptor file should be referenced by its package endpoint."""

        # Load the package JSON file
        with open(package_path) as f:
            package_data = json.load(f)

        package_id = package_data.get("id")
        assert package_id, f"Missing 'id' in {package_path}"

        # Collect the listed descriptor files from the endpoints
        listed_descriptors = set()
        for endpoint in package_data.get("api", {}).get("endpoints", []):
            descriptor_path = endpoint.get("descriptor")
            if descriptor_path:
                descriptor_file = os.path.basename(descriptor_path)
                listed_descriptors.add(descriptor_file)

        # Check for orphaned descriptor files
        descriptor_dir = Path("descriptors") / package_id
        if descriptor_dir.exists():
            actual_descriptors = set(f.name for f in descriptor_dir.glob("*.json"))
            orphaned_files = actual_descriptors - listed_descriptors

            assert not orphaned_files, (
                f"Found orphaned descriptor files in {package_id}:\n"
                f"{chr(10).join('  ' + str(f) for f in orphaned_files)}"
            )

    def test_descriptor_files_exist(self, package_path):
        """Each descriptor referenced in package endpoints should exist."""

        # Load the package JSON file
        with open(package_path) as f:
            package_data = json.load(f)

        package_id = package_data.get("id")
        assert package_id, f"Missing 'id' in {package_path}"

        # Check each endpoint's descriptor exists
        for endpoint in package_data.get("api", {}).get("endpoints", []):
            descriptor_path = endpoint.get("descriptor")
            if descriptor_path:
                full_path = (
                    Path("descriptors") / package_id / os.path.basename(descriptor_path)
                )
                assert full_path.exists(), (
                    f"Referenced descriptor does not exist: {full_path}"
                )
