from enum import Enum

from pygame import (
    K_DOWN,
    K_ESCAPE,
    K_LEFT,
    K_LSHIFT,
    K_RIGHT,
    K_SPACE,
    K_UP,
    K_a,
    K_d,
    K_r,
    K_s,
    K_w,
)


class KeyboardInput(Enum):
    KEY_UP = K_UP
    KEY_W = K_w
    KEY_DOWN = K_DOWN
    KEY_S = K_s
    KEY_LEFT = K_LEFT
    KEY_A = K_a
    KEY_RIGHT = K_RIGHT
    KEY_D = K_d
    KEY_SPACE = K_SPACE
    KEY_SHIFT = K_LSHIFT
    KEY_R = K_r
    KEY_ESCAPE = K_ESCAPE
