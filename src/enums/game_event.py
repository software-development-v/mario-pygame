from enum import Enum


class GameEvent(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    JUMP = "JUMP"
    RUN = "RUN"
    ATTACK = "ATTACK"
    PAUSE = "PAUSE"
