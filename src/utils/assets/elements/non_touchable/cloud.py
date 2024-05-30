from pygame import image, transform

from src.utils.directories import CLOUD_DIR

BIG_CLOUD = transform.scale(image.load(CLOUD_DIR + "big-cloud.png"), (150, 100))
MEDIUM_CLOUD = transform.scale(
    image.load(CLOUD_DIR + "medium-cloud.png"), (125, 75)
)
SMALL_CLOUD = transform.scale(
    image.load(CLOUD_DIR + "small-cloud.png"), (100, 50)
)
