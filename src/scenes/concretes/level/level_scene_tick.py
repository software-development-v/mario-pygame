from pygame import time

from src.enums import GameEvent, GameState
from src.managers import GameManager, LevelManager
from src.utils.constants import INIT_GAME_THRESHOLD, TO_SECONDS

from ...interfaces import ITick


class LevelSceneTick(ITick):
    def __init__(self, level_manager: LevelManager) -> None:
        self.level_manager = level_manager
        super().__init__()

    def tick(self, game_manager: GameManager) -> None:
        seconds_elapsed = (
            time.get_ticks() - self.level_manager.start_tick
        ) // TO_SECONDS

        if seconds_elapsed >= INIT_GAME_THRESHOLD:
            self.level_manager.current_time = (
                self.level_manager.start_time
                - seconds_elapsed
                + INIT_GAME_THRESHOLD
            )

        if game_manager.game_events[GameEvent.JUMP]:
            game_manager.game_state = GameState.NEXT_SCENE

        self.level_manager.hero.update(game_manager.game_events)
        for manager in self.level_manager.managers:
            manager.update()
