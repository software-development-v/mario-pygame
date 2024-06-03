from typing import Optional

from src.inputs import IEventManager

from ...abstractions import Scene
from ...interfaces import IScene, ISceneManager
from .mode_selection_render import ModeSelectionSceneRender
from .mode_selection_tick import ModeSelectionSceneTick


class ModeSelectionScene(Scene):
    def __init__(
        self,
        scene_manager: ISceneManager,
        events_manager: IEventManager,
        next_scene: Optional[IScene] = None,
    ):
        super().__init__(
            scene_manager,
            events_manager,
            ModeSelectionSceneRender(),
            ModeSelectionSceneTick(),
            next_scene,
        )
