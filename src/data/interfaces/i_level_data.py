from abc import ABC, abstractmethod
from typing import List

from pygame import Surface

from src.entities import Element, Sprite
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
    def get_screen_width(self) -> int:
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
    def get_enemies(self) -> List[Sprite]:
        pass

    @abstractmethod
    def get_elements(self) -> List[Element]:
        pass

    @abstractmethod
    def get_power_ups(self) -> List[Sprite]:
        pass
