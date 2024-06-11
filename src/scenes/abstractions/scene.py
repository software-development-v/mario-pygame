from abc import ABC
from typing import Callable, Dict

from pygame import Clock, display, time

from src.enums import GameEvent, SceneAction
from src.utils.constants import FPS

from ..interfaces import IRender, IScene


class Scene(IScene, ABC):
    def __init__(
        self,
        scene_render: IRender,
    ) -> None:
        self.__scene_render = scene_render
        self.__frame_rate: float = FPS
        self.__clock: Clock = time.Clock()

    def display(
        self,
        game_events: Dict[GameEvent, bool],
        set_next_scene: Callable[["IScene"], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        self.__scene_render.render(set_next_scene, dispatcher)
        display.update()
        self.__clock.tick(self.__frame_rate)

    def _set_frame_rate(self, frame_rate: float):
        self.__frame_rate = frame_rate
