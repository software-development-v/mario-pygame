from abc import ABC
from typing import Callable, Dict

from pygame import display

from src.enums import GameEvent, SceneAction
from src.utils import FPS

from ..interfaces import IScene
from .render import Render
from .tick import Tick


class Scene(IScene, ABC):
    def __init__(
        self,
        scene_render: Render,
        scene_tick: Tick,
        dispatcher: Dict[SceneAction, Callable[..., None]],
        frame_rate: float = FPS,
    ) -> None:
        self.__scene_render: Render = scene_render
        self.__scene_tick: Tick = scene_tick
        dispatcher[SceneAction.SET_FRAME_RATE](frame_rate)

    def tick(self, game_events: Dict[GameEvent, bool]) -> None:
        self.__scene_tick.tick(game_events)

    def display(self) -> None:
        self.__scene_render.render()
        display.update()
