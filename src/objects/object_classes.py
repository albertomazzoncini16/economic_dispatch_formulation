from src.objects.abstract_object_class import AbstractObject
from dataclasses import dataclass, field

@dataclass
class Node(AbstractObject):
    pass

@dataclass
class Fuel(AbstractObject):
    price: float = 0

@dataclass
class Load(AbstractObject):
     load: float = 0.0

@dataclass
class Generator(AbstractObject):
    nominal_power: float = 0.0