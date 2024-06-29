from abc import ABC
from typing import Generic, List, Optional, TypeVar

from pygame import Surface

from src.entities import IAnimate, IDrawable, Sprite
from src.utils import Camera

T = TypeVar("T", bound=Sprite)


class SpritesManager(Generic[T], IDrawable, IAnimate, ABC):
    def __init__(self, sprites: List[T]) -> None:
        self.__sprites = sprites

    def get_sprites(self) -> List[T]:
        return self.__sprites

    def draw(self, screen: Surface, camera: Optional[Camera]) -> None:
        for sprite in self.__sprites:
            if sprite.is_disposed():
                self.__sprites.remove(sprite)

        for sprite in self.__sprites:
            sprite.draw(screen, camera)

    def animate(self) -> None:
        for sprite in self.__sprites:
            sprite.animate()
