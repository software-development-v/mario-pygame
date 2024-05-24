from src.scene_abstraction.interact.interact_scene import InteractScene
from src.scene_abstraction.scene import Scene
from src.scenes.mode_selection.render import ModeSelectionSceneRender
from src.scenes.mode_selection.tick import ModeSelectionSceneTick
from src.state.game_state import GameState


class ModeSelectionScene(InteractScene):
    def __init__(
        self,
        game_state: GameState,
        next_window: Scene,
    ):
        super().__init__(
            game_state,
            ModeSelectionSceneRender(),
            ModeSelectionSceneTick(),
            next_window,
        )
