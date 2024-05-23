from enum import Enum


class CustomEvent(Enum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    JUMP = "JUMP"
    RUN = "RUN"
    ATTACK = "ATTACK"
    PAUSE = "PAUSE"
