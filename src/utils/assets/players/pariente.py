from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import PARIENTE_LVL_1_DEFAULT_DIR

PARIENTE_IDLE = transform.scale(
    image.load(PARIENTE_LVL_1_DEFAULT_DIR + "front.png"), PLAYER_SIZE
)
