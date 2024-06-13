from pygame import Surface

from src.entities import Hero
from src.enums import Level, World

from ..interfaces import ILevelManager
from .entity_managers import ObstacleManager


class LevelManager(ILevelManager):
    def __init__(
        self,
        hero: Hero,
        obstacle_manager: ObstacleManager,
        world: World,
        level: Level,
        background: Surface,
        time: int,
    ) -> None:
        self.__hero = hero
        self.__obstacle_manager = obstacle_manager
        self.__world = world
        self.__level = level
        self.__background = background
        self.__start_time = time
        self.__current_time = time
        self.__start_tick: int

    def get_hero(self) -> Hero:
        return self.__hero

    def get_obstacle_manager(self) -> ObstacleManager:
        return self.__obstacle_manager

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
