from typing import Dict, List, Tuple

from pygame import Surface

from src.enums import CollectedType, AnimationType
from src.utils import Position

from ..interfaces import IElementObserver, IObservableElement
from .element import Element


class InteractiveElement(Element, IObservableElement[int]):
    def __init__(
        self,
        position: Position,
        images: List[Surface],
        value: int = 0,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        self.__value = value
        self.observers: Dict[CollectedType, IElementObserver[int]] = {}
        self.animation_oberservers: IElementObserver[
            Tuple["InteractiveElement", List[AnimationType]]
        ]
        super().__init__(
            position,
            images,
            x_rect_percent=x_rect_percent,
            y_rect_percent=y_rect_percent,
        )

    def add_observer(
        self, key: CollectedType, observer: IElementObserver[int]
    ) -> None:
        self.observers[key] = observer

    def add_animation_oberver(
        self, observer: IElementObserver[Tuple["InteractiveElement", List[AnimationType]]]
    ) -> None:
        self.animation_oberservers = observer

    def remove_observer(self, key: CollectedType) -> None:
        if key in self.observers:
            del self.observers[key]

    def notify_observers(self) -> None:
        if CollectedType.COLLECTED_COIN in self.observers:
            self.observers[CollectedType.COLLECTED_COIN].notify(1)

        if self.__value > 0:
            self.observers[CollectedType.COLLECTED_SCORE].notify(self.__value)

    def get_value(self) -> int:
        return self.__value
