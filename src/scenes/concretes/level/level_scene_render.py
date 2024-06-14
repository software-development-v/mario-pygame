from src.level import ILevelManager
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_format_number, get_message

from ...abstractions import Render


class LevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.level_manager = level_manager
        super().__init__()

    def render(self) -> None:
        background = self.level_manager.get_background()
        current_time = self.level_manager.get_current_time()

        self._screen.blit(background, (0, 0))

        format_time = get_format_number(current_time)
        time_message = f"TIME\n {format_time}"
        time, time_rect = get_message(
            time_message, 1400, 70, text_color=WHITE_COLOR, size=30
        )
        self._screen.blit(time, time_rect)

        obstacle_manager = self.level_manager.get_obstacle_manager()
        hero = self.level_manager.get_hero()

        obstacle_manager.draw(self._screen)
        hero.draw(self._screen)
