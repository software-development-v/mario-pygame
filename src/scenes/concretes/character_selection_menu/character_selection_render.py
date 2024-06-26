from typing import List, Tuple

from pygame import Rect, Surface, display, font

from src.enums import HeroType
from src.utils import (
    CHARACTER_SELECTION_MENU,
    GAME_FONT,
    ORANGE_COLOR,
    WHITE_COLOR,
)

from ...abstractions import Render


class CharacterSelectionRender(Render):
    def __init__(self) -> None:
        super().__init__()
        self.character_options: List[str] = [
            HeroType.CUMPA.value,
            HeroType.HIJITA.value,
            HeroType.PARIENTE.value,
        ]
        self.selected_character: int = 0

        screen_width: int = self._screen.get_width()
        screen_height: int = self._screen.get_height()

        self.background_image: Surface = CHARACTER_SELECTION_MENU

        self.character_positions: List[Tuple[int, int]] = [
            (
                screen_width // 5 + 20,
                screen_height // 2 + 100,
            ),
            (screen_width // 2, screen_height // 2 + 100),
            (
                5 * screen_width // 6 - 60,
                screen_height // 2 + 100,
            ),
        ]

        self.character_fonts: List[font.Font] = [
            font.Font(GAME_FONT, 30),
            font.Font(GAME_FONT, 30),
            font.Font(GAME_FONT, 30),
        ]

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
