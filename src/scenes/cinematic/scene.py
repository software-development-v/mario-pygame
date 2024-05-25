from src.scenes.scene import Scene
from src.scenes.cinematic.render import CinematicSceneRender
from src.state.game_state import GameState


class CinematicScene(Scene):
    def __init__(
        self,
        game_state: GameState,
        video_path: str,
        audio_path: str
    ):
        super().__init__(
            game_state,
            CinematicSceneRender(video_path, audio_path),
        )
