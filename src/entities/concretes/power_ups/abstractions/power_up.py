from abc import ABC, abstractmethod
from typing import List

from pygame import Surface

from src.utils import Position

from ....abstractions import Sprite
from ...hero import IHero
from ..interfaces import IPowerUp


class PowerUp(Sprite, IPowerUp, ABC):
    def __init__(self, position: Position, surfaces: List[Surface]):
        self.__surfaces = surfaces
        super().__init__(position)

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces

    def update(self, hero: IHero) -> None:
        if not self.is_visible():
            return

        if self.get_rect().colliderect(hero.get_rect()):
            self._handle_collision(hero)
            self.disappear()

    @abstractmethod
    def _handle_collision(self, hero: IHero) -> None:
        pass

    def reset(self) -> None:
        self.appear()
