from abc import ABC, abstractmethod
from typing import Tuple

from src.enums import Direction


class IMovementHandler(ABC):
    @abstractmethod
    def move(self, direction: Direction) -> Tuple[float, float]:
        pass
