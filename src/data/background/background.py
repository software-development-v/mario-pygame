from abc import ABC , abstractmethod

from pygame import Surface
from src.data.background.background_type import BackgroundType



class IBackground (ABC):

    def __init__(self, background_type: BackgroundType) -> None:
        self.background_type = background_type

    @abstractmethod
    def get_background(self) -> Surface:
        pass
