from typing import Type, Dict, TypeVar, Generic, Any
from abc import ABC
import pkgutil
import importlib
import inspect


T = TypeVar('T')

class BaseFactory(ABC,Generic[T]):
    def __init__(self, base_class: Type[T], modules: list[str]) -> None:
        self.registry: Dict[str, Type[T]] = {}
        self.base_class = base_class

        for module in modules:
            self._register_all_subclasses(module)

    def _register_all_subclasses(self, module_name: str) -> None:
        package = importlib.import_module(module_name)
        for _, module_name, ispkg in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
            if not ispkg:
                module = importlib.import_module(module_name)
                self._register_classes_from_module(module)

    def _register_classes_from_module(self, module: Any) -> None:
        for _, cls in inspect.getmembers(module, inspect.isclass):
            if issubclass(cls, self.base_class) and cls is not self.base_class:
                self._register(cls)

    def _register(self, cls: Type[T]) -> None:
        self.registry[cls.__name__.lower()] = cls

    def _create(self, obj_type: str, *args: Any, **kwargs: Any) -> T:
        cls = self.registry.get(obj_type.lower())
        if not cls:
            raise ValueError(f"Unknown object type: {obj_type}. Available types: {list(self.registry.keys())}")
        return cls(*args, **kwargs)
