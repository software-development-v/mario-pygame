from typing import List

from pygame import Surface

from src.entities import Hero
from src.enums import Level, World

from ..abstractions import Manager


class LevelManager:
    def __init__(
        self,
        hero: Hero,
        managers: List[Manager],
        world: World,
        level: Level,
        background: Surface,
        time: int,
        start_tick: int,
    ) -> None:
        self.hero = hero
        self.managers = managers
        self.world = world
        self.level = level
        self.background = background
        self.start_time = time
        self.current_time = time
        self.start_tick = start_tick
