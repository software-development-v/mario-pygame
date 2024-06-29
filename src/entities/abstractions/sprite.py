from abc import ABC, abstractmethod
from typing import List, Optional

from pygame import Rect, Surface, time, transform
from pygame.sprite import Sprite as PygameSprite

from src.utils import ANIMATION_INTERVAL, INIT_IMAGE_INDEX, Camera, Position

from ..interfaces import ISprite


class Sprite(PygameSprite, ISprite, ABC):
    def __init__(
        self,
        position: Position,
        animation_interval: int = ANIMATION_INTERVAL,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ):
        super().__init__()
        self.__index: int = INIT_IMAGE_INDEX
        self.__face_right: float = True
        self.__last_update: int = time.get_ticks()
        self.__animation_interval: int = animation_interval
        self.__disposed = False

        self.__image_rect: Rect = self.__get_image().get_rect(
            topleft=position.to_tuple()
        )

        self.__width = self.__image_rect.width * x_rect_percent
        self.__height = self.__image_rect.height * y_rect_percent

        self.__rect = Rect(
            self.__image_rect.x + (self.__image_rect.width - self.__width) / 2,
            self.__image_rect.y
            + (self.__image_rect.height - self.__height) / 2,
            self.__width,
            self.__height,
        )

    @abstractmethod
    def _get_surfaces(self) -> List[Surface]:
        pass

    def get_rect(self) -> Rect:
        return self.__rect

    def add_x_rect(self, x: float) -> None:
        self.__image_rect.x += x
        self.__rect.x = (
            self.__image_rect.x + (self.__image_rect.width - self.__width) / 2
        )

    def add_y_rect(self, y: float) -> None:
        self.__image_rect.y += y
        self.__rect.y = (
            self.__image_rect.y + (self.__image_rect.height - self.__height) / 2
        )

    def set_face_right(self, face_right: bool) -> None:
        self.__face_right = face_right

    def __get_image(self) -> Surface:
        image = self._get_surfaces()[self.__index]

        if not self.__face_right:
            image = transform.flip(image, True, False)

        return image

    def __check_change_image(
        self, image: Surface, x_rect_percent: float, y_rect_percent: float
    ) -> None:
        if (
            self.__image_rect.width == image.width
            and self.__image_rect.height == image.height
        ):
            return

        x, y = self.__image_rect.x, self.__image_rect.y

        self.__image_rect: Rect = image.get_rect()
        self.__image_rect.x = x
        self.__image_rect.y = y

        self.__width = self.__image_rect.width * x_rect_percent
        self.__height = self.__image_rect.height * y_rect_percent

        self.__rect = Rect(
            self.__image_rect.x + (self.__image_rect.width - self.__width) / 2,
            self.__image_rect.y
            + (self.__image_rect.height - self.__height) / 2,
            self.__width,
            self.__height,
        )

    def draw(
        self,
        screen: Surface,
        camera: Optional[Camera]=None,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        image = self.__get_image()
        self.__check_change_image(image, x_rect_percent, y_rect_percent)
        rect = self.__rect.topleft
        if camera is not None:
            rect = camera.apply(self.__rect)

        screen.blit(image, rect)

    def animate(self) -> None:
        surfaces = self._get_surfaces()
        current_time = time.get_ticks()

        if current_time - self.__last_update > self.__animation_interval:
            self.__index = self.__index + 1
            self.__last_update = current_time

        if self.__index >= len(surfaces):
            self.__index = INIT_IMAGE_INDEX

    def dispose(self) -> None:
        self.__disposed = True

    def is_disposed(self) -> bool:
        return self.__disposed
