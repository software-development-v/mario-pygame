from abc import ABC
from typing import List
from pygame import Surface

from src.utils import Position, ANIMATION_INTERVAL
from .sprite import Sprite


class Animation(Sprite, ABC):
    DEFAULT_SPEED: float = 10
    DEFAULT_TRANSITION: List[Position] = [Position(0, 0)]

    def __init__(
        self,
        surfaces: List[Surface],
        repeat: bool = False,
        speed: int = DEFAULT_SPEED,
        transitions: List[Position] = DEFAULT_TRANSITION,
        animation_interval: int = ANIMATION_INTERVAL,
    ):
        self.__surfaces: List[Surface] = surfaces
        super().__init__(transitions[0], animation_interval=animation_interval)

        self.__repeat: bool = repeat
        self.__transitions: List[Position] = transitions

        self.__total_transitions: int = len(transitions)
        self.__current_index: int = 0
        self.__current_transition: Position = transitions[0]
        self.__from: Position = transitions[0]
        self.__to: Position = self.__from
        if self.__total_transitions > 1:
            self.__to = transitions[1]

        self.__speed: float = speed
        self.__calculate_speed_axes()


    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces

    def __calculate_speed_axes(self) -> None:
        difference_y = abs(self.__to.y - self.__from.y)
        difference_x = abs(self.__to.x - self.__from.x)

        self.__speed_y = self.__speed
        self.__speed_x = 0

        if difference_x>0:
            self.__speed_x = difference_x/(difference_y/difference_y)

    def animate(self) -> None:
        super().animate()
        if self.__total_transitions <= 1:
            return

        self.translate(self.accelerate_x(), self.accelerate_y())

    def translate(self, x: float = 0, y: float = 0) -> None:
        self.add_y_rect(y)
        self.add_x_rect(x)
        rect = self.get_rect()
        self.__current_transition = Position(rect.centerx, rect.centery)
        self.check_change_transition()

    def accelerate_y(self) -> float:
        return self.__speed_y * (1 if self.__from.y < self.__to.y else -1)

    def accelerate_x(self) -> float:
        return self.__speed_x * (1 if self.__from.x < self.__to.x else -1)

    def check_change_transition(self) -> None:
        if self.__has_reached_transition(
            self.__from.y, self.__to.y, self.__current_transition.y
        ):
            self.__change_to_next_state()
        if self.__has_reached_transition(
            self.__from.x, self.__to.x, self.__current_transition.x
        ):
            self.__change_to_next_state()

    def __has_reached_transition(
        self, from_value: int, to_value: int, current_value: int
    ) -> bool:
        return (
            current_value > to_value
            if from_value < to_value
            else current_value < to_value
        )

    def __change_to_next_state(self) -> None:
        if self.__current_index < self.__total_transitions - 1:
            self.__current_index += 1
            self.__from = self.__to
            self.__to = self.__transitions[self.__current_index]
        else:
            if self.__repeat:
                self.__current_index = 0
                self.__from = self.__transitions[self.__current_index]
                self.__to = self.__transitions[self.__current_index + 1]
                self.__calculate_speed_axes()
            else:
                self.dispose()

        self.__current_transition = self.__from
