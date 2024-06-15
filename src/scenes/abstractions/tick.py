from abc import ABC, abstractmethod
from typing import Callable, Dict

from src.enums import GameEvent, SceneAction


class Tick(ABC):
    def __init__(self, dispatcher: Dict[SceneAction, Callable[..., None]]):
        self._dispatcher: Dict[SceneAction, Callable[..., None]] = dispatcher

    @abstractmethod
    def tick(
        self,
        game_events: Dict[GameEvent, bool],
    ) -> None:
        pass
