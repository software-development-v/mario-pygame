
from typing import Tuple
from pygame import Surface
from src.data.background.i_background import IBackground
from src.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH


class BackgroundColor(IBackground):
    def __init__(self , color: Tuple[int, int, int]) -> None:
        self.color = color
        self.surface = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))


    def get_background(self) -> Surface:
        self.surface.fill(self.color)
        return self.surface
