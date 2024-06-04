from pygame import time

from src.level import ILevelManager

from ...abstractions import InteractScene
from .level_scene_render import LevelSceneRender
from .level_scene_tick import LevelSceneTick


class LevelScene(InteractScene):
    def __init__(
        self,
        level_manager: ILevelManager,
    ):
        level_manager.set_start_tick(time.get_ticks())

        super().__init__(
            LevelSceneRender(level_manager),
            LevelSceneTick(level_manager),
        )
