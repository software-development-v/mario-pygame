from typing import Tuple

from pygame import Surface
from src.data.background.background import IBackground
from src.data.background.background_type import BackgroundType
from src.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT


class BackgroundColor(IBackground):

    def __init__(self,background_color: Tuple[int, int, int]) -> None:
        super().__init__(BackgroundType.BACKGROUND_COLOR)
        self.color = background_color

    def get_background(self) -> Surface:
        surface = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        surface.fill(self.color)
        return surface
