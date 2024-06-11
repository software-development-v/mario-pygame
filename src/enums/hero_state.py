from enum import Enum


class HeroState(Enum):
    IDLE = "IDLE"
    RUN = "RUN"
    JUMP = "JUMP"
    DUCK = "DUCK"
    BRAKE = "BRAKE"
    DEAD = "DEAD"
    DOWN = "DOWN"
