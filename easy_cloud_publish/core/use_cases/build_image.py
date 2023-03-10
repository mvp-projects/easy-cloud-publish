"""Build image."""
import pathlib
import subprocess
from typing import Any

from result import Err, Ok, Result
from use_case_registry import UseCaseRegistry
from use_case_registry.base import ICommand
from use_case_registry.errors import CommandInputValidationError


class BuildImageCommand(ICommand):
    """Command to build_image."""

    def __init__(  # noqa: D107
        self,
        dockerfile_path: str,
        wdir: str,
    ) -> None:
        self.dockerfile_path = pathlib.Path(dockerfile_path)
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

        if not (self.wdir / self.dockerfile_path).exists():
            return Err(
                CommandInputValidationError(
                    f"{self.dockerfile_path} does not exits.",
                ),
            )

        return Ok()

    def execute(  # noqa: D102
        self,
        write_ops_registry: UseCaseRegistry[Any],
    ) -> Result[Any, Exception]:
        _ = write_ops_registry

        subprocess.run(
            args=[
                "docker",
                "build",
                "-t",
                "simple-cli:latest",
                "-f",
                f"{self.dockerfile_path}",
                ".",
            ],
            cwd=self.wdir,
        )
        return Ok()
