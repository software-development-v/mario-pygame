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
    ) -> None:
        self.__surfaces: List[Surface] = images
        self.__is_touchable = is_touchable
        super().__init__(position)

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces

    def get_is_touchable(self) -> bool:
        return self.__is_touchable
