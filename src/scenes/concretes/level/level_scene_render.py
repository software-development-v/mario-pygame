from src.managers import GameManager, LevelManager
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message, get_format_number, get_message

from ...interfaces import IRender


class LevelSceneRender(IRender):
    def __init__(self, level_manager: LevelManager) -> None:
        self.level_manager = level_manager
        super().__init__()

    def render(self, game_manager: GameManager) -> None:
        game_manager.screen.blit(self.level_manager.background, (0, 0))

        format_time = get_format_number(self.level_manager.current_time)
        time_message = f"TIME\n {format_time}"

        time, time_rect = get_message(
            time_message, 1400, 70, text_color=WHITE_COLOR, size=30
        )
        game_manager.screen.blit(time, time_rect)

        message = "Playing: Press X or Space to finish"
        text, text_rect = get_centered_message(message)
        game_manager.screen.blit(text, text_rect)

        self.level_manager.hero.draw(game_manager.screen)
        for manager in self.level_manager.managers:
            manager.draw(game_manager.screen)
