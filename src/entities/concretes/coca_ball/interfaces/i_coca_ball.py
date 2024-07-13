from abc import ABC, abstractmethod
from typing import Sequence

from ....interfaces import ISprite


class ICocaBall(ISprite, ABC):
    @abstractmethod
    def get_speed(self) -> float:
        pass

    @abstractmethod
    def get_vel_y(self) -> float:
        pass

    @abstractmethod
    def set_vel_y(self, vel_y: float) -> None:
        pass

    @abstractmethod
    def add_vel_y(self, vel_y: float) -> None:
        pass

    @abstractmethod
    def update(
        self, obstacles: Sequence[ISprite], enemies: Sequence[ISprite]
    ) -> None:
        pass
