import cv2 as cv
from pygame import image

from src.enums import GameState
from src.managers import GameManager
from src.utils.constants import (
    BGR_FORMAT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    VIDEO_SCREEN_POSITION,
)

from ...interfaces import IRender


class CinematicSceneRender(IRender):
    def __init__(self, video_path: str, audio_path: str) -> None:
        super().__init__()
        self.audio_path = audio_path
        self.cap = cv.VideoCapture(video_path)

    def render(self, game_manager: GameManager) -> None:
        scene_size = (SCREEN_WIDTH, SCREEN_HEIGHT)

        frame_rate = self.cap.get(cv.CAP_PROP_FPS)
        success = self.cap.read()

        audio = game_manager.mixer.Sound(self.audio_path)
        audio.play()

        while success:
            game_manager.check_close_event()
            success, img = self.cap.read()

            if not success:
                break

            resized_img = cv.resize(img, scene_size)

            game_manager.screen.blit(
                image.frombuffer(resized_img.tobytes(), scene_size, BGR_FORMAT),
                VIDEO_SCREEN_POSITION,
            )
            game_manager.display.update()
            game_manager.clock.tick(frame_rate)

        audio.stop()
        game_manager.game_state = GameState.NEXT_SCENE
