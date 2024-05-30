from src.enums import Level, World
from src.managers import GameManager
from src.utils.text import get_centered_message

from ...interfaces import IRender


class LevelSceneRender(IRender):
    def __init__(self, world: World, level: Level) -> None:
        super().__init__()
        self.world = world
        self.level = level

    def render(self, game_manager: GameManager) -> None:
        level_data = game_manager.game_data.get_level_data(
            self.world, self.level
        )
        game_manager.screen.blit(level_data.get_background(), (0, 0))

        message = "Playing: Press X or Space to finish"
        text, text_rect = get_centered_message(message)
        game_manager.screen.blit(text, text_rect)

        if game_manager.hero:
            game_manager.hero.draw(game_manager.screen)

        if game_manager.elements_manager:
            game_manager.elements_manager.draw(game_manager.screen)
