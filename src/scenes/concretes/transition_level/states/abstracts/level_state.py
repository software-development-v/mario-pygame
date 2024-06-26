from abc import ABC, abstractmethod
from pygame import Surface
from typing import Callable
from src.data import GameData
from src.level import ILevelManager

class LevelState(ABC):


    def __init__(self, level_manager: ILevelManager, game_data : GameData, change_state:Callable[["LevelState"], None]) -> None:
        self.level_manager = level_manager
        self.game_data = game_data
        self.change_state = change_state

    @abstractmethod
    def render(self, screen: Surface) -> None:
        pass

