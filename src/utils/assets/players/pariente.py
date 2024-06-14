from ..create_images import create_image
from src.utils.constants import GENERAL_SIZE, BIG_SIZE
from src.utils.directories import (
    PARIENTE_LVL_1_BRAKE_DIR,
    PARIENTE_LVL_1_DEFAULT_DIR,
    PARIENTE_LVL_1_DIED_DIR,
    PARIENTE_LVL_1_DOWN_DIR,
    PARIENTE_LVL_1_JUMP_DIR,
    PARIENTE_LVL_1_WALKING_DIR,
    PARIENTE_LVL_2_DEFAULT_DIR,
    PARIENTE_LVL_2_BRAKE_DIR,
    PARIENTE_LVL_2_DUCK_DIR,
    PARIENTE_LVL_2_DOWN_DIR,
    PARIENTE_LVL_2_JUMP_DIR,
    PARIENTE_LVL_2_WALKING_DIR,
    PARIENTE_LVL_3_DEFAULT_DIR,
    PARIENTE_LVL_3_BRAKE_DIR,
    PARIENTE_LVL_3_DOWN_DIR,
    PARIENTE_LVL_3_DUCK_DIR,
    PARIENTE_LVL_3_JUMP_DIR,
    PARIENTE_LVL_3_WALKING_DIR,
    PARIENTE_LVL_4_1_BRAKE_DIR,
    PARIENTE_LVL_4_1_DEFAULT_DIR,
    PARIENTE_LVL_4_1_DIED_DIR,
    PARIENTE_LVL_4_1_DOWN_DIR,
    PARIENTE_LVL_4_1_JUMP_DIR,
    PARIENTE_LVL_4_1_WALKING_DIR,
    PARIENTE_LVL_4_2_DEFAULT_DIR,
    PARIENTE_LVL_4_2_BRAKE_DIR,
    PARIENTE_LVL_4_2_DOWN_DIR,
    PARIENTE_LVL_4_2_DUCK_DIR,
    PARIENTE_LVL_4_2_JUMP_DIR,
    PARIENTE_LVL_4_2_WALKING_DIR,
)

# ==== LEVEL 1 ====

# Default
PARIENTE_LVL_1 = create_image(
    PARIENTE_LVL_1_DEFAULT_DIR + "default.png", GENERAL_SIZE
)

# Brake
PARIENTE_LVL_1_BRAKE = create_image(
    PARIENTE_LVL_1_BRAKE_DIR + "brake.png", GENERAL_SIZE
)

# Died
PARIENTE_LVL_1_DIED = create_image(
    PARIENTE_LVL_1_DIED_DIR + "died.png", GENERAL_SIZE
)

# Down
PARIENTE_LVL_1_DOWN_1 = create_image(
    PARIENTE_LVL_1_DOWN_DIR + "down_1.png", GENERAL_SIZE
)

PARIENTE_LVL_1_DOWN_2 = create_image(
    PARIENTE_LVL_1_DOWN_DIR + "down_2.png", GENERAL_SIZE
)

# Jump
PARIENTE_LVL_1_JUMP = create_image(
    PARIENTE_LVL_1_JUMP_DIR + "jump.png", GENERAL_SIZE
)

# Walking
PARIENTE_LVL_1_WALKING_1 = create_image(
    PARIENTE_LVL_1_WALKING_DIR + "walking_1.png", GENERAL_SIZE
)

PARIENTE_LVL_1_WALKING_2 = create_image(
    PARIENTE_LVL_1_WALKING_DIR + "walking_2.png", GENERAL_SIZE
)

PARIENTE_LVL_1_WALKING_3 = create_image(
    PARIENTE_LVL_1_WALKING_DIR + "walking_3.png", GENERAL_SIZE
)

# ==== LEVEL 2 ====

# Default
PARIENTE_LVL_2 = create_image(
    PARIENTE_LVL_2_DEFAULT_DIR + "default.png", BIG_SIZE
)

# Brake
PARIENTE_LVL_2_BRAKE = create_image(
    PARIENTE_LVL_2_BRAKE_DIR + "brake.png", BIG_SIZE
)

# Duck
PARIENTE_LVL_2_DUCK = create_image(
    PARIENTE_LVL_2_DUCK_DIR + "duck.png", BIG_SIZE
)

# Down
PARIENTE_LVL_2_DOWN_1 = create_image(
    PARIENTE_LVL_2_DOWN_DIR + "down_1.png", BIG_SIZE
)

PARIENTE_LVL_2_DOWN_2 = create_image(
    PARIENTE_LVL_2_DOWN_DIR + "down_2.png", BIG_SIZE
)

# Jump
PARIENTE_LVL_2_JUMP = create_image(
    PARIENTE_LVL_2_JUMP_DIR + "jump.png", BIG_SIZE
)

# Walking
PARIENTE_LVL_2_WALKING_1 = create_image(
    PARIENTE_LVL_2_WALKING_DIR + "walking_1.png", BIG_SIZE
)

PARIENTE_LVL_2_WALKING_2 = create_image(
    PARIENTE_LVL_2_WALKING_DIR + "walking_2.png", BIG_SIZE
)

