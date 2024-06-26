# En un archivo nuevo, por ejemplo, character_selection_render.py

from typing import List, Tuple

from pygame import Rect, Surface, display, font

from src.enums import HeroType
from src.utils import GAME_FONT, MENU_BACKGROUND, ORANGE_COLOR, WHITE_COLOR

from ...abstractions import Render


class CharacterSelectionRender(Render):
    def __init__(self) -> None:
        super().__init__()
        self.character_options: List[str] = [
            HeroType.PARIENTE.value,
            HeroType.HIJITA.value,
            HeroType.CUMPA.value,
        ]
        self.selected_character: int = 0

        screen_width: int = self._screen.get_width()
        screen_height: int = self._screen.get_height()

        self.background_image: Surface = MENU_BACKGROUND

        self.character_positions: List[Tuple[int, int]] = [
            (screen_width // 2, (screen_height // 2) - 75),
            (200, 140),
            (200, 200),
        ]

        self.character_fonts: List[font.Font] = [
            font.Font(GAME_FONT, 50),
            font.Font(GAME_FONT, 40),
            font.Font(GAME_FONT, 40),
        ]

        self.top_text_font: font.Font = font.Font(GAME_FONT, 20)
        self.top_text_position: Tuple[int, int] = (
            screen_width - 200,
            140,
        )
        self.top_score: int = 0

    def render(self) -> None:
        self._screen.blit(self.background_image, (0, 0))
        for index, character in enumerate(self.character_options):
            font = self.character_fonts[index]
            color = (
                ORANGE_COLOR
                if self.selected_character == index
                else WHITE_COLOR
            )
            text = font.render(character, True, color)
            text_rect = text.get_rect(center=self.character_positions[index])
            self._screen.blit(text, text_rect)

        top_text = f"Top: {self.top_score:06}"
        top_text_surface = self.top_text_font.render(
            top_text, True, WHITE_COLOR
        )
        top_text_rect = top_text_surface.get_rect(center=self.top_text_position)
        self._screen.blit(top_text_surface, top_text_rect)

        display.flip()

    def get_selected_character(self) -> int:
        return self.selected_character

    def set_selected_character(self, character: int):
        self.selected_character = character % len(self.character_options)

    def get_character_rects(self) -> List[Rect]:
        character_rects: List[Rect] = []
        for index, position in enumerate(self.character_positions):
            font = self.character_fonts[index]
            text = font.render(self.character_options[index], True, (0, 0, 0))
            text_rect = text.get_rect(center=position)
            character_rects.append(text_rect)
        return character_rects

    def handle_mouse_event(self, mouse_pos: Tuple[int, int]) -> bool:
        for index, rect in enumerate(self.get_character_rects()):
            if rect.collidepoint(mouse_pos):
                self.selected_character = index
                return True
        return False
