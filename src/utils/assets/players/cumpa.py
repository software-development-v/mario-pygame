from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import CUMPA_LVL_1_DEFAULT_DIR

CUMPA_IDLE = transform.scale(image.load(CUMPA_LVL_1_DEFAULT_DIR + "front.png"), PLAYER_SIZE)
