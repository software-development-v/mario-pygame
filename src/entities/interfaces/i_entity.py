from abc import ABC, abstractmethod

from pygame import Rect

from .i_drawable import IDrawable
from .i_updatable import IUpdatable


class IEntity(IDrawable, IUpdatable, ABC):
    @abstractmethod
    def get_rect(self) -> Rect:
        pass
