from pygame import time

from src.enums import GameEvent
from src.inputs import IEventManager
from src.level import ILevelManager
from src.utils.constants import INIT_GAME_THRESHOLD, TO_SECONDS

from ...interfaces import ISceneManager, ITick


class LevelSceneTick(ITick):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.level_manager = level_manager

    def tick(
        self, events_manager: IEventManager, scene_manager: ISceneManager
    ) -> None:
        start_tick = self.level_manager.get_start_tick()
        start_time = self.level_manager.get_start_time()

        seconds_elapsed = (time.get_ticks() - start_tick) // TO_SECONDS

        if seconds_elapsed >= INIT_GAME_THRESHOLD:
            self.level_manager.set_current_time(
                start_time - seconds_elapsed + INIT_GAME_THRESHOLD
            )

        events = events_manager.get_events()

        if events[GameEvent.JUMP]:
            scene_manager.next_scene()

        self.level_manager.get_hero().update(events)
        for manager in self.level_manager.get_managers():
            manager.update()
