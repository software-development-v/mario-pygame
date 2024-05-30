from typing import Optional

from src.entities import Hero
from src.enums import HeroType, Level, World
from src.managers import GameManager, ObstacleManager

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
        self.level = level
        self.world = world
        self.setup_level(game_manager, hero)
        super().__init__(
            game_manager,
            LevelSceneRender(world, level),
            LevelSceneTick(),
            next_scene,
        )

    def setup_level(self, game_manager: GameManager, hero: HeroType) -> None:
        level_data = game_manager.game_data.get_level_data(
            self.world, self.level
        )

        game_manager.hero = Hero(
            game_manager.game_data.get_hero_data(hero),
            level_data.player_start_position,
        )
        game_manager.managers = [ObstacleManager(level_data.elements)]
