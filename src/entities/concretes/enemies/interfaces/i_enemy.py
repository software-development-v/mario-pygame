from abc import ABC, abstractmethod
from typing import List

from src.enums import EnemyState
from src.utils import Camera

from ....abstractions import Element, Sprite
from ...hero import IHero


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
        pass

    @abstractmethod
    def set_is_touchable(self, is_touchable: bool) -> None:
        pass

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
    def get_hero_collision(self, hero: IHero) -> bool:
        pass
