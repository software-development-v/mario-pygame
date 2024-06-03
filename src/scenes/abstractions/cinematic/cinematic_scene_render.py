import cv2 as cv
from cv2.typing import MatLike
from pygame import image
from pygame.mixer import Sound

from src.utils.constants import BGR_FORMAT, SCREEN_SIZE, VIDEO_SCREEN_POSITION

from ...interfaces import IRender, ISceneManager


class CinematicSceneRender(IRender):
    def __init__(
        self,
        capture: cv.VideoCapture,
        success: bool,
        image: MatLike,
        audio: Sound,
    ) -> None:
        self.__capture = capture
        self.__success = success
        self.__image = image
        self.__audio = audio

    def render(self, scene_manager: ISceneManager) -> None:
        if not self.__success:
            self.__audio.stop()
            scene_manager.next_scene()
            return

        screen = scene_manager.get_screen()

        resized_img = cv.resize(self.__image, SCREEN_SIZE)
        screen.blit(
            image.frombuffer(resized_img.tobytes(), SCREEN_SIZE, BGR_FORMAT),
            VIDEO_SCREEN_POSITION,
        )

        self.__success, self.__image = self.__capture.read()
