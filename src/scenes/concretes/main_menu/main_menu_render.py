from typing import List, Tuple

from pygame import Rect, Surface, display, font

from src.utils import GAME_FONT, MENU_BACKGROUND, ORANGE_COLOR, WHITE_COLOR

from ...abstractions import Render


class MainMenuRender(Render):
    def __init__(self) -> None:
        super().__init__()
        self.menu_options: List[str] = [
            "Start Game",
            "Quit",
        ]
        self.selected_option: int = 0

        screen_width: int = self._screen.get_width()
        screen_height: int = self._screen.get_height()

        self.background_image: Surface = MENU_BACKGROUND

        self.option_positions: List[Tuple[int, int]] = [
            (screen_width // 2, (screen_height // 2) - 75),
            (200, 140),
        ]

        self.option_fonts: List[font.Font] = [
            font.Font(GAME_FONT, 70),
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
        for index, option in enumerate(self.menu_options):
            font = self.option_fonts[index]
            color = (
                ORANGE_COLOR if self.selected_option == index else WHITE_COLOR
            )
            text = font.render(option, True, color)
            text_rect = text.get_rect(center=self.option_positions[index])
            self._screen.blit(text, text_rect)

        top_text = f"Top: {self.top_score:06}"
        top_text_surface = self.top_text_font.render(
            top_text, True, WHITE_COLOR
        )
        top_text_rect = top_text_surface.get_rect(center=self.top_text_position)
        self._screen.blit(top_text_surface, top_text_rect)

        display.flip()

    def get_selected_option(self) -> int:
        return self.selected_option

    def set_selected_option(self, option: int):
        self.selected_option = option % len(self.menu_options)

    def get_option_rects(self) -> List[Rect]:
        option_rects: List[Rect] = []
        for index, position in enumerate(self.option_positions):
            font = self.option_fonts[index]
            text = font.render(self.menu_options[index], True, (0, 0, 0))
            text_rect = text.get_rect(center=position)
            option_rects.append(text_rect)
        return option_rects
