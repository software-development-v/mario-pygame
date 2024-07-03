class CheckpointManager:
    __has_checkpoint: bool = False

    @classmethod
    def has_checkpoint(cls) -> bool:
        return cls.__has_checkpoint

    @classmethod
    def set_checkpoint_reached(cls) -> None:
        cls.__has_checkpoint = True

    @classmethod
    def reset_checkpoint(cls) -> None:
        cls.__has_checkpoint = False
