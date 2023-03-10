"""Image group cli application."""

import sys
from typing import Any

import click
from use_case_registry import UseCaseRegistry

from easy_cloud_publish.core.use_cases import BuildImageCommand
from easy_cloud_publish.logging import logger


@click.group()
def image() -> None:
    """Image CLI."""


@image.command()
@click.option(
    "-wdir",
    "workdir",
    help="Specify project cwd location when running build command",
)
@click.option(
    "-f",
    "dockerfile_path",
    help="Path from working directory to Dockfile. Including Dockerfile name",
)
def build(
    workdir: str,
    dockerfile_path: str,
) -> None:
    """Build image."""
    command = BuildImageCommand(
        path_to_dockerfile=dockerfile_path,
        wdir=workdir,
    )
    validated_or_err = command.validate()
    validate_err = validated_or_err.err()
    if validate_err is not None:
        logger.error(validate_err)
        sys.exit(1)

    success_or_err = command.execute(
        write_ops_registry=UseCaseRegistry[Any](max_length=0),
    )

    err = success_or_err.err()
    if err is not None:
        logger.error(err)
        sys.exit(1)
