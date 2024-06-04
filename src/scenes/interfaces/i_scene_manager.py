from abc import ABC, abstractmethod
from typing import Dict

from src.enums import GameEvent

from .i_scene import IScene


class ISceneManager(ABC):
    @abstractmethod
    def get_initial_scene(self) -> IScene:
        pass

    @abstractmethod
    def set_next_scene(self, scene: IScene) -> None:
        pass

    @abstractmethod
    def pause_scene(self) -> None:
        pass

    @abstractmethod
    def continue_scene(self) -> None:
        pass

    @abstractmethod
    def end_scene(self) -> None:
        pass

    @abstractmethod
    def display_current_scene(self, game_events: Dict[GameEvent, bool]) -> None:
        pass
