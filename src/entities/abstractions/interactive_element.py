from typing import Dict, List

from pygame import Surface

from src.enums import CollectedType
from src.utils import Position

from ..interfaces import IElementObserver, IObservableElement
from .element import Element


class InteractiveElement(Element, IObservableElement):

    def __init__(
        self, position: Position, images: List[Surface], value: int = 0
    ) -> None:
        super().__init__(position, images)
        self.value = value
        self.observers: Dict[CollectedType, IElementObserver] = {}

    def add_observer(
        self, key: CollectedType, observer: IElementObserver
    ) -> None:
        self.observers[key] = observer

    def remove_observer(self, key: CollectedType) -> None:
        if key in self.observers:
            del self.observers[key]

    def notify_observers(self) -> None:
        if CollectedType.COLLECTED_SCORE in self.observers:
            self.observers[CollectedType.COLLECTED_SCORE].update(self.value)
