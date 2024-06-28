from typing import Callable, Dict, Optional

from src.data import GameData
from src.entities import Coin, Hero, InteractiveElement
from src.enums import CollectedType, HeroType, Level, SceneAction, World
from src.level import (
    CoinObserver,
    ILevelManager,
    LevelManager,
    ObstaclesManager,
    ScoreObserver,
)
from src.utils import (
    SCREEN_CAMERA_THRESHOLD,
    SCREEN_HEIGHT,
    SCREEN_VIEW_PLAY_HEIGHT,
    SCREEN_VIEW_PLAY_WIDTH,
    Camera,
)

from ...abstractions import Scene
from .transition_level_scene_render import TransitionLevelSceneRender
from .transition_level_scene_tick import TransitionLevelSceneTick


class TransitionLevelScene(Scene):
    def __init__(
        self,
        hero: HeroType,
        world: World,
        level: Level,
        dispatcher: Dict[SceneAction, Callable[..., None]],
        level_manager: Optional[ILevelManager] = None,
    ) -> None:
        self.__game_data = GameData()
        self.__score_manager = ScoreObserver()
        self.__coin_manager = CoinObserver()
        self.__level_manager: ILevelManager = self.setup_level(
            hero, world, level
        )

        if level_manager is not None:
            self.__level_manager.configure_level(
                level_manager.get_hero(),
                level_manager.get_hero_type(),
                level_manager.get_current_time(),
                level_manager.get_score(),
                level_manager.get_lives(),
                level_manager.get_coins(),
            )

        super().__init__(
            TransitionLevelSceneRender(self.__level_manager, self.__game_data),
            TransitionLevelSceneTick(
                self.__level_manager, dispatcher, self.__score_manager
            ),
            dispatcher,
        )

    def setup_level(
        self,
        hero: HeroType,
        world: World,
        level: Level,
    ) -> ILevelManager:

        level_data = self.__game_data.get_level_data(world, level)

        for element in level_data.get_elements():
            if isinstance(element, InteractiveElement):
                element.add_observer(
                    CollectedType.COLLECTED_SCORE, self.__score_manager
                )
                if isinstance(element, Coin):
                    element.add_observer(
                        CollectedType.COLLECTED_COIN, self.__coin_manager
                    )

        camera = Camera(
            level_data.get_screen_width(),
            SCREEN_HEIGHT,
            SCREEN_VIEW_PLAY_WIDTH,
            SCREEN_CAMERA_THRESHOLD,
            SCREEN_VIEW_PLAY_HEIGHT,
        )

        return LevelManager(
            Hero(
                self.__game_data.get_hero_data(hero),
                level_data.get_player_init_position(),
            ),
            hero,
            ObstaclesManager(level_data.get_elements()),
            world,
            level,
            level_data.get_background(),
            level_data.get_time(),
            level_data.get_screen_width(),
            self.__score_manager,
            self.__coin_manager,
            camera,
        )
