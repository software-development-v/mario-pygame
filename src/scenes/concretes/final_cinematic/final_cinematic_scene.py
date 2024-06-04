from src.utils.assets import FINAL_CINEMATIC_AUDIO, FINAL_CINEMATIC_VIDEO

from ...abstractions import CinematicScene


class FinalCinematicScene(CinematicScene):
    def __init__(self):
        super().__init__(FINAL_CINEMATIC_VIDEO, FINAL_CINEMATIC_AUDIO)
