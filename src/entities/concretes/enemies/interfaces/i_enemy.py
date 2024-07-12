from abc import ABC, abstractmethod
from typing import List

from pygame import Rect

from src.enums import EnemyState
from src.utils import Camera

from ....abstractions import Element, Sprite


class IEnemy(Sprite, ABC):

    @abstractmethod
    def get_state(self) -> EnemyState:
        pass

    @abstractmethod
    def set_state(self, state: EnemyState):
        pass

    @abstractmethod
    def get_speed(self) -> int:
        pass

    @abstractmethod
    def get_vel_y(self) -> float:
        pass

    @abstractmethod
    def get_is_touchable(self) -> bool:
        return self.__is_touchable

    @abstractmethod
    def _set_is_touchable(self, is_touchable: bool) -> None:
        self.__is_touchable = is_touchable

    @abstractmethod
    def set_vel_y(self, vel_y: float) -> None:
        pass

    @abstractmethod
    def add_vel_y(self, vel_y: float) -> None:
        pass

    @abstractmethod
    def update(
        self,
        obstacles: List[Element],
        enemies: List["IEnemy"],
        camera: Camera,
    ) -> None:
        pass

    @abstractmethod
    def get_hero_collision(self, hero_rect: Rect) -> bool:
        pass
