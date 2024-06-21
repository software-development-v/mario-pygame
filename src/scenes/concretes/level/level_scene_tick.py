from typing import Callable, Dict
from pygame import time
from src.enums import GameEvent, HeroState, SceneAction
from src.level import ILevelManager
from src.utils.constants import TO_SECONDS
from ...abstractions import Tick
from ..final_cinematic import FinalCinematicScene

class LevelSceneTick(Tick):
    def __init__(
        self,
        level_manager: ILevelManager,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ) -> None:
        self.level_manager = level_manager
        super().__init__(dispatcher)

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
    ) -> None:
        start_tick = self.level_manager.get_start_tick()
        start_time = self.level_manager.get_start_time()

        seconds_elapsed = (time.get_ticks() - start_tick) // TO_SECONDS

        self.level_manager.set_current_time(start_time - seconds_elapsed)

        obstacle_manager = self.level_manager.get_obstacle_manager()
        hero = self.level_manager.get_hero()
        camera = self.level_manager.get_camera()

        obstacle_manager.update()

        hero.update(game_events, obstacle_manager.get_obstacles(), camera)

        if hero.hero_state == HeroState.DEAD:
            self._dispatcher[SceneAction.SET_NEXT_SCENE](
                FinalCinematicScene(self._dispatcher)
            )
            self._dispatcher[SceneAction.END]()
