from typing import Dict, List

from pygame import Surface

from src.enums import HeroLevel, HeroState, HeroType, Level, World
from src.utils import Singleton
from src.utils.assets import (
    CUMPA_DIE,
    CUMPA_IDLE,
    CUMPA_JUMP,
    CUMPA_WALK_ANIMATION_1,
    CUMPA_WALK_ANIMATION_2,
    CUMPA_WALK_ANIMATION_3,
    HIJITA_DIE,
    HIJITA_IDLE,
    HIJITA_JUMP,
    HIJITA_WALK_ANIMATION_1,
    HIJITA_WALK_ANIMATION_2,
    HIJITA_WALK_ANIMATION_3,
    PARIENTE_DIE,
    PARIENTE_IDLE,
    PARIENTE_JUMP,
    PARIENTE_WALK_ANIMATION_1,
    PARIENTE_WALK_ANIMATION_2,
    PARIENTE_WALK_ANIMATION_3,
)

from .interfaces import IGameData, ILevelData
from .mappers import LevelMapper


class GameData(IGameData):
    __metaclass__ = Singleton

    def __init__(self):
        self.level_mapper = LevelMapper()

        self.level_data: Dict[World, Dict[Level, ILevelData]] = {}

        self.heroes_data: Dict[
            HeroType, Dict[HeroLevel, Dict[HeroState, List[Surface]]]
        ] = {
            HeroType.PARIENTE: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [PARIENTE_IDLE],
                    HeroState.RUN: [
                        PARIENTE_WALK_ANIMATION_1,
                        PARIENTE_WALK_ANIMATION_2,
                        PARIENTE_WALK_ANIMATION_3,
                    ],
                    HeroState.JUMP: [PARIENTE_JUMP],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [PARIENTE_DIE],
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
                    HeroState.RUN: [
                        HIJITA_WALK_ANIMATION_1,
                        HIJITA_WALK_ANIMATION_2,
                        HIJITA_WALK_ANIMATION_3,
                    ],
                    HeroState.JUMP: [HIJITA_JUMP],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [HIJITA_DIE],
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
                    HeroState.RUN: [
                        CUMPA_WALK_ANIMATION_1,
                        CUMPA_WALK_ANIMATION_2,
                        CUMPA_WALK_ANIMATION_3,
                    ],
                    HeroState.JUMP: [CUMPA_JUMP],
                    HeroState.DUCK: [],
                    HeroState.BRAKE: [],
                    HeroState.DEAD: [CUMPA_DIE],
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
        return self.heroes_data[hero_type]
