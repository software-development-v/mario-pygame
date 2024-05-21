from src.design.settings.keyboard.keyboard_conf import KeyboardConf


class Settings:
    def __init__(
        self,
        music_volume: int,
        sound_effects_volume: int,
        keyboard_configuration: KeyboardConf,
    ):
        self.music_volume = music_volume
        self.sound_effects_volume = sound_effects_volume
        self.keyboard_configuration = keyboard_configuration

    def get_music_volume(self) -> int:
        return self.music_volume

    def set_music_volume(self, volume: int) -> None:
        self.music_volume = volume

    def get_sound_effects_volume(self) -> int:
        return self.sound_effects_volume

    def set_sound_effects_volume(self, volume: int) -> None:
        self.sound_effects_volume = volume

    def get_keyboard_conf(self) -> KeyboardConf:
        return self.keyboard_configuration

    def set_keyboard_conf(self, keyboard_conf: KeyboardConf) -> None:
        self.keyboard_configuration = keyboard_conf
