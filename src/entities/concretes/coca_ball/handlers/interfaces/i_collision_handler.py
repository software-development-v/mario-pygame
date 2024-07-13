from abc import ABC, abstractmethod
from typing import Sequence, Tuple

from .....interfaces import ISprite


class ICollisionHandler(ABC):
    @abstractmethod
    def handle_collision(
        self,
        obstacles: Sequence[ISprite],
        enemies: Sequence[ISprite],
        dx: float,
        dy: float,
    ) -> Tuple[float, float]:
        pass

    @abstractmethod
    def check_dispose(self) -> None:
        pass
