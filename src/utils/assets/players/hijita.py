from pygame import image, transform

from src.utils.constants import PLAYER_SIZE
from src.utils.directories import HIJITA_DIR

HIJITA_IDLE = transform.scale(image.load(HIJITA_DIR + "idle.png"), PLAYER_SIZE)
