from abc import ABC, abstractmethod

from .....interfaces import IHero


class IHeroActionStrategy(ABC):
    @abstractmethod
    def execute(self, hero: IHero):
        pass
