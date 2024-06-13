from typing import Callable, Dict

from src.enums import SceneAction

from ...abstractions import Scene
from .mode_selection_render import ModeSelectionSceneRender
from .mode_selection_tick import ModeSelectionSceneTick


class ModeSelectionScene(Scene):
    def __init__(
        self,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ):
        super().__init__(
            ModeSelectionSceneRender(),
            ModeSelectionSceneTick(dispatcher),
            dispatcher,
        )
