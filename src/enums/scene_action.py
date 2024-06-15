from enum import Enum


class SceneAction(Enum):
    CONTINUE = "CONTINUE"
    PAUSE = "PAUSE"
    END = "END"
    SET_NEXT_SCENE = "SET_NEXT_SCENE"
    SET_FRAME_RATE = "SET_FRAME_RATE"
