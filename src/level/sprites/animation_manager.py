from typing import List, Tuple


from src.entities import (
    CollectedCoin,
    IElementObserver,
    CollectedScore,
    InteractiveElement,
    Animation,
    AnimationCompose,
)

from src.enums import AnimationType
from src.utils import Position
from ..abstractions.sprites_manager import SpritesManager


class AnimationManager(
    SpritesManager[Animation],
    IElementObserver[Tuple[InteractiveElement, List[AnimationType]]],
):
    def __init__(self) -> None:
        super().__init__([])

    def notify(
        self, value: Tuple[InteractiveElement, List[AnimationType]]
    ) -> None:
        if len(value[1]) == 0:
            return

        rect = value[0].get_rect()
        pos = Position(rect.centerx, rect.centery)

        animations: List[Animation] = []

        for element in value[1]:
            if element == AnimationType.COLLECTED_COIN:
                animations.append(CollectedCoin(pos))
            elif element == AnimationType.COLLECTED_SCORE:
                animations.append(CollectedScore(pos, value[0].get_value()))

        self.get_sprites().append(AnimationCompose(animations))
