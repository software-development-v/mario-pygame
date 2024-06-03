from pygame.mixer import Sound

from src.inputs import IEventManager

from ...interfaces import ISceneManager, ITick


class CinematicSceneTick(ITick):
    def __init__(
        self,
        frame_rate: float,
        audio: Sound,
    ) -> None:
        self.__frame_rate = frame_rate
        self.__audio = audio

    def tick(
        self, events_manager: IEventManager, scene_manager: ISceneManager
    ) -> None:
        if self.__audio.get_num_channels() == 0:
            scene_manager.set_frame_rate(self.__frame_rate)
            self.__audio.play()
