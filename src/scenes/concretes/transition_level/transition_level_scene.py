from src.data import GameData
from src.entities import Hero
from src.enums import HeroType, Level, World
from src.level import ILevelManager, LevelManager, ObstacleManager

from ...abstractions import InteractScene
from .transition_level_scene_render import TransitionLevelSceneRender
from .transition_level_scene_tick import TransitionLevelSceneTick


class TransitionLevelScene(InteractScene):
    def __init__(
        self,
        hero: HeroType,
        world: World,
        level: Level,
    ) -> None:
        self.__level_manager: ILevelManager = self.setup_level(
            hero, world, level
        )

        super().__init__(
            TransitionLevelSceneRender(self.__level_manager),
            TransitionLevelSceneTick(self.__level_manager),
        )

    def setup_level(
        self,
        hero: HeroType,
        world: World,
        level: Level,
    ) -> ILevelManager:
        game_data = GameData()

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
        )
