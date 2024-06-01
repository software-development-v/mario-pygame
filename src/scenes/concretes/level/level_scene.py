from typing import Optional

from pygame import time

from src.entities import Hero
from src.enums import HeroType, Level, World
from src.managers import GameManager, LevelManager, ObstacleManager

from ...abstractions import InteractScene, Scene
from .level_scene_render import LevelSceneRender
from .level_scene_tick import LevelSceneTick


class LevelScene(InteractScene):
    def __init__(
        self,
        game_manager: GameManager,
        world: World,
        level: Level,
        hero: HeroType,
        next_scene: Optional["Scene"] = None,
    ):
        self.level_manager: LevelManager
        self.setup_level(game_manager, hero, world, level)
        super().__init__(
            game_manager,
            LevelSceneRender(self.level_manager),
            LevelSceneTick(self.level_manager),
            next_scene,
        )

    def setup_level(
        self,
        game_manager: GameManager,
        hero: HeroType,
        world: World,
        level: Level,
    ) -> None:
        level_data = game_manager.game_data.get_level_data(world, level)

        self.level_manager = LevelManager(
            Hero(
                game_manager.game_data.get_hero_data(hero),
                level_data.player_start_position,
            ),
            [ObstacleManager(level_data.elements)],
            world,
            level,
            level_data.get_background(),
            level_data.time,
            time.get_ticks(),
        )
