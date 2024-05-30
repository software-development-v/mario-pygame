from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import PARIENTE_DIR

PARIENTE_IDLE = transform.scale(
    image.load(PARIENTE_DIR + "idle.png"), PLAYER_SIZE
)
