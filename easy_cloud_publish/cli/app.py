"""CLI application entrypoint."""


import sys
from typing import Any

import click
from use_case_registry import UseCaseRegistry

from easy_cloud_publish.core.use_cases import BuildImageCommand
from easy_cloud_publish.logging import logger


@click.group()
def root_cli() -> None:
    """CLI Root."""


@root_cli.command()
@click.option(
    "-wdir",
    "workdir",
    help="Specify project wdir location when running build command",
)
@click.option(
    "-f",
    "dockerfile_path",
    help="Path from working directory to Dockfile. Including Dockerfile name",
)
def build_image(
    workdir: str,
    dockerfile_path: str,
) -> None:
    """Build image."""
    command = BuildImageCommand(
        dockerfile_path=dockerfile_path,
        wdir=workdir,
    )
    validated_or_err = command.validate()
    validate_err = validated_or_err.err()
    if validate_err is not None:
        logger.error(validate_err)
        sys.exit(1)

    command.execute(
        write_ops_registry=UseCaseRegistry[Any](max_length=10),
    )
