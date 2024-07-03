from typing import Callable, Dict, Optional

from src.data import GameData
from src.entities import Coin, Hero, InteractiveElement
from src.enums import CollectedType, HeroType, Level, SceneAction, World
from src.level import (
    EnemyManager,
    ILevelManager,
    LevelManager,
    ObstaclesManager,
)
from src.utils import (
    SCREEN_CAMERA_THRESHOLD,
    SCREEN_HEIGHT,
    SCREEN_VIEW_PLAY_LEFT,
    SCREEN_VIEW_PLAY_LEFT_WITH_CHECKPOINT,
    SCREEN_VIEW_PLAY_RIGHT,
    Camera,
)
from src.utils.classes import CheckpointManager

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
        self.__level_manager: ILevelManager = self.setup_level(
            hero, world, level
        )

        if level_manager is not None:
            self.configure_next_level(level_manager)

        super().__init__(
            TransitionLevelSceneRender(self.__level_manager, self.__game_data),
            TransitionLevelSceneTick(self.__level_manager, dispatcher),
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

        if CheckpointManager.has_checkpoint():
            self.screen_view_left = SCREEN_VIEW_PLAY_LEFT_WITH_CHECKPOINT
        else:
            self.screen_view_left = SCREEN_VIEW_PLAY_LEFT

        camera = Camera(
            level_data.get_screen_width(),
            SCREEN_HEIGHT,
            SCREEN_VIEW_PLAY_RIGHT,
            SCREEN_CAMERA_THRESHOLD,
            self.screen_view_left,
        )

        return LevelManager(
            Hero(
                self.__game_data.get_hero_data(hero),
                level_data.get_player_init_position(),
            ),
            hero,
            ObstaclesManager(level_data.get_elements()),
            EnemyManager(level_data.get_enemies()),
            world,
            level,
            level_data.get_background(),
            level_data.get_time(),
            level_data.get_screen_width(),
            camera,
        )

    def configure_next_level(self, level_manager: ILevelManager) -> None:
        self.__level_manager.configure_level(
            level_manager.get_hero(),
            level_manager.get_hero_type(),
            level_manager.get_current_time(),
            level_manager.get_score(),
            level_manager.get_lives(),
            level_manager.get_coins(),
        )

    def get_level_manager(self) -> ILevelManager:
        return self.__level_manager
