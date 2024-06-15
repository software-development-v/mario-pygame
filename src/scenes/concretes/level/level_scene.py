from typing import Callable, Dict

from pygame import time

from src.enums import SceneAction
from src.level import ILevelManager

from ...abstractions import Scene
from .level_scene_render import LevelSceneRender
from .level_scene_tick import LevelSceneTick


class LevelScene(Scene):
    def __init__(
        self,
        level_manager: ILevelManager,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ):
        level_manager.set_start_tick(time.get_ticks())

        super().__init__(
            LevelSceneRender(level_manager),
            LevelSceneTick(level_manager, dispatcher),
            dispatcher,
        )
