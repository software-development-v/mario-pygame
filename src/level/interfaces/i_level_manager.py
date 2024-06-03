from abc import ABC, abstractmethod
from typing import List

from pygame import Surface

from src.entities import Hero
from src.enums import Level, World

from ..abstractions import Manager


class ILevelManager(ABC):
    @abstractmethod
    def get_hero(self) -> Hero:
        pass

    @abstractmethod
    def get_managers(self) -> List[Manager]:
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
