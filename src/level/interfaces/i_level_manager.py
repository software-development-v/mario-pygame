from abc import ABC, abstractmethod

from pygame import Surface

from src.entities import Hero
from src.enums import HeroType, Level, World
from src.utils import Camera

from ..sprites import ObstaclesManager


class ILevelManager(ABC):
    @abstractmethod
    def get_hero(self) -> Hero:
        pass

    @abstractmethod
    def get_hero_type(self) -> HeroType:
        pass

    @abstractmethod
    def get_obstacles_manager(self) -> ObstaclesManager:
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

    @abstractmethod
    def get_camera(self) -> Camera:
        pass

    @abstractmethod
    def get_lives(self) -> int:
        pass

    @abstractmethod
    def set_lives(self, lives: int) -> None:
        pass

    @abstractmethod
    def get_coins(self) -> int:
        pass

    @abstractmethod
    def add_coins(self, value: int) -> None:
        pass

    @abstractmethod
    def is_win(self) -> bool:
        pass

    @abstractmethod
    def win(self) -> None:
        pass

    @abstractmethod
    def configure_level(
        self,
        hero: Hero,
        hero_type: HeroType,
        time: int,
        score: int,
        lives: int,
        coins: int,
    ) -> None:
        pass
