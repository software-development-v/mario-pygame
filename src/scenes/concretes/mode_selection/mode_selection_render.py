from src.managers import GameManager
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message

from ...interfaces import IRender


class ModeSelectionSceneRender(IRender):
    def __init__(self) -> None:
        super().__init__()

    def render(self, game_manager: GameManager) -> None:
        game_manager.screen.fill(WHITE_COLOR)
        text, text_rect = get_centered_message(
            "     Super Mario Piton Bros\nPress X or Space to play the game"
        )
        game_manager.screen.blit(text, text_rect)
