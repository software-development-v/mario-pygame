from abc import ABC, abstractmethod

from .i_drawable import IDrawable


class IEntity(IDrawable, ABC):

    @abstractmethod
    def update(self) -> None:
        pass
