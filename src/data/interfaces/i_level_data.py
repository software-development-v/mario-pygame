from abc import ABC, abstractmethod
from typing import List

from pygame import Surface

from src.entities import IEntity
from src.enums import Level, World
from src.utils import Position


class ILevelData(ABC):
    @abstractmethod
    def get_world(self) -> World:
        pass

    @abstractmethod
    def get_level(self) -> Level:
        pass

    @abstractmethod
    def get_time(self) -> int:
        pass

    @abstractmethod
    def get_background(self) -> Surface:
        pass

    @abstractmethod
    def get_brackground_music(self) -> str:
        pass

    @abstractmethod
    def get_player_init_position(self) -> Position:
        pass

    @abstractmethod
    def get_enemies(self) -> List[IEntity]:
        pass

    @abstractmethod
    def get_elements(self) -> List[IEntity]:
        pass

    @abstractmethod
    def get_power_ups(self) -> List[IEntity]:
        pass
