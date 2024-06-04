from typing import List

from pygame import Surface

from src.entities import Hero
from src.enums import Level, World

from ..abstractions import Manager
from ..interfaces import ILevelManager


class LevelManager(ILevelManager):
    def __init__(
        self,
        hero: Hero,
        managers: List[Manager],
        world: World,
        level: Level,
        background: Surface,
        time: int,
    ) -> None:
        self.__hero = hero
        self.__managers = managers
        self.__world = world
        self.__level = level
        self.__background = background
        self.__start_time = time
        self.__current_time = time
        self.__start_tick: int

    def get_hero(self) -> Hero:
        return self.__hero

    def get_managers(self) -> List[Manager]:
        return self.__managers

    def get_world(self) -> World:
        return self.__world

    def get_level(self) -> Level:
        return self.__level

    def get_background(self) -> Surface:
        return self.__background

    def get_start_time(self) -> int:
        return self.__start_time

    def get_current_time(self) -> int:
        return self.__current_time

    def set_current_time(self, time: int) -> None:
        self.__current_time = time

    def get_start_tick(self) -> int:
        return self.__start_tick

    def set_start_tick(self, tick: int) -> None:
        self.__start_tick = tick
