from src.data import GameData
from src.level import ILevelManager
from src.utils import BLACK_COLOR

from ...abstractions import Render
from ..level import LevelMetricsRenderer
from .states import GameOverState, LevelState, LevelStatusState, TimeoutState


class TransitionLevelSceneRender(Render):
    def __init__(self, level_manager: ILevelManager, game: GameData) -> None:
        self.__level_manager = level_manager
        self.game = game

        super().__init__()

        self.level_metrics_renderer = LevelMetricsRenderer()
        self.state: LevelState = LevelStatusState(
            level_manager, game, self.change_state
        )
        self.state_initialized = False

    def render(self) -> None:
        self.ensure_state_initialized()
        self._screen.fill(BLACK_COLOR)

        self.level_metrics_renderer.render(
            self._screen,
            self.__level_manager.get_hero_type().value,
            -1,
            self.__level_manager.get_score(),
            self.__level_manager.get_coins(),
            self.__level_manager.get_world().value,
            self.__level_manager.get_level().value,
            True
        )

        self.state.render(self._screen)

    def change_state(self, state: LevelState) -> None:
        self.state = state

    def ensure_state_initialized(self) -> None:
        if self.state_initialized:
            return

        self.state_initialized = True
        if self.__level_manager.get_current_time() <= 0:
            self.state = TimeoutState(
                self.__level_manager, self.game, self.change_state
            )
        elif self.__level_manager.get_lives() == 0:
            self.state = GameOverState(
                self.__level_manager, self.game, self.change_state
            )
