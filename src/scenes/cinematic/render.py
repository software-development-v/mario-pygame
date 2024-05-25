from sys import exit

import cv2 as cv
from pygame import QUIT, Surface, display, event, image, mixer, quit, time

from src.enums.state import State
from src.scenes.render import IRender
from src.state.game_state import GameState
from src.utils.constants import (
    BGR_FORMAT,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    VIDEO_SCREEN_POSITION,
)


class CinematicSceneRender(IRender):
    def __init__(self, video_path: str, audio_path: str) -> None:
        self.cap = cv.VideoCapture(video_path)
        self.frame_rate = self.cap.get(cv.CAP_PROP_FPS)
        self.success = self.cap.read()
        self.shape = (SCREEN_WIDTH, SCREEN_HEIGHT)

        self.clock = time.Clock()
        self.audio = mixer.Sound(audio_path)

    def render(self, game_state: GameState, screen: Surface) -> None:
        screen = display.set_mode(self.shape)

        self.audio.play(loops=-1)

        while self.success:
            for e in event.get():
                if e.type == QUIT:
                    quit()
                    exit()

            self.success, self.img = self.cap.read()

            if not self.success:
                break

            resized_img = cv.resize(self.img, self.shape)

            screen.blit(
                image.frombuffer(
                    resized_img.tobytes(), self.shape, BGR_FORMAT
                ),
                VIDEO_SCREEN_POSITION,
            )

            display.update()
            self.clock.tick(self.frame_rate)

        self.audio.stop()
        game_state.state = State.NEXT
