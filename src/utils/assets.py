from pygame import image, transform

PICTURE_WIDTH = 130
PICTURE_HEIGHT = 200

ICON = image.load("assets/player.png")
BG = image.load("assets/enemy.png")

PLAYER_PARIENTE = transform.scale(
    image.load("assets/mario/mario1.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)
PLAYER_PARIENTE1 = transform.scale(
    image.load("assets/mario/mario2.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)
PLAYER_PARIENTE2 = transform.scale(
    image.load("assets/mario/mario3.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)
PLAYER_HIJITA = transform.scale(
    image.load("assets/warrior/warrior1.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)
PLAYER_HIJITA1 = transform.scale(
    image.load("assets/warrior/warrior2.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)
PLAYER_HIJITA2 = transform.scale(
    image.load("assets/warrior/warrior3.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)
ENEMY = transform.scale(
    image.load("assets/enemy.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)
OBSTACLE = transform.scale(
    image.load("assets/obstacle.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)
POWER_UP = transform.scale(
    image.load("assets/power-up.png"),
    (PICTURE_WIDTH, PICTURE_HEIGHT),
)

CINEMATICS_ROOT = "assets/cinematics"

FINAL_CINEMATIC_VIDEO = CINEMATICS_ROOT + "/final_cinematic/video.mp4"
FINAL_CINEMATIC_AUDIO = CINEMATICS_ROOT + "/final_cinematic/audio.mp3"
