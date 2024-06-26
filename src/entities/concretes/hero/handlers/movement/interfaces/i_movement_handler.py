from abc import ABC, abstractmethod
from typing import Dict, Tuple

from pygame import Rect

from src.enums import GameEvent
from src.utils import Camera


class IMovementHandler(ABC):
    @abstractmethod
    def handle_hero_movements(
        self,
        hero_rect: Rect,
        game_events: Dict[GameEvent, bool],
        camera: Camera,
    ) -> Tuple[float, float]:
        pass
