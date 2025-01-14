from abc import ABC, abstractmethod
from typing import Dict, Any
from src.data.core_objects import GenericCoreObject

class ObjectCollection(ABC):
    def __init__(self):
        self._items: Dict[str, GenericCoreObject] = {}

    def add_property(self, object_name: str, property_name: str, property_value: Any):
        if object_name not in self._items:
            raise ValueError(f"Object {object_name} not found in the collection.")
        setattr(self._items[object_name], property_name, property_value)

    def add_membership(self, object_name: str, related_object_name: str):
        if object_name not in self._items or related_object_name not in self._items:
            raise ValueError("One or both objects not found in the collection.")
        obj = self._items[object_name]
        related_obj = self._items[related_object_name]
        obj.related_objects = getattr(obj, "related_objects", [])
        obj.related_objects.append(related_obj)

