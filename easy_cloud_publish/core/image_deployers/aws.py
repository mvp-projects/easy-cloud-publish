"""AWS Image Deployer."""
from easy_cloud_publish.core.image_deployers.base import BaseImageDeployer


class AWSImageDeployer(BaseImageDeployer):  # noqa: D101
    def __init__(self, *, image_tag: str) -> None:
        """Image deployer AWS class."""
        super().__init__(
            image_tag=image_tag,
        )
