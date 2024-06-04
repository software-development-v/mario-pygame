from typing import Callable, Dict, Optional

import cv2 as cv
from cv2.typing import MatLike
from pygame import image
from pygame.mixer import Sound

from src.enums import SceneAction
from src.utils.constants import BGR_FORMAT, SCREEN_SIZE, VIDEO_SCREEN_POSITION

from ...interfaces import IRender, IScene


class CinematicSceneRender(IRender):
    def __init__(
        self,
        capture: cv.VideoCapture,
        success: bool,
        image: MatLike,
        audio: Sound,
        next_scene: Optional[IScene] = None,
    ) -> None:
        self.__capture = capture
        self.__success = success
        self.__image = image
        self.__audio = audio
        self.__next_scene = next_scene
        super().__init__()

    def render(
        self,
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        if not self.__success:
            self.__audio.stop()
            if self.__next_scene is not None:
                set_next_scene(self.__next_scene)
            dispatcher[SceneAction.END]()
            return

        resized_img = cv.resize(self.__image, SCREEN_SIZE)
        self._screen.blit(
            image.frombuffer(resized_img.tobytes(), SCREEN_SIZE, BGR_FORMAT),
            VIDEO_SCREEN_POSITION,
        )

        self.__success, self.__image = self.__capture.read()
