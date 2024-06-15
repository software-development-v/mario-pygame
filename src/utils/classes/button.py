from typing import Tuple
import pygame
from src.utils.assets.elements.touchable import BUTTON


class Button:
    def __init__(
        self,
        text: str,
        font: pygame.font.Font,
        position: Tuple[int, int],
        selected_color: Tuple[int, int, int],
        normal_color: Tuple[int, int, int],
    ) -> None:
        self.text = text
        self.font = font
        self.position = position
        self.selected_color = selected_color
        self.normal_color = normal_color
        self.image = BUTTON
        self.text_surface = self.font.render(self.text, True, self.normal_color)
        self.rect = self.image.get_rect(center=self.position)
        self.update_image()

    def update_image(self):
        text_rect = self.text_surface.get_rect(center=self.rect.center)
        self.image = pygame.transform.scale(
            self.image, (text_rect.width + 30, text_rect.height + 20)
        )
        self.rect = self.image.get_rect(center=self.position)

    def render(self, screen: pygame.Surface, is_selected: bool) -> None:
        color = self.selected_color if is_selected else self.normal_color
        self.text_surface = self.font.render(self.text, True, color)
        screen.blit(self.image, self.rect)
        screen.blit(
            self.text_surface,
            self.text_surface.get_rect(center=self.rect.center),
        )

    def is_hovered(self, mouse_pos: Tuple[int, int]) -> bool:
        return self.rect.collidepoint(mouse_pos)
