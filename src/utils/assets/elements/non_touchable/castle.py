from pygame import image, transform

from src.utils.constants import GENERAL_HEIGHT, GENERAL_WIDTH
from src.utils.directories import CASTLE_DIR

CASTLE = transform.scale(
    image.load(CASTLE_DIR + "motel.png"),
    ((GENERAL_WIDTH * 8) + (GENERAL_HEIGHT / 3), GENERAL_HEIGHT * 4),
)
