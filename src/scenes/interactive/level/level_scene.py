from src.data.level_data import LevelData
from src.scenes.interactive.interact_scene import InteractScene
from src.scenes.interactive.level.render import  LevelSceneRender
from src.scenes.interactive.level.tick import LevelSceneTick
from src.state.game_state import GameState


class LevelScene(InteractScene):
    def __init__(
        self,
        game_state: GameState,
        data:LevelData
    ):
        super().__init__(
            game_state,
            LevelSceneRender(data),
            LevelSceneTick()
        )
