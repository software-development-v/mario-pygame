from abc import ABC, abstractmethod
from typing import List

from pygame import Rect, Surface, time, transform
from pygame.sprite import Sprite as PygameSprite

from src.utils import ANIMATION_INTERVAL, INIT_IMAGE_INDEX, Camera, Position

from ..interfaces import IAnimate, IDrawable


class Sprite(PygameSprite, IDrawable, IAnimate, ABC):
    def __init__(
        self, position: Position, animation_interval: int = ANIMATION_INTERVAL
    ):
        super().__init__()
        self.__index = INIT_IMAGE_INDEX
        self.__face_right = True
        self.__last_update = time.get_ticks()
        self.__animation_interval = animation_interval
        self.__rect = self.__get_image().get_rect()
        self.__rect.x = position.x
        self.__rect.y = position.y
        self.__width = self.__rect.width
        self.__height = self.__rect.height

    @abstractmethod
    def _get_surfaces(self) -> List[Surface]:
        pass

    def get_rect(self) -> Rect:
        return self.__rect

    def get_x_rect(self) -> int:
        return self.__rect.x

    def get_y_rect(self) -> int:
        return self.__rect.y

    def set_x_rect(self, x: int) -> None:
        self.__rect.x = x

    def set_y_rect(self, y: int) -> None:
        self.__rect.y = y

    def get_width(self) -> int:
        return self.__width

    def get_height(self) -> int:
        return self.__height

    def set_face_right(self, face_right: bool) -> None:
        self.__face_right = face_right

    def __get_image(self) -> Surface:
        image = self._get_surfaces()[self.__index]

        if not self.__face_right:
            image = transform.flip(image, True, False)

        return image

    def draw(self, screen: Surface, camera: Camera) -> None:
        screen.blit(self.__get_image(), camera.apply(self.__rect))

    def animate(self) -> None:
        surfaces = self._get_surfaces()
        current_time = time.get_ticks()

        if current_time - self.__last_update > self.__animation_interval:
            self.__index = self.__index + 1
            self.__last_update = current_time

        if self.__index >= len(surfaces):
            self.__index = INIT_IMAGE_INDEX
