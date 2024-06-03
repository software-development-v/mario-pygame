from typing import Optional

from pygame import time

from src.data import IGameData
from src.entities import Hero
from src.enums import HeroType, Level, World
from src.inputs import IEventManager
from src.level import ILevelManager, LevelManager, ObstacleManager

from ...abstractions import Scene
from ...interfaces import IScene, ISceneManager
from ..level import LevelScene
from .transition_level_scene_render import TransitionLevelSceneRender
from .transition_level_scene_tick import TransitionLevelSceneTick


class TransitionLevelScene(Scene):
    def __init__(
        self,
        scene_manager: ISceneManager,
        events_manager: IEventManager,
        game_data: IGameData,
        hero: HeroType,
        world: World,
        level: Level,
        next_scene: Optional[IScene] = None,
    ) -> None:
        self.__level_manager: ILevelManager = self.setup_level(
            game_data, hero, world, level
        )

        super().__init__(
            scene_manager,
            events_manager,
            TransitionLevelSceneRender(self.__level_manager),
            TransitionLevelSceneTick(),
            LevelScene(
                scene_manager, events_manager, self.__level_manager, next_scene
            ),
        )

    def setup_level(
        self,
        game_data: IGameData,
        hero: HeroType,
        world: World,
        level: Level,
    ) -> ILevelManager:
        level_data = game_data.get_level_data(world, level)

        return LevelManager(
            Hero(
                game_data.get_hero_data(hero),
                level_data.get_player_init_position(),
            ),
            [ObstacleManager(level_data.get_elements())],
            world,
            level,
            level_data.get_background(),
            level_data.get_time(),
            time.get_ticks(),
        )
