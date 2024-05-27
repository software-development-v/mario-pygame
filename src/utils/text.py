from typing import Tuple

from pygame import Rect, Surface, font

from .colors import BLACK_COLOR
from .constants import FONT_SIZE, HALF, SCREEN_HEIGHT, SCREEN_WIDTH


def get_centered_message(
    message: str,
    width: int = SCREEN_WIDTH // HALF,
    height: int = SCREEN_HEIGHT // HALF,
    size: int = FONT_SIZE,
    text_color: Tuple[int, int, int] = BLACK_COLOR,
) -> tuple[Surface, Rect]:
    pygame_font = font.Font(None, size)
    text = pygame_font.render(message, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)

    return text, text_rect
