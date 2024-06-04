from typing import Any, Dict, Tuple, Type


class Singleton(type):
    _instances: Dict[Any, Any] = {}

    def __call__(
        cls: Type["Singleton"], *args: Tuple[Any, ...], **kwargs: Dict[str, Any]
    ) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(
                *args, **kwargs
            )
        return cls._instances[cls]
