from typing import Callable, Dict, Text

from ....enums.scene_action import SceneAction
from ....utils import (
    VICTORY_CINEMATIC_NORMAL_VIDEO,
    VICTORY_CINEMATIC_ONE_FIREWORK_VIDEO,
    VICTORY_CINEMATIC_THREE_FIREWORKS_VIDEO,
    VICTORY_CINEMATIC_SIX_FIREWORKS_VIDEO,
    VICTORY_CINEMATIC_ONE_FIREWORK_AUDIO,
    VICTORY_CINEMATIC_THREE_FIREWORKS_AUDIO,
    VICTORY_CINEMATIC_SIX_FIREWORKS_AUDIO
)
from ...abstractions import CinematicScene


class VictoryCinematic(CinematicScene):
    def __init__(
        self,
        dispatcher: Dict[SceneAction, Callable[..., None]],
        current_time: int,
    ):
        self.__victory_video: Text = self.__define_video_path(current_time)
        self.__victory_audio: Text = self.__define_audio_path(current_time)
        super().__init__(self.__victory_video, self.__victory_audio, dispatcher)

    def __define_video_path(self, current_time: int) -> Text:
        video_path = VICTORY_CINEMATIC_NORMAL_VIDEO

        number = str(current_time)
        last_number = number[-1]

        if last_number == "1":
            video_path = VICTORY_CINEMATIC_ONE_FIREWORK_VIDEO
        elif last_number == "3":
            video_path = VICTORY_CINEMATIC_THREE_FIREWORKS_VIDEO
        elif last_number == "6":
            video_path = VICTORY_CINEMATIC_SIX_FIREWORKS_VIDEO

        return video_path

    def __define_audio_path(self, current_time: int) -> Text:
        audio_path = VICTORY_CINEMATIC_ONE_FIREWORK_AUDIO

        number = str(current_time)
        last_number = number[-1]

        if last_number == "1":
            audio_path = VICTORY_CINEMATIC_ONE_FIREWORK_AUDIO
        elif last_number == "3":
            audio_path = VICTORY_CINEMATIC_THREE_FIREWORKS_AUDIO
        elif last_number == "6":
            audio_path = VICTORY_CINEMATIC_SIX_FIREWORKS_AUDIO

        return audio_path
