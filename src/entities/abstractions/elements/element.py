from typing import List

from pygame import Rect, Surface, image, time

from src.utils.classes import Position, Size
from src.utils.constants import ANIMATION_INTERVAL, INIT_IMAGE_INDEX

from ...interfaces import IEntity


class Element(IEntity):
    def __init__(
        self,
        position: Position,
        size: Size,
        images: List[str],
        is_touchable: bool = True,
    ) -> None:
        self.rect = Rect(position.x, position.y, size.width, size.height)
        self.images: List[Surface] = [image.load(img) for img in images]
        self.current_image_index = INIT_IMAGE_INDEX
        self.last_update = time.get_ticks()
        self.animation_interval = ANIMATION_INTERVAL
        self.is_touchable = is_touchable

    def draw(self, screen: Surface) -> None:
        screen.blit(self.images[self.current_image_index], self.rect)

    def update(self) -> None:
        current_time = time.get_ticks()

        if current_time - self.last_update > self.animation_interval:
            self.last_update = current_time
            self.current_image_index = ++self.current_image_index % len(
                self.images
            )
