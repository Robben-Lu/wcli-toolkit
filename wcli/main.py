"""Main entry point for wcli CLI application."""

import typer
from rich.console import Console

from wcli import __version__

app = typer.Typer(
    name="wcli",
    help="WeCom CLI Toolkit - A powerful tool for Enterprise WeChat operations",
    add_completion=True,
)
console = Console()


def version_callback(value: bool):
    """Show version and exit."""
    if value:
        console.print(f"wcli version: {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=version_callback,
        is_eager=True,
    ),
):
    """
    WeCom CLI Toolkit - Enterprise WeChat command line interface.
    
    Designed for both AI agents and human users to interact with WeCom APIs.
    """
    pass


if __name__ == "__main__":
    app()