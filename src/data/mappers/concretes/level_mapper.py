from json import load
from typing import Any, Dict, List

from src.entities import Element, ElementFactory, IEntity
from src.enums import BackgroundType, ElementSubType, ElementType, Level, World
from src.utils.classes import Position
from src.utils.colors import BLACK_COLOR
from src.utils.directories import LEVELS_DIR

from ...background import BackgroundColor, IBackground
from ...interfaces import ILevelData
from ...level_data import LevelData
from ..interfaces import ILevelMapper
from ..validations.json_validation import validate_level_data


class LevelMapper(ILevelMapper):

    def __init__(self) -> None:
        self.element_factory = ElementFactory()

    def map_level(self, world: World, level: Level) -> ILevelData:
        data = self.read_file_level(world, level)

        validate_level_data(data)

        background = self._map_background(data["background"])
        position = self._map_player_start_position(
            data["start_player_position"]
        )
        enemies = self._map_enemies(data["enemies"])
        elements = self._map_elements(data["elements"])
        power_ups = self._map_power_ups(data["power_ups"])

        return LevelData(
            world,
            level,
            data["time"],
            background,
            data["background_music"],
            position,
            enemies,
            elements,
            power_ups,
        )

    def read_file_level(self, world: World, level: Level) -> Dict[str, Any]:
        path = f"{LEVELS_DIR}/{world.value}/{level.value}.json"

        try:
            with open(path) as file:
                return load(file)
        except FileNotFoundError:
            raise ValueError(f"File not found: {path}")

    def _map_background(self, background_data: Dict[str, Any]) -> IBackground:
        background_type = BackgroundType(background_data["type"])

        if background_type is BackgroundType.COLOR:
            color = background_data["resource"]
            return BackgroundColor(color)
        else:
            return BackgroundColor(BLACK_COLOR)

    def _map_player_start_position(self, data: Dict[str, Any]) -> Position:
        return Position(data["x"], data["y"])

    def _map_elements(self, elements: list[Dict[str, Any]]) -> List[Element]:
        mappedElements: List[Element] = []

        for element in elements:
            position = Position(element["position"][0], element["position"][1])
            mappedElements.append(
                self.element_factory.create(
                    ElementType(element["type"]),
                    position,
                    ElementSubType(element["subtype"]),
                )
            )

        return mappedElements

    def _map_enemies(self, _enemies: list[Dict[str, Any]]) -> List[IEntity]:
        return []

    def _map_power_ups(self, _power_ups: list[Dict[str, Any]]) -> List[IEntity]:
        return []
