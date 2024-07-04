from enum import Enum


class EnemyState(Enum):
    WALKING = "WALKING"
    INSIDE = "INSIDE"
    SPINNING = "SPINNING"
    COMING_OUT = "COMING_OUT"
    DEAD = "DEAD"
