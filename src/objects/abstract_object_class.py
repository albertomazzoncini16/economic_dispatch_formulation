from dataclasses import dataclass, field

@dataclass
class AbstractObject:
    object_name: str  # Required attribute for all subclasses
    parent: dict = field(default_factory=dict)  # Stores references to parent objects
    children: dict = field(default_factory=dict)  # Stores references to child objects
