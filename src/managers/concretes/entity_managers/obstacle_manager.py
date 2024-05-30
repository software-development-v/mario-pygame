from pygame import Surface
from src.managers.interfaces.i_manager import IManager


class ObstacleManager(IManager):

    def draw(self, screen: Surface) -> None:
        for element in self.entities:
            element.draw(screen)


    def update(self) -> None:
        return super().update()
