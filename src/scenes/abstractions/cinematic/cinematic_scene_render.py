from typing import Callable

from cv2 import VideoCapture, resize
from cv2.typing import MatLike
from pygame import image

from src.utils import BGR_FORMAT, SCREEN_SIZE, VIDEO_SCREEN_POSITION

from ..render import Render


class CinematicSceneRender(Render):
    def __init__(
        self,
        capture: VideoCapture,
        set_success: Callable[[bool], None],
        image: MatLike,
    ) -> None:
        self.__capture = capture
        self.__set_success = set_success
        self.__image = image
        super().__init__()

    def render(self) -> None:
        resized_img = resize(self.__image, SCREEN_SIZE)

        self._screen.blit(
            image.frombuffer(resized_img.tobytes(), SCREEN_SIZE, BGR_FORMAT),
            VIDEO_SCREEN_POSITION,
        )

        success, self.__image = self.__capture.read()
        self.__set_success(success)
