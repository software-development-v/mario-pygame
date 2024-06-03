from pygame import Clock, Surface, display, time

from src.data import IGameData
from src.enums import HeroType, Level, World
from src.inputs import IEventManager
from src.utils.assets import ICON
from src.utils.constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE

from .concretes import (
    FinalCinematicScene,
    ModeSelectionScene,
    TransitionLevelScene,
)
from .interfaces import IScene, ISceneManager


class SceneManager(ISceneManager):
    def __init__(
        self, events_manager: IEventManager, game_data: IGameData
    ) -> None:
        self.__events_manager: IEventManager = events_manager
        self.__game_data: IGameData = game_data
        self.__current_scene: IScene = self.reset_scene()

        display.set_caption(TITLE)
        display.set_icon(ICON)
        self.__screen: Surface = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.__frame_rate: float = FPS
        self.__clock: Clock = time.Clock()

    def reset_scene(self) -> IScene:
        return ModeSelectionScene(
            self,
            self.__events_manager,
            TransitionLevelScene(
                self,
                self.__events_manager,
                self.__game_data,
                HeroType.CUMPA,
                World.ONE,
                Level.FIRST,
                FinalCinematicScene(
                    self,
                    self.__events_manager,
                ),
            ),
        )

    def next_scene(self) -> None:
        next_scene = self.__current_scene.next_scene()

        if next_scene is None:
            self.__current_scene = self.reset_scene()
        else:
            self.__current_scene = next_scene

        self.__events_manager.reset_events()
        self.reset_frame_rate()

    def set_next_scene(self, scene: IScene) -> None:
        scene.set_next_scene(self.__current_scene)

        self.__current_scene = scene
        self.__events_manager.reset_events()
        self.reset_frame_rate()

    def display_current_scene(self) -> None:
        self.__current_scene.display()
        display.update()
        self.__clock.tick(self.__frame_rate)

    def get_screen(self) -> Surface:
        return self.__screen

    def set_frame_rate(self, frame_rate: float) -> None:
        self.__frame_rate = frame_rate

    def reset_frame_rate(self) -> None:
        self.__frame_rate = FPS
