from typing import Tuple

from pygame import Rect, Surface, font

from .assets import GAME_FONT
from .colors import BLACK_COLOR
from .constants import FONT_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH


def get_centered_message(
    message: str,
    width: int = SCREEN_WIDTH // 2,
    height: int = SCREEN_HEIGHT // 2,
    size: int = FONT_SIZE,
    text_color: Tuple[int, int, int] = BLACK_COLOR,
) -> tuple[Surface, Rect]:
    pygame_font = font.Font(GAME_FONT, size)
    text = pygame_font.render(message, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)

    return text, text_rect


def get_message(
    message: str,
    width: int,
    height: int,
    size: int = FONT_SIZE,
    text_color: Tuple[int, int, int] = BLACK_COLOR,
) -> tuple[Surface, Rect]:
    pygame_font = font.Font(GAME_FONT, size)
    text = pygame_font.render(message, True, text_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)

    return text, text_rect


def get_format_number(number: int, width: int) -> str:
    return f"{number:0{width}d}"
