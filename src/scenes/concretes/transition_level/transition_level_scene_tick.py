from typing import Callable, Dict

from pygame import time

from src.enums import GameEvent, SceneAction
from src.level import ILevelManager
from src.utils import TRANSITION_DURATION

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

        current_time = time.get_ticks()

        if (
            game_events[GameEvent.PAUSE]
            or current_time - self.__start_time >= TRANSITION_DURATION
        ):
            if self.__level_manager.get_lifes() != 0:
                self._dispatcher[SceneAction.SET_NEXT_SCENE](
                    LevelScene(self.__level_manager, self._dispatcher)
                )


            self._dispatcher[SceneAction.END]()
