from typing import Dict, List
from pygame import Surface
from src.enums import HeroLevel, HeroState, HeroType, Level, World
from src.utils.assets import (
    CUMPA_LVL_1,
    CUMPA_LVL_1_BRAKE,
    CUMPA_LVL_1_DIED,
    CUMPA_LVL_1_DOWN_1,
    CUMPA_LVL_1_DOWN_2,
    CUMPA_LVL_1_JUMP,
    CUMPA_LVL_1_WALKING_1,
    CUMPA_LVL_1_WALKING_2,
    CUMPA_LVL_1_WALKING_3,
    CUMPA_LVL_2,
    CUMPA_LVL_2_BRAKE,
    CUMPA_LVL_2_DUCK,
    CUMPA_LVL_2_DOWN_1,
    CUMPA_LVL_2_DOWN_2,
    CUMPA_LVL_2_JUMP,
    CUMPA_LVL_2_WALKING_1,
    CUMPA_LVL_2_WALKING_2,
    CUMPA_LVL_2_WALKING_3,
    CUMPA_LVL_3,
    CUMPA_LVL_3_BRAKE,
    CUMPA_LVL_3_DUCK,
    CUMPA_LVL_3_DOWN_1,
    CUMPA_LVL_3_DOWN_2,
    CUMPA_LVL_3_JUMP,
    CUMPA_LVL_3_WALKING_1,
    CUMPA_LVL_3_WALKING_2,
    CUMPA_LVL_3_WALKING_3,
    CUMPA_LVL_4_1,
    CUMPA_LVL_4_1_BRAKE,
    CUMPA_LVL_4_1_DIED,
    CUMPA_LVL_4_1_DOWN_1,
    CUMPA_LVL_4_1_DOWN_2,
    CUMPA_LVL_4_1_JUMP,
    CUMPA_LVL_4_1_WALKING_1,
    CUMPA_LVL_4_1_WALKING_2,
    CUMPA_LVL_4_1_WALKING_3,
    CUMPA_LVL_4_2,
    CUMPA_LVL_4_2_BRAKE,
    CUMPA_LVL_4_2_DUCK,
    CUMPA_LVL_4_2_DOWN_1,
    CUMPA_LVL_4_2_DOWN_2,
    CUMPA_LVL_4_2_JUMP,
    CUMPA_LVL_4_2_WALKING_1,
    CUMPA_LVL_4_2_WALKING_2,
    CUMPA_LVL_4_2_WALKING_3,
    HIJITA_LVL_1,
    HIJITA_LVL_1_BRAKE,
    HIJITA_LVL_1_DIED,
    HIJITA_LVL_1_DOWN_1,
    HIJITA_LVL_1_DOWN_2,
    HIJITA_LVL_1_JUMP,
    HIJITA_LVL_1_WALKING_1,
    HIJITA_LVL_1_WALKING_2,
    HIJITA_LVL_1_WALKING_3,
    HIJITA_LVL_2,
    HIJITA_LVL_2_BRAKE,
    HIJITA_LVL_2_DUCK,
    HIJITA_LVL_2_DOWN_1,
    HIJITA_LVL_2_DOWN_2,
    HIJITA_LVL_2_JUMP,
    HIJITA_LVL_2_WALKING_1,
    HIJITA_LVL_2_WALKING_2,
    HIJITA_LVL_2_WALKING_3,
    HIJITA_LVL_3,
    HIJITA_LVL_3_BRAKE,
    HIJITA_LVL_3_DUCK,
    HIJITA_LVL_3_DOWN_1,
    HIJITA_LVL_3_DOWN_2,
    HIJITA_LVL_3_JUMP,
    HIJITA_LVL_3_WALKING_1,
    HIJITA_LVL_3_WALKING_2,
    HIJITA_LVL_3_WALKING_3,
    HIJITA_LVL_4_1,
    HIJITA_LVL_4_1_BRAKE,
    HIJITA_LVL_4_1_DIED,
    HIJITA_LVL_4_1_DOWN_1,
    HIJITA_LVL_4_1_DOWN_2,
    HIJITA_LVL_4_1_JUMP,
    HIJITA_LVL_4_1_WALKING_1,
    HIJITA_LVL_4_1_WALKING_2,
    HIJITA_LVL_4_1_WALKING_3,
    HIJITA_LVL_4_2,
    HIJITA_LVL_4_2_BRAKE,
    HIJITA_LVL_4_2_DUCK,
    HIJITA_LVL_4_2_DOWN_1,
    HIJITA_LVL_4_2_DOWN_2,
    HIJITA_LVL_4_2_JUMP,
    HIJITA_LVL_4_2_WALKING_1,
    HIJITA_LVL_4_2_WALKING_2,
    HIJITA_LVL_4_2_WALKING_3,
    PARIENTE_LVL_1,
    PARIENTE_LVL_1_BRAKE,
    PARIENTE_LVL_1_DIED,
    PARIENTE_LVL_1_DOWN_1,
    PARIENTE_LVL_1_DOWN_2,
    PARIENTE_LVL_1_JUMP,
    PARIENTE_LVL_1_WALKING_1,
    PARIENTE_LVL_1_WALKING_2,
    PARIENTE_LVL_1_WALKING_3,
    PARIENTE_LVL_2,
    PARIENTE_LVL_2_BRAKE,
    PARIENTE_LVL_2_DUCK,
    PARIENTE_LVL_2_DOWN_1,
    PARIENTE_LVL_2_DOWN_2,
    PARIENTE_LVL_2_JUMP,
    PARIENTE_LVL_2_WALKING_1,
    PARIENTE_LVL_2_WALKING_2,
    PARIENTE_LVL_2_WALKING_3,
    PARIENTE_LVL_3,
    PARIENTE_LVL_3_BRAKE,
    PARIENTE_LVL_3_DUCK,
    PARIENTE_LVL_3_DOWN_1,
    PARIENTE_LVL_3_DOWN_2,
    PARIENTE_LVL_3_JUMP,
    PARIENTE_LVL_3_WALKING_1,
    PARIENTE_LVL_3_WALKING_2,
    PARIENTE_LVL_3_WALKING_3,
    PARIENTE_LVL_4_1,
    PARIENTE_LVL_4_1_BRAKE,
    PARIENTE_LVL_4_1_DIED,
    PARIENTE_LVL_4_1_DOWN_1,
    PARIENTE_LVL_4_1_DOWN_2,
    PARIENTE_LVL_4_1_JUMP,
    PARIENTE_LVL_4_1_WALKING_1,
    PARIENTE_LVL_4_1_WALKING_2,
    PARIENTE_LVL_4_1_WALKING_3,
    PARIENTE_LVL_4_2,
    PARIENTE_LVL_4_2_BRAKE,
    PARIENTE_LVL_4_2_DUCK,
    PARIENTE_LVL_4_2_DOWN_1,
    PARIENTE_LVL_4_2_DOWN_2,
    PARIENTE_LVL_4_2_JUMP,
    PARIENTE_LVL_4_2_WALKING_1,
    PARIENTE_LVL_4_2_WALKING_2,
    PARIENTE_LVL_4_2_WALKING_3
)
from src.utils import Singleton
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
                    HeroState.IDLE: [PARIENTE_LVL_1],
                    HeroState.RUN: [
                        PARIENTE_LVL_1_WALKING_1,
                        PARIENTE_LVL_1_WALKING_2,
                        PARIENTE_LVL_1_WALKING_3,
                    ],
                    HeroState.JUMP: [PARIENTE_LVL_1_JUMP],
                    HeroState.DOWN: [
                        PARIENTE_LVL_1_DOWN_1,
                        PARIENTE_LVL_1_DOWN_2,
                    ],
                    HeroState.BRAKE: [PARIENTE_LVL_1_BRAKE],
                    HeroState.DEAD: [PARIENTE_LVL_1_DIED],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [PARIENTE_LVL_2],
                    HeroState.RUN: [
                        PARIENTE_LVL_2_WALKING_1,
                        PARIENTE_LVL_2_WALKING_2,
                        PARIENTE_LVL_2_WALKING_3,
                    ],
                    HeroState.JUMP: [PARIENTE_LVL_2_JUMP],
                    HeroState.DUCK: [PARIENTE_LVL_2_DUCK],
                    HeroState.BRAKE: [PARIENTE_LVL_2_BRAKE],
                    HeroState.DOWN: [
                        PARIENTE_LVL_2_DOWN_1,
                        PARIENTE_LVL_2_DOWN_2,
                    ],
                },
                HeroLevel.COCA: {
                    HeroState.IDLE: [PARIENTE_LVL_3],
                    HeroState.RUN: [
                        PARIENTE_LVL_3_WALKING_1,
                        PARIENTE_LVL_3_WALKING_2,
                        PARIENTE_LVL_3_WALKING_3,
                    ],
                    HeroState.JUMP: [PARIENTE_LVL_3_JUMP],
                    HeroState.DUCK: [PARIENTE_LVL_3_DUCK],
                    HeroState.BRAKE: [PARIENTE_LVL_3_BRAKE],
                    HeroState.DOWN: [
                        PARIENTE_LVL_3_DOWN_1,
                        PARIENTE_LVL_3_DOWN_2,
                    ],
                },
                HeroLevel.BORRACHO_SMALL: {
                    HeroState.IDLE: [PARIENTE_LVL_4_1],
                    HeroState.RUN: [
                        PARIENTE_LVL_4_1_WALKING_1,
                        PARIENTE_LVL_4_1_WALKING_2,
                        PARIENTE_LVL_4_1_WALKING_3,
                    ],
                    HeroState.JUMP: [PARIENTE_LVL_4_1_JUMP],
                    HeroState.DOWN: [
                        PARIENTE_LVL_4_1_DOWN_1,
                        PARIENTE_LVL_4_1_DOWN_2,
                    ],
                    HeroState.BRAKE: [PARIENTE_LVL_4_1_BRAKE],
                    HeroState.DEAD: [PARIENTE_LVL_4_1_DIED],
                },
                HeroLevel.BORRACHO_BIG: {
                    HeroState.IDLE: [PARIENTE_LVL_4_2],
                    HeroState.RUN: [
                        PARIENTE_LVL_4_2_WALKING_1,
                        PARIENTE_LVL_4_2_WALKING_2,
                        PARIENTE_LVL_4_2_WALKING_3,
                    ],
                    HeroState.JUMP: [PARIENTE_LVL_4_2_JUMP],
                    HeroState.DUCK: [PARIENTE_LVL_4_2_DUCK],
                    HeroState.BRAKE: [PARIENTE_LVL_4_2_BRAKE],
                    HeroState.DOWN: [
                        PARIENTE_LVL_4_2_DOWN_1,
                        PARIENTE_LVL_4_2_DOWN_2,
                    ],
                },
            },
            HeroType.HIJITA: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [HIJITA_LVL_1],
                    HeroState.RUN: [
                        HIJITA_LVL_1_WALKING_1,
                        HIJITA_LVL_1_WALKING_2,
                        HIJITA_LVL_1_WALKING_3,
                    ],
                    HeroState.JUMP: [HIJITA_LVL_1_JUMP],
                    HeroState.DOWN: [HIJITA_LVL_1_DOWN_1, HIJITA_LVL_1_DOWN_2],
                    HeroState.BRAKE: [HIJITA_LVL_1_BRAKE],
                    HeroState.DEAD: [HIJITA_LVL_1_DIED],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [HIJITA_LVL_2],
                    HeroState.RUN: [
                        HIJITA_LVL_2_WALKING_1,
                        HIJITA_LVL_2_WALKING_2,
                        HIJITA_LVL_2_WALKING_3,
                    ],
                    HeroState.JUMP: [HIJITA_LVL_2_JUMP],
                    HeroState.DUCK: [HIJITA_LVL_2_DUCK],
                    HeroState.BRAKE: [HIJITA_LVL_2_BRAKE],
                    HeroState.DOWN: [HIJITA_LVL_2_DOWN_1, HIJITA_LVL_2_DOWN_2],
                },
                HeroLevel.COCA: {
                    HeroState.IDLE: [HIJITA_LVL_3],
                    HeroState.RUN: [
                        HIJITA_LVL_3_WALKING_1,
                        HIJITA_LVL_3_WALKING_2,
                        HIJITA_LVL_3_WALKING_3,
                    ],
                    HeroState.JUMP: [HIJITA_LVL_3_JUMP],
                    HeroState.DUCK: [HIJITA_LVL_3_DUCK],
                    HeroState.BRAKE: [HIJITA_LVL_3_BRAKE],
                    HeroState.DOWN: [HIJITA_LVL_3_DOWN_1, HIJITA_LVL_3_DOWN_2],
                },
                HeroLevel.BORRACHO_SMALL: {
                    HeroState.IDLE: [HIJITA_LVL_4_1],
                    HeroState.RUN: [
                        HIJITA_LVL_4_1_WALKING_1,
                        HIJITA_LVL_4_1_WALKING_2,
                        HIJITA_LVL_4_1_WALKING_3,
                    ],
                    HeroState.JUMP: [HIJITA_LVL_4_1_JUMP],
                    HeroState.DOWN: [
                        HIJITA_LVL_4_1_DOWN_1,
                        HIJITA_LVL_4_1_DOWN_2,
                    ],
                    HeroState.BRAKE: [HIJITA_LVL_4_1_BRAKE],
                    HeroState.DEAD: [HIJITA_LVL_4_1_DIED],
                },
                HeroLevel.BORRACHO_BIG: {
                    HeroState.IDLE: [HIJITA_LVL_4_2],
                    HeroState.RUN: [
                        HIJITA_LVL_4_2_WALKING_1,
                        HIJITA_LVL_4_2_WALKING_2,
                        HIJITA_LVL_4_2_WALKING_3,
                    ],
                    HeroState.JUMP: [HIJITA_LVL_4_2_JUMP],
                    HeroState.DUCK: [HIJITA_LVL_4_2_DUCK],
                    HeroState.BRAKE: [HIJITA_LVL_4_2_BRAKE],
                    HeroState.DOWN: [
                        HIJITA_LVL_4_2_DOWN_1,
                        HIJITA_LVL_4_2_DOWN_2,
                    ],
                },
            },
            HeroType.CUMPA: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [CUMPA_LVL_1],
                    HeroState.RUN: [
                        CUMPA_LVL_1_WALKING_1,
                        CUMPA_LVL_1_WALKING_2,
                        CUMPA_LVL_1_WALKING_3,
                    ],
                    HeroState.JUMP: [CUMPA_LVL_1_JUMP],
                    HeroState.DOWN: [CUMPA_LVL_1_DOWN_1, CUMPA_LVL_1_DOWN_2],
                    HeroState.BRAKE: [CUMPA_LVL_1_BRAKE],
                    HeroState.DEAD: [CUMPA_LVL_1_DIED],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [CUMPA_LVL_2],
                    HeroState.RUN: [
                        CUMPA_LVL_2_WALKING_1,
                        CUMPA_LVL_2_WALKING_2,
                        CUMPA_LVL_2_WALKING_3,
                    ],
                    HeroState.JUMP: [CUMPA_LVL_2_JUMP],
                    HeroState.DUCK: [CUMPA_LVL_2_DUCK],
                    HeroState.BRAKE: [CUMPA_LVL_2_BRAKE],
                    HeroState.DOWN: [CUMPA_LVL_2_DOWN_1, CUMPA_LVL_2_DOWN_2],
                },
                HeroLevel.COCA: {
                    HeroState.IDLE: [CUMPA_LVL_3],
                    HeroState.RUN: [
                        CUMPA_LVL_3_WALKING_1,
                        CUMPA_LVL_3_WALKING_2,
                        CUMPA_LVL_3_WALKING_3,
                    ],
                    HeroState.JUMP: [CUMPA_LVL_3_JUMP],
                    HeroState.DUCK: [CUMPA_LVL_3_DUCK],
                    HeroState.BRAKE: [CUMPA_LVL_3_BRAKE],
                    HeroState.DOWN: [CUMPA_LVL_3_DOWN_1, CUMPA_LVL_3_DOWN_2],
                },
                HeroLevel.BORRACHO_SMALL: {
                    HeroState.IDLE: [CUMPA_LVL_4_1],
                    HeroState.RUN: [
                        CUMPA_LVL_4_1_WALKING_1,
                        CUMPA_LVL_4_1_WALKING_2,
                        CUMPA_LVL_4_1_WALKING_3,
                    ],
                    HeroState.JUMP: [CUMPA_LVL_4_1_JUMP],
                    HeroState.DOWN: [
                        CUMPA_LVL_4_1_DOWN_1,
                        CUMPA_LVL_4_1_DOWN_2,
                    ],
                    HeroState.BRAKE: [CUMPA_LVL_4_1_BRAKE],
                    HeroState.DEAD: [CUMPA_LVL_4_1_DIED],
                },
                HeroLevel.BORRACHO_BIG: {
                    HeroState.IDLE: [CUMPA_LVL_4_2],
                    HeroState.RUN: [
                        CUMPA_LVL_4_2_WALKING_1,
                        CUMPA_LVL_4_2_WALKING_2,
                        CUMPA_LVL_4_2_WALKING_3,
                    ],
                    HeroState.JUMP: [CUMPA_LVL_4_2_JUMP],
                    HeroState.DUCK: [CUMPA_LVL_4_2_DUCK],
                    HeroState.BRAKE: [CUMPA_LVL_4_2_BRAKE],
                    HeroState.DOWN: [
                        CUMPA_LVL_4_2_DOWN_1,
                        CUMPA_LVL_4_2_DOWN_2,
                    ],
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
