from typing import Dict, Optional

from pygame import display, time

from src.enums import GameEvent, SceneAction
from src.utils import FPS, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE

from .concretes import MainMenuScene
from .interfaces import IScene, ISceneManager


class SceneManager(ISceneManager):
    def __init__(self) -> None:
        display.set_caption(TITLE)
        display.set_icon(ICON)
        display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.__frame_rate: float = FPS
        self.__clock = time.Clock()
        self.__current_scene: IScene = self.get_initial_scene()
        self.__next_scene: Optional[IScene] = None
        self.__is_paused: bool = False

    def get_initial_scene(self) -> IScene:
        return MainMenuScene(
            {
                SceneAction.PAUSE: self.pause_scene,
                SceneAction.CONTINUE: self.continue_scene,
                SceneAction.END: self.end_scene,
                SceneAction.SET_NEXT_SCENE: self.set_next_scene,
                SceneAction.SET_FRAME_RATE: self.set_frame_rate,
            }
        )

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

    def set_frame_rate(self, frame_rate: float) -> None:
        self.__frame_rate = frame_rate

    def display_current_scene(self, game_events: Dict[GameEvent, bool]) -> None:
        if self.__is_paused:
            return

        self.__current_scene.display()
        self.__current_scene.tick(game_events)

        self.__clock.tick(self.__frame_rate)
