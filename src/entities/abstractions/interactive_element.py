from typing import Dict, List

from pygame import Surface

from src.enums import CollectedType
from src.utils import Position

from ..interfaces import IElementObserver, IObservableElement
from .element import Element


class InteractiveElement(Element, IObservableElement):
    def __init__(
        self,
        position: Position,
        images: List[Surface],
        value: int = 0,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        self.__value = value
        self.__observers: Dict[CollectedType, IElementObserver[int]] = {}
        super().__init__(
            position,
            images,
            x_rect_percent=x_rect_percent,
            y_rect_percent=y_rect_percent,
        )

    def add_observer(
        self, key: CollectedType, observer: IElementObserver[int]
    ) -> None:
        self.__observers[key] = observer

    def remove_observer(self, key: CollectedType) -> None:
        if key in self.__observers:
            del self.__observers[key]

    def notify_observers(self) -> None:
        if CollectedType.COLLECTED_COIN in self.__observers:
            self.__observers[CollectedType.COLLECTED_COIN].notify(1)

        if self.__value>0:
            self.__observers[CollectedType.COLLECTED_SCORE].notify(self.__value)
