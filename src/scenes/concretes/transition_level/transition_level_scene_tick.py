from typing import Callable, Dict

from pygame import time

from src.enums import GameEvent, SceneAction
from src.level import ILevelManager
from src.level.concretes.entity_observers.score_observer import ScoreObserver
from src.scenes.concretes.final_cinematic.final_cinematic_scene import (
    FinalCinematicScene,
)
from src.utils import TRANSITION_DURATION

from ...abstractions import Tick
from ..level import LevelScene


class TransitionLevelSceneTick(Tick):
    def __init__(
        self,
        level_manager: ILevelManager,
        dispatcher: Dict[SceneAction, Callable[..., None]],
        score_manager: ScoreObserver,
    ) -> None:
        self.__start_time = time.get_ticks()
        self.__level_manager = level_manager
        self.___score_manager = score_manager
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
            if self.__level_manager.get_lives() != 0:
                self._dispatcher[SceneAction.SET_NEXT_SCENE](
                    LevelScene(self.__level_manager, self._dispatcher)
                )
            else:
                self.___score_manager.update_high_score()
                self._dispatcher[SceneAction.SET_NEXT_SCENE](
                    FinalCinematicScene(self._dispatcher)
                )

            self._dispatcher[SceneAction.END]()
