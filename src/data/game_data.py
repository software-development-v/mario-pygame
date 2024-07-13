from typing import Dict, List

from pygame import Surface

from src.enums import HeroLevel, HeroState, HeroType, Level, World
from src.utils import Singleton, heroes

from .interfaces import IGameData, ILevelData
from .mappers import LevelMapper


class GameData(IGameData):
    __metaclass__ = Singleton

    def __init__(self):
        self.level_mapper = LevelMapper()

        self.level_data: Dict[World, Dict[Level, ILevelData]] = {}

    def get_level_data(self, world: World, level: Level) -> ILevelData:
        if (
            (self.level_data == {})
            or (self.level_data[world] == {})
            or (self.level_data[world][level] is {})
        ):
            self.level_data[world] = {
                level: self.level_mapper.map_level(world, level)
            }

        return self.level_data[world][level]

    def get_hero_data(
        self, hero_type: HeroType
    ) -> Dict[HeroLevel, Dict[HeroState, List[Surface]]]:
        return heroes[hero_type]
