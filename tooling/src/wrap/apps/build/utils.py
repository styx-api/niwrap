def print_box(title: str, items: list[str]) -> None:
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
