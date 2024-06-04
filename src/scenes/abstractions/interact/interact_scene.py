from abc import ABC
from typing import Callable, Dict

from src.enums import GameEvent, SceneAction

from ...interfaces import IRender, IScene, ITick
from ..scene import Scene


class InteractScene(Scene, ABC):
    def __init__(self, scene_render: IRender, tick_handler: ITick):
        self.__tick_handler = tick_handler
        super().__init__(scene_render)

    def display(
        self,
        game_events: Dict[GameEvent, bool],
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        self.__tick_handler.tick(game_events, set_next_scene, dispatcher)
        super().display(game_events, set_next_scene, dispatcher)
