from abc import ABC, abstractmethod
from typing import Dict, List

from pygame import Event

from src.enums import GameEvent


class IInputHandler(ABC):
    @abstractmethod
    def handle(self, events: List[Event], game_events: Dict[GameEvent, bool]):
        pass
