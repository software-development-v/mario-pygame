from ...abstractions import InteractScene
from .mode_selection_render import ModeSelectionSceneRender
from .mode_selection_tick import ModeSelectionSceneTick


class ModeSelectionScene(InteractScene):
    def __init__(
        self,
    ):
        super().__init__(
            ModeSelectionSceneRender(),
            ModeSelectionSceneTick(),
        )
