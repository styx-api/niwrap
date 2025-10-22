import html


def progress_bar(done: int, total: int) -> str:
    return f"![{done}/{total}](https://progress-bar.xyz/{done}/?scale={total}&suffix=%2F{total})"


def dict_to_markdown_table(data: dict[str, list[str]]) -> str:
    """
    Convert a dictionary with string keys and list[str] values to a markdown table.

    Args:
        data: Dictionary where keys become column headers and values are column data

    Returns:
        A string containing a formatted markdown table
    """
    if not data:
        return ""

    # Get column headers and ensure all lists have the same length
    headers = list(data.keys())
    max_rows = max(len(v) for v in data.values()) if data else 0

    # Pad shorter columns with empty strings
    padded_data = {}
    for key, values in data.items():
        padded_data[key] = values + [""] * (max_rows - len(values))

    # Build table
    lines = []

    # Header row
    lines.append("| " + " | ".join(headers) + " |")

    # Separator row
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    # Data rows
    for i in range(max_rows):
        row = "| " + " | ".join(padded_data[h][i] for h in headers) + " |"
        lines.append(row)

    return "\n".join(lines)


def markdown_url(url: str, title: str | None = None) -> str:
    if title:
        return f"[{html.escape(title)}]({url})"
    return f"[{url}]({url})"


def patch_section(file, replacement, token):
    # Replace text in file between <!-- START_{token} --> and <!-- END_{token} -->
    TOKEN_START = f"<!-- START_{token} -->"
    TOKEN_END = f"<!-- END_{token} -->"

    with open(file, "r", encoding="utf-8") as f:
        readme = f.read()
        start = readme.find(TOKEN_START) + len(TOKEN_START)
        end = readme.find(TOKEN_END)
        assert start >= 0
        assert end >= 0
        assert start < end
        new_readme = readme[:start] + "\n\n" + replacement + "\n" + readme[end:]

    with open(file, "w", encoding="utf-8") as f:
        f.write(new_readme)
