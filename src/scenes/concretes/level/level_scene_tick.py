from typing import Callable, Dict

from pygame import Rect, time

from src.enums import GameEvent, HeroAction, HeroState, SceneAction
from src.level import AnimationManager, ILevelManager
from src.utils import TIME_POINTS, TO_SECONDS, update_score

from ...abstractions import Tick
from ..victory_cinematic.victory_cinematic import VictoryCinematic


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
        self.__finish_time: int = -1

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

        enemies_manager = self.__level_manager.get_enemy_manager()
        enemies_manager.animate()

        auxiliar_game_events = game_events

        if (
            self.__level_manager.is_win()
            or self.__level_manager.get_hero().get_actions()[HeroAction.DEAD]
        ):
            auxiliar_game_events = {
                GameEvent.UP: False,
                GameEvent.DOWN: False,
                GameEvent.LEFT: False,
                GameEvent.RIGHT: False,
                GameEvent.JUMP: False,
                GameEvent.RUN: False,
                GameEvent.PAUSE: False,
                GameEvent.ATTACK: False,
            }

        hero.update(
            auxiliar_game_events, obstacles_manager.get_sprites(), camera
        )
        hero.animate()

        hero_rect: Rect = hero.get_rect()
        camera.update(hero_rect.x, hero_rect.width)

        enemies_manager.update(camera, obstacles_manager.getElements())
        self.__animation_manager.reset()

        if enemies_manager.if_there_a_collide_with_enemy(hero):
            hero.set_index(0)
            hero.set_hero_state(HeroState.DEAD)
            hero.set_action(HeroAction.DEAD, True)

        self.__animation_manager.animate()

        if (
            self.__level_manager.is_win()
            and self.__level_manager.get_current_time() > 0
        ):
            if self.__finish_time == -1:
                self.__finish_time = self.__level_manager.get_current_time()

            current_time = self.__level_manager.get_current_time() - 1
            score = self.__level_manager.get_score() + TIME_POINTS
            self.__level_manager.set_current_time(current_time)
            self.__level_manager.set_score(score)

        if self.__level_manager.get_current_time() <= 0:
            hero.set_action(HeroAction.DEAD, True)

        if (
            (hero.get_hero_state() == HeroState.DEAD)
            and hero.get_rect().y > 900
        ) and not self.__level_manager.is_win():

            self.__level_manager.set_lives(self.__level_manager.get_lives() - 1)
            enemies_manager.reset_enemies()

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
        elif (
            self.__level_manager.is_win()
            and (hero.get_rect().x >= 12480 and hero.get_rect().y >= 660)
            and self.__level_manager.get_current_time() == 0
        ):
            print("WIN")
            self.__victory_manager()
        elif (
            hero.get_hero_state() == HeroState.DOWN
            and hero.get_actions()[HeroAction.WIN]
        ):
            self.__level_manager.win()

    def __victory_manager(self) -> None:
        self._dispatcher[SceneAction.SET_NEXT_SCENE](
            VictoryCinematic(
                self._dispatcher, self.__finish_time, self.__level_manager
            )
        )

        update_score(self.__level_manager.get_score())

        self._dispatcher[SceneAction.END]()
