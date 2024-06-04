from typing import Dict, Optional

from pygame import display

from src.enums import GameEvent, SceneAction
from src.utils.assets import ICON
from src.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH, TITLE

from .concretes import ModeSelectionScene
from .interfaces import IScene, ISceneManager


class SceneManager(ISceneManager):
    def __init__(self) -> None:
        display.set_caption(TITLE)
        display.set_icon(ICON)
        display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.__current_scene: IScene = self.get_initial_scene()
        self.__next_scene: Optional[IScene] = None
        self.__is_paused: bool = False

    def get_initial_scene(self) -> IScene:
        return ModeSelectionScene()

    def set_next_scene(self, scene: IScene) -> None:
        self.__next_scene = scene

    def pause_scene(self) -> None:
        self.__is_paused = True

    def continue_scene(self) -> None:
        self.__is_paused = False

    def end_scene(self) -> None:
        if self.__next_scene is None:
            self.__current_scene = self.get_initial_scene()
            return

        self.__current_scene = self.__next_scene
        self.__next_scene = None

    def display_current_scene(self, game_events: Dict[GameEvent, bool]) -> None:
        if self.__is_paused:
            return

        self.__current_scene.display(
            game_events,
            self.set_next_scene,
            {
                SceneAction.PAUSE: self.pause_scene,
                SceneAction.CONTINUE: self.continue_scene,
                SceneAction.END: self.end_scene,
            },
        )
