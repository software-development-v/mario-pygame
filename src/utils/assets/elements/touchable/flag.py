from pygame import image, transform

from src.utils.constants import GENERAL_SIZE
from src.utils.directories import FLAG_STAND_DIR, FLAG_PIPE_DIR, FLAG_WIN_DIR, FLAG_SUPPORT_DIR

FLAG_STAND = transform.scale(
    image.load(FLAG_STAND_DIR + "stand.png"), (50, 25)
)
FLAG_PIPE = transform.scale(
    image.load(FLAG_PIPE_DIR + "flag_pipe.png"), (10, 50)
)
FLAG_WIN = transform.scale(
    image.load(FLAG_WIN_DIR + "flag_win.png"), (100, 70)
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
