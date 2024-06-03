from typing import Optional

from src.inputs import IEventManager
from src.utils.assets import FINAL_CINEMATIC_AUDIO, FINAL_CINEMATIC_VIDEO

from ...abstractions import CinematicScene
from ...interfaces import IScene, ISceneManager


class FinalCinematicScene(CinematicScene):
    def __init__(
        self,
        scene_manager: ISceneManager,
        events_manager: IEventManager,
        next_scene: Optional[IScene] = None,
    ):
        super().__init__(
            scene_manager,
            events_manager,
            FINAL_CINEMATIC_VIDEO,
            FINAL_CINEMATIC_AUDIO,
            next_scene,
        )
