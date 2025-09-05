from abc import ABCMeta, abstractmethod
from collections.abc import Callable
from typing import Any


class BaseService(metaclass=ABCMeta):
    """This is a template of a base service.
    All services in the app should follow this rules:
      * Input variables should be done at the __init__ phase
      * Service should implement a single entrypoint without arguments
    """

    def __call__(self) -> Any:
        self.validate()
        return self.act()

    def get_validators(self) -> list[Callable]:
        return []

    def validate(self) -> None:
        validators = self.get_validators()
        for validator in validators:
            validator()

    @abstractmethod
    def act(self) -> Any:
        raise NotImplementedError("Please implement in the service class")
