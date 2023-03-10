"""Image Docker Client."""
import pathlib
import subprocess

from result import Err, Ok, Result

from easy_cloud_publish.core.services.docker.clients.base import BaseClient
from easy_cloud_publish.core.services.docker.exceptions import (
    DockerError,
    DockerfileNotFoundError,
)


class ImageClient(BaseClient):
    """Image group client."""

    def __init__(  # noqa: D107
        self,
        *,
        workdir: pathlib.Path,
    ) -> None:
        super().__init__(
            workdir=workdir,
        )

    def build(
        self,
        path_to_dockerfile: pathlib.Path,
        tag: str,
    ) -> Result[None, DockerError]:
        """Build image from Dockerfile."""
        if not (self.workdir / path_to_dockerfile).exists():
            return Err(DockerfileNotFoundError(path_to_dockerfile=path_to_dockerfile))

        subprocess.run(
            cwd=self.workdir,
            args=[
                "docker",
                "build",
                "-t",
                f"{tag}",
                "-f",
                f"{path_to_dockerfile}",
                ".",
            ],
        )

        return Ok()

    def remove(self, tag: str) -> Result[None, DockerError]:
        """Remove image."""
        subprocess.run(
            cwd=self.workdir,
            args=[
                "docker",
                "rmi",
                f"{tag}",
            ],
        )

        return Ok()

    def check_exists(self, tag: str) -> bool:
        """Check if image exists."""
        response = subprocess.run(
            cwd=self.workdir,
            args=[
                "docker",
                "image",
                "inspect",
                f"{tag}",
            ],
            capture_output=True,
            text=True,
        )
        if not response.stderr:
            return True
        return False
