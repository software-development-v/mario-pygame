from abc import ABC
from typing import Optional

import cv2 as cv
from pygame import mixer

from src.inputs import IEventManager

from ...interfaces import IScene, ISceneManager
from ..scene import Scene
from .cinematic_scene_render import CinematicSceneRender
from .cinematic_scene_tick import CinematicSceneTick


class CinematicScene(Scene, ABC):
    def __init__(
        self,
        scene_manager: ISceneManager,
        events_manager: IEventManager,
        video_path: str,
        audio_path: str,
        next_scene: Optional[IScene] = None,
    ):
        capture = cv.VideoCapture(video_path)

        frame_rate = capture.get(cv.CAP_PROP_FPS)

        success, image = capture.read()
        self.__audio = mixer.Sound(audio_path)

        super().__init__(
            scene_manager,
            events_manager,
            CinematicSceneRender(capture, success, image, self.__audio),
            CinematicSceneTick(frame_rate, self.__audio),
            next_scene,
        )
