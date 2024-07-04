from abc import ABC, abstractmethod
from typing import Dict, List

from pygame import Surface

from src.enums import EnemyState
from src.utils import Position

from .sprite import Sprite


class Enemy(Sprite, ABC):
    def __init__(
        self,
        surfaces: Dict[EnemyState, List[Surface]],
        position: Position,
        initial_state: EnemyState,
    ):
        self.__surfaces = surfaces
        self.__state = initial_state

        super().__init__(position)

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces[self.__state]

    @abstractmethod
    def update_state(self) -> None:
        pass
