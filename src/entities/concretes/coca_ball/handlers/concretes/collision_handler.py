from typing import Optional, Sequence, Tuple

from .....interfaces import ISprite
from ...interfaces import ICocaBall
from ..interfaces import ICollisionHandler


class CollisionHandler(ICollisionHandler):
    def __init__(self, ball: ICocaBall):
        self.__dispose_time: Optional[int] = None
        self.__ball = ball

    def handle_collision(
        self,
        obstacles: Sequence[ISprite],
        enemies: Sequence[ISprite],
        dx: float,
        dy: float,
    ) -> Tuple[float, float]:
        return dx, dy

    def check_dispose(self) -> None:
        pass
