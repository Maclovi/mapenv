from typing import Any, Callable, Optional, TypeVar

from typing_extensions import Annotated, Doc

T = TypeVar("T")


class Improve:
    def __init__(
        self,
        envfile: Annotated[
            Optional[str],
            Doc(
                """
                **Note**: variables from a file do not export files
                to global visibility, but are stored in memory.

                ---

                Write the path to the file to expand the environment variables.
                """
            ),
        ] = None,
        override: Annotated[
            bool,
            Doc(
                """
                Set to true to load variables from file in priority order.
                """
            ),
        ] = False,
        frozen: Annotated[
            bool,
            Doc(
                """
                Set to true to disable writing and deleting variables.
                """
            ),
        ] = False,
    ) -> None:
        self.envfile = envfile
        self.override = override
        self.frozen = frozen

    def __call__(self, class_: Callable[..., T]) -> Callable[..., T]:
        def wrapper(*args: Any, **kwargs: Any) -> T:
            return class_(
                *args,
                envfile=self.envfile,
                override=self.override,
                frozen=self.frozen,
                **kwargs,
            )

        return wrapper