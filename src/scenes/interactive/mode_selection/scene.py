from src.scenes.interactive.interact_scene import InteractScene
from src.scenes.interactive.mode_selection.render import (
    ModeSelectionSceneRender,
)
from src.scenes.interactive.mode_selection.tick import ModeSelectionSceneTick
from src.state.game_state import GameState


class ModeSelectionScene(InteractScene):
    def __init__(
        self,
        game_state: GameState,
    ):
        super().__init__(
            game_state,
            ModeSelectionSceneRender(),
            ModeSelectionSceneTick()
        )
