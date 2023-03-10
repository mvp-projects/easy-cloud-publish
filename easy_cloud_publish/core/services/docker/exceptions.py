"""Custom exceptions."""
import pathlib


class DockerError(Exception):
    """Base class for Docker service errors."""


class DockerfileNotFoundError(DockerError):
    """Raised when Dockerfile does not exists."""

    def __init__(  # noqa: D107
        self,
        path_to_dockerfile: pathlib.Path,
    ) -> None:
        super().__init__(
            f"{path_to_dockerfile} not found.",
        )
