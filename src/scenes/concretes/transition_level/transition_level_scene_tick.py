from typing import Callable, Dict

from pygame import time

from src.enums import GameEvent, SceneAction
from src.level import ILevelManager
from src.utils.constants import TRANSITION_DURATION

from ...abstractions import Tick
from ..level import LevelScene


class TransitionLevelSceneTick(Tick):
    def __init__(
        self,
        level_manager: ILevelManager,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ) -> None:
        self.__start_time = time.get_ticks()
        self.__level_manager = level_manager
        super().__init__(dispatcher)

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
    ) -> None:
        pass
        current_time = time.get_ticks()

        if (
            game_events[GameEvent.PAUSE]
            or current_time - self.__start_time >= TRANSITION_DURATION
        ):
            self._dispatcher[SceneAction.SET_NEXT_SCENE](
                LevelScene(self.__level_manager, self._dispatcher)
            )
            self._dispatcher[SceneAction.END]()
