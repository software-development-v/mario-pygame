from typing import Dict, List

from pygame import Surface

from src.enums import HeroLevel, HeroState, HeroType, Level, World
from src.utils import Position
from src.utils.assets import CUMPA_IDLE, HIJITA_IDLE, PARIENTE_IDLE
from src.utils.colors import BLUE_SKY

from .background import BackgroundColor
from .level_data import LevelData


class GameData:
    def __init__(self):
        self.levels_data: Dict[World, Dict[Level, LevelData]] = {
            World.ONE: {
                Level.FIRST: LevelData(
                    World.ONE,
                    Level.FIRST,
                    400,
                    BackgroundColor(BLUE_SKY),
                    "test",
                    Position(0, 0),
                    {},
                    {},
                    {},
                )
            },
        }

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
        return self.levels_data[world][level]

    def get_hero_data(
        self, hero_type: HeroType
    ) -> Dict[HeroLevel, Dict[HeroState, List[Surface]]]:
        return self.heroes_data[hero_type]
