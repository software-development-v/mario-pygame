from abc import ABC, abstractmethod
from typing import Dict

from src.enums import GameEvent


class IScene(ABC):

    @abstractmethod
    def tick(self, game_events: Dict[GameEvent, bool]) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass
