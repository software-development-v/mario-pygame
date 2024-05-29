from abc import ABC, abstractmethod

from pygame import Surface


class IBackground(ABC):

    @abstractmethod
    def get_background(self) -> Surface:
        pass
