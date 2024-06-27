from abc import ABC, abstractmethod
from typing import List

from pygame import Rect

from src.entities import Element


class ICollisionsHandler(ABC):

    @abstractmethod
    def handle_collisions(
        self, hero_rect: Rect, obstacles: List[Element], dx: float, dy: float
    ) -> tuple[float, float]:
        pass
