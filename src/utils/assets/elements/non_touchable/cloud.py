from pygame import image, transform

from src.utils.directories import CLOUD_BACKGROUND_DIR

BIG_CLOUD = transform.scale(
    image.load(CLOUD_BACKGROUND_DIR + "big_cloud.png"), (300, 150)
)
MEDIUM_CLOUD = transform.scale(
    image.load(CLOUD_BACKGROUND_DIR + "medium_cloud.png"), (250, 110)
)
SMALL_CLOUD = transform.scale(
    image.load(CLOUD_BACKGROUND_DIR + "small_cloud.png"), (150, 70)
)
