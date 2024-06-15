from pygame import image, transform

from src.utils.directories import MOUNTAIN_BACKGROUND_DIR

BIG_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "big_mountain.png"), (400, 300)
)
MEDIUM_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "medium_mountain.png"), (350, 250)
)
SMALL_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "small_mountain.png"), (250, 100)
)
