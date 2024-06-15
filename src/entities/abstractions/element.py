from typing import List

from pygame import Rect, Surface, time

from src.enums.element_type import ElementType
from src.utils.camera import Camera
from src.utils.classes import Position
from src.utils.constants import ANIMATION_INTERVAL, INIT_IMAGE_INDEX

from ..interfaces import IEntity


class Element(IEntity):
    def __init__(
        self,
        position: Position,
        images: List[Surface],
        is_touchable: bool = True,
        type_element: ElementType = ElementType.BLOCK
    ) -> None:
        self.position = position
        self.surfaces: List[Surface] = images
        self.current_image_index = INIT_IMAGE_INDEX
        self.last_update = time.get_ticks()
        self.animation_interval = ANIMATION_INTERVAL
        self.is_touchable = is_touchable
        self.image = self.surfaces[self.current_image_index]
        self.rect = self.image.get_rect()
        self.rect.x = position.x
        self.rect.y = position.y
        self.type_element = type_element

    def get_rect(self) -> Rect:
        return self.rect

    def draw(self, screen: Surface, camera: Camera) -> None:
        screen.blit(self.image, camera.apply(self.rect))

    def update(self) -> None:
        current_time = time.get_ticks()

        if current_time - self.last_update > self.animation_interval:
            self.last_update = current_time
            self.current_image_index = ++self.current_image_index % len(
                self.surfaces
            )
