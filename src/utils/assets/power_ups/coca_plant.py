from ...constants import GENERAL_SIZE, SMALL_SIZE
from ...directories import (
    PIJCHU_BALL_BOOM_DIR,
    PIJCHU_BALL_COCA_BALL_DIR,
    PLANT_DIR,
)
from ..create_images import create_image

COCA_PLANT_1 = create_image(PLANT_DIR + "plant_1.png", GENERAL_SIZE)
COCA_PLANT_2 = create_image(PLANT_DIR + "plant_2.png", GENERAL_SIZE)

PIJCHU_BALL_1 = create_image(
    PIJCHU_BALL_COCA_BALL_DIR + "coca_ball_1.png", SMALL_SIZE
)
PIJCHU_BALL_2 = create_image(
    PIJCHU_BALL_COCA_BALL_DIR + "coca_ball_2.png", SMALL_SIZE
)
PIJCHU_BALL_3 = create_image(
    PIJCHU_BALL_COCA_BALL_DIR + "coca_ball_3.png", SMALL_SIZE
)
PIJCHU_BALL_4 = create_image(
    PIJCHU_BALL_COCA_BALL_DIR + "coca_ball_4.png", SMALL_SIZE
)

PIJCHU_BALL_BOOM_1 = create_image(
    PIJCHU_BALL_BOOM_DIR + "boom_1.png", GENERAL_SIZE
)
PIJCHU_BALL_BOOM_2 = create_image(
    PIJCHU_BALL_BOOM_DIR + "boom_2.png", GENERAL_SIZE
)
PIJCHU_BALL_BOOM_3 = create_image(
    PIJCHU_BALL_BOOM_DIR + "boom_3.png", GENERAL_SIZE
)
