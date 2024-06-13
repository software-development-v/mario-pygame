from typing import Dict, List
from pygame import Surface
from src.enums import HeroLevel, HeroState, HeroType, Level, World
from src.utils.assets import (
    PARIENTE_LVL_1_FRONT,
    PARIENTE_LVL_1_BACK,
    PARIENTE_LVL_1_BRAKE_FRONT,
    PARIENTE_LVL_1_BRAKE_BACK,
    PARIENTE_LVL_1_DIED,
    PARIENTE_LVL_1_DOWN_1_FRONT,
    PARIENTE_LVL_1_DOWN_2_FRONT,
    PARIENTE_LVL_1_DOWN_1_BACK,
    PARIENTE_LVL_1_DOWN_2_BACK,
    PARIENTE_LVL_1_JUMP_FRONT,
    PARIENTE_LVL_1_JUMP_BACK,
    PARIENTE_LVL_1_WALKING_1_FRONT,
    PARIENTE_LVL_1_WALKING_2_FRONT,
    PARIENTE_LVL_1_WALKING_3_FRONT,
    PARIENTE_LVL_1_WALKING_1_BACK,
    PARIENTE_LVL_1_WALKING_2_BACK,
    PARIENTE_LVL_1_WALKING_3_BACK,
    PARIENTE_LVL_2_FRONT,
    PARIENTE_LVL_2_BACK,
    PARIENTE_LVL_2_BRAKE_FRONT,
    PARIENTE_LVL_2_BRAKE_BACK,
    PARIENTE_LVL_2_DUCK_FRONT,
    PARIENTE_LVL_2_DUCK_BACK,
    PARIENTE_LVL_2_DOWN_1_FRONT,
    PARIENTE_LVL_2_DOWN_2_FRONT,
    PARIENTE_LVL_2_DOWN_1_BACK,
    PARIENTE_LVL_2_DOWN_2_BACK,
    PARIENTE_LVL_2_JUMP_FRONT,
    PARIENTE_LVL_2_JUMP_BACK,
    PARIENTE_LVL_2_WALKING_1_FRONT,
    PARIENTE_LVL_2_WALKING_2_FRONT,
    PARIENTE_LVL_2_WALKING_3_FRONT,
    PARIENTE_LVL_2_WALKING_1_BACK,
    PARIENTE_LVL_2_WALKING_2_BACK,
    PARIENTE_LVL_2_WALKING_3_BACK,
    PARIENTE_LVL_3_FRONT,
    PARIENTE_LVL_3_BACK,
    PARIENTE_LVL_3_BRAKE_FRONT,
    PARIENTE_LVL_3_BRAKE_BACK,
    PARIENTE_LVL_3_DUCK_FRONT,
    PARIENTE_LVL_3_DUCK_BACK,
    PARIENTE_LVL_3_DOWN_1_FRONT,
    PARIENTE_LVL_3_DOWN_2_FRONT,
    PARIENTE_LVL_3_DOWN_1_BACK,
    PARIENTE_LVL_3_DOWN_2_BACK,
    PARIENTE_LVL_3_JUMP_FRONT,
    PARIENTE_LVL_3_JUMP_BACK,
    PARIENTE_LVL_3_WALKING_1_FRONT,
    PARIENTE_LVL_3_WALKING_2_FRONT,
    PARIENTE_LVL_3_WALKING_3_FRONT,
    PARIENTE_LVL_3_WALKING_1_BACK,
    PARIENTE_LVL_3_WALKING_2_BACK,
    PARIENTE_LVL_3_WALKING_3_BACK,
    PARIENTE_LVL_4_1_FRONT,
    PARIENTE_LVL_4_1_BACK,
    PARIENTE_LVL_4_1_BRAKE_FRONT,
    PARIENTE_LVL_4_1_BRAKE_BACK,
    PARIENTE_LVL_4_1_DIED,
    PARIENTE_LVL_4_1_DOWN_1_FRONT,
    PARIENTE_LVL_4_1_DOWN_2_FRONT,
    PARIENTE_LVL_4_1_DOWN_1_BACK,
    PARIENTE_LVL_4_1_DOWN_2_BACK,
    PARIENTE_LVL_4_1_JUMP_FRONT,
    PARIENTE_LVL_4_1_JUMP_BACK,
    PARIENTE_LVL_4_1_WALKING_1_FRONT,
    PARIENTE_LVL_4_1_WALKING_2_FRONT,
    PARIENTE_LVL_4_1_WALKING_3_FRONT,
    PARIENTE_LVL_4_1_WALKING_1_BACK,
    PARIENTE_LVL_4_1_WALKING_2_BACK,
    PARIENTE_LVL_4_1_WALKING_3_BACK,
    PARIENTE_LVL_4_2_FRONT,
    PARIENTE_LVL_4_2_BACK,
    PARIENTE_LVL_4_2_BRAKE_FRONT,
    PARIENTE_LVL_4_2_BRAKE_BACK,
    PARIENTE_LVL_4_2_DUCK_FRONT,
    PARIENTE_LVL_4_2_DUCK_BACK,
    PARIENTE_LVL_4_2_DOWN_1_FRONT,
    PARIENTE_LVL_4_2_DOWN_2_FRONT,
    PARIENTE_LVL_4_2_DOWN_1_BACK,
    PARIENTE_LVL_4_2_DOWN_2_BACK,
    PARIENTE_LVL_4_2_JUMP_FRONT,
    PARIENTE_LVL_4_2_JUMP_BACK,
    PARIENTE_LVL_4_2_WALKING_1_FRONT,
    PARIENTE_LVL_4_2_WALKING_2_FRONT,
    PARIENTE_LVL_4_2_WALKING_3_FRONT,
    PARIENTE_LVL_4_2_WALKING_1_BACK,
    PARIENTE_LVL_4_2_WALKING_2_BACK,
    PARIENTE_LVL_4_2_WALKING_3_BACK,
    HIJITA_LVL_1_FRONT,
    HIJITA_LVL_1_BACK,
    HIJITA_LVL_1_BRAKE_FRONT,
    HIJITA_LVL_1_BRAKE_BACK,
    HIJITA_LVL_1_DIED,
    HIJITA_LVL_1_DOWN_1_FRONT,
    HIJITA_LVL_1_DOWN_2_FRONT,
    HIJITA_LVL_1_DOWN_1_BACK,
    HIJITA_LVL_1_DOWN_2_BACK,
    HIJITA_LVL_1_JUMP_FRONT,
    HIJITA_LVL_1_JUMP_BACK,
    HIJITA_LVL_1_WALKING_1_FRONT,
    HIJITA_LVL_1_WALKING_2_FRONT,
    HIJITA_LVL_1_WALKING_3_FRONT,
    HIJITA_LVL_1_WALKING_1_BACK,
    HIJITA_LVL_1_WALKING_2_BACK,
    HIJITA_LVL_1_WALKING_3_BACK,
    HIJITA_LVL_2_FRONT,
    HIJITA_LVL_2_BACK,
    HIJITA_LVL_2_BRAKE_FRONT,
    HIJITA_LVL_2_BRAKE_BACK,
    HIJITA_LVL_2_DUCK_FRONT,
    HIJITA_LVL_2_DUCK_BACK,
    HIJITA_LVL_2_DOWN_1_FRONT,
    HIJITA_LVL_2_DOWN_2_FRONT,
    HIJITA_LVL_2_DOWN_1_BACK,
    HIJITA_LVL_2_DOWN_2_BACK,
    HIJITA_LVL_2_JUMP_FRONT,
    HIJITA_LVL_2_JUMP_BACK,
    HIJITA_LVL_2_WALKING_1_FRONT,
    HIJITA_LVL_2_WALKING_2_FRONT,
    HIJITA_LVL_2_WALKING_3_FRONT,
    HIJITA_LVL_2_WALKING_1_BACK,
    HIJITA_LVL_2_WALKING_2_BACK,
    HIJITA_LVL_2_WALKING_3_BACK,
    HIJITA_LVL_3_FRONT,
    HIJITA_LVL_3_BACK,
    HIJITA_LVL_3_BRAKE_FRONT,
    HIJITA_LVL_3_BRAKE_BACK,
    HIJITA_LVL_3_DUCK_FRONT,
    HIJITA_LVL_3_DUCK_BACK,
    HIJITA_LVL_3_DOWN_1_FRONT,
    HIJITA_LVL_3_DOWN_2_FRONT,
    HIJITA_LVL_3_DOWN_1_BACK,
    HIJITA_LVL_3_DOWN_2_BACK,
    HIJITA_LVL_3_JUMP_FRONT,
    HIJITA_LVL_3_JUMP_BACK,
    HIJITA_LVL_3_WALKING_1_FRONT,
    HIJITA_LVL_3_WALKING_2_FRONT,
    HIJITA_LVL_3_WALKING_3_FRONT,
    HIJITA_LVL_3_WALKING_1_BACK,
    HIJITA_LVL_3_WALKING_2_BACK,
    HIJITA_LVL_3_WALKING_3_BACK,
    HIJITA_LVL_4_1_FRONT,
    HIJITA_LVL_4_1_BACK,
    HIJITA_LVL_4_1_BRAKE_FRONT,
    HIJITA_LVL_4_1_BRAKE_BACK,
    HIJITA_LVL_4_1_DIED,
    HIJITA_LVL_4_1_DOWN_1_FRONT,
    HIJITA_LVL_4_1_DOWN_2_FRONT,
    HIJITA_LVL_4_1_DOWN_1_BACK,
    HIJITA_LVL_4_1_DOWN_2_BACK,
    HIJITA_LVL_4_1_JUMP_FRONT,
    HIJITA_LVL_4_1_JUMP_BACK,
    HIJITA_LVL_4_1_WALKING_1_FRONT,
    HIJITA_LVL_4_1_WALKING_2_FRONT,
    HIJITA_LVL_4_1_WALKING_3_FRONT,
    HIJITA_LVL_4_1_WALKING_1_BACK,
    HIJITA_LVL_4_1_WALKING_2_BACK,
    HIJITA_LVL_4_1_WALKING_3_BACK,
    HIJITA_LVL_4_2_FRONT,
    HIJITA_LVL_4_2_BACK,
    HIJITA_LVL_4_2_BRAKE_FRONT,
    HIJITA_LVL_4_2_BRAKE_BACK,
    HIJITA_LVL_4_2_DUCK_FRONT,
    HIJITA_LVL_4_2_DUCK_BACK,
    HIJITA_LVL_4_2_DOWN_1_FRONT,
    HIJITA_LVL_4_2_DOWN_2_FRONT,
    HIJITA_LVL_4_2_DOWN_1_BACK,
    HIJITA_LVL_4_2_DOWN_2_BACK,
    HIJITA_LVL_4_2_JUMP_FRONT,
    HIJITA_LVL_4_2_JUMP_BACK,
    HIJITA_LVL_4_2_WALKING_1_FRONT,
    HIJITA_LVL_4_2_WALKING_2_FRONT,
    HIJITA_LVL_4_2_WALKING_3_FRONT,
    HIJITA_LVL_4_2_WALKING_1_BACK,
    HIJITA_LVL_4_2_WALKING_2_BACK,
    HIJITA_LVL_4_2_WALKING_3_BACK,
    CUMPA_LVL_1_FRONT,
    CUMPA_LVL_1_BACK,
    CUMPA_LVL_1_BRAKE_FRONT,
    CUMPA_LVL_1_BRAKE_BACK,
    CUMPA_LVL_1_DIED,
    CUMPA_LVL_1_DOWN_1_FRONT,
    CUMPA_LVL_1_DOWN_2_FRONT,
    CUMPA_LVL_1_DOWN_1_BACK,
    CUMPA_LVL_1_DOWN_2_BACK,
    CUMPA_LVL_1_JUMP_FRONT,
    CUMPA_LVL_1_JUMP_BACK,
    CUMPA_LVL_1_WALKING_1_FRONT,
    CUMPA_LVL_1_WALKING_2_FRONT,
    CUMPA_LVL_1_WALKING_3_FRONT,
    CUMPA_LVL_1_WALKING_1_BACK,
    CUMPA_LVL_1_WALKING_2_BACK,
    CUMPA_LVL_1_WALKING_3_BACK,
    CUMPA_LVL_2_FRONT,
    CUMPA_LVL_2_BACK,
    CUMPA_LVL_2_BRAKE_FRONT,
    CUMPA_LVL_2_BRAKE_BACK,
    CUMPA_LVL_2_DUCK_FRONT,
    CUMPA_LVL_2_DUCK_BACK,
    CUMPA_LVL_2_DOWN_1_FRONT,
    CUMPA_LVL_2_DOWN_2_FRONT,
    CUMPA_LVL_2_DOWN_1_BACK,
    CUMPA_LVL_2_DOWN_2_BACK,
    CUMPA_LVL_2_JUMP_FRONT,
    CUMPA_LVL_2_JUMP_BACK,
    CUMPA_LVL_2_WALKING_1_FRONT,
    CUMPA_LVL_2_WALKING_2_FRONT,
    CUMPA_LVL_2_WALKING_3_FRONT,
    CUMPA_LVL_2_WALKING_1_BACK,
    CUMPA_LVL_2_WALKING_2_BACK,
    CUMPA_LVL_2_WALKING_3_BACK,
    CUMPA_LVL_3_FRONT,
    CUMPA_LVL_3_BACK,
    CUMPA_LVL_3_BRAKE_FRONT,
    CUMPA_LVL_3_BRAKE_BACK,
    CUMPA_LVL_3_DUCK_FRONT,
    CUMPA_LVL_3_DUCK_BACK,
    CUMPA_LVL_3_DOWN_1_FRONT,
    CUMPA_LVL_3_DOWN_2_FRONT,
    CUMPA_LVL_3_DOWN_1_BACK,
    CUMPA_LVL_3_DOWN_2_BACK,
    CUMPA_LVL_3_JUMP_FRONT,
    CUMPA_LVL_3_JUMP_BACK,
    CUMPA_LVL_3_WALKING_1_FRONT,
    CUMPA_LVL_3_WALKING_2_FRONT,
    CUMPA_LVL_3_WALKING_3_FRONT,
    CUMPA_LVL_3_WALKING_1_BACK,
    CUMPA_LVL_3_WALKING_2_BACK,
    CUMPA_LVL_3_WALKING_3_BACK,
    CUMPA_LVL_4_1_FRONT,
    CUMPA_LVL_4_1_BACK,
    CUMPA_LVL_4_1_BRAKE_FRONT,
    CUMPA_LVL_4_1_BRAKE_BACK,
    CUMPA_LVL_4_1_DIED,
    CUMPA_LVL_4_1_DOWN_1_FRONT,
    CUMPA_LVL_4_1_DOWN_2_FRONT,
    CUMPA_LVL_4_1_DOWN_1_BACK,
    CUMPA_LVL_4_1_DOWN_2_BACK,
    CUMPA_LVL_4_1_JUMP_FRONT,
    CUMPA_LVL_4_1_JUMP_BACK,
    CUMPA_LVL_4_1_WALKING_1_FRONT,
    CUMPA_LVL_4_1_WALKING_2_FRONT,
    CUMPA_LVL_4_1_WALKING_3_FRONT,
    CUMPA_LVL_4_1_WALKING_1_BACK,
    CUMPA_LVL_4_1_WALKING_2_BACK,
    CUMPA_LVL_4_1_WALKING_3_BACK,
    CUMPA_LVL_4_2_FRONT,
    CUMPA_LVL_4_2_BACK,
    CUMPA_LVL_4_2_BRAKE_FRONT,
    CUMPA_LVL_4_2_BRAKE_BACK,
    CUMPA_LVL_4_2_DUCK_FRONT,
    CUMPA_LVL_4_2_DUCK_BACK,
    CUMPA_LVL_4_2_DOWN_1_FRONT,
    CUMPA_LVL_4_2_DOWN_2_FRONT,
    CUMPA_LVL_4_2_DOWN_1_BACK,
    CUMPA_LVL_4_2_DOWN_2_BACK,
    CUMPA_LVL_4_2_JUMP_FRONT,
    CUMPA_LVL_4_2_JUMP_BACK,
    CUMPA_LVL_4_2_WALKING_1_FRONT,
    CUMPA_LVL_4_2_WALKING_2_FRONT,
    CUMPA_LVL_4_2_WALKING_3_FRONT,
    CUMPA_LVL_4_2_WALKING_1_BACK,
    CUMPA_LVL_4_2_WALKING_2_BACK,
    CUMPA_LVL_4_2_WALKING_3_BACK,
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
            HeroType, Dict[HeroLevel, Dict[HeroState, List[List[Surface]]]]
        ] = {
            HeroType.PARIENTE: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [
                        [PARIENTE_LVL_1_FRONT],
                        [PARIENTE_LVL_1_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            PARIENTE_LVL_1_WALKING_1_FRONT,
                            PARIENTE_LVL_1_WALKING_2_FRONT,
                            PARIENTE_LVL_1_WALKING_3_FRONT,
                        ],
                        [
                            PARIENTE_LVL_1_WALKING_1_BACK,
                            PARIENTE_LVL_1_WALKING_2_BACK,
                            PARIENTE_LVL_1_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [PARIENTE_LVL_1_JUMP_FRONT],
                        [PARIENTE_LVL_1_JUMP_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            PARIENTE_LVL_1_DOWN_1_FRONT,
                            PARIENTE_LVL_1_DOWN_2_FRONT,
                        ],
                        [
                            PARIENTE_LVL_1_DOWN_1_BACK,
                            PARIENTE_LVL_1_DOWN_2_BACK,
                        ],
                    ],
                    HeroState.BRAKE: [
                        [PARIENTE_LVL_1_BRAKE_FRONT],
                        [PARIENTE_LVL_1_BRAKE_BACK],
                    ],
                    HeroState.DEAD: [[PARIENTE_LVL_1_DIED]],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [
                        [PARIENTE_LVL_2_FRONT],
                        [PARIENTE_LVL_2_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            PARIENTE_LVL_2_WALKING_1_FRONT,
                            PARIENTE_LVL_2_WALKING_2_FRONT,
                            PARIENTE_LVL_2_WALKING_3_FRONT,
                        ],
                        [
                            PARIENTE_LVL_2_WALKING_1_BACK,
                            PARIENTE_LVL_2_WALKING_2_BACK,
                            PARIENTE_LVL_2_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [PARIENTE_LVL_2_JUMP_FRONT],
                        [PARIENTE_LVL_2_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [PARIENTE_LVL_2_DUCK_FRONT],
                        [PARIENTE_LVL_2_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [PARIENTE_LVL_2_BRAKE_FRONT],
                        [PARIENTE_LVL_2_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            PARIENTE_LVL_2_DOWN_1_FRONT,
                            PARIENTE_LVL_2_DOWN_2_FRONT,
                        ],
                        [
                            PARIENTE_LVL_2_DOWN_1_BACK,
                            PARIENTE_LVL_2_DOWN_2_BACK,
                        ],
                    ],
                },
                HeroLevel.COCA: {
                    HeroState.IDLE: [
                        [PARIENTE_LVL_3_FRONT],
                        [PARIENTE_LVL_3_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            PARIENTE_LVL_3_WALKING_1_FRONT,
                            PARIENTE_LVL_3_WALKING_2_FRONT,
                            PARIENTE_LVL_3_WALKING_3_FRONT,
                        ],
                        [
                            PARIENTE_LVL_3_WALKING_1_BACK,
                            PARIENTE_LVL_3_WALKING_2_BACK,
                            PARIENTE_LVL_3_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [PARIENTE_LVL_3_JUMP_FRONT],
                        [PARIENTE_LVL_3_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [PARIENTE_LVL_3_DUCK_FRONT],
                        [PARIENTE_LVL_3_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [PARIENTE_LVL_3_BRAKE_FRONT],
                        [PARIENTE_LVL_3_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            PARIENTE_LVL_3_DOWN_1_FRONT,
                            PARIENTE_LVL_3_DOWN_2_FRONT,
                        ],
                        [
                            PARIENTE_LVL_3_DOWN_1_BACK,
                            PARIENTE_LVL_3_DOWN_2_BACK,
                        ],
                    ],
                },
                HeroLevel.BORRACHO_SMALL: {
                    HeroState.IDLE: [
                        [PARIENTE_LVL_4_1_FRONT],
                        [PARIENTE_LVL_4_1_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            PARIENTE_LVL_4_1_WALKING_1_FRONT,
                            PARIENTE_LVL_4_1_WALKING_2_FRONT,
                            PARIENTE_LVL_4_1_WALKING_3_FRONT,
                        ],
                        [
                            PARIENTE_LVL_4_1_WALKING_1_BACK,
                            PARIENTE_LVL_4_1_WALKING_2_BACK,
                            PARIENTE_LVL_4_1_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [PARIENTE_LVL_4_1_JUMP_FRONT],
                        [PARIENTE_LVL_4_1_JUMP_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            PARIENTE_LVL_4_1_DOWN_1_FRONT,
                            PARIENTE_LVL_4_1_DOWN_2_FRONT,
                        ],
                        [
                            PARIENTE_LVL_4_1_DOWN_1_BACK,
                            PARIENTE_LVL_4_1_DOWN_2_BACK,
                        ],
                    ],
                    HeroState.BRAKE: [
                        [PARIENTE_LVL_4_1_BRAKE_FRONT],
                        [PARIENTE_LVL_4_1_BRAKE_BACK],
                    ],
                    HeroState.DEAD: [[PARIENTE_LVL_4_1_DIED]],
                },
                HeroLevel.BORRACHO_BIG: {
                    HeroState.IDLE: [
                        [PARIENTE_LVL_4_2_FRONT],
                        [PARIENTE_LVL_4_2_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            PARIENTE_LVL_4_2_WALKING_1_FRONT,
                            PARIENTE_LVL_4_2_WALKING_2_FRONT,
                            PARIENTE_LVL_4_2_WALKING_3_FRONT,
                        ],
                        [
                            PARIENTE_LVL_4_2_WALKING_1_BACK,
                            PARIENTE_LVL_4_2_WALKING_2_BACK,
                            PARIENTE_LVL_4_2_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [PARIENTE_LVL_4_2_JUMP_FRONT],
                        [PARIENTE_LVL_4_2_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [PARIENTE_LVL_4_2_DUCK_FRONT],
                        [PARIENTE_LVL_4_2_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [PARIENTE_LVL_4_2_BRAKE_FRONT],
                        [PARIENTE_LVL_4_2_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            PARIENTE_LVL_4_2_DOWN_1_FRONT,
                            PARIENTE_LVL_4_2_DOWN_2_FRONT,
                        ],
                        [
                            PARIENTE_LVL_4_2_DOWN_1_BACK,
                            PARIENTE_LVL_4_2_DOWN_2_BACK,
                        ],
                    ],
                },
            },
            HeroType.HIJITA: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [
                        [HIJITA_LVL_1_FRONT],
                        [HIJITA_LVL_1_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            HIJITA_LVL_1_WALKING_1_FRONT,
                            HIJITA_LVL_1_WALKING_2_FRONT,
                            HIJITA_LVL_1_WALKING_3_FRONT,
                        ],
                        [
                            HIJITA_LVL_1_WALKING_1_BACK,
                            HIJITA_LVL_1_WALKING_2_BACK,
                            HIJITA_LVL_1_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [HIJITA_LVL_1_JUMP_FRONT],
                        [HIJITA_LVL_1_JUMP_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            HIJITA_LVL_1_DOWN_1_FRONT,
                            HIJITA_LVL_1_DOWN_2_FRONT,
                        ],
                        [
                            HIJITA_LVL_1_DOWN_1_BACK,
                            HIJITA_LVL_1_DOWN_2_BACK,
                        ],
                    ],
                    HeroState.BRAKE: [
                        [HIJITA_LVL_1_BRAKE_FRONT],
                        [HIJITA_LVL_1_BRAKE_BACK],
                    ],
                    HeroState.DEAD: [[HIJITA_LVL_1_DIED]],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [[HIJITA_LVL_2_FRONT], [HIJITA_LVL_2_BACK]],
                    HeroState.RUN: [
                        [
                            HIJITA_LVL_2_WALKING_1_FRONT,
                            HIJITA_LVL_2_WALKING_2_FRONT,
                            HIJITA_LVL_2_WALKING_3_FRONT,
                        ],
                        [
                            HIJITA_LVL_2_WALKING_1_BACK,
                            HIJITA_LVL_2_WALKING_2_BACK,
                            HIJITA_LVL_2_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [HIJITA_LVL_2_JUMP_FRONT],
                        [HIJITA_LVL_2_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [HIJITA_LVL_2_DUCK_FRONT],
                        [HIJITA_LVL_2_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [HIJITA_LVL_2_BRAKE_FRONT],
                        [HIJITA_LVL_2_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [HIJITA_LVL_2_DOWN_1_FRONT, HIJITA_LVL_2_DOWN_2_FRONT],
                        [HIJITA_LVL_2_DOWN_1_BACK, HIJITA_LVL_2_DOWN_2_BACK],
                    ],
                },
                HeroLevel.COCA: {
                    HeroState.IDLE: [[HIJITA_LVL_3_FRONT], [HIJITA_LVL_3_BACK]],
                    HeroState.RUN: [
                        [
                            HIJITA_LVL_3_WALKING_1_FRONT,
                            HIJITA_LVL_3_WALKING_2_FRONT,
                            HIJITA_LVL_3_WALKING_3_FRONT,
                        ],
                        [
                            HIJITA_LVL_3_WALKING_1_BACK,
                            HIJITA_LVL_3_WALKING_2_BACK,
                            HIJITA_LVL_3_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [HIJITA_LVL_3_JUMP_FRONT],
                        [HIJITA_LVL_3_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [HIJITA_LVL_3_DUCK_FRONT],
                        [HIJITA_LVL_3_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [HIJITA_LVL_3_BRAKE_FRONT],
                        [HIJITA_LVL_3_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [HIJITA_LVL_3_DOWN_1_FRONT, HIJITA_LVL_3_DOWN_2_FRONT],
                        [HIJITA_LVL_3_DOWN_1_BACK, HIJITA_LVL_3_DOWN_2_BACK],
                    ],
                },
                HeroLevel.BORRACHO_SMALL: {
                    HeroState.IDLE: [
                        [HIJITA_LVL_4_1_FRONT],
                        [HIJITA_LVL_4_1_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            HIJITA_LVL_4_1_WALKING_1_FRONT,
                            HIJITA_LVL_4_1_WALKING_2_FRONT,
                            HIJITA_LVL_4_1_WALKING_3_FRONT,
                        ],
                        [
                            HIJITA_LVL_4_1_WALKING_1_BACK,
                            HIJITA_LVL_4_1_WALKING_2_BACK,
                            HIJITA_LVL_4_1_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [HIJITA_LVL_4_1_JUMP_FRONT],
                        [HIJITA_LVL_4_1_JUMP_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            HIJITA_LVL_4_1_DOWN_1_FRONT,
                            HIJITA_LVL_4_1_DOWN_2_FRONT,
                        ],
                        [
                            HIJITA_LVL_4_1_DOWN_1_BACK,
                            HIJITA_LVL_4_1_DOWN_2_BACK,
                        ],
                    ],
                    HeroState.BRAKE: [
                        [HIJITA_LVL_4_1_BRAKE_FRONT],
                        [HIJITA_LVL_4_1_BRAKE_BACK],
                    ],
                    HeroState.DEAD: [[HIJITA_LVL_4_1_DIED]],
                },
                HeroLevel.BORRACHO_BIG: {
                    HeroState.IDLE: [
                        [HIJITA_LVL_4_2_FRONT],
                        [HIJITA_LVL_4_2_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            HIJITA_LVL_4_2_WALKING_1_FRONT,
                            HIJITA_LVL_4_2_WALKING_2_FRONT,
                            HIJITA_LVL_4_2_WALKING_3_FRONT,
                        ],
                        [
                            HIJITA_LVL_4_2_WALKING_1_BACK,
                            HIJITA_LVL_4_2_WALKING_2_BACK,
                            HIJITA_LVL_4_2_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [HIJITA_LVL_4_2_JUMP_FRONT],
                        [HIJITA_LVL_4_2_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [HIJITA_LVL_4_2_DUCK_FRONT],
                        [HIJITA_LVL_4_2_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [HIJITA_LVL_4_2_BRAKE_FRONT],
                        [HIJITA_LVL_4_2_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            HIJITA_LVL_4_2_DOWN_1_FRONT,
                            HIJITA_LVL_4_2_DOWN_2_FRONT,
                        ],
                        [
                            HIJITA_LVL_4_2_DOWN_1_BACK,
                            HIJITA_LVL_4_2_DOWN_2_BACK,
                        ],
                    ],
                },
            },
            HeroType.CUMPA: {
                HeroLevel.NORMAL: {
                    HeroState.IDLE: [
                        [CUMPA_LVL_1_FRONT],
                        [CUMPA_LVL_1_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            CUMPA_LVL_1_WALKING_1_FRONT,
                            CUMPA_LVL_1_WALKING_2_FRONT,
                            CUMPA_LVL_1_WALKING_3_FRONT,
                        ],
                        [
                            CUMPA_LVL_1_WALKING_1_BACK,
                            CUMPA_LVL_1_WALKING_2_BACK,
                            CUMPA_LVL_1_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [CUMPA_LVL_1_JUMP_FRONT],
                        [CUMPA_LVL_1_JUMP_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            CUMPA_LVL_1_DOWN_1_FRONT,
                            CUMPA_LVL_1_DOWN_2_FRONT,
                        ],
                        [
                            CUMPA_LVL_1_DOWN_1_BACK,
                            CUMPA_LVL_1_DOWN_2_BACK,
                        ],
                    ],
                    HeroState.BRAKE: [
                        [CUMPA_LVL_1_BRAKE_FRONT],
                        [CUMPA_LVL_1_BRAKE_BACK],
                    ],
                    HeroState.DEAD: [[CUMPA_LVL_1_DIED]],
                },
                HeroLevel.BIG: {
                    HeroState.IDLE: [[CUMPA_LVL_2_FRONT], [CUMPA_LVL_2_BACK]],
                    HeroState.RUN: [
                        [
                            CUMPA_LVL_2_WALKING_1_FRONT,
                            CUMPA_LVL_2_WALKING_2_FRONT,
                            CUMPA_LVL_2_WALKING_3_FRONT,
                        ],
                        [
                            CUMPA_LVL_2_WALKING_1_BACK,
                            CUMPA_LVL_2_WALKING_2_BACK,
                            CUMPA_LVL_2_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [CUMPA_LVL_2_JUMP_FRONT],
                        [CUMPA_LVL_2_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [CUMPA_LVL_2_DUCK_FRONT],
                        [CUMPA_LVL_2_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [CUMPA_LVL_2_BRAKE_FRONT],
                        [CUMPA_LVL_2_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [CUMPA_LVL_2_DOWN_1_FRONT, CUMPA_LVL_2_DOWN_2_FRONT],
                        [CUMPA_LVL_2_DOWN_1_BACK, CUMPA_LVL_2_DOWN_2_BACK],
                    ],
                },
                HeroLevel.COCA: {
                    HeroState.IDLE: [[CUMPA_LVL_3_FRONT], [CUMPA_LVL_3_BACK]],
                    HeroState.RUN: [
                        [
                            CUMPA_LVL_3_WALKING_1_FRONT,
                            CUMPA_LVL_3_WALKING_2_FRONT,
                            CUMPA_LVL_3_WALKING_3_FRONT,
                        ],
                        [
                            CUMPA_LVL_3_WALKING_1_BACK,
                            CUMPA_LVL_3_WALKING_2_BACK,
                            CUMPA_LVL_3_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [CUMPA_LVL_3_JUMP_FRONT],
                        [CUMPA_LVL_3_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [CUMPA_LVL_3_DUCK_FRONT],
                        [CUMPA_LVL_3_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [CUMPA_LVL_3_BRAKE_FRONT],
                        [CUMPA_LVL_3_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [CUMPA_LVL_3_DOWN_1_FRONT, CUMPA_LVL_3_DOWN_2_FRONT],
                        [CUMPA_LVL_3_DOWN_1_BACK, CUMPA_LVL_3_DOWN_2_BACK],
                    ],
                },
                HeroLevel.BORRACHO_SMALL: {
                    HeroState.IDLE: [
                        [CUMPA_LVL_4_1_FRONT],
                        [CUMPA_LVL_4_1_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            CUMPA_LVL_4_1_WALKING_1_FRONT,
                            CUMPA_LVL_4_1_WALKING_2_FRONT,
                            CUMPA_LVL_4_1_WALKING_3_FRONT,
                        ],
                        [
                            CUMPA_LVL_4_1_WALKING_1_BACK,
                            CUMPA_LVL_4_1_WALKING_2_BACK,
                            CUMPA_LVL_4_1_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [CUMPA_LVL_4_1_JUMP_FRONT],
                        [CUMPA_LVL_4_1_JUMP_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            CUMPA_LVL_4_1_DOWN_1_FRONT,
                            CUMPA_LVL_4_1_DOWN_2_FRONT,
                        ],
                        [
                            CUMPA_LVL_4_1_DOWN_1_BACK,
                            CUMPA_LVL_4_1_DOWN_2_BACK,
                        ],
                    ],
                    HeroState.BRAKE: [
                        [CUMPA_LVL_4_1_BRAKE_FRONT],
                        [CUMPA_LVL_4_1_BRAKE_BACK],
                    ],
                    HeroState.DEAD: [[CUMPA_LVL_4_1_DIED]],
                },
                HeroLevel.BORRACHO_BIG: {
                    HeroState.IDLE: [
                        [CUMPA_LVL_4_2_FRONT],
                        [CUMPA_LVL_4_2_BACK],
                    ],
                    HeroState.RUN: [
                        [
                            CUMPA_LVL_4_2_WALKING_1_FRONT,
                            CUMPA_LVL_4_2_WALKING_2_FRONT,
                            CUMPA_LVL_4_2_WALKING_3_FRONT,
                        ],
                        [
                            CUMPA_LVL_4_2_WALKING_1_BACK,
                            CUMPA_LVL_4_2_WALKING_2_BACK,
                            CUMPA_LVL_4_2_WALKING_3_BACK,
                        ],
                    ],
                    HeroState.JUMP: [
                        [CUMPA_LVL_4_2_JUMP_FRONT],
                        [CUMPA_LVL_4_2_JUMP_BACK],
                    ],
                    HeroState.DUCK: [
                        [CUMPA_LVL_4_2_DUCK_FRONT],
                        [CUMPA_LVL_4_2_DUCK_BACK],
                    ],
                    HeroState.BRAKE: [
                        [CUMPA_LVL_4_2_BRAKE_FRONT],
                        [CUMPA_LVL_4_2_BRAKE_BACK],
                    ],
                    HeroState.DOWN: [
                        [
                            CUMPA_LVL_4_2_DOWN_1_FRONT,
                            CUMPA_LVL_4_2_DOWN_2_FRONT,
                        ],
                        [CUMPA_LVL_4_2_DOWN_1_BACK, CUMPA_LVL_4_2_DOWN_2_BACK],
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
    ) -> Dict[HeroLevel, Dict[HeroState, List[List[Surface]]]]:
        return self.heroes_data[hero_type]
