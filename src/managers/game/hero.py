from pygame import Surface, transform
from ...data import GameData
from ...enums import HeroType, HeroState
from ...utils.constants import CENTER_X, CENTER_Y, CURRENT_ANIMATION_FRAME, FACING_RIGHT, FACING_LEFT, HERO_MOVE_SPEED

class Hero:
    def __init__(self, hero_type: HeroType) -> None:
        self.game_data = GameData()
        self.hero_type = hero_type
        self.current_animation_frame = CURRENT_ANIMATION_FRAME
        self.facing_right = FACING_RIGHT

        self.character_animations = {
            HeroType.PARIENTE: [
                self.game_data.get_hero_data(HeroType.PARIENTE, HeroState.IDLE)[0],
                self.game_data.get_hero_data(HeroType.PARIENTE, HeroState.RUN)[0],
                self.game_data.get_hero_data(HeroType.PARIENTE, HeroState.RUN)[1]
            ],
            HeroType.HIJITA: [
                self.game_data.get_hero_data(HeroType.HIJITA, HeroState.IDLE)[0],
                self.game_data.get_hero_data(HeroType.HIJITA, HeroState.RUN)[0],
                self.game_data.get_hero_data(HeroType.HIJITA, HeroState.RUN)[1]
            ],
            HeroType.CUMPA: [
                self.game_data.get_hero_data(HeroType.CUMPA, HeroState.IDLE)[0],
                self.game_data.get_hero_data(HeroType.CUMPA, HeroState.RUN)[0],
                self.game_data.get_hero_data(HeroType.CUMPA, HeroState.RUN)[1]
            ]
        }

        self.image: Surface = self.get_current_image()
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (CENTER_X, CENTER_Y)

    def get_current_image(self) -> Surface:
        animation_frames = self.character_animations[self.hero_type]
        current_image = animation_frames[self.current_animation_frame]
        return current_image if self.facing_right else transform.flip(current_image, True, False)

    def update_image(self) -> None:
        self.image = self.get_current_image()

    def move_left(self) -> None:
        if self.facing_right:
            self.facing_right = FACING_LEFT
        self.current_animation_frame = (self.current_animation_frame + 1) % len(self.character_animations[self.hero_type])
        self.update_image()
        self.image_rect.x -= HERO_MOVE_SPEED

    def move_right(self) -> None:
        if not self.facing_right:
            self.facing_right = FACING_RIGHT
        self.current_animation_frame = (self.current_animation_frame + 1) % len(self.character_animations[self.hero_type])
        self.update_image()
        self.image_rect.x += HERO_MOVE_SPEED

    def change_hero(self, hero_type: HeroType) -> None:
        self.hero_type = hero_type
        self.current_animation_frame = 0
        self.update_image()
        self.image_rect.center = (CENTER_X, CENTER_Y)
