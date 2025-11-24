"""Boutiques application testing framework."""

import json
from dataclasses import dataclass, field
from enum import IntEnum
from pathlib import Path
from typing import Any, Protocol

from wrap.catalog_niwrap import iter_all_apps_niwrap


class ResultStatus(IntEnum):
    """Status codes for test results."""

    OK = 1
    ERROR = 0


@dataclass(frozen=True)
class TestResult:
    """Immutable test result with status and optional message."""

    status: ResultStatus
    message: str = ""

    @property
    def is_ok(self) -> bool:
        """Check if the test passed."""
        return self.status == ResultStatus.OK

    @classmethod
    def ok(cls) -> "TestResult":
        """Create a successful test result."""
        return cls(ResultStatus.OK)

    @classmethod
    def error(cls, message: str | None = None) -> "TestResult":
        """Create a failed test result with an error message."""
        return cls(ResultStatus.ERROR, message or "Error")


class BoutiquesTest(Protocol):
    """Protocol for boutiques test functions."""

    def __call__(self, path: Path, data: dict[str, Any]) -> TestResult: ...


@dataclass
class TestRunner:
    """Manages and runs boutiques tests."""

    tests: list[BoutiquesTest] = field(default_factory=list)

    def register(self, func: BoutiquesTest) -> BoutiquesTest:
        """Register a boutiques test function.

        Args:
            func: Test function to register

        Returns:
            The registered function (for use as decorator)
        """
        if func in self.tests:
            print(f"Warning: Test '{func.__name__}' already registered")
        else:
            self.tests.append(func)
        return func

    def run(self) -> "TestSummary":
        """Run all registered tests on boutiques applications.

        Returns:
            Summary of test results
        """
        print(f"Running {len(self.tests)} tests...")

        if not self.tests:
            print("No tests registered")
            return TestSummary()

        summary = TestSummary()

        for ctx in iter_all_apps_niwrap():
            source = ctx.app.get("source")
            if not source or source["type"] != "boutiques":
                continue

            boutiques_path = Path(ctx.app["__path__"]).parent / source["path"]
            app_results = self._test_application(boutiques_path)

            if app_results:
                summary.add_application_results(boutiques_path, app_results)
                self._print_errors(boutiques_path, app_results)

        return summary

    def _test_application(self, path: Path) -> "ApplicationTestResults | None":
        """Run all tests on a single boutiques application.

        Args:
            path: Path to the boutiques JSON file

        Returns:
            Test results for the application, or None if file couldn't be loaded
        """
        try:
            with path.open(encoding="utf-8") as f:
                boutiques_data = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading {path}: {e}")
            return None

        results = ApplicationTestResults(path)

        for test in self.tests:
            try:
                result = test(path, boutiques_data)
                results.add_result(test.__name__, result)
            except Exception as e:
                # Catch any unexpected errors from tests
                error_msg = f"Test '{test.__name__}' raised exception: {e}"
                results.add_result(test.__name__, TestResult.error(error_msg))

        return results

    def _print_errors(self, path: Path, results: "ApplicationTestResults") -> None:
        """Print errors for a specific application if any exist."""
        if results.error_count > 0:
            print(f"\nFile: {path}")
            for test_name, message in results.errors:
                print(f"  ✗ {test_name}: {message}")
            print("-" * 80)


@dataclass
class ApplicationTestResults:
    """Results for all tests run on a single application."""

    path: Path
    ok_count: int = 0
    error_count: int = 0
    errors: list[tuple[str, str]] = field(default_factory=list)

    def add_result(self, test_name: str, result: TestResult) -> None:
        """Add a test result."""
        if result.is_ok:
            self.ok_count += 1
        else:
            self.error_count += 1
            self.errors.append((test_name, result.message))

    @property
    def total_tests(self) -> int:
        """Total number of tests run."""
        return self.ok_count + self.error_count

    @property
    def success_rate(self) -> float:
        """Percentage of successful tests."""
        if self.total_tests == 0:
            return 0.0
        return (self.ok_count / self.total_tests) * 100


@dataclass
class TestSummary:
    """Summary statistics for all test runs."""

    applications: dict[Path, ApplicationTestResults] = field(default_factory=dict)

    def add_application_results(
        self, path: Path, results: ApplicationTestResults
    ) -> None:
        """Add results for an application."""
        self.applications[path] = results

    @property
    def total_applications(self) -> int:
        """Total number of applications tested."""
        return len(self.applications)

    @property
    def total_tests_run(self) -> int:
        """Total number of individual tests run."""
        return sum(r.total_tests for r in self.applications.values())

    @property
    def total_passed(self) -> int:
        """Total number of passed tests."""
        return sum(r.ok_count for r in self.applications.values())

    @property
    def total_failed(self) -> int:
        """Total number of failed tests."""
        return sum(r.error_count for r in self.applications.values())

    @property
    def applications_with_errors(self) -> int:
        """Number of applications with at least one test failure."""
        return sum(1 for r in self.applications.values() if r.error_count > 0)

    @property
    def applications_all_passed(self) -> int:
        """Number of applications where all tests passed."""
        return sum(1 for r in self.applications.values() if r.error_count == 0)

    def print_summary(self) -> None:
        """Print a formatted summary of test results."""
        print("\n" + "=" * 80)
        print("TEST SUMMARY")
        print("=" * 80)

        if self.total_applications == 0:
            print("No boutiques applications found to test")
            return

        print(f"Applications tested: {self.total_applications}")
        print(f"  ✓ All tests passed: {self.applications_all_passed}")
        print(f"  ✗ With failures: {self.applications_with_errors}")

        print(f"\nTotal tests run: {self.total_tests_run}")
        print(f"  ✓ Passed: {self.total_passed}")
        print(f"  ✗ Failed: {self.total_failed}")

        if self.total_tests_run > 0:
            success_rate = (self.total_passed / self.total_tests_run) * 100
            print(f"\nOverall success rate: {success_rate:.1f}%")

        if self.applications_with_errors > 0:
            print("\nApplications with errors:")
            for path, results in sorted(
                self.applications.items(), key=lambda x: x[1].error_count, reverse=True
            ):
                if results.error_count > 0:
                    print(f"  {path.name}: {results.error_count} error(s)")


# Global test runner instance
_runner = TestRunner()

# Public API
test_boutiques = _runner.register
run_tests = lambda: _runner.run().print_summary()


# Convenience functions
def ok() -> TestResult:
    """Create a successful test result."""
    return TestResult.ok()


def skip(reason: str | None = None):
    return ok()


def error(message: str | None = None) -> TestResult:
    """Create a failed test result."""
    return TestResult.error(message)
