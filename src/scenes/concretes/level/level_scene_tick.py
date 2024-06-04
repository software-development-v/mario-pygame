from typing import Callable, Dict

from pygame import time

from src.enums import GameEvent, SceneAction
from src.level import ILevelManager
from src.utils.constants import TO_SECONDS

from ...interfaces import IScene, ITick
from ..final_cinematic import FinalCinematicScene


class LevelSceneTick(ITick):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.level_manager = level_manager

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        start_tick = self.level_manager.get_start_tick()
        start_time = self.level_manager.get_start_time()

        seconds_elapsed = (time.get_ticks() - start_tick) // TO_SECONDS

        self.level_manager.set_current_time(start_time - seconds_elapsed)

        if game_events[GameEvent.JUMP]:
            set_next_scene(FinalCinematicScene())
            dispatcher[SceneAction.END]()

        self.level_manager.get_hero().update(game_events)
        for manager in self.level_manager.get_managers():
            manager.update()
