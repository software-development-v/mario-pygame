from abc import ABC , abstractmethod

from src.data.level_data import LevelData
from src.enums.level import Level
from src.enums.world import World


class ILevelMapper(ABC):

    @abstractmethod
    def map_level(self,world:World, level:Level) -> LevelData :
        pass
