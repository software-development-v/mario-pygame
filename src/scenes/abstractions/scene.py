from abc import ABC
from typing import Optional

from src.inputs import IEventManager

from ..interfaces import IRender, IScene, ISceneManager, ITick


class Scene(IScene, ABC):
    def __init__(
        self,
        scene_manager: ISceneManager,
        events_manager: IEventManager,
        scene_render: IRender,
        tick_handler: ITick,
        next_scene: Optional[IScene] = None,
    ) -> None:
        self.__scene_manager = scene_manager
        self.__events_manager = events_manager
        self.__tick_handler = tick_handler
        self.__scene_render = scene_render
        self.__next_scene = next_scene

    def next_scene(self) -> Optional[IScene]:
        return self.__next_scene

    def set_next_scene(self, scene: IScene) -> None:
        self.__next_scene = scene

    def display(self) -> None:
        self.__tick_handler.tick(self.__events_manager, self.__scene_manager)
        self.__scene_render.render(self.__scene_manager)
