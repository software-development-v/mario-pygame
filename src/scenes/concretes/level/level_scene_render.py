from src.enums import Level, World
from src.managers import GameManager
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message

from ...interfaces import IRender


class LevelSceneRender(IRender):
    def __init__(self, world: World, level: Level) -> None:
        super().__init__()
        self.world = world
        self.level = level

    def render(self, game_manager: GameManager) -> None:
        game_manager.screen.fill(WHITE_COLOR)
        text, text_rect = get_centered_message(
            "Playing: Press X or Space to finish"
        )
        game_manager.screen.blit(text, text_rect)
