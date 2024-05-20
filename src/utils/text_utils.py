from pygame import Rect, Surface, font

from src.utils.constants import BLACK_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH


def get_centered_message(
    message: str,
    width: int = SCREEN_WIDTH // 2,
    height: int = SCREEN_HEIGHT // 2,
    size: int = 30,
) -> tuple[Surface, Rect]:
    pygame_font = font.Font(None, size)
    text = pygame_font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)

    return text, text_rect
