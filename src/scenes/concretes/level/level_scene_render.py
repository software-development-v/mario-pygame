from src.level import ILevelManager
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message, get_format_number, get_message

from ...interfaces import IRender, ISceneManager


class LevelSceneRender(IRender):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.level_manager = level_manager

    def render(self, scene_manager: ISceneManager) -> None:
        screen = scene_manager.get_screen()
        background = self.level_manager.get_background()
        current_time = self.level_manager.get_current_time()

        screen.blit(background, (0, 0))

        format_time = get_format_number(current_time)
        time_message = f"TIME\n {format_time}"
        time, time_rect = get_message(
            time_message, 1400, 70, text_color=WHITE_COLOR, size=30
        )
        screen.blit(time, time_rect)

        message = "Playing: Press X or Space to finish"
        text, text_rect = get_centered_message(message)
        screen.blit(text, text_rect)

        self.level_manager.get_hero().draw(screen)
        for manager in self.level_manager.get_managers():
            manager.draw(screen)
