from abc import ABC, abstractmethod
from typing import Dict, List

from pygame import Surface

from src.enums import HeroLevel, HeroState, HeroType, Level, World

from .i_level_data import ILevelData


class IGameData(ABC):
    @abstractmethod
    def get_level_data(self, world: World, level: Level) -> ILevelData:
        pass

    @abstractmethod
    def get_hero_data(
        self, hero_type: HeroType
    ) -> Dict[HeroLevel, Dict[HeroState, List[List[Surface]]]]:
        pass
