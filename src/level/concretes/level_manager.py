from pygame import Surface

from src.entities import Hero, IElementObserver
from src.enums import HeroType, Level, World
from src.utils import Camera
from src.utils import PLAYER_LIVES

from ..interfaces import ILevelManager
from .sprites_managers import ObstaclesManager


class LevelManager(ILevelManager):
    def __init__(
        self,
        hero: Hero,
        hero_type: HeroType,
        obstacles_manager: ObstaclesManager,
        world: World,
        level: Level,
        background: Surface,
        time: int,
        level_screen_width: int,
        score_observer: IElementObserver,
        camera: Camera,
        lives: int = PLAYER_LIVES,
    ) -> None:
        self.__hero = hero
        self.__hero_type = hero_type
        self.__obstacles_manager = obstacles_manager
        self.__world = world
        self.__level = level
        self.__background = background
        self.__start_time = time
        self.__current_time = time
        self.__start_tick = 0
        self.__level_screen_width = level_screen_width
        self.__score_observer = score_observer
        self.__camera = camera
        self.__lives = lives

    def get_hero(self) -> Hero:
        return self.__hero

    def get_hero_type(self) -> HeroType:
        return self.__hero_type

    def get_obstacles_manager(self) -> ObstaclesManager:
        return self.__obstacles_manager

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

    def get_score(self) -> int:
        return self.__score_observer.get_value()

    def get_screen_width(self) -> int:
        return self.__level_screen_width

    def get_camera(self) -> Camera:
        return self.__camera

    def get_lives(self) -> int:
        return self.__lives

    def set_lives(self, lives: int) -> None:
        self.__lives = lives

    def get_coins(self) -> int:
        return 0

    def configure_level(
        self,
        hero: Hero,
        hero_type: HeroType,
        time: int,
        score: int,
        lives: int,
        coins: int,
    ) -> None:
        self.__hero.set_hero_level(hero.get_hero_level())
        self.__hero_type = hero_type
        self.__start_tick = time
        self.__current_time = time
        self.__score_observer.update(score)
        self.__lives = lives
