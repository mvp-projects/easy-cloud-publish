"""Test docker service client."""

import pathlib

import pytest

from easy_cloud_publish.core.services.docker.client import DockerClient
from easy_cloud_publish.core.services.docker.exceptions import DockerfileNotFoundError


@pytest.mark.integration()
class TestDockerClient:
    """Test defined for the docker service."""

    def test_image_build_and_remove(self) -> None:
        """Test build and remove image."""
        client = DockerClient(
            workdir=pathlib.Path().cwd()
            / pathlib.Path("tests/integrations/sample_cli_project"),
        )
        test_image_tag = "test-build:latest"
        client.image.build(
            path_to_dockerfile=pathlib.Path("docker/Dockerfile"),
            tag=test_image_tag,
        )
        exists = client.image.check_exists(tag=test_image_tag)
        assert exists
        client.image.remove(
            tag=test_image_tag,
        )
        exists = client.image.check_exists(tag=test_image_tag)
        assert not exists

    def test_dockerfile_not_found(self) -> None:
        """Assert error when dockerfile not found."""
        client = DockerClient(
            workdir=pathlib.Path().cwd()
            / pathlib.Path("tests/integrations/sample_cli_project"),
        )
        err = client.image.build(
            path_to_dockerfile=pathlib.Path("not/existing/path"),
            tag="abc",
        ).err()

        assert isinstance(err, DockerfileNotFoundError)
