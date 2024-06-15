from ...abstractions import InteractScene
from .mode_selection_render import ModeSelectionSceneRender
from .mode_selection_tick import ModeSelectionSceneTick


class ModeSelectionScene(InteractScene):
    def __init__(self):
        render = ModeSelectionSceneRender()
        tick = ModeSelectionSceneTick(render)
        super().__init__(render, tick)
