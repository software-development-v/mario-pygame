from typing import Tuple

from pygame import Surface

from src.utils import SCREEN_HEIGHT, SCREEN_WIDTH

from ..interfaces import IBackground


class BackgroundColor(IBackground):
    def __init__(self, color: Tuple[int, int, int]) -> None:
        self.color = color
        self.surface = Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def get_background(self) -> Surface:
        self.surface.fill(self.color)
        return self.surface
