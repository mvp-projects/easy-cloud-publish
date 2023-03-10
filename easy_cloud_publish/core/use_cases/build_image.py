"""Build image."""
import pathlib
from typing import Any

from result import Err, Ok, Result
from use_case_registry import UseCaseRegistry
from use_case_registry.base import ICommand
from use_case_registry.errors import CommandInputValidationError

from easy_cloud_publish.core.services.docker import DockerClient


class BuildImageCommand(ICommand):
    """Command to build_image."""

    def __init__(  # noqa: D107
        self,
        path_to_dockerfile: str,
        wdir: str,
    ) -> None:
        self.path_to_dockerfile = pathlib.Path(path_to_dockerfile)
        self.wdir = pathlib.Path(wdir)

    def validate(  # noqa: D102
        self,
    ) -> Result[None, CommandInputValidationError]:
        if not self.wdir.is_dir():
            return Err(
                CommandInputValidationError(
                    f"{self.wdir} is not a directory.",
                ),
            )

        return Ok()

    def execute(  # noqa: D102
        self,
        write_ops_registry: UseCaseRegistry[Any],
    ) -> Result[Any, Exception]:
        _ = write_ops_registry
        docker = DockerClient(workdir=self.wdir)
        image_tag = "simple-cli:latest"

        image_built_or_err = docker.image.build(
            path_to_dockerfile=self.path_to_dockerfile,
            tag=image_tag,
        )
        image_built_err = image_built_or_err.err()
        if image_built_err is not None:
            return Err(image_built_err)

        image_removed_or_err = docker.image.remove(tag=image_tag)
        image_removed_err = image_removed_or_err.err()
        if image_removed_err is not None:
            return Err(image_removed_err)

        return Ok()
