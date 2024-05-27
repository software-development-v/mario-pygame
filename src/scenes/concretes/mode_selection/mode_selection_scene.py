from src.managers import GameManager

from ...abstractions import InteractScene, Scene
from .mode_selection_render import ModeSelectionSceneRender
from .mode_selection_tick import ModeSelectionSceneTick


class ModeSelectionScene(InteractScene):
    def __init__(
        self,
        game_manager: GameManager,
        next_scene: Scene,
    ):
        super().__init__(
            game_manager,
            ModeSelectionSceneRender(),
            ModeSelectionSceneTick(),
            next_scene,
        )
