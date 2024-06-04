from typing import Callable, Dict

from src.enums import SceneAction
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message

from ...interfaces import IRender, IScene


class ModeSelectionSceneRender(IRender):
    def __init__(self) -> None:
        super().__init__()

    def render(
        self,
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        self._screen.fill(WHITE_COLOR)
        text, text_rect = get_centered_message(
            "         Super Piton Bros\nPress X or Space to play the game"
        )
        self._screen.blit(text, text_rect)
