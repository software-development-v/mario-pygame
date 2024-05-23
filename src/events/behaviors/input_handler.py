from abc import ABC, abstractmethod
from typing import Dict, List

from pygame.event import Event

from src.enums.custom_event import CustomEvent


class IInputHandler(ABC):
    @abstractmethod
    def handle(
        self, events: List[Event], game_events: Dict[CustomEvent, bool]
    ):
        pass
