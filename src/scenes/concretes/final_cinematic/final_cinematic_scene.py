from typing import Callable, Dict

from src.enums.scene_action import SceneAction
from src.utils import FINAL_CINEMATIC_AUDIO, FINAL_CINEMATIC_VIDEO

from ...abstractions import CinematicScene


class FinalCinematicScene(CinematicScene):
    def __init__(self, dispatcher: Dict[SceneAction, Callable[..., None]]):
        super().__init__(
            FINAL_CINEMATIC_VIDEO, FINAL_CINEMATIC_AUDIO, dispatcher
        )
