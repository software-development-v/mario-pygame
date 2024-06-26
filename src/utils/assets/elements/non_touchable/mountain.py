from pygame import image, transform

from ....constants import (
    BIG_MOUNTAIN_SIZE,
    MEDIUM_MOUNTAIN_SIZE,
    SMALL_MOUNTAIN_SIZE,
)
from ....directories import MOUNTAIN_BACKGROUND_DIR

BIG_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "big_mountain.png"),
    (BIG_MOUNTAIN_SIZE),
)

MEDIUM_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "medium_mountain.png"),
    (MEDIUM_MOUNTAIN_SIZE),
)

SMALL_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "small_mountain.png"),
    (SMALL_MOUNTAIN_SIZE),
)
