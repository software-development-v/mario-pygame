from abc import ABC
from typing import Callable, Dict, Optional

from cv2 import CAP_PROP_FPS, VideoCapture
from pygame import mixer

from src.enums import SceneAction

from ...interfaces import IScene
from ..scene import Scene
from .cinematic_scene_render import CinematicSceneRender
from .cinematic_scene_tick import CinematicSceneTick


class CinematicScene(Scene, ABC):
    def __init__(
        self,
        video_path: str,
        audio_path: str,
        dispatcher: Dict[SceneAction, Callable[..., None]],
        next_scene: Optional[IScene] = None,
    ):
        capture = VideoCapture(video_path)
        frame_rate = capture.get(CAP_PROP_FPS)

        self.__success, image = capture.read()
        self.__audio = mixer.Sound(audio_path)
        self.__audio.play()

        super().__init__(
            CinematicSceneRender(
                capture,
                self.set_success,
                image,
            ),
            CinematicSceneTick(
                self.get_success,
                self.__audio,
                dispatcher,
                next_scene,
            ),
            dispatcher,
            frame_rate,
        )

    def set_success(self, success: bool) -> None:
        self.__success = success

    def get_success(self) -> bool:
        return self.__success
