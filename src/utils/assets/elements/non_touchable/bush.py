from pygame import image, transform

from src.utils.constants import GENERAL_HEIGHT, GENERAL_WIDTH
from src.utils.directories import BUSH_BACKGROUND_DIR

BIG_BUSH = transform.scale(
    image.load(BUSH_BACKGROUND_DIR + "big_bush.png"), (
        ((GENERAL_WIDTH * 6) - (GENERAL_WIDTH / 6)),
        ((GENERAL_HEIGHT * 2) + (GENERAL_HEIGHT / 3))
    )
)

MEDIUM_BUSH = transform.scale(
    image.load(BUSH_BACKGROUND_DIR + "medium_bush.png"), (
        ((GENERAL_WIDTH * 4) + (GENERAL_WIDTH / 6)),
        ((GENERAL_HEIGHT * 2) + (GENERAL_HEIGHT / 6))
    )
)

SMALL_BUSH = transform.scale(
    image.load(BUSH_BACKGROUND_DIR + "small_bush.png"), (
         GENERAL_WIDTH * 3,
        ((GENERAL_HEIGHT * 2) + (GENERAL_HEIGHT / 6))
    )
)
