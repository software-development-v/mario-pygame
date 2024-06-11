from typing import Callable, Dict

from src.enums import SceneAction
from src.level import ILevelManager
from src.utils.colors import BLACK_COLOR, WHITE_COLOR
from src.utils.text import get_centered_message

from ...interfaces import IRender, IScene


class TransitionLevelSceneRender(IRender):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.__level_manager = level_manager
        super().__init__()

    def render(
        self,
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        world = self.__level_manager.get_world()
        level = self.__level_manager.get_level()

        text, text_rect = get_centered_message(
            f"Enter to {world} - {level}",
            text_color=WHITE_COLOR,
        )

        self._screen.fill(BLACK_COLOR)
        self._screen.blit(text, text_rect)
