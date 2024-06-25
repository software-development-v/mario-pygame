from src.level import ILevelManager
from src.utils import BLACK_COLOR, WHITE_COLOR, get_centered_message

from ...abstractions import Render


class TransitionLevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.__level_manager = level_manager
        super().__init__()

    def render(self) -> None:
        world = self.__level_manager.get_world()
        level = self.__level_manager.get_level()

        text, text_rect = get_centered_message(
            f"Enter to {world} - {level}",
            text_color=WHITE_COLOR,
        )

        self._screen.fill(BLACK_COLOR)
        self._screen.blit(text, text_rect)
