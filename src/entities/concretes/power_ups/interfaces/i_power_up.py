from abc import ABC, abstractmethod

from ....interfaces import ISprite
from ...hero import IHero


class IPowerUp(ISprite, ABC):
    @abstractmethod
    def update(self, hero: IHero) -> None:
        pass
