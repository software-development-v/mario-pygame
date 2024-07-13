from typing import List, Tuple

from src.entities import (
    Animation,
    AnimationCompose,
    Coin,
    CollectedCoin,
    CollectedScore,
    Enemy,
    IElementObserver,
    IHero,
    Sprite,
)
from src.enums import SpriteEventType
from src.utils import Position

from ..abstractions import SpritesManager


class AnimationManager(
    SpritesManager[Animation],
    IElementObserver[Tuple[Sprite, List[SpriteEventType]]],
):
    INCREMENT_BY_BOUNCE = 100

    def __init__(
        self,
        hero: IHero,
        coin_observer: IElementObserver[int],
        score_observer: IElementObserver[int],
    ) -> None:
        self.__hero = hero
        self.__bouncing_counter = 0
        self.__coin_observer = coin_observer
        self.__score_observer = score_observer
        super().__init__([])

    def notify(self, value: Tuple[Sprite, List[SpriteEventType]]) -> None:
        self.__manage_bouncing(value[0])
        if len(value[1]) == 0:
            return
        self.get_sprites().append(
            AnimationCompose(self.__handle_sprite_events(value))
        )

    def __manage_bouncing(self, sprite: Sprite) -> None:
        if self.__hero.is_bouncing() and isinstance(sprite, Enemy):
            self.__bouncing_counter += 1
            sprite.set_value(
                sprite.get_value()
                + (self.INCREMENT_BY_BOUNCE * self.__bouncing_counter)
            )

        else:
            self.__bouncing_counter = 0

    def __handle_sprite_events(
        self, value: Tuple[Sprite, List[SpriteEventType]]
    ) -> List[Animation]:
        sprite = value[0]
        animations: list[Animation] = []
        rect = sprite.get_rect()
        pos = Position(rect.centerx, rect.centery)

        for element in value[1]:
            if element == SpriteEventType.COLLECTED_COIN:
                if not isinstance(sprite, Coin):
                    animations.append(CollectedCoin(pos))
                self.__coin_observer.notify(1)
            elif element == SpriteEventType.COLLECTED_SCORE:
                self.__score_observer.notify(sprite.get_value())
                animations.append(CollectedScore(pos, sprite.get_value()))

        return animations

    def reset(self):
        self.__bouncing_counter = 0
