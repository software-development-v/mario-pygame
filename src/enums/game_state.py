from enum import Enum


class GameState(Enum):
    RUNNING = "RUNNING"
    IN_GAME = "IN_GAME"
    NEXT_SCENE = "NEXT_SCENE"
    BACK_SCENE = "BACK_SCENE"
    JUMP_SCENE = "JUMP_SCENE"
    PAUSE = "PAUSE"
    QUIT = "QUIT"

