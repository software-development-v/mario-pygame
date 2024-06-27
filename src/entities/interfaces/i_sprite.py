from abc import ABC, abstractmethod

from pygame import Rect

from .i_animate import IAnimate
from .i_drawable import IDrawable


class ISprite(IDrawable, IAnimate, ABC):
    @abstractmethod
    def get_rect(self) -> Rect:
        pass

    @abstractmethod
    def add_x_rect(self, x: float) -> None:
        pass

    @abstractmethod
    def add_y_rect(self, y: float) -> None:
        pass

    @abstractmethod
    def set_face_right(self, face_right: bool) -> None:
        pass
