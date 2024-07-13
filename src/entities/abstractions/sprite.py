from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from pygame import Rect, Surface, time, transform
from pygame.sprite import Sprite as PygameSprite

from src.enums import SpriteEventType
from src.utils import ANIMATION_INTERVAL, INIT_IMAGE_INDEX, Camera, Position

from ..interfaces import IElementObserver, IObservableElement, ISprite


class Sprite(
    PygameSprite,
    ISprite,
    IObservableElement[Tuple["Sprite", List[SpriteEventType]]],
    ABC,
):
    def __init__(
        self,
        init_position: Position,
        animation_interval: int = ANIMATION_INTERVAL,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
        check_point: Optional[Position] = None,
        value: int = 0,
        alpha: bool = False,
    ):
        super().__init__()
        self.__init_position: Position = init_position
        self.__check_point: Optional[Position] = check_point
        self.__reach_check_point: bool = False
        self.__index: int = INIT_IMAGE_INDEX
        self.__face_right: bool = True
        self.__last_update: int = time.get_ticks()
        self.__animation_interval: int = animation_interval
        self.__disposed = False
        self.__visible = True
        self.__value = value
        self.__observer: Optional[
            IElementObserver[Tuple["Sprite", List[SpriteEventType]]]
        ]
        self.__alpha = alpha
        self.__transparency = 255

        self.__image_rect: Rect = self.__get_image().get_rect(
            topleft=init_position.to_tuple()
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

    def get_check_point(self) -> Optional[Position]:
        return self.__check_point

    def get_reach_check_point(self) -> bool:
        return self.__reach_check_point

    def set_reach_check_point(self, value: bool) -> None:
        self.__reach_check_point = value

    def reset(self) -> None:
        if self.__reach_check_point and self.__check_point is not None:
            self.__image_rect.topleft = self.__check_point.to_tuple()
        else:
            self.__image_rect.topleft = self.__init_position.to_tuple()

        self.__rect = Rect(
            self.__image_rect.x + (self.__image_rect.width - self.__width) / 2,
            self.__image_rect.y
            + (self.__image_rect.height - self.__height) / 2,
            self.__width,
            self.__height,
        )

    def set_index(self, index: int) -> None:
        self.__index = index

    def get_rect(self) -> Rect:
        return self.__rect

    def set_transparency(self, transparency: int) -> None:
        self.__transparency = transparency

    def appear(self):
        self.__visible = True

    def disappear(self):
        self.__visible = False

    def set_rect(self, position: Position) -> None:
        self.__image_rect.topleft = position.to_tuple()
        self.__rect = Rect(
            self.__image_rect.x + (self.__image_rect.width - self.__width) / 2,
            self.__image_rect.y
            + (self.__image_rect.height - self.__height) / 2,
            self.__width,
            self.__height,
        )

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

    def get_face_right(self) -> bool:
        return self.__face_right

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
        camera: Optional[Camera] = None,
        x_rect_percent: float = 1,
        y_rect_percent: float = 1,
    ) -> None:
        if not self.__visible:
            return

        image = self.__get_image()

        if self.__alpha:
            image.convert_alpha()
            image.set_alpha(self.__transparency)

        self.__check_change_image(image, x_rect_percent, y_rect_percent)

        rect = self.__image_rect.topleft

        if camera is not None:
            rect = camera.apply(self.__image_rect)

        screen.blit(image, rect)

    def animate(self) -> None:
        surfaces = self._get_surfaces()

        if len(surfaces) == 1:
            if self.__index >= len(surfaces):
                self.__index = INIT_IMAGE_INDEX

            return

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

    def get_value(self) -> int:
        return self.__value

    def set_value(self, value: int) -> None:
        self.__value = value

    def is_visible(self) -> bool:
        return self.__visible

    def set_observer(
        self,
        observer: Optional[
            IElementObserver[Tuple["Sprite", List[SpriteEventType]]]
        ],
    ):
        self.__observer = observer

    def remove_observer(self):
        self.__observer = None

    def notify_observer(self, event: Tuple["Sprite", List[SpriteEventType]]):
        if self.__observer is not None:
            self.__observer.notify(event)
