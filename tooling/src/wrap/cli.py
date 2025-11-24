import argparse
import sys
from typing import Optional, Sequence

# Import your app modules here
from wrap.apps import build, check_container, sync, test


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
    parser = argparse.ArgumentParser(
        prog="wrap",
        description="NiWrap developer and build tools.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Add global options
    # parser.add_argument(
    #     "-v", "--verbose", action="store_true", help="Enable verbose output"
    # )

    # Create subparsers
    subparsers = parser.add_subparsers(
        title="commands",
        description="Available commands",
        help="Command help",
        dest="command",
        required=True,
    )

    # Register each module's subcommand
    build.register_command(subparsers)
    sync.register_command(subparsers)
    test.register_command(subparsers)
    check_container.register_command(subparsers)

    return parser


def cli(argv: Optional[Sequence[str]] = None) -> str | int:
    """Main CLI entry point."""
    parser = create_parser()

    try:
        args = parser.parse_args(argv)
    except SystemExit as e:
        return e.code if e.code is not None else 1

    # Execute the appropriate subcommand
    if hasattr(args, "func"):
        return args.func(args)

    # Should not reach here if parser is configured correctly
    parser.print_help()
    return 1


def main() -> None:
    """Main entry point for console script."""
    sys.exit(cli())


if __name__ == "__main__":
    main()
