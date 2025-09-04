"""Run Styx to compile descriptors into wrappers & generate package metadata."""

import json
import sys
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

    elapsed = time.time() - dist_start
    print(f"    → {file_count:>4} files ({elapsed:.1f}s)")

    return file_count


def filter_distributions(requested_dists: list[str]) -> list[tuple[str, str, bool]]:
    """Filter distributions based on command line arguments.
    
    Args:
        requested_dists: List of distribution names requested
        
    Returns:
        Filtered list of distribution configurations
        
    Raises:
        ValueError: If any requested distribution is not available
    """
    if not requested_dists:
        return DISTRIBUTIONS
    
    available_dists = {dist[0]: dist for dist in DISTRIBUTIONS}
    invalid_dists = [d for d in requested_dists if d not in available_dists]
    
    if invalid_dists:
        available = ", ".join(available_dists.keys())
        raise ValueError(
            f"Unknown distribution(s): {', '.join(invalid_dists)}. "
            f"Available: {available}"
        )
    
    return [available_dists[dist] for dist in requested_dists]


def compile_all_distributions(stats: BuildStats, selected_distributions: list[tuple[str, str, bool]]):
    """Compile selected distributions with progress tracking."""
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
            f"Distributions: {len(selected_distributions)}",
        ],
    )

    project = create_project_metadata()

    print("\n🔄 Generating distributions...")
    build_start = time.time()

    for i, (dist_name, backend_name, needs_readme) in enumerate(selected_distributions, 1):
        print(f"\n  [{i}/{len(selected_distributions)}] ", end="")
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


def validate_build(stats: BuildStats, selected_distributions: list[tuple[str, str, bool]]):
    """Validate the build output."""
    print("\n🔍 Validating...", end=" ", flush=True)

    # Check that at least one distribution was built
    built_distributions = list(PATH_DIST_ROOT.glob("niwrap-*"))
    if not built_distributions:
        raise ValueError("No distributions were built")

    # Validate each built distribution
    total_files = 0
    for dist_name, _, _ in selected_distributions:
        dist_path = PATH_DIST_ROOT / f"niwrap-{dist_name}"
        if not dist_path.exists():
            raise ValueError(f"Distribution '{dist_name}' not found at {dist_path}")
        
        # Count files in this distribution
        files = list(dist_path.glob("**/*"))
        files = [f for f in files if f.is_file()]
        total_files += len(files)

    # Validate package structure (only if we have packages)
    for package_file, package_data in iter_packages():
        if not package_data.get("id"):
            raise ValueError(f"Package {package_file.name} missing 'id'")

        package_descriptors = list(
            (PATH_DESCRIPTORS / package_data["id"]).glob("**/*.json")
        )
        if not package_descriptors:
            raise ValueError(f"No descriptors for package {package_data['id']}")

    print(f"✅ {total_files} files from {stats.descriptors} descriptors")


def parse_args() -> list[str]:
    """Parse command line arguments for distribution selection."""
    if len(sys.argv) == 1:
        return []  # No arguments, build all distributions
    
    # Handle help
    if "--help" in sys.argv or "-h" in sys.argv:
        available = [dist[0] for dist in DISTRIBUTIONS]
        print(f"Usage: {sys.argv[0]} [distribution1] [distribution2] ...")
        print(f"Available distributions: {', '.join(available)}")
        print("If no distributions specified, all will be built.")
        sys.exit(0)
    
    return sys.argv[1:]


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

    # Parse command line arguments
    try:
        requested_dists = parse_args()
        selected_distributions = filter_distributions(requested_dists)
        
        if requested_dists:
            dist_names = [dist[0] for dist in selected_distributions]
            print(f"Building selected distributions: {', '.join(dist_names)}")
        else:
            print("Building all distributions")
            
    except ValueError as e:
        print(f"❌ Error: {e}")
        return 1

    stats = BuildStats()
    stats.start()

    try:
        compile_all_distributions(stats, selected_distributions)
        validate_build(stats, selected_distributions)

        print(f"\n✅ Build completed successfully in {stats.elapsed():.1f}s")
        return 0

    except Exception as e:
        print(f"\n❌ Build failed: {e}")
        import traceback

        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())