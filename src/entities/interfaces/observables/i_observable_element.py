from abc import ABC, abstractmethod

from src.enums import CollectedType

from .i_element_observer import IElementObserver


class IObservableElement(ABC):

    @abstractmethod
    def add_observer(self, key: CollectedType, observer: IElementObserver[int]):
        pass

    @abstractmethod
    def remove_observer(self, key: CollectedType):
        pass
