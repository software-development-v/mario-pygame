
from typing import Any, Dict
from src.data.background.concretes.background_color import BackgroundColor
from src.data.background.interfaces.i_background import IBackground
from src.data.level_data import LevelData
from src.entities.abstractions.elements.element import Element
from src.entities.concretes.elements.factory_elements import FactoryElement
from src.entities.interfaces.i_entity import IEntity
from src.enums.background_type import BackgroundType
from src.enums.element_sub_type import ElementSubType
from src.enums.element_type import ElementType
from src.enums.level import Level
from src.enums.world import World
from src.utils.colors import BLACK_COLOR
from src.utils.constants import LEVELS_PATH
from ..interfaces.i_level_mapper import ILevelMapper
from src.utils.classes.position import Position
from .file_validation import validate_level_data
import json



class LevelMapper(ILevelMapper):

    def __init__(self) -> None:
        self.element_factory = FactoryElement()

    def map_level(self,world:World, level:Level) -> LevelData :

        data = self.read_file_level(world, level)
        validate_level_data(data)

        background = self._map_background(data["background"])
        position = self._map_player_start_position(data["start_player_position"])
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
            power_ups
        )


    def read_file_level(self,world:World, level:Level) -> Dict[str,Any]:
        path = f"{LEVELS_PATH}/{world.name.lower()}/{level.name.lower()}.json"
        try:
            with open(path) as file:
                return json.load(file)
        except FileNotFoundError:
            raise ValueError(f"File not found: {path}")


    def _map_background(self, background_data: Dict[str, Any]) -> IBackground:
        background_type = BackgroundType(background_data["type"])

        if background_type is BackgroundType.COLOR:
            color = background_data["resource"]
            return BackgroundColor(color)
        else:
            # by default
            return BackgroundColor(BLACK_COLOR)

    def _map_player_start_position(self, data: Dict[str, Any]) -> Position:
        return Position(data["x"],data["y"])


    def _map_elements(self,elements:list[Dict[str,Any]]) -> Dict[Position,Element]:
        mappedElements :Dict[Position,Element] = {}

        for element in elements:
            position = Position(element["position"][0],element["position"][1])
            mappedElements[position] = self.element_factory.create(ElementType(element["type"]),position,ElementSubType(element["subtype"]))

        return mappedElements


    def _map_enemies(self,enemies:list[Dict[str,Any]]) -> Dict[Position,IEntity]:
        return {}

    def _map_power_ups(self,power_ups:list[Dict[str,Any]]) -> Dict[Position,IEntity]:
        return {}



