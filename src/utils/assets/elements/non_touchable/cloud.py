from pygame import image, transform

from src.utils.constants import GENERAL_HEIGHT, GENERAL_WIDTH
from src.utils.directories import CLOUD_BACKGROUND_DIR

BIG_CLOUD = transform.scale(
    image.load(CLOUD_BACKGROUND_DIR + "big_cloud.png"),
    (
        ((GENERAL_WIDTH * 6) - (GENERAL_WIDTH / 6)),
        ((GENERAL_HEIGHT * 3) - (GENERAL_HEIGHT / 12)),
    ),
)

MEDIUM_CLOUD = transform.scale(
    image.load(CLOUD_BACKGROUND_DIR + "medium_cloud.png"),
    (
        ((GENERAL_WIDTH * 5) - (GENERAL_WIDTH / 3)),
        ((GENERAL_HEIGHT * 2) + (GENERAL_HEIGHT / 3)),
    ),
)

SMALL_CLOUD = transform.scale(
    image.load(CLOUD_BACKGROUND_DIR + "small_cloud.png"),
    (
        ((GENERAL_WIDTH * 3) - (GENERAL_WIDTH / 6)),
        ((GENERAL_HEIGHT * 2) - (GENERAL_HEIGHT / 2)),
    ),
)