PARIENTE_LVL_2_WALKING_3 = create_image(
    PARIENTE_LVL_2_WALKING_DIR + "walking_3.png", BIG_SIZE
)

# ==== LEVEL 3 ====

# Default
PARIENTE_LVL_3 = create_image(
    PARIENTE_LVL_3_DEFAULT_DIR + "default.png", BIG_SIZE
)

# Brake
PARIENTE_LVL_3_BRAKE = create_image(
    PARIENTE_LVL_3_BRAKE_DIR + "brake.png", BIG_SIZE
)

# Duck
PARIENTE_LVL_3_DUCK = create_image(
    PARIENTE_LVL_3_DUCK_DIR + "duck.png", BIG_SIZE
)

# Down
PARIENTE_LVL_3_DOWN_1 = create_image(
    PARIENTE_LVL_3_DOWN_DIR + "down_1.png", BIG_SIZE
)

PARIENTE_LVL_3_DOWN_2 = create_image(
    PARIENTE_LVL_3_DOWN_DIR + "down_2.png", BIG_SIZE
)

# Jump
PARIENTE_LVL_3_JUMP = create_image(
    PARIENTE_LVL_3_JUMP_DIR + "jump.png", BIG_SIZE
)

# Walking
PARIENTE_LVL_3_WALKING_1 = create_image(
    PARIENTE_LVL_3_WALKING_DIR + "walking_1.png", BIG_SIZE
)

PARIENTE_LVL_3_WALKING_2 = create_image(
    PARIENTE_LVL_3_WALKING_DIR + "walking_2.png", BIG_SIZE
)

PARIENTE_LVL_3_WALKING_3 = create_image(
    PARIENTE_LVL_3_WALKING_DIR + "walking_3.png", BIG_SIZE
)

# ==== LEVEL 4 ====

# == Level 1

# Default
PARIENTE_LVL_4_1 = create_image(
    PARIENTE_LVL_4_1_DEFAULT_DIR + "default.png", GENERAL_SIZE
)

# Brake
PARIENTE_LVL_4_1_BRAKE = create_image(
    PARIENTE_LVL_4_1_BRAKE_DIR + "brake.png", GENERAL_SIZE
)

# Died
PARIENTE_LVL_4_1_DIED = create_image(
    PARIENTE_LVL_4_1_DIED_DIR + "died.png", GENERAL_SIZE
)

# Down
PARIENTE_LVL_4_1_DOWN_1 = create_image(
    PARIENTE_LVL_4_1_DOWN_DIR + "down_1.png", GENERAL_SIZE
)

PARIENTE_LVL_4_1_DOWN_2 = create_image(
    PARIENTE_LVL_4_1_DOWN_DIR + "down_2.png", GENERAL_SIZE
)

# Jump
PARIENTE_LVL_4_1_JUMP = create_image(
    PARIENTE_LVL_4_1_JUMP_DIR + "jump.png", GENERAL_SIZE
)

# Walking
PARIENTE_LVL_4_1_WALKING_1 = create_image(
    PARIENTE_LVL_4_1_WALKING_DIR + "walking_1.png", GENERAL_SIZE
)

PARIENTE_LVL_4_1_WALKING_2 = create_image(
    PARIENTE_LVL_4_1_WALKING_DIR + "walking_2.png", GENERAL_SIZE
)

PARIENTE_LVL_4_1_WALKING_3 = create_image(
    PARIENTE_LVL_4_1_WALKING_DIR + "walking_3.png", GENERAL_SIZE
)

# == Level 2

# Default
PARIENTE_LVL_4_2 = create_image(
    PARIENTE_LVL_4_2_DEFAULT_DIR + "default.png", BIG_SIZE
)

# Brake
PARIENTE_LVL_4_2_BRAKE = create_image(
    PARIENTE_LVL_4_2_BRAKE_DIR + "brake.png", BIG_SIZE
)

# Duck
PARIENTE_LVL_4_2_DUCK = create_image(
    PARIENTE_LVL_4_2_DUCK_DIR + "duck.png", BIG_SIZE
)

# Down
PARIENTE_LVL_4_2_DOWN_1 = create_image(
    PARIENTE_LVL_4_2_DOWN_DIR + "down_1.png", BIG_SIZE
)

PARIENTE_LVL_4_2_DOWN_2 = create_image(
    PARIENTE_LVL_4_2_DOWN_DIR + "down_2.png", BIG_SIZE
)

# Jump
PARIENTE_LVL_4_2_JUMP = create_image(
    PARIENTE_LVL_4_2_JUMP_DIR + "jump.png", BIG_SIZE
)

# Walking
PARIENTE_LVL_4_2_WALKING_1 = create_image(
    PARIENTE_LVL_4_2_WALKING_DIR + "walking_1.png", BIG_SIZE
)

PARIENTE_LVL_4_2_WALKING_2 = create_image(
    PARIENTE_LVL_4_2_WALKING_DIR + "walking_2.png", BIG_SIZE
)

PARIENTE_LVL_4_2_WALKING_3 = create_image(
    PARIENTE_LVL_4_2_WALKING_DIR + "walking_3.png", BIG_SIZE
)
