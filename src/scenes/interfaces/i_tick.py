from abc import ABC, abstractmethod
from typing import Callable, Dict

from src.enums import GameEvent, SceneAction

from .i_scene import IScene


class ITick(ABC):
    @abstractmethod
    def tick(
        self,
        game_events: Dict[GameEvent, bool],
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        pass
