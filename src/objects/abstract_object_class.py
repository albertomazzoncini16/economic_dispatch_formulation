from abc import ABC
from dataclasses import dataclass, field

@dataclass
class AbstractObject(ABC):
    object_name: str  # Required attribute for all subclasses
    parent: dict = field(default_factory=dict)  # Stores references to parent objects
    children: dict = field(default_factory=dict)  # Stores references to child objects
