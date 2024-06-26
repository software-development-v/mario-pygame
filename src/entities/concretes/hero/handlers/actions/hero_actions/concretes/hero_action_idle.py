from src.enums import HeroAction, HeroState

from .....interfaces import IHero
from ..interfaces import IHeroActionStrategy


class HeroActionIdle(IHeroActionStrategy):
    def execute(self, hero: IHero):
        hero.set_hero_state(HeroState.IDLE)
        hero.set_actions(
            {
                HeroAction.JUMPING: False,
                HeroAction.RUNNING: False,
                HeroAction.IDLE: True,
            }
        )
