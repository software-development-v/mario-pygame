from typing import List

from src.entities import IEntity


class Manager(IEntity):
    def __init__(self, entities: List[IEntity] = []) -> None:
        self.entities = entities

    def add_entities(self, entities: List[IEntity]) -> None:
        for entity in entities:
            self.entities.append(entity)