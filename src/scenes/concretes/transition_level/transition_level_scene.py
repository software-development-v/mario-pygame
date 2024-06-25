from typing import Callable, Dict, Optional

from src.data import GameData
from src.entities import Hero, InteractiveElement
from src.enums import CollectedType, HeroType, Level, SceneAction, World
from src.level import (
    ILevelManager,
    LevelManager,
    ObstacleManager,
    ScoreObserver,
)
from src.utils import Camera
from src.utils.constants import (
    SCREEN_CAMERA_THRESHOLD,
    SCREEN_HEIGHT,
    SCREEN_VIEW_PLAY_HEIGHT,
    SCREEN_VIEW_PLAY_WIDTH,
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
        level_manager :Optional[ILevelManager] = None
    ) -> None:
        self.game_data = GameData()
        self.__level_manager: ILevelManager = self.setup_level(
                hero, world, level
        )
        if level_manager is not None:
            self.__level_manager.configure_level(
                level_manager.get_hero(),
                level_manager.get_hero_type(),
                level_manager.get_current_time(),
                level_manager.get_score(),
                level_manager.get_lifes(),0
            )



        super().__init__(
            TransitionLevelSceneRender(self.__level_manager,self.game_data),
            TransitionLevelSceneTick(self.__level_manager, dispatcher),
            dispatcher,
        )


    def setup_level(
        self,
        hero: HeroType,
        world: World,
        level: Level,
    ) -> ILevelManager:

        level_data = self.game_data.get_level_data(world, level)
        score_manager = ScoreObserver()

        for element in level_data.get_elements():
            if isinstance(element, InteractiveElement):
                element.add_observer(
                    CollectedType.COLLECTED_SCORE, score_manager
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
                self.game_data.get_hero_data(hero),
                level_data.get_player_init_position(),
            ),
            hero,
            ObstacleManager(level_data.get_elements()),
            world,
            level,
            level_data.get_background(),
            level_data.get_time(),
            level_data.get_screen_width(),
            score_manager,
            camera,
        )
