from pygame import image, transform

from src.utils.constants import GENERAL_HEIGHT, GENERAL_SIZE, GENERAL_WIDTH
from src.utils.directories import (
    FLAG_PIPE_DIR,
    FLAG_STAND_DIR,
    FLAG_SUPPORT_DIR,
    FLAG_WIN_DIR,
)

FLAG_STAND = transform.scale(
    image.load(FLAG_STAND_DIR + "stand.png"), GENERAL_SIZE
)

FLAG_PIPE = transform.scale(
    image.load(FLAG_PIPE_DIR + "flag_pipe.png"),
    (GENERAL_WIDTH / 4, GENERAL_HEIGHT),
)

FLAG_WIN = transform.scale(
    image.load(FLAG_WIN_DIR + "flag_win.png"),
    (GENERAL_WIDTH * 2, GENERAL_HEIGHT + (GENERAL_HEIGHT / 3)),
)

FLAG_SUPPORT_1 = transform.scale(
    image.load(FLAG_SUPPORT_DIR + "support_stand_1.png"), GENERAL_SIZE
)

FLAG_SUPPORT_2 = transform.scale(
    image.load(FLAG_SUPPORT_DIR + "support_stand_2.png"), GENERAL_SIZE
)

FLAG_SUPPORT_3 = transform.scale(
    image.load(FLAG_SUPPORT_DIR + "support_stand_3.png"), GENERAL_SIZE
)
