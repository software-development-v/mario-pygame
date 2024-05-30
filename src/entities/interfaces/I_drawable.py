from abc import ABC, abstractmethod

from pygame import Surface


class IDrawable(ABC):

    @abstractmethod
    def draw(self, screen: Surface) -> None:
        pass
