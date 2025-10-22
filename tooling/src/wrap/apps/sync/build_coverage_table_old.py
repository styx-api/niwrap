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
