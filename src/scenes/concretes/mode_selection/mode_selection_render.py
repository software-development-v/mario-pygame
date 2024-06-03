from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message

from ...interfaces import IRender, ISceneManager


class ModeSelectionSceneRender(IRender):
    def render(self, scene_manager: ISceneManager) -> None:
        screen = scene_manager.get_screen()

        screen.fill(WHITE_COLOR)
        text, text_rect = get_centered_message(
            "         Super Piton Bros\nPress X or Space to play the game"
        )
        screen.blit(text, text_rect)
