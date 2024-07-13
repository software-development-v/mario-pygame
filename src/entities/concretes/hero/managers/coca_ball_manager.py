from typing import List, Optional, Sequence

from pygame import Surface

from src.enums import Direction
from src.utils import Camera, Position

from ....interfaces import ISprite
from ...coca_ball import CocaBall, ICocaBall


class CocaBallManager:
    def __init__(self) -> None:
        self.__balls: List[ICocaBall] = []

    def draw(self, screen: Surface, camera: Optional[Camera]) -> None:
        for ball in self.__balls:
            if ball.is_disposed():
                self.__balls.remove(ball)

        for ball in self.__balls:
            ball.draw(screen, camera)

    def update(self, obstacles: Sequence[ISprite], enemies: Sequence[ISprite]):
        for ball in self.__balls:
            ball.update(obstacles, enemies)

            if ball.is_disposed():
                self.__balls.remove(ball)

    def animate(self) -> None:
        for ball in self.__balls:
            ball.animate()

    def create_ball(self, hero: ISprite) -> None:
        x = hero.get_rect().x
        y = hero.get_rect().y
        direction = Direction.RIGHT if hero.get_face_right() else Direction.LEFT

        self.__balls.append(CocaBall(Position(x, y), direction))

    def reset_balls(self) -> None:
        self.__balls = []
