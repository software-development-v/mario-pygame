from src.managers import GameManager
from src.utils.assets import FINAL_CINEMATIC_AUDIO, FINAL_CINEMATIC_VIDEO

from ...abstractions import CinematicScene


class FinalCinematicScene(CinematicScene):
    def __init__(self, game_manager: GameManager):
        super().__init__(
            game_manager, FINAL_CINEMATIC_VIDEO, FINAL_CINEMATIC_AUDIO
        )
