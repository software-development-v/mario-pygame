from typing import List

from pygame import Surface

from src.entities import IEntity
from src.enums import Level, World
from src.utils import Position

from .background import IBackground
from .interfaces import ILevelData


class LevelData(ILevelData):
    def __init__(
        self,
        world: World,
        level: Level,
        time: int,
        background: IBackground,
        background_music: str,
        player_init_position: Position,
        enemies: List[IEntity],
        elements: List[IEntity],
        power_ups: List[IEntity],
    ) -> None:

        self.__world: World = world
        self.__level: Level = level
        self.__time: int = time
        self.__background: IBackground = background
        self.__background_music: str = background_music
        self.__player_init_position: Position = player_init_position
        self.__enemies: List[IEntity] = enemies
        self.__elements: List[IEntity] = elements
        self.__power_ups: List[IEntity] = power_ups

    def get_world(self) -> World:
        return self.__world

    def get_level(self) -> Level:
        return self.__level

    def get_time(self) -> int:
        return self.__time

    def get_background(self) -> Surface:
        return self.__background.get_background()

    def get_brackground_music(self) -> str:
        return self.__background_music

    def get_player_init_position(self) -> Position:
        return self.__player_init_position

    def get_enemies(self) -> List[IEntity]:
        return self.__enemies

    def get_elements(self) -> List[IEntity]:
        return self.__elements

    def get_power_ups(self) -> List[IEntity]:
        return self.__power_ups
