"""Base class for image deployers."""

import abc


class BaseImageDeployer(abc.ABC):  # noqa: D101
    @abc.abstractmethod
    def __init__(
        self,
        *,
        image_tag: str,
    ) -> None:
        """Image deployer base class."""
        self.image_tag = image_tag

    @abc.abstractmethod
    def deploy(self) -> None:
        """Deploy image to the cloud."""
