from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message

from ...abstractions import Render


class ModeSelectionSceneRender(Render):
    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        self._screen.fill(WHITE_COLOR)
        text, text_rect = get_centered_message(
            "         Super Piton Bros\nPress X or Space to play the game"
        )
        self._screen.blit(text, text_rect)
