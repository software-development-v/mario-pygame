from typing import List

from pygame import Surface

from src.entities import Element, Sprite
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
        map_width: int,
        background: IBackground,
        background_music: str,
        player_init_position: Position,
        enemies: List[Sprite],
        elements: List[Element],
        power_ups: List[Sprite],
    ) -> None:

        self.__world: World = world
        self.__level: Level = level
        self.__time: int = time
        self.__map_width: int = map_width
        self.__background: IBackground = background
        self.__background_music: str = background_music
        self.__player_init_position: Position = player_init_position
        self.__enemies: List[Sprite] = enemies
        self.__elements: List[Element] = elements
        self.__power_ups: List[Sprite] = power_ups

    def get_world(self) -> World:
        return self.__world

    def get_level(self) -> Level:
        return self.__level

    def get_screen_width(self) -> int:
        return self.__map_width

    def get_time(self) -> int:
        return self.__time

    def get_background(self) -> Surface:
        return self.__background.get_background()

    def get_brackground_music(self) -> str:
        return self.__background_music

    def get_player_init_position(self) -> Position:
        return self.__player_init_position

    def get_enemies(self) -> List[Sprite]:
        return self.__enemies

    def get_elements(self) -> List[Element]:
        return self.__elements

    def get_power_ups(self) -> List[Sprite]:
        return self.__power_ups
