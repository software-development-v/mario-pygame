from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class IElementObserver(Generic[T],ABC):

    @abstractmethod
    def notify(self, value: T):
        pass
