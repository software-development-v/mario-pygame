from enum import Enum


class SpriteEventType(Enum):
    COLLECTED_COIN = 1
    COLLECTED_SCORE = 2
    ENEMY_DIE = 3
