from abc import ABC
from typing import List

from pygame import Surface

from src.utils import Position

from ....abstractions import Sprite
from ..interfaces import IPowerUp


class PowerUp(Sprite, IPowerUp, ABC):
    def __init__(self, position: Position, surfaces: List[Surface]):
        self.__surfaces = surfaces
        super().__init__(position)

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces
