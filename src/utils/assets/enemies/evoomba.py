from ...constants import GENERAL_SIZE
from ...directories import (
    EVOOMBA_DEFAULT_DIR,
    EVOOMBA_DIED_DIR,
    EVOOMBA_WALKING_DIR,
)
from ..create_images import create_image

EVOOMBA_DEFAULT = create_image(
    EVOOMBA_DEFAULT_DIR + "default.png", GENERAL_SIZE
)

EVOOMBA_DIED = create_image(EVOOMBA_DIED_DIR + "died.png", GENERAL_SIZE)

EVOOMBA_WALKING_1 = create_image(
    EVOOMBA_WALKING_DIR + "walking_1.png", GENERAL_SIZE
)
EVOOMBA_WALKING_2 = create_image(
    EVOOMBA_WALKING_DIR + "walking_2.png", GENERAL_SIZE
)
