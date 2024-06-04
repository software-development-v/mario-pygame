from typing import List

from pygame import Surface

from src.entities import IEntity

from ...abstractions import Manager


class ObstacleManager(Manager):
    def __init__(self, entities: List[IEntity]) -> None:
        super().__init__(entities)

    def draw(self, screen: Surface) -> None:
        for element in self.entities:
            element.draw(screen)

    def update(self) -> None:
        for element in self.entities:
            element.update()
