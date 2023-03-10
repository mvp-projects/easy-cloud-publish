"""Docker service client."""

import pathlib

from easy_cloud_publish.core.services.docker.clients.image import ImageClient


class DockerClient:
    """Docker service root client."""

    def __init__(  # noqa: D107
        self,
        workdir: pathlib.Path,
    ) -> None:
        self.workdir = workdir

    @property
    def image(self) -> ImageClient:
        """Image client."""
        return ImageClient(
            workdir=self.workdir,
        )
