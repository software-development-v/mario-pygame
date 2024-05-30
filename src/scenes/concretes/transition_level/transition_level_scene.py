from typing import Optional

from src.enums import HeroType, Level, World
from src.managers import GameManager

from ...abstractions import Scene
from ..level import LevelScene
from .transition_level_scene_render import TransitionLevelSceneRender


class TransitionLevelScene(Scene):
    def __init__(
        self,
        game_manager: GameManager,
        world: World,
        level: Level,
        hero: HeroType,
        next_scene: Optional["Scene"],
    ) -> None:
        super().__init__(
            game_manager,
            TransitionLevelSceneRender(world, level),
            LevelScene(game_manager, world, level, hero, next_scene),
        )
