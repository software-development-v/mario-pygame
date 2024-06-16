from src.utils.assets.create_images import create_image
from src.utils.constants import GENERAL_SIZE, VALVOOPA_SIZE
from src.utils.directories import (
    VALVOOPA_COMING_OUT_DIR,
    VALVOOPA_DEFAULT_DIR,
    VALVOOPA_INSIDE_DIR,
    VALVOOPA_WALKING_DIR,
)

VALVOOPA_DEFAULT = create_image(
    VALVOOPA_DEFAULT_DIR + "default.png", VALVOOPA_SIZE
)

VALVOOPA_INSIDE = create_image(VALVOOPA_INSIDE_DIR + "inside.png", GENERAL_SIZE)

VALVOOPA_COMING_OUT_1 = create_image(
    VALVOOPA_COMING_OUT_DIR + "coming_out_1.png", GENERAL_SIZE
)
VALVOOPA_COMING_OUT_2 = create_image(
    VALVOOPA_COMING_OUT_DIR + "coming_out_2.png", GENERAL_SIZE
)

VALVOOPA_WALKING_1 = create_image(
    VALVOOPA_WALKING_DIR + "walking_1.png", VALVOOPA_SIZE
)
VALVOOPA_WALKING_2 = create_image(
    VALVOOPA_WALKING_DIR + "walking_2.png", VALVOOPA_SIZE
)
