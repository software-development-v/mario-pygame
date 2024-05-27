from typing import List

import pygame

from src.entities.i_entity import IEntity
from src.utils.position import Position
from src.utils.size import Size


class Element(IEntity):
    def __init__(
        self,
        position: Position,
        size: Size,
        images: List[str],
        is_touchable: bool = True,
    ) -> None:
        self.rect = pygame.Rect(
            position.x, position.y, size.width, size.height
        )
        self.images: List[pygame.Surface] = [
            pygame.image.load(img) for img in images
        ]
        self.current_image_index = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_interval = 100
        self.is_touchable = is_touchable

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.images[self.current_image_index], self.rect)

    def update(self) -> None:
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_interval:
            self.last_update = now
            self.current_image_index = (self.current_image_index + 1) % len(
                self.images
            )
