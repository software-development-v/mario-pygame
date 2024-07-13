from .concretes import (
    HeroActionIdle,
    HeroActionRun,
    HeroActionWin,
    HeroActionDead
)
from .interfaces import IHeroActionStrategy

__all__ = [
    "HeroActionIdle",
    "HeroActionRun",
    "HeroActionWin",
    "HeroActionDead",
    "IHeroActionStrategy",
]
