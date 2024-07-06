from src.utils.constants import GENERAL_SIZE
from src.utils.directories import FIREWORKS_DIR
from ...create_images import create_image


FIREWORK_SMALL = create_image(
    FIREWORKS_DIR + "firework_1", GENERAL_SIZE
)

FIREWORK_MEDIUM = create_image(
    FIREWORKS_DIR + "firework_2", GENERAL_SIZE
)

FIREWORK_LARGE = create_image(
    FIREWORKS_DIR + "firework_3", GENERAL_SIZE
)
