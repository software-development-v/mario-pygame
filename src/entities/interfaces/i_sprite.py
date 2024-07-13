from abc import ABC, abstractmethod
from typing import Optional

from pygame import Rect

from src.utils import Position

from .i_animate import IAnimate
from .i_drawable import IDrawable


class ISprite(IDrawable, IAnimate, ABC):
    @abstractmethod
    def get_rect(self) -> Rect:
        pass

    @abstractmethod
    def set_index(self, index: int) -> None:
        pass

    @abstractmethod
    def add_x_rect(self, x: float) -> None:
        pass

    @abstractmethod
    def add_y_rect(self, y: float) -> None:
        pass

    @abstractmethod
    def get_face_right(self) -> bool:
        pass

    @abstractmethod
    def set_face_right(self, face_right: bool) -> None:
        pass

    @abstractmethod
    def get_check_point(self) -> Optional[Position]:
        pass

    @abstractmethod
    def get_reach_check_point(self) -> bool:
        pass

    @abstractmethod
    def set_reach_check_point(self, value: bool) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def dispose(self) -> None:
        pass

    @abstractmethod
    def is_disposed(self) -> bool:
        pass

    @abstractmethod
    def get_value(self) -> int:
        pass

    @abstractmethod
    def set_value(self, value: int) -> None:
        pass

    @abstractmethod
    def is_visible(self) -> bool:
        pass

    @abstractmethod
    def remove_observer(self):
        pass
