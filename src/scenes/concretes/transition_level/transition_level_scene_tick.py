from pygame import time

from src.inputs import IEventManager
from src.utils.constants import TRANSITION_DURATION

from ...interfaces import ISceneManager, ITick


class TransitionLevelSceneTick(ITick):
    def __init__(self) -> None:
        self.start_time = time.get_ticks()

    def tick(self, events_manager: IEventManager, scene_manager: ISceneManager):
        current_time = time.get_ticks()
        if current_time - self.start_time >= TRANSITION_DURATION:
            scene_manager.next_scene()
