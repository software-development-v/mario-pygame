from typing import List, Tuple
import pygame
from src.utils.colors import ORANGE_COLOR, WHITE_COLOR
from src.utils.assets.fonts import GAME_FONT
from src.utils.assets.backgrounds.menu import MENU_BACKGROUND

from ...abstractions import Render


class MainMenuRender(Render):
    def __init__(self) -> None:
        super().__init__()
        self.menu_options: List[str] = ["Start Game", "Quit"]
        self.selected_option: int = 0

        screen_width: int = self._screen.get_width()
        screen_height: int = self._screen.get_height()

        self.background_image: pygame.Surface = MENU_BACKGROUND

        self.option_positions: List[Tuple[int, int]] = [
            (screen_width // 2, (screen_height // 2) - 65),
            (200, 140),
        ]

        self.option_fonts: List[pygame.font.Font] = [
            pygame.font.Font(GAME_FONT, 70),
            pygame.font.Font(GAME_FONT, 40),
        ]

    def render(self) -> None:
        self._screen.blit(self.background_image, (0, 0))
        for index, option in enumerate(self.menu_options):
            font = self.option_fonts[index]
            color = (
                ORANGE_COLOR if self.selected_option == index else WHITE_COLOR
            )
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=self.option_positions[index])
            self._screen.blit(text, text_rect)
        pygame.display.flip()

    def get_selected_option(self) -> int:
        return self.selected_option

    def set_selected_option(self, option: int):
        self.selected_option = option % len(self.menu_options)

    def get_option_rects(self) -> List[pygame.Rect]:
        option_rects: List[pygame.Rect] = []
        for index, position in enumerate(self.option_positions):
            font = self.option_fonts[index]
            text = font.render(self.menu_options[index], True, (0, 0, 0))
            text_rect = text.get_rect(center=position)
            option_rects.append(text_rect)
        return option_rects

    def handle_mouse_event(self, mouse_pos: Tuple[int, int]) -> bool:
        for index, rect in enumerate(self.get_option_rects()):
            if rect.collidepoint(mouse_pos):
                self.selected_option = index
                return True
        return False
