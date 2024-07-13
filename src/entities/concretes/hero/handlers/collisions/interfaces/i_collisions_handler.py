from abc import ABC, abstractmethod
from typing import Sequence

from pygame import Rect

from src.entities import Element


class ICollisionsHandler(ABC):

    @abstractmethod
    def handle_collisions(
        self,
        hero_rect: Rect,
        obstacles: Sequence[Element],
        dx: float,
        dy: float,
    ) -> tuple[float, float]:
        pass
