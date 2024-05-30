from typing import List

from pygame import Surface, time

from src.utils.classes import Position
from src.utils.constants import ANIMATION_INTERVAL, INIT_IMAGE_INDEX

from ..interfaces import IEntity


class Element(IEntity):
    def __init__(
        self,
        position: Position,
        images: List[Surface],
        is_touchable: bool = True,
    ) -> None:
        self.position = position
        self.images: List[Surface] = images
        self.current_image_index = INIT_IMAGE_INDEX
        self.last_update = time.get_ticks()
        self.animation_interval = ANIMATION_INTERVAL
        self.is_touchable = is_touchable

    def draw(self, screen: Surface) -> None:
        element_surface = self.images[self.current_image_index]
        screen.blit(element_surface, self.position.to_tuple())

    def update(self) -> None:
        current_time = time.get_ticks()

        if current_time - self.last_update > self.animation_interval:
            self.last_update = current_time
            self.current_image_index = ++self.current_image_index % len(
                self.images
            )
