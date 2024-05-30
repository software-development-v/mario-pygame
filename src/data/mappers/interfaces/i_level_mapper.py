from abc import ABC, abstractmethod

from src.enums import Level, World

from ...level_data import LevelData


class ILevelMapper(ABC):

    @abstractmethod
    def map_level(self, world: World, level: Level) -> LevelData:
        pass
