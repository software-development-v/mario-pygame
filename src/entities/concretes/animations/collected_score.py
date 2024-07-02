from pygame import Surface, transform
from src.utils import Camera, Position,GENERAL_HEIGHT, get_centered_message, FONT_MEDIUM_SIZE
from ...abstractions.animation import Animation



class CollectedScore(Animation):
    def __init__(self, position: Position, value: int, height: float=GENERAL_HEIGHT*2):
        surface, rect = get_centered_message(str(value), size=FONT_MEDIUM_SIZE)
        surface = transform.scale(surface, (rect.width-20, rect.height+10))
        self.__last_camara_left_edge: float = 0
        self.__x_increment: float = 0
        position.x+=25-(rect.width//2)
        super().__init__(
            [surface],
            transitions=[position, Position(position.x, int(position.y - height))],
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
