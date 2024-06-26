from collections.abc import Callable
from pygame import Surface

from .game_over_state import GameOverState
from .level_status_state import LevelStatusState
from ..abstracts import LevelState
from src.level import ILevelManager
from src.data import GameData
from src.utils import get_centered_message


class TimeoutState(LevelState):

    def __init__(
        self,
        level_manager: ILevelManager,
        game_data: GameData,
        change_state: Callable[["LevelState"], None],
    ) -> None:
        super().__init__(level_manager, game_data, change_state)
        self.time = 50

    def render(self, screen: Surface) -> None:
        self.time -= 1
        message, message_rect = get_centered_message("TIME OUT")
        screen.blit(message, (message_rect.x, message_rect.y))
        if self.time <= 0:
            self.level_manager.set_current_time(
                self.level_manager.get_start_time()
            )

            if self.level_manager.get_lives() == 0:
                self.change_state(
                    GameOverState(
                        self.level_manager, self.game_data, self.change_state
                    )
                )
            else:
                self.change_state(
                    LevelStatusState(
                        self.level_manager, self.game_data, self.change_state
                    )
                )
