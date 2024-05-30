from src.enums import ElementSubType
from src.enums import ElementType
from src.utils.classes.position import Position
from src.utils.factories import BaseFactory
from src.utils.factories.constants import NON_TOUCHABLE_ELEMENTS_PATH, TOUCHABLE_ELEMENTS_PATH
from ...abstractions import Element


class FactoryElement(BaseFactory[Element]):

    def __init__(self) -> None:
        super().__init__(Element, [TOUCHABLE_ELEMENTS_PATH,NON_TOUCHABLE_ELEMENTS_PATH])


    def create(self, type : ElementType,position:Position, subtype:ElementSubType)-> Element:
        classname = type.name.lower().replace("_","")
        return self._create(classname, position,subtype)
