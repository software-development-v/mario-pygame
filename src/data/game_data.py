from typing import Dict, List

from pygame import Surface
from src.enums import HeroState, HeroType, Level, World
from ..utils.assets import (
    PLAYER_PARIENTE, PLAYER_PARIENTE1, PLAYER_PARIENTE2, 
    PLAYER_HIJITA, PLAYER_HIJITA1, PLAYER_HIJITA2,
    PLAYER_CUMPA, PLAYER_CUMPA1, PLAYER_CUMPA2
)
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

        self.heores_data: Dict[HeroType, Dict[HeroState, List[Surface]]] = {
            HeroType.PARIENTE: {
                HeroState.IDLE: [PLAYER_PARIENTE],
                HeroState.RUN: [PLAYER_PARIENTE1, PLAYER_PARIENTE2],
                HeroState.JUMP: [],
                HeroState.DUCK: [],
                HeroState.BRAKE: [],
                HeroState.DEAD: []
            },
            HeroType.HIJITA: {
                HeroState.IDLE: [PLAYER_HIJITA],
                HeroState.RUN: [PLAYER_HIJITA1, PLAYER_HIJITA2],
                HeroState.JUMP: [],
                HeroState.DUCK: [],
                HeroState.BRAKE: [],
                HeroState.DEAD: []
            },
            HeroType.CUMPA: {
                HeroState.IDLE: [PLAYER_CUMPA],
                HeroState.RUN: [PLAYER_CUMPA1, PLAYER_CUMPA2],
                HeroState.JUMP: [],
                HeroState.DUCK: [],
                HeroState.BRAKE: [],
                HeroState.DEAD: []
            }
        }

    def get_level_data(self, world: World, level: Level) -> LevelData:
        return self.levels_data[world][level]

    def get_hero_data(
        self, hero_type: HeroType, hero_state: HeroState
    ) -> List[Surface]:
        return self.heores_data[hero_type][hero_state]
