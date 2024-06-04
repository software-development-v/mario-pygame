from typing import Callable, Dict

from src.enums import SceneAction
from src.level import ILevelManager
from src.utils.colors import WHITE_COLOR
from src.utils.text import get_centered_message, get_format_number, get_message

from ...interfaces import IRender, IScene


class LevelSceneRender(IRender):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.level_manager = level_manager
        super().__init__()

    def render(
        self,
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        background = self.level_manager.get_background()
        current_time = self.level_manager.get_current_time()

        self._screen.blit(background, (0, 0))

        format_time = get_format_number(current_time)
        time_message = f"TIME\n {format_time}"
        time, time_rect = get_message(
            time_message, 1400, 70, text_color=WHITE_COLOR, size=30
        )
        self._screen.blit(time, time_rect)

        message = "Playing: Press X or Space to finish"
        text, text_rect = get_centered_message(message)
        self._screen.blit(text, text_rect)

        self.level_manager.get_hero().draw(self._screen)
        for manager in self.level_manager.get_managers():
            manager.draw(self._screen)
