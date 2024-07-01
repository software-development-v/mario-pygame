from typing import Dict, Optional

from src.enums import GameEvent, HeroAction

from ....interfaces import IHero
from ..hero_actions import (
    HeroActionIdle,
    HeroActionJump,
    HeroActionRun,
    HeroActionWin,
    IHeroActionStrategy,
)
from ..interfaces import IActionsHandler


class ActionsHandler(IActionsHandler):
    def __init__(self, hero: IHero):
        self.__hero = hero

    def handle_hero_actions(self, game_events: Dict[GameEvent, bool]):
        hero_actions = self.__hero.get_actions()
        hero_action_strategy: Optional[IHeroActionStrategy] = None

        if (
            game_events[GameEvent.UP]
            and not hero_actions[HeroAction.JUMPING]
            and not hero_actions[HeroAction.WIN]
        ):
            hero_action_strategy = HeroActionJump()
        elif (
            (game_events[GameEvent.LEFT] or game_events[GameEvent.RIGHT])
            and not hero_actions[HeroAction.JUMPING]
            and not hero_actions[HeroAction.RUNNING]
            and not hero_actions[HeroAction.WIN]
        ):
            hero_action_strategy = HeroActionRun()
        elif (
            hero_actions[HeroAction.WIN]
        ):
            hero_action_strategy = HeroActionWin()
        elif (
            not hero_actions[HeroAction.JUMPING]
            and not hero_actions[HeroAction.RUNNING]
            and not hero_actions[HeroAction.WIN]
        ):
            hero_action_strategy = HeroActionIdle()

        if hero_action_strategy is not None:
            hero_action_strategy.execute(self.__hero)
