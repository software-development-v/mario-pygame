from typing import Dict, List, Optional, Tuple

from pygame import Surface

from src.enums import AnimationType, CollectedType
from src.utils import Position

from ..interfaces import IElementObserver, IObservableElement, ISprite
from .element import Element


class InteractiveElement(Element, IObservableElement[int]):
    def __init__(
        self,
        position: Position,
        images: List[Surface],
        value: int = 0,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
        is_touchable: bool = True,
    ) -> None:
        self.__value = value
        self.__observers: Dict[CollectedType, IElementObserver[int]] = {}
        self.animation_oberservers: IElementObserver[
            Tuple["InteractiveElement", List[AnimationType]]
        ]
        super().__init__(
            position,
            images,
            x_rect_percent=x_rect_percent,
            y_rect_percent=y_rect_percent,
            is_touchable=is_touchable,
        )

    def add_observer(
        self, key: CollectedType, observer: IElementObserver[int]
    ) -> None:
        self.__observers[key] = observer

    def get_observer(self) -> Dict[CollectedType, IElementObserver[int]]:
        return self.__observers

    def add_animation_oberver(
        self,
        observer: IElementObserver[
            Tuple["InteractiveElement", List[AnimationType]]
        ],
    ) -> None:
        self.animation_oberservers = observer

    def remove_observer(self, key: CollectedType) -> None:
        if key in self.__observers:
            del self.__observers[key]

    def notify_observers(self, sprite: Optional[ISprite] = None) -> None:
        if CollectedType.COLLECTED_COIN in self.__observers:
            self.__observers[CollectedType.COLLECTED_COIN].notify(1)

        if self.__value > 0:
            self.__observers[CollectedType.COLLECTED_SCORE].notify(self.__value)

    def get_value(self) -> int:
        return self.__value
