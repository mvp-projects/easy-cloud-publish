"""Base Docker Client."""
import abc
import pathlib


class BaseClient(abc.ABC):
    """Base client for each group client."""

    @abc.abstractmethod
    def __init__(  # noqa: D107
        self,
        *,
        workdir: pathlib.Path,
    ) -> None:
        self.workdir = workdir
