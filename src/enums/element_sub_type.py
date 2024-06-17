from enum import Enum


class ElementSubType(Enum):
    # == TOUCHABLE ==
    # == BLOCK ==
    OVERWORLD_BLOCK = "OVERWORLD_BLOCK"
    WALL_BLOCK= "WALL_BLOCK"
    OVERWORLD_TERRAIN_BLOCK="OVERWORLD_TERRAIN_BLOCK"

    # == COIN ==
    COIN = "COIN"

    # == FLAG ==
    FLAG_PIPE = "FLAG_PIPE"
    FLAG_WIN = "FLAG_WIN"
    FLAG_STAND = "FLAG_STAND"
    FLAG_SUPPORT_1 = "FLAG_SUPPORT_1"
    FLAG_SUPPORT_2 = "FLAG_SUPPORT_2"
    FLAG_SUPPORT_3 = "FLAG_SUPPORT_3"

    # == MISTERY_BOX ==
    DEFAULT_MISTERY_BOX = "DEFAULT_MISTERY_BOX"

    # == PIP ==
    PIPE_HEAD = "PIPE_HEAD"
    PIPE_BODY_STYLE_1 = "PIPE_BODY_STYLE_1"
    PIPE_BODY_STYLE_2 = "PIPE_BODY_STYLE_2"
    PIPE_BODY_STYLE_3 = "PIPE_BODY_STYLE_3"
    PIPE_BODY_STYLE_4 = "PIPE_BODY_STYLE_4"

    # == NON TOUCHABLE ==
    # == BUSH ==
    SMALL_BUSH = "SMALL_BUSH"
    MEDIUM_BUSH = "MEDIUM_BUSH"
    BIG_BUSH = "BIG_BUSH"

    # == CLOUD ==
    SMALL_CLOUD = "SMALL_CLOUD"
    MEDIUM_CLOUD = "MEDIUM_CLOUD"
    BIG_CLOUD = "BIG_CLOUD"

    # == TREE ==
    SMALL_TREE = "SMALL_TREE"
    MEDIUM_TREE = "MEDIUM_TREE"
    BIG_TREE = "BIG_TREE"

    # == MOUNTAIN ==
    SMALL_MOUNTAIN = "SMALL_MOUNTAIN"
    MEDIUM_MOUNTAIN = "MEDIUM_MOUNTAIN"
    BIG_MOUNTAIN = "BIG_MOUNTAIN"

    # == CASTLE ==
    DEFAULT_CASTLE = "DEFAULT_CASTLE"
