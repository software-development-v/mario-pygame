from typing import Callable, Dict

from pygame import Rect, time

from src.enums import GameEvent, HeroState, SceneAction
from src.level import AnimationManager, ILevelManager
from src.utils import TO_SECONDS

from ...abstractions import Tick


class LevelSceneTick(Tick):
    def __init__(
        self,
        level_manager: ILevelManager,
        dispatcher: Dict[SceneAction, Callable[..., None]],
        animation_manager: AnimationManager,
    ) -> None:
        self.__level_manager = level_manager
        self.__animation_manager = animation_manager
        super().__init__(dispatcher)

    def tick(
        self,
        game_events: Dict[GameEvent, bool],
    ) -> None:
        start_tick = self.__level_manager.get_start_tick()
        start_time = self.__level_manager.get_start_time()

        seconds_elapsed = (time.get_ticks() - start_tick) // TO_SECONDS

        if not self.__level_manager.is_win():
            self.__level_manager.set_current_time(start_time - seconds_elapsed)

        hero = self.__level_manager.get_hero()
        camera = self.__level_manager.get_camera()

        obstacles_manager = self.__level_manager.get_obstacles_manager()
        obstacles_manager.animate()

        hero.update(game_events, obstacles_manager.get_sprites(), camera)
        hero.animate()

        hero_rect: Rect = hero.get_rect()
        camera.update(hero_rect.x, hero_rect.width)

        self.__animation_manager.animate()

        if (
            hero.get_hero_state() == HeroState.DEAD
            or self.__level_manager.get_current_time() <= 0
        ):

            self.__level_manager.set_lives(self.__level_manager.get_lives() - 1)
            from ..transition_level import TransitionLevelScene

            self._dispatcher[SceneAction.SET_NEXT_SCENE](
                TransitionLevelScene(
                    self.__level_manager.get_hero_type(),
                    self.__level_manager.get_world(),
                    self.__level_manager.get_level(),
                    self._dispatcher,
                    self.__level_manager,
                )
            )
            self._dispatcher[SceneAction.END]()
        elif hero.get_hero_state() == HeroState.DOWN:
            self.__level_manager.win()
