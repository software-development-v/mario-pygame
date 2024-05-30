from pygame import image, transform

PLAYER_SIZE = (100, 100)

# Root directory
ASSETS_DIR = "assets/"

# Logos directory
LOGOS_DIR = ASSETS_DIR + "logo/"
ICON = image.load(LOGOS_DIR + "icon.png")

# Fonts directory
FONTS_DIR = ASSETS_DIR + "fonts/"
GAME_FONT = FONTS_DIR + "game-font.ttf"

# Players directory
PLAYERS_DIR = ASSETS_DIR + "players/"

# Pariente Foianini directory
PARIENTE_DIR = PLAYERS_DIR + "pariente_foianini/"
PARIENTE_IDLE = transform.scale(
    image.load(PARIENTE_DIR + "idle.png"), PLAYER_SIZE
)

# Hijita Mamani directory
HIJITA_DIR = PLAYERS_DIR + "hijita_mamani/"
HIJITA_IDLE = transform.scale(image.load(HIJITA_DIR + "idle.png"), PLAYER_SIZE)

# Cumpa Mendez directory
CUMPA_DIR = PLAYERS_DIR + "cumpa_mendez/"
CUMPA_IDLE = transform.scale(image.load(CUMPA_DIR + "idle.png"), PLAYER_SIZE)

# Cinematic directory
CINEMATICS_DIR = ASSETS_DIR + "cinematics/"

# Final cinematic
FINAL_CINEMATIC_DIR = CINEMATICS_DIR + "final_cinematic/"
FINAL_CINEMATIC_VIDEO = FINAL_CINEMATIC_DIR + "video.mp4"
FINAL_CINEMATIC_AUDIO = FINAL_CINEMATIC_DIR + "audio.mp3"
