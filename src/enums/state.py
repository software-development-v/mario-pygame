from enum import Enum


class State(Enum):
    RUNNING = "RUNNING"
    RESTART = "RESTART"
    PAUSE = "PAUSE"
    BACK = "BACK"
    NEXT = "NEXT"
