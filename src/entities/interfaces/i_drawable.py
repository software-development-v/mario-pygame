from abc import ABC, abstractmethod

from pygame import Surface

from src.utils import Camera


class IDrawable(ABC):

    @abstractmethod
    def draw(self, screen: Surface, camera: Camera) -> None:
        pass
