from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import HIJITA_LVL_1_DEFAULT_DIR

HIJITA_IDLE = transform.scale(image.load(HIJITA_LVL_1_DEFAULT_DIR + "front.png"), PLAYER_SIZE)
