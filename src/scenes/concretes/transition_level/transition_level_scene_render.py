from src.level import ILevelManager
from src.utils.colors import BLACK_COLOR, WHITE_COLOR
from src.utils.text import get_centered_message

from ...interfaces import IRender, ISceneManager


class TransitionLevelSceneRender(IRender):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.__level_manager = level_manager

    def render(self, scene_manager: ISceneManager) -> None:
        screen = scene_manager.get_screen()
        world = self.__level_manager.get_world()
        level = self.__level_manager.get_level()

        text, text_rect = get_centered_message(
            f"Enter to {world} - {level}",
            text_color=WHITE_COLOR,
        )

        screen.fill(BLACK_COLOR)
        screen.blit(text, text_rect)
