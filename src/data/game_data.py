from typing import Dict, List

from pygame import Surface

from src.enums import HeroState, HeroType, Level, World

from .level_data import LevelData


class GameData:
    def __init__(self):
        self.levels_data: Dict[World, Dict[Level, LevelData]] = {
            World.ONE: {
                Level.FIRST: LevelData(),
                Level.SECOND: LevelData(),
                Level.THIRD: LevelData(),
                Level.FOURTH: LevelData(),
            },
        }

        self.heores_data: Dict[HeroType, Dict[HeroState, List[Surface]]] = {}

    def get_level_data(self, world: World, level: Level) -> LevelData:
        return self.levels_data[world][level]

    def get_hero_data(
        self, hero_type: HeroType, hero_state: HeroState
    ) -> List[Surface]:
        return self.heores_data[hero_type][hero_state]