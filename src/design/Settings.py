class Settings:
    def __init__(self, music_volume: int, sound_effects_volume: int, keyboard_configuration: str):
        self.music_volume = music_volume  # GameMusic instance
        self.sound_effects_volume = sound_effects_volume  # EffectMusic instance
        self.keyboard_configuration = keyboard_configuration  # KeyboardConf instance

    def get_music_volume(self) -> int:
        # Returns the current music volume
        return self.music_volume

    def set_music_volume(self, volume: int) -> None:
        # Sets the music volume to the specified value
        self.music_volume = volume

    def get_sound_effects_volume(self) -> int:
        # Returns the current sound effects volume
        return self.sound_effects_volume

    def set_sound_effects_volume(self, volume: int) -> None:
        # Sets the sound effects volume to the specified value
        self.sound_effects_volume = volume
