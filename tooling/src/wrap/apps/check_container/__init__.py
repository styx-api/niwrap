"""Validate that executables listed in version files exist in their containers.

This module provides a robust validation system that:
1. Groups executables by container to minimize docker operations
2. Tests all executables in batched container runs
3. Provides detailed reporting and CI-friendly exit codes
4. Handles errors gracefully with comprehensive logging
"""

import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Set, Tuple

from wrap.apps.find_niwrap import find_niwrap
from wrap.catalog import PackageType, VersionType
from wrap.catalog_niwrap import (
    get_version_niwrap,
    iter_packages_niwrap,
)


class ValidationStatus(Enum):
    """Validation status for executables."""

    FOUND = "found"
    MISSING = "missing"
    ERROR = "error"


@dataclass
class ExecutableResult:
    """Result of checking a single executable."""

    name: str
    status: ValidationStatus
    versions: List[str]  # List of version IDs that require this executable
    error_message: Optional[str] = None


@dataclass
class ContainerValidation:
    """Validation results for a single container."""

    container: str
    versions: List[Tuple[PackageType, VersionType]]
    results: List[ExecutableResult] = field(default_factory=list)
    validation_errors: List[str] = field(default_factory=list)

    @property
    def missing_executables(self) -> List[ExecutableResult]:
        """Get all missing executables."""
        return [r for r in self.results if r.status == ValidationStatus.MISSING]

    @property
    def found_executables(self) -> List[ExecutableResult]:
        """Get all found executables."""
        return [r for r in self.results if r.status == ValidationStatus.FOUND]

    @property
    def has_failures(self) -> bool:
        """Check if this validation has any failures."""
        return bool(self.missing_executables or self.validation_errors)

    @property
    def affected_version_ids(self) -> Set[str]:
        """Get all version IDs affected by this container."""
        return {f"{pkg['name']}/{ver['name']}" for pkg, ver in self.versions}


