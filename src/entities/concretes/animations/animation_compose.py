from typing import List

from pygame import Surface

from src.utils import Camera
from ...abstractions.animation import Animation


class AnimationCompose(Animation):
    def __init__(self, animations: List[Animation]):
        super().__init__([Surface((0,0))])
        self.__animations = animations
        self.__animation_index = 0
        self.__total_animations = len(animations)


    def draw(self, screen: Surface, camera: Camera | None = None, x_rect_percent: float = 1, y_rect_percent: float = 1) -> None:
        if self.__animation_index < self.__total_animations:
            self.__animations[self.__animation_index].draw(screen, camera, x_rect_percent, y_rect_percent)

    def animate(self) -> None:
        if self.__animation_index >= self.__total_animations:
            self.dispose()
            return

        self.__animations[self.__animation_index].animate()

        if self.__animations[self.__animation_index].is_disposed():
            self.__animation_index += 1


