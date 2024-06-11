from abc import ABC, abstractmethod
from typing import Dict

from src.enums import GameEvent


class IEventManager(ABC):
    @abstractmethod
    def reset_events(self) -> None:
        pass

    @abstractmethod
    def handle_events(self) -> None:
        pass

    @abstractmethod
    def get_events(self) -> Dict[GameEvent, bool]:
        pass
