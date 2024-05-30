from typing import Dict, List

from pygame import Surface

from src.enums import HeroLevel, HeroState, HeroType, Level, World
from src.services.mapping.concretes.level_mapper import LevelMapper
from src.utils.assets import CUMPA_IDLE, HIJITA_IDLE, PARIENTE_IDLE
from .level_data import LevelData



class GameData:
    def __init__(self):
        self.level_mapper = LevelMapper()
        self.level_data : Dict[World, Dict[Level, LevelData]] = {}

        self.heroes_data: Dict[
            HeroType, Dict[HeroLevel, Dict[HeroState, List[Surface]]]
        ] = {
            HeroType.PARIENTE: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [PARIENTE_IDLE],
                    HeroState.RUN: [],
                    HeroState.JUMP: [],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [],
                    HeroState.RUN: [],
                    HeroState.JUMP: [],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [],
                },
            },
            HeroType.HIJITA: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [HIJITA_IDLE],
                    HeroState.RUN: [],
                    HeroState.JUMP: [],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [],
                    HeroState.RUN: [],
                    HeroState.JUMP: [],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [],
                },
            },
            HeroType.CUMPA: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [CUMPA_IDLE],
                    HeroState.RUN: [],
                    HeroState.JUMP: [],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [],
                    HeroState.RUN: [],
                    HeroState.JUMP: [],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [],
                },
            },
        }

    def get_level_data(self, world: World, level: Level) -> LevelData:
        if (self.level_data=={}) or (self.level_data[world] == {}) or (self.level_data[world][level] is {}):
            self.level_data[world]={
                level: self.level_mapper.map_level(world, level)
            }
        return self.level_data[world][level]

    def get_hero_data(
        self, hero_type: HeroType
    ) -> Dict[HeroLevel, Dict[HeroState, List[Surface]]]:
        return self.heroes_data[hero_type]
