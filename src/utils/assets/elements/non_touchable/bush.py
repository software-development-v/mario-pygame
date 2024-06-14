from pygame import image, transform

from src.utils.directories import BUSH_BACKGROUND_DIR

BIG_BUSH = transform.scale(image.load(BUSH_BACKGROUND_DIR + "big_bush.png"), (350, 200))
MEDIUM_BUSH = transform.scale(
    image.load(BUSH_BACKGROUND_DIR + "medium_bush.png"), (250, 100)
)
SMALL_BUSH = transform.scale(
    image.load(BUSH_BACKGROUND_DIR + "small_bush.png"), (150, 100)
)
