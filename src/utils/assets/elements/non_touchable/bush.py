from pygame import image, transform

from ....constants import BUSH_HEIGHT, BUSH_WIDTH_FACTOR
from ....directories import BUSH_BACKGROUND_DIR

BIG_BUSH = transform.scale(
    image.load(BUSH_BACKGROUND_DIR + "big_bush.png"),
    (
        BUSH_HEIGHT * BUSH_WIDTH_FACTOR,
        BUSH_HEIGHT,
    ),
)

MEDIUM_BUSH = transform.scale(
    image.load(BUSH_BACKGROUND_DIR + "medium_bush.png"),
    (
        (BUSH_HEIGHT - 10) * BUSH_WIDTH_FACTOR,
        BUSH_HEIGHT - 10,
    ),
)

SMALL_BUSH = transform.scale(
    image.load(BUSH_BACKGROUND_DIR + "small_bush.png"),
    (
        (BUSH_HEIGHT - 20) * BUSH_WIDTH_FACTOR,
        BUSH_HEIGHT - 20,
    ),
)
