from pygame import Surface
from src.utils.camera import Camera
from src.utils.constants import FONT_SIZE
from src.utils.text import get_centered_message
from ...abstractions.animation import Animation
from src.utils import Position


class CollectedScore(Animation):
    def __init__(self, position: Position, value: int):
        surface, rect = get_centered_message(str(value), size=FONT_SIZE)
        self.__last_camara_left_edge: float = 0
        self.__x_increment: float = 0
        position.x+=10-(rect.width//2)
        super().__init__(
            [surface],
            transitions=[position, Position(position.x, position.y - 200)],
            speed=6,
        )

    def draw(
        self,
        screen: Surface,
        camera: Camera | None = None,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        if camera is not None:
            if self.__last_camara_left_edge > 0:
                self.add_x_rect(
                    self.__x_increment
                    - (self.get_rect().x - camera.get_left_edge())
                )
            else:
                self.__x_increment = self.get_rect().x - camera.get_left_edge()
            self.__last_camara_left_edge = camera.get_left_edge()

        return super().draw(screen, camera, x_rect_percent, y_rect_percent)
