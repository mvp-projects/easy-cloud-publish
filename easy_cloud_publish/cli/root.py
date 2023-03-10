"""Root cli application."""
import click

from easy_cloud_publish.cli.image.cli import image


@click.group()
def cli() -> None:
    """Root cli."""


cli.add_command(
    cmd=image,
    name="image",
)
