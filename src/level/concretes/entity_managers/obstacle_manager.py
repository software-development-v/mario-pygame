from typing import List

from pygame import Surface

from src.entities import Element, IDrawable, IUpdatable
from src.utils.camera import Camera


class ObstacleManager(IDrawable, IUpdatable):
    def __init__(self, obstacles: List[Element]) -> None:
        self.obstacles = obstacles

    def get_obstacles(self) -> List[Element]:
        return self.obstacles

    def draw(self, screen: Surface, camera: Camera) -> None:
        for obstacle in self.obstacles:
            screen.blit(obstacle.image, camera.apply(obstacle))

    def update(self) -> None:
        for obstacle in self.obstacles:
            obstacle.update()
