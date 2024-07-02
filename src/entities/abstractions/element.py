from abc import ABC
from typing import List

from pygame import Surface

from src.utils import Position

from .sprite import Sprite


class Element(Sprite, ABC):
    def __init__(
        self,
        position: Position,
        images: List[Surface],
        is_touchable: bool = True,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        self.__surfaces: List[Surface] = images
        self.__is_touchable = is_touchable
        super().__init__(
            position,
            x_rect_percent=x_rect_percent,
            y_rect_percent=y_rect_percent,
        )

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces

    def get_is_touchable(self) -> bool:
        return self.__is_touchable

    def _set_is_touchable(self, is_touchable: bool) -> None:
        self.__is_touchable = is_touchable
