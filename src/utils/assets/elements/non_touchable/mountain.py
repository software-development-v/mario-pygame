from pygame import image, transform

from src.utils.directories import MOUNTAIN_BACKGROUND_DIR

BIG_MOUNTAIN = transform.scale(image.load(MOUNTAIN_BACKGROUND_DIR + "big_mountain.png"), (150, 100))
MEDIUM_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "medium_mountain.png"), (125, 75)
)
SMALL_MOUNTAIN = transform.scale(
    image.load(MOUNTAIN_BACKGROUND_DIR + "small_mountain.png"), (100, 50)
)
