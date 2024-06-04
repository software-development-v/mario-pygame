from typing import Callable, Dict

from pygame import time

from src.enums import GameEvent, SceneAction
from src.level import ILevelManager
from src.utils.constants import TRANSITION_DURATION

from ...interfaces import IScene, ITick
from ..level import LevelScene


class TransitionLevelSceneTick(ITick):
    def __init__(self, level_manager: ILevelManager) -> None:
        self.__start_time = time.get_ticks()
        self.__level_manager = level_manager

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
        set_next_scene: Callable[[IScene], None],
        dispatcher: Dict[SceneAction, Callable[[], None]],
    ) -> None:
        pass
        current_time = time.get_ticks()
        if current_time - self.__start_time >= TRANSITION_DURATION:
            set_next_scene(LevelScene(self.__level_manager))
            dispatcher[SceneAction.END]()
