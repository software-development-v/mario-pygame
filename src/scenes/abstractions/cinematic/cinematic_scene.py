from abc import ABC
from typing import Optional

import cv2 as cv
from pygame import mixer

from ...interfaces import IScene
from ..scene import Scene
from .cinematic_scene_render import CinematicSceneRender


class CinematicScene(Scene, ABC):
    def __init__(
        self,
        video_path: str,
        audio_path: str,
        next_scene: Optional[IScene] = None,
    ):
        capture = cv.VideoCapture(video_path)
        frame_rate = capture.get(cv.CAP_PROP_FPS)
        success, image = capture.read()

        self._set_frame_rate(frame_rate)
        self.__audio = mixer.Sound(audio_path)
        self.__audio.play()

        super().__init__(
            CinematicSceneRender(
                capture, success, image, self.__audio, next_scene
            ),
        )
