from enum import Enum


class ControllerInput(Enum):
    HORIZONTAL_AXIS = 0
    VERTICAL_AXIS = 1
    UP_ARROW = 11
    DOWN_ARROW = 12
    LEFT_ARROW = 13
    RIGHT_ARROW = 14
    X = 0
    LEFT_STICK_PRESS = 7
    R_TWO = 5
    OPTIONS = 6
