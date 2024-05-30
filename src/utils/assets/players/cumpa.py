from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import CUMPA_DIR

CUMPA_IDLE = transform.scale(image.load(CUMPA_DIR + "idle.png"), PLAYER_SIZE)
