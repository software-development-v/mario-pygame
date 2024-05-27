from typing import Optional

from src.enums import Level, World
from src.managers import GameManager

from ...abstractions import InteractScene, Scene
from .level_scene_render import LevelSceneRender
from .level_scene_tick import LevelSceneTick


class LevelScene(InteractScene):
    def __init__(
        self,
        game_manager: GameManager,
        world: World,
        level: Level,
        next_scene: Optional["Scene"] = None,
    ):
        super().__init__(
            game_manager,
            LevelSceneRender(world, level),
            LevelSceneTick(),
            next_scene,
        )

    def setup_level(self) -> None:
        pass
