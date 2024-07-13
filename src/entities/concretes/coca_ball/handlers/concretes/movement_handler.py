from typing import Tuple

from src.enums import Direction

from ...interfaces import ICocaBall
from ..interfaces import IMovementHandler


class MovementHandler(IMovementHandler):
    def __init__(self, ball: ICocaBall):
        self.__ball = ball
        self.__y_sign = 1

    def move(self, direction: Direction) -> Tuple[float, float]:
        dy = self.__ball.get_vel_y()
        self.__ball.add_vel_y((0.5 * self.__y_sign))

        if abs(dy) > 5:
            self.__ball.set_vel_y((5 * self.__y_sign))

        if self.__ball.get_rect().y <= 450:
            if self.__y_sign == -1:
                self.__y_sign = 1
                self.__ball.set_vel_y((0.5 * self.__y_sign))
        if self.__ball.get_rect().y >= 750:
            if self.__y_sign == 1:
                self.__y_sign = -1
                self.__ball.set_vel_y((0.5 * self.__y_sign))

        dx = self.__ball.get_speed()
        dx = dx if direction == Direction.RIGHT else -dx

        return dx, dy
