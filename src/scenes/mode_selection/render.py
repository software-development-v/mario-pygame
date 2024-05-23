from pygame import Surface

from src.scene_abstraction.behaviors.render import IRender
from src.state.game_state import GameState
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message


class ModeSelectionSceneRender(IRender):
    def __init__(self) -> None:
        return

    def render(self, game_state: GameState, screen: Surface) -> None:
        screen.fill(WHITE_COLOR)
        text, text_rect = get_centered_message(
            "Press X or Space to play the game"
        )
        screen.blit(text, text_rect)
