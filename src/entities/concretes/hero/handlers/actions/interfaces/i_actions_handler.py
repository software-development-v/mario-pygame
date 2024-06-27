from abc import ABC, abstractmethod
from typing import Dict

from src.enums import GameEvent


class IActionsHandler(ABC):
    @abstractmethod
    def handle_hero_actions(self, game_events: Dict[GameEvent, bool]):
        pass
