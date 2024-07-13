from typing import Dict, Optional

from pygame import time

from src.enums import GameEvent, HeroAction, HeroLevel

from ....interfaces import IHero
from ..hero_actions import (
    HeroActionDead,
    HeroActionIdle,
    HeroActionRun,
    HeroActionWin,
    IHeroActionStrategy,
)
from ..interfaces import IActionsHandler


class ActionsHandler(IActionsHandler):
    def __init__(self, hero: IHero):
        self.__hero = hero
        self.__time_to_disappear: Optional[int] = None

    def handle_hero_actions(self, game_events: Dict[GameEvent, bool]):
        hero_actions = self.__hero.get_actions()
        hero_action_strategy: Optional[IHeroActionStrategy] = None

        if (
            self.__time_to_disappear is not None
            and time.get_ticks() > self.__time_to_disappear
        ):
            self.__time_to_disappear = None

        if (
            game_events[GameEvent.ATTACK]
            and self.__time_to_disappear is None
            and (
                self.__hero.get_hero_level() == HeroLevel.COCA
                or (
                    self.__hero.get_pre_level() is not None
                    and self.__hero.get_pre_level() == HeroLevel.COCA
                )
            )
        ):
            self.__hero.get_coca_ball_manager().create_ball(self.__hero)
            self.__time_to_disappear = time.get_ticks() + 500

        if (
            (game_events[GameEvent.LEFT] or game_events[GameEvent.RIGHT])
            and not hero_actions[HeroAction.JUMPING]
            and not hero_actions[HeroAction.RUNNING]
            and not hero_actions[HeroAction.WIN]
            and not hero_actions[HeroAction.DEAD]
        ):
            hero_action_strategy = HeroActionRun()
        elif hero_actions[HeroAction.WIN] and not hero_actions[HeroAction.DEAD]:
            hero_action_strategy = HeroActionWin()
        elif (
            not hero_actions[HeroAction.JUMPING]
            and not hero_actions[HeroAction.RUNNING]
            and not hero_actions[HeroAction.WIN]
            and not hero_actions[HeroAction.DEAD]
        ):
            hero_action_strategy = HeroActionIdle()
        elif hero_actions[HeroAction.DEAD]:
            hero_action_strategy = HeroActionDead()

        if hero_action_strategy is not None:
            hero_action_strategy.execute(self.__hero)
