from pygame import image, transform

from src.utils.constants import GENERAL_HEIGHT, GENERAL_WIDTH
from src.utils.directories import MOUNTAIN_BACKGROUND_DIR

BIG_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "big_mountain.png"),
    (
        ((GENERAL_WIDTH * 7) - (GENERAL_WIDTH / 3)),
        ((GENERAL_HEIGHT * 5) + (GENERAL_HEIGHT / 3)),
    ),
)

MEDIUM_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "medium_mountain.png"),
    (
        ((GENERAL_WIDTH * 6) - (GENERAL_WIDTH / 6)),
        ((GENERAL_HEIGHT * 4) + (GENERAL_HEIGHT / 6)),
    ),
)

SMALL_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "small_mountain.png"),
    (
        ((GENERAL_WIDTH * 4) + (GENERAL_WIDTH / 6)),
        ((GENERAL_HEIGHT * 2) + (GENERAL_HEIGHT / 12)),
    ),
)
