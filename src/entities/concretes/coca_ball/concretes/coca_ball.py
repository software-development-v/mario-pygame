from typing import List, Sequence

from pygame import Surface

from src.enums import CocaBallStates, Direction
from src.utils import Position, coca_ball

from ....abstractions import Sprite
from ....interfaces import ISprite
from ..handlers import (
    CollisionHandler,
    ICollisionHandler,
    IMovementHandler,
    MovementHandler,
)
from ..interfaces import ICocaBall


class CocaBall(Sprite, ICocaBall):
    def __init__(self, position: Position, direction: Direction):
        self.__state = CocaBallStates.MOVING
        self.__surfaces = coca_ball
        self.__direction = direction
        self.__movement_handler: IMovementHandler = MovementHandler(self)
        self.__collision_handler: ICollisionHandler = CollisionHandler(self)
        self.vel_y = 0.5
        self.speed = 5.0
        super().__init__(position)

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces[self.__state]

    def get_speed(self):
        return self.speed

    def get_vel_y(self):
        return self.vel_y

    def set_vel_y(self, vel_y: float):
        self.vel_y = vel_y

    def add_vel_y(self, vel_y: float):
        self.vel_y += vel_y

    def update(
        self, obstacles: Sequence[ISprite], enemies: Sequence[ISprite]
    ) -> None:
        dx, dy = self.__movement_handler.move(self.__direction)
        dx, dy = self.__collision_handler.handle_collision(
            obstacles, enemies, dx, dy
        )

        self.add_x_rect(dx)
        self.add_y_rect(dy)

        self.__collision_handler.check_dispose()
