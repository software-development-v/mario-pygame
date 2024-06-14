from typing import Callable, Dict

from src.data import GameData
from src.entities import Hero
from src.entities.abstractions.interactive_element import InteractiveElement
from src.enums import HeroType, Level, SceneAction, World
from src.enums.collected_type import CollectedType
from src.level import ILevelManager, LevelManager, ObstacleManager, ScoreObserver

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
    ) -> None:
        self.__level_manager: ILevelManager = self.setup_level(
            hero, world, level
        )

        super().__init__(
            TransitionLevelSceneRender(self.__level_manager),
            TransitionLevelSceneTick(self.__level_manager, dispatcher),
            dispatcher,
        )

    def setup_level(
        self,
        hero: HeroType,
        world: World,
        level: Level,
    ) -> ILevelManager:
        game_data = GameData()

        level_data = game_data.get_level_data(world, level)
        score_manager = ScoreObserver()

        for element in level_data.get_elements():
            if isinstance(element, InteractiveElement):
                element.add_observer(CollectedType.COLLECTED_SCORE,score_manager)

        return LevelManager(
            Hero(
                game_data.get_hero_data(hero),
                level_data.get_player_init_position(),
            ),
            ObstacleManager(level_data.get_elements()),
            world,
            level,
            level_data.get_background(),
            level_data.get_time(),
            score_manager
        )
