from typing import Callable, Dict

from pygame import time

from src.entities import InteractiveElement, Coin
from src.enums import SceneAction, CollectedType
from src.level import ILevelManager
from src.level import ScoreObserver, CoinObserver, AnimationManager
from ...abstractions import Scene
from .level_scene_render import LevelSceneRender
from .level_scene_tick import LevelSceneTick


class LevelScene(Scene):
    def __init__(
        self,
        level_manager: ILevelManager,
        dispatcher: Dict[SceneAction, Callable[..., None]],
    ):
        self.__animation_manager = AnimationManager()
        level_manager.set_start_tick(time.get_ticks())
        self.__configure_observers(level_manager)

        super().__init__(
            LevelSceneRender(level_manager, self.__animation_manager),
            LevelSceneTick(level_manager, dispatcher, self.__animation_manager),
            dispatcher,
        )

    def __configure_observers(self, level_manager: ILevelManager) -> None:
        score_observer = ScoreObserver(level_manager)
        coin_observer = CoinObserver(level_manager)

        for element in level_manager.get_obstacles_manager().get_sprites():
            if isinstance(element, InteractiveElement):
                element.add_observer(
                    CollectedType.COLLECTED_SCORE, score_observer
                )
                element.add_animation_oberver(self.__animation_manager)
                if isinstance(element, Coin):
                    element.add_observer(
                        CollectedType.COLLECTED_COIN, coin_observer
                    )
