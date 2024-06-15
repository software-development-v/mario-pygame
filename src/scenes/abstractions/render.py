from abc import ABC, abstractmethod

from pygame import Surface, display


class Render(ABC):
    def __init__(self):
        self._screen: Surface = display.get_surface()

    @abstractmethod
    def render(self) -> None:
        pass
