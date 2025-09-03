"""Run Styx to compile descriptors into wrappers & generate package metadata."""

import json
import time
from pathlib import Path
from shutil import rmtree
from typing import Iterator, Any

from styx.backend import compile_language
from styx.frontend.boutiques import from_boutiques
from styx.ir import core as ir
from styx.ir.optimize import optimize

# Configuration
PATH_PACKAGES = Path("packages")
PATH_DESCRIPTORS = Path("descriptors")
PATH_BUILD_TEMPLATES = Path("build-templates")
PATH_DIST_ROOT = Path("dist")

# Distribution configurations
DISTRIBUTIONS = [
    ("python", "python", True),
    ("js", "typescript", False),
    ("json-schema", "jsonschema", False),
    ("ir-dump", "ir", False),
]


class BuildStats:
    """Track build statistics."""

    def __init__(self):
        self.packages = 0
        self.descriptors = 0
        self.files_generated = 0
        self.errors = []
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def elapsed(self) -> float:
        return time.time() - self.start_time if self.start_time else 0


def load_json_file(filepath: Path) -> dict[str, Any]:
    """Load JSON file with proper encoding."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def iter_packages() -> Iterator[tuple[Path, dict[str, Any]]]:
    """Iterate over all package definitions."""
    for package_file in PATH_PACKAGES.glob("*.json"):
        yield package_file, load_json_file(package_file)


def iter_descriptors(package: dict[str, Any]) -> Iterator[tuple[Path, dict[str, Any]]]:
    """Iterate over all descriptors for a given package."""
    package_path = PATH_DESCRIPTORS / package["id"]
    for descriptor_file in sorted(package_path.glob("**/*.json")):
        yield descriptor_file, load_json_file(descriptor_file)


def get_niwrap_version() -> str:
    """Get the niwrap version from VERSION file."""
    return Path("VERSION").read_text(encoding="utf-8").strip()


def calculate_api_coverage(endpoints: list[dict[str, str]]) -> tuple[int, int, str]:
    """Calculate API coverage statistics.

    Returns:
        tuple of (done_count, relevant_count, formatted_coverage)
    """
    done = sum(1 for ep in endpoints if ep["status"] == "done")
    ignored = sum(1 for ep in endpoints if ep["status"] == "ignore")
    relevant = len(endpoints) - ignored

    if relevant == 0:
        return done, relevant, "N/A"

    percentage = done / relevant * 100
    if percentage == 100:
        return done, relevant, f"{done}/{relevant} (100% 🎉)"
    return done, relevant, f"{done}/{relevant} ({percentage:.1f}%)"


def build_package_overview_table() -> str:
    """Build markdown table summarizing all packages."""
    packages = sorted([pkg for _, pkg in iter_packages()], key=lambda x: x["name"])

    lines = [
        "| Package | Status | Version | API Coverage |",
        "| --- | --- | --- | --- |",
    ]

    for pkg in packages:
        # Package name with link
        name_link = f"[{pkg['name']}]({pkg['url']})"

        # API coverage
        _, _, coverage = calculate_api_coverage(pkg["api"]["endpoints"])

        # Container version
        container_tag = pkg.get("container", "")
        if container_tag:
            docker_image = container_tag.split(":")[0]
            docker_hub = f"https://hub.docker.com/r/{docker_image}"
            container = f"[`{pkg['version']}`]({docker_hub})"
        else:
            container = "?"

        lines.append(f"| {name_link} | {pkg['status']} | {container} | {coverage} |")

    return "\n".join(lines)


def generate_python_readme() -> str:
    """Generate README for Python distribution."""
    template_path = PATH_BUILD_TEMPLATES / "python/README-template.md"
    template = template_path.read_text(encoding="utf-8")
    return template.replace("{{PACKAGES_TABLE}}", build_package_overview_table())


def print_box(title: str, items: list[str]):
    """Print a formatted box with title and items."""
    item_widths = [len(item) + 2 for item in items]
    dividers = "┬".join("─" * w for w in item_widths)
    top_line = list(f"┌{dividers}┐")
    title_text = f"─ {title} ─"
    for i, char in enumerate(title_text):
        if i + 1 < len(top_line):
            top_line[i + 1] = char

    print("".join(top_line))
    print("│" + "│".join(f" {item} " for item in items) + "│")
    print("└" + "┴".join("─" * w for w in item_widths) + "┘")


def create_project_metadata() -> ir.Project:
    """Create the main project metadata."""
    return ir.Project(
        name="niwrap",
        version=get_niwrap_version(),
        license="MIT",
        docs=ir.Documentation(
            title="NiWrap",
            description="Neuroimaging wrappers.",
            authors=["CMI DAIR"],
            literature=[
                "Rupprecht, F. J., Kai, J., Shrestha, B., Giavasis, S., Xu, T., "
                "Glatard, T., ... & Kiar, G. (2025). Styx: A multi-language API "
                "Generator for Command-Line Tools. bioRxiv, 2025-07."
            ],
            urls=["https://github.com/styx-api/niwrap"],
        ),
    )


def process_package(pkg_json: dict[str, Any]) -> tuple[ir.Package, Any]:
    """Process a single package and its descriptors.

    Returns:
        tuple of (package_metadata, interface_generator)
    """
    start_time = time.time()
    print(f"    📦 {pkg_json['name']:<24} ", end="", flush=True)

    package = ir.Package(
        name=pkg_json["id"],
        version=pkg_json["version"],
        docker=pkg_json["container"],
        docs=ir.Documentation(
            title=pkg_json["name"],
            description=pkg_json["description"],
            authors=[pkg_json["author"]],
            urls=[pkg_json["url"]],
        ),
    )

    def interface_generator():
        descriptor_count = 0
        errors = []

        for file_descriptor, descriptor in iter_descriptors(pkg_json):
            descriptor_count += 1
            try:
                yield optimize(from_boutiques(descriptor))
            except Exception as e:
                error_msg = f"{file_descriptor.stem}: {str(e)}"
                errors.append(error_msg)
                print(f"\n      ❌ {error_msg}", end="")

        # Report package completion
        elapsed = time.time() - start_time
        status = "⚠️" if errors else "✅"
        error_text = f" ({len(errors)} errors)" if errors else ""
        print(
            f"{status} {descriptor_count:>3} descriptors ({elapsed:.2f}s){error_text}"
        )

    return package, interface_generator()


def compile_distribution(
    dist_name: str,
    backend_name: str,
    needs_readme: bool,
    project: ir.Project,
    stats: BuildStats,
) -> int:
    """Compile a single distribution.

    Returns:
        Number of files generated.
    """
    print(f"  {dist_name}")

    # Set distribution-specific metadata
    project.extras["dist_repo_url"] = f"https://github.com/styx-api/niwrap-{dist_name}"
    project.extras["readme_md"] = generate_python_readme() if needs_readme else None

    dist_path = PATH_DIST_ROOT / f"niwrap-{dist_name}"
    dist_start = time.time()
    file_count = 0

    # Generate package stream for this distribution
    def create_package_stream():
        for _, pkg_json in iter_packages():
            yield process_package(pkg_json)

    # Compile files
    for file in compile_language(backend_name, project, create_package_stream()):
        file.write(dist_path)
        file_count += 1

    # Add special files if needed
    if dist_name == "json-schema":
        (dist_path / ".nojekyll").touch()

    elapsed = time.time() - dist_start
    print(f"    → {file_count:>4} files ({elapsed:.1f}s)")

    return file_count


def compile_all_distributions(stats: BuildStats):
    """Compile all distributions with progress tracking."""
    # Clean and create output directory
    rmtree(PATH_DIST_ROOT, ignore_errors=True)
    PATH_DIST_ROOT.mkdir(parents=True, exist_ok=True)

    # Calculate build stats
    stats.packages = sum(1 for _ in PATH_PACKAGES.glob("*.json"))
    stats.descriptors = sum(1 for _ in PATH_DESCRIPTORS.glob("**/*.json"))

    print_box(
        title="Build Overview",
        items=[
            f"Packages: {stats.packages}",
            f"Descriptors: {stats.descriptors}",
            f"Distributions: {len(DISTRIBUTIONS)}",
        ],
    )

    project = create_project_metadata()

    print("\n🔄 Generating distributions...")
    build_start = time.time()

    for i, (dist_name, backend_name, needs_readme) in enumerate(DISTRIBUTIONS, 1):
        print(f"\n  [{i}/{len(DISTRIBUTIONS)}] ", end="")
        file_count = compile_distribution(
            dist_name, backend_name, needs_readme, project, stats
        )
        stats.files_generated += file_count

    total_elapsed = time.time() - build_start

    print()
    print_box(
        title="Build Summary",
        items=[
            f"Total files: {stats.files_generated}",
            f"Build time: {total_elapsed:.1f}s",
        ],
    )


def validate_build(stats: BuildStats):
    """Validate the build output."""
    print("\n🔍 Validating...", end=" ", flush=True)

    # Check Python distribution exists
    path_dist_python = PATH_DIST_ROOT / "niwrap-python"
    if not path_dist_python.exists():
        raise ValueError("Python distribution not found")

    # Check for generated Python files
    python_files = [
        f for f in path_dist_python.glob("**/*.py") if f.name != "__init__.py"
    ]
    if not python_files:
        raise ValueError("No Python files generated")

    # Validate package structure
    for package_file, package_data in iter_packages():
        if not package_data.get("id"):
            raise ValueError(f"Package {package_file.name} missing 'id'")

        package_descriptors = list(
            (PATH_DESCRIPTORS / package_data["id"]).glob("**/*.json")
        )
        if not package_descriptors:
            raise ValueError(f"No descriptors for package {package_data['id']}")

    print(f"✅ {len(python_files)} files from {stats.descriptors} descriptors")


def main():
    """Main build function."""
    # Change to script directory
    script_dir = Path(__file__).parent
    if script_dir != Path.cwd():
        import os

        os.chdir(script_dir)

    # Verify paths exist
    if not PATH_DESCRIPTORS.exists() or not PATH_PACKAGES.exists():
        print("❌ Error: Please ensure working directory is niwrap repo root.")
        print(f"   Current directory: {Path.cwd()}")
        return 1

    print("🚀 NiWrap Build Process")

    stats = BuildStats()
    stats.start()

    try:
        compile_all_distributions(stats)
        validate_build(stats)

        print(f"\n✅ Build completed successfully in {stats.elapsed():.1f}s")
        return 0

    except Exception as e:
        print(f"\n❌ Build failed: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys

    sys.exit(main())
