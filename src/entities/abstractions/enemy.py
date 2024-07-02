from abc import ABC, abstractmethod
from typing import Dict, List

from pygame import Rect, Surface, time, transform
from pygame.sprite import Sprite
from src.entities.interfaces.i_sprite import ISprite
from src.enums.enemy_state import EnemyState
from src.utils import ANIMATION_INTERVAL, Camera, Position


class Enemy(Sprite, ISprite, ABC):
    def __init__(
        self,
        surfaces: Dict[EnemyState, List[Surface]],
        position: Position,
        initial_state: EnemyState,
        animation_interval: int = ANIMATION_INTERVAL,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ):
        super().__init__()
        self.__surfaces = surfaces
        self.__state = initial_state
        self.__index: int = 0
        self.__face_right: bool = True
        self.__last_update: int = time.get_ticks()
        self.__animation_interval: int = animation_interval

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

    def _get_surfaces(self) -> List[Surface]:
        return self.__surfaces[self.__state]

    @abstractmethod
    def update_state(self) -> None:
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
            self.__image_rect.width == image.get_width()
            and self.__image_rect.height == image.get_height()
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
        camera: Camera,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        image = self.__get_image()
        self.__check_change_image(image, x_rect_percent, y_rect_percent)

        screen.blit(image, camera.apply(self.__image_rect))

    def animate(self) -> None:
        surfaces = self._get_surfaces()
        current_time = time.get_ticks()

        if current_time - self.__last_update > self.__animation_interval:
            self.__index = (self.__index + 1) % len(surfaces)
            self.__last_update = current_time