class DockerExecutor:
    """Handles Docker command execution with proper error handling."""

    def __init__(self, timeout: int = 120) -> None:
        self.timeout = timeout
        self._check_docker_available()

    def _check_docker_available(self) -> None:
        """Verify Docker is available on the system."""
        try:
            subprocess.run(
                ["docker", "--version"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=5,
                check=True,
            )
        except FileNotFoundError:
            raise RuntimeError(
                "Docker is not installed or not in PATH. "
                "Please install Docker to use this validation tool."
            )
        except subprocess.SubprocessError as e:
            raise RuntimeError(f"Docker is not functioning correctly: {e}")

    def check_executables(
        self, container: str, executables: List[str]
    ) -> Dict[str, bool]:
        """Check multiple executables in a single container run.

        Args:
            container: Docker container image
            executables: List of executable names to check

        Returns:
            Dict mapping executable name to whether it exists

        Raises:
            RuntimeError: If Docker command fails
            subprocess.TimeoutExpired: If command times out
        """
        if not executables:
            return {}

        # Build a shell script that checks all executables
        # Use 'command -v' which is POSIX-compliant and more reliable than 'which'
        checks = []
        for exe in executables:
            # Properly escape executable name for shell
            escaped = exe.replace("'", "'\\''")
            checks.append(
                f"command -v '{escaped}' >/dev/null 2>&1 && "
                f"echo 'FOUND:{exe}' || echo 'MISSING:{exe}'"
            )

        script = " && ".join(checks)

        try:
            result = subprocess.run(
                [
                    "docker",
                    "run",
                    "--rm",
                    "--user",
                    "root",
                    "--entrypoint",
                    "sh",
                    container,
                    "-c",
                    script,
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                timeout=self.timeout,
                check=False,
            )
        except subprocess.TimeoutExpired:
            raise subprocess.TimeoutExpired(
                cmd=["docker", "run", container], timeout=self.timeout
            )

        # Check for Docker-level errors
        if result.returncode not in (0, 1):
            stderr = result.stderr.strip()
            if stderr:
                raise RuntimeError(f"Docker command failed: {stderr}")
            raise RuntimeError(
                f"Docker command failed with exit code {result.returncode}"
            )

        # Parse output
        return self._parse_check_output(result.stdout, executables)

    def _parse_check_output(
        self, output: str, expected_executables: List[str]
    ) -> Dict[str, bool]:
        """Parse the output from executable checks.

        Args:
            output: stdout from the Docker command
            expected_executables: List of executables we checked for

        Returns:
            Dict mapping executable name to whether it exists
        """
        results = {}

        for line in output.strip().split("\n"):
            line = line.strip()
            if line.startswith("FOUND:"):
                exe = line[6:]
                results[exe] = True
            elif line.startswith("MISSING:"):
                exe = line[8:]
                results[exe] = False

        # Verify we got results for all expected executables
        missing_results = set(expected_executables) - set(results.keys())
        if missing_results:
            # This shouldn't happen but handle it gracefully
            for exe in missing_results:
                results[exe] = False

        return results


class BatchExecutableValidator:
    """Validates executables in containers with batched operations."""

    DEFAULT_CHUNK_SIZE = 100

    def __init__(
        self, chunk_size: int = DEFAULT_CHUNK_SIZE, timeout: int = 120
    ) -> None:
        """Initialize the validator.

        Args:
            chunk_size: Maximum executables to check per container run
            timeout: Timeout in seconds for Docker operations
        """
        self.chunk_size = chunk_size
        self.validations: Dict[str, ContainerValidation] = {}
        self.docker = DockerExecutor(timeout=timeout)

    def _group_by_container(
        self, versions: List[Tuple[PackageType, VersionType]]
    ) -> Dict[str, List[Tuple[PackageType, VersionType]]]:
        """Group versions by their container image."""
        grouped: defaultdict[str, List[Tuple[PackageType, VersionType]]] = defaultdict(
            list
        )

        for package, version in versions:
            container = version.get("container")
            executables = version.get("executables")

            if container and executables:
                grouped[container].append((package, version))

        return dict(grouped)

    def _collect_executables(
        self, versions: List[Tuple[PackageType, VersionType]]
    ) -> Tuple[Set[str], Dict[str, List[str]]]:
        """Collect all unique executables and map them to their versions.

        Returns:
            Tuple of (set of unique executables, dict mapping exe to version IDs)
        """
        all_executables: Set[str] = set()
        exe_to_versions: defaultdict[str, List[str]] = defaultdict(list)

        for package, version in versions:
            version_id = f"{package['name']}/{version['name']}"

            for exe in version.get("executables", {}).get("required", []):
                all_executables.add(exe)
                exe_to_versions[exe].append(version_id)

        return all_executables, dict(exe_to_versions)

    def _check_executables_chunked(
        self, container: str, executables: Set[str]
    ) -> Dict[str, bool]:
        """Check executables in chunks to avoid command line length limits.

        Args:
            container: Docker container image
            executables: Set of executable names to check

        Returns:
            Dict mapping executable name to whether it exists
        """
        if not executables:
            return {}

        exe_list = sorted(executables)
        all_results: Dict[str, bool] = {}

        for i in range(0, len(exe_list), self.chunk_size):
            chunk = exe_list[i : i + self.chunk_size]
            chunk_results = self.docker.check_executables(container, chunk)
            all_results.update(chunk_results)

        return all_results

    def validate_container(
        self, container: str, versions: List[Tuple[PackageType, VersionType]]
    ) -> ContainerValidation:
        """Validate all executables for a container across multiple versions."""
        validation = ContainerValidation(container=container, versions=versions)

        # Collect executables
        all_executables, exe_to_versions = self._collect_executables(versions)

        print(f"Validating container: {container}")
        print(
            f"  Checking {len(all_executables)} unique executable(s) "
            f"for {len(versions)} version(s)"
        )

        # Show chunking info if needed
        num_chunks = (len(all_executables) + self.chunk_size - 1) // self.chunk_size
        if num_chunks > 1:
            print(
                f"  (Will run {num_chunks} batch(es) of up to "
                f"{self.chunk_size} executables each)"
            )

        try:
            # Check all executables
            results = self._check_executables_chunked(container, all_executables)

            # Build result objects
            for exe, exists in sorted(results.items()):
                status = ValidationStatus.FOUND if exists else ValidationStatus.MISSING
                result = ExecutableResult(
                    name=exe, status=status, versions=exe_to_versions.get(exe, [])
                )
                validation.results.append(result)

                symbol = "PASS" if exists else "FAIL"
                print(f"    {symbol} {exe}")

        except subprocess.TimeoutExpired:
            error = f"Timeout checking executables (>{self.docker.timeout}s)"
            validation.validation_errors.append(error)
            print(f"  FAIL {error}")
        except RuntimeError as e:
            validation.validation_errors.append(str(e))
            print(f"  ✗ Error: {e}")
        except Exception as e:
            error = f"Unexpected error: {type(e).__name__}: {e}"
            validation.validation_errors.append(error)
            print(f"  FAIL {error}")

        return validation

    def validate_all(self) -> Dict[str, ContainerValidation]:
        """Validate all versions in the repository.

        Returns:
            Dict mapping container name to validation results
        """
        # Collect all versions
        versions: List[Tuple[PackageType, VersionType]] = []

        for package in iter_packages_niwrap():
            package_name = package["name"]
            for version_name in package["versions"]:
                version = get_version_niwrap(package_name, version_name)
                versions.append((package, version))

        print(f"Found {len(versions)} version file(s)\n")

        # Group by container
        grouped = self._group_by_container(versions)
        print(f"Validating {len(grouped)} unique container(s)\n")

        # Validate each container
        for container in sorted(grouped.keys()):
            validation = self.validate_container(container, grouped[container])
            self.validations[container] = validation
            print()

        return self.validations

    def print_summary(self) -> None:
        """Print a detailed summary of validation results."""
        if not self.validations:
            print("No validation results to summarize")
            return

        print("=" * 80)
        print("VALIDATION SUMMARY")
        print("=" * 80)
        print()

        # Calculate statistics
        total_containers = len(self.validations)
        total_versions = sum(len(v.versions) for v in self.validations.values())
        total_missing = sum(
            len(v.missing_executables) for v in self.validations.values()
        )
        total_found = sum(len(v.found_executables) for v in self.validations.values())
        total_errors = sum(len(v.validation_errors) for v in self.validations.values())

        print(f"Containers checked:    {total_containers}")
        print(f"Versions validated:    {total_versions}")
        print(f"Executables found:     {total_found}")
        print(f"Executables missing:   {total_missing}")
        print(f"Validation errors:     {total_errors}")
        print()

        # Report failures
        failed = {c: v for c, v in self.validations.items() if v.has_failures}

        if failed:
            print(f"FAILED VALIDATIONS ({len(failed)} container(s)):")
            print("-" * 80)

            for container in sorted(failed.keys()):
                validation = failed[container]
                print(f"\nContainer: {container}")
                print(f"Affects: {', '.join(sorted(validation.affected_version_ids))}")

                if validation.missing_executables:
                    print(
                        f"\n  Missing executables "
                        f"({len(validation.missing_executables)}):"
                    )
                    for result in sorted(
                        validation.missing_executables, key=lambda r: r.name
                    ):
                        print(f"    - {result.name}")
                        print(f"      Required by: {', '.join(result.versions)}")

                if validation.validation_errors:
                    print(f"\n  Errors ({len(validation.validation_errors)}):")
                    for error in validation.validation_errors:
                        print(f"    - {error}")
        else:
            print("All validations passed!")

        print()
        print("=" * 80)

    def get_exit_code(self) -> int:
        """Return appropriate exit code based on validation results.

        Returns:
            0 if all validations passed
            1 if any validation failed or no results
        """
        if not self.validations:
            return 1  # No results

        if any(v.has_failures for v in self.validations.values()):
            return 1  # Validation failures

        return 0  # All passed


def main() -> int:
    """Main entry point for the validation script.

    Returns:
        Exit code (0 for success, non-zero for failure)
    """
    try:
        find_niwrap()
    except Exception as e:
        print(f"Error: Failed to initialize niwrap: {e}", file=sys.stderr)
        return 1

    # Run validation
    validator = BatchExecutableValidator()

    try:
        validator.validate_all()
        validator.print_summary()
        return validator.get_exit_code()
    except RuntimeError as e:
        print(f"\nError: {e}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\n\nValidation interrupted by user", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"\nUnexpected error: {type(e).__name__}: {e}", file=sys.stderr)
        return 1


def register_command(subparsers: Any) -> None:
    """Register this command with the argument parser.

    Args:
        subparsers: Subparser object from argparse
    """
    parser = subparsers.add_parser(
        "check-container",
        help="Validate that required executables exist in container images",
    )

    parser.set_defaults(func=lambda args: main())


if __name__ == "__main__":
    sys.exit(main())
