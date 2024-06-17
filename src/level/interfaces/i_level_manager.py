from abc import ABC, abstractmethod

from pygame import Surface

from src.entities import Hero
from src.enums import Level, World

from ..concretes.entity_managers import ObstacleManager


class ILevelManager(ABC):
    @abstractmethod
    def get_hero(self) -> Hero:
        pass

    @abstractmethod
    def get_obstacle_manager(self) -> ObstacleManager:
        pass

    @abstractmethod
    def get_world(self) -> World:
        pass

    @abstractmethod
    def get_level(self) -> Level:
        pass

    @abstractmethod
    def get_background(self) -> Surface:
        pass

    @abstractmethod
    def get_start_time(self) -> int:
        pass

    @abstractmethod
    def get_current_time(self) -> int:
        pass

    @abstractmethod
    def set_current_time(self, time: int) -> None:
        pass

    @abstractmethod
    def get_start_tick(self) -> int:
        pass

    @abstractmethod
    def set_start_tick(self, tick: int) -> None:
        pass

    @abstractmethod
    def get_score(self) -> int:
        pass

    @abstractmethod
    def get_screen_width(self) -> int:
        pass
