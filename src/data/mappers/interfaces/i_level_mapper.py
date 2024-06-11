from abc import ABC, abstractmethod

from src.enums import Level, World

from ...interfaces import ILevelData


class ILevelMapper(ABC):

    @abstractmethod
    def map_level(self, world: World, level: Level) -> ILevelData:
        pass
