from abc import ABC, abstractmethod
from typing import Optional
from pygame import Surface

from src.utils import Camera


class IDrawable(ABC):

    @abstractmethod
    def draw(self, screen: Surface, camera: Optional[Camera]) -> None:
        pass
