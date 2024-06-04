from abc import ABC, abstractmethod
from typing import Callable, Dict

from src.enums import GameEvent, SceneAction


class IScene(ABC):
    @abstractmethod
    def display(
        self,
        game_events: Dict[GameEvent, bool],
        set_next_scene: Callable[["IScene"], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        pass

    @abstractmethod
    def _set_frame_rate(self, frame_rate: float):
        pass
