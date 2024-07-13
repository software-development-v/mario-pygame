from typing import Callable, Dict, Optional

from src.data import GameData
from src.entities import Hero
from src.enums import HeroType, Level, SceneAction, World
from src.level import (
    EnemyManager,
    ILevelManager,
    LevelManager,
    ObstaclesManager,
    PowerUpManager,
)
from src.utils import SCREEN_CAMERA_THRESHOLD, SCREEN_VIEWPORT_WIDTH, Camera

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

        if level_manager is not None:
            self.__level_manager = level_manager
            self.__level_manager.reset()
        else:
            self.__level_manager = self.setup_level(hero, world, level)

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

        camera = Camera(
            level_data.get_screen_width(),
            SCREEN_VIEWPORT_WIDTH,
            SCREEN_CAMERA_THRESHOLD,
        )

        return LevelManager(
            Hero(
                self.__game_data.get_hero_data(hero),
                level_data.get_player_init_position(),
                level_data.get_checkpoint(),
            ),
            hero,
            ObstaclesManager(level_data.get_elements()),
            EnemyManager(level_data.get_enemies()),
            PowerUpManager(level_data.get_power_ups()),
            world,
            level,
            level_data.get_background(),
            level_data.get_time(),
            level_data.get_screen_width(),
            camera,
        )
