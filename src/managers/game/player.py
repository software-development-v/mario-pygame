from typing import List
import pygame
from src.entities.interfaces.i_entity import IEntity

class Player(IEntity):
    def __init__(self, x: int, y: int, images: List[pygame.Surface]) -> None:
        self.x = x
        self.y = y
        self.images = images
        self.current_image_index = 0

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.images[self.current_image_index], (self.x, self.y))

    def update(self) -> None:
        if self.direction == "right": # type: ignore
            self.current_image_index = 1
        elif self.direction == "left": # type: ignore
            self.current_image_index = 0


    def move_right(self) -> None:
        self.x += 5 

    def move_left(self) -> None:
        self.x -= 5 
