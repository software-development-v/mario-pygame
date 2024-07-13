from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .i_element_observer import IElementObserver

T = TypeVar("T")


class IObservableElement(ABC, Generic[T]):

    @abstractmethod
    def set_observer(self, observer: IElementObserver[T]) -> None:
        pass

    @abstractmethod
    def remove_observer(self):
        pass

    @abstractmethod
    def notify_observer(self, event: T):
        pass
