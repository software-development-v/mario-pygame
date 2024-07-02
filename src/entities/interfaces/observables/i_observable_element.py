from abc import ABC, abstractmethod

from src.enums import CollectedType

from .i_element_observer import IElementObserver
from typing import Generic, TypeVar

T = TypeVar('T')


class IObservableElement(ABC, Generic[T]):

    @abstractmethod
    def add_observer(self, key: CollectedType, observer: IElementObserver[T]):
        pass

    @abstractmethod
    def remove_observer(self, key: CollectedType):
        pass
