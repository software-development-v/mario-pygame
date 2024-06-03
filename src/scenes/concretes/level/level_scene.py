from typing import Optional

from src.inputs import IEventManager
from src.level import ILevelManager

from ...abstractions import Scene
from ...interfaces import IScene, ISceneManager
from .level_scene_render import LevelSceneRender
from .level_scene_tick import LevelSceneTick


class LevelScene(Scene):
    def __init__(
        self,
        scene_manager: ISceneManager,
        events_manager: IEventManager,
        level_manager: ILevelManager,
        next_scene: Optional[IScene] = None,
    ):
        super().__init__(
            scene_manager,
            events_manager,
            LevelSceneRender(level_manager),
            LevelSceneTick(level_manager),
            next_scene,
        )
