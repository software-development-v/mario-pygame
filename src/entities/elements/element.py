from typing import List

import pygame


class Element:
    def __init__(
        self,
        x: int,
        y: int,
        width: int,
        height: int,
        images: List[str],
        is_touchable: bool = True,
    ) -> None:
        self.rect = pygame.Rect(x, y, width, height)
        self.images: List[pygame.Surface] = [
            pygame.image.load(img) for img in images
        ]
        self.current_image_index = 0
        self.last_update = pygame.time.get_ticks()
        self.animation_interval = 100
        self.is_touchable = is_touchable

    def set_images(self, images: List[str]) -> None:
        self.images = [pygame.image.load(img) for img in images]

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.images[self.current_image_index], self.rect)

    def update(self) -> None:
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_interval:
            self.last_update = now
            self.current_image_index = (self.current_image_index + 1) % len(
                self.images
            )
