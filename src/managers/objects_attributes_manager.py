from src.objects.abstract_object_class import AbstractObject
from typing import Type

class ObjectAttributesManager:
    """Manages setting and retrieving attributes of an object."""

    @staticmethod
    def set_attribute(obj: AbstractObject, attr_name: str, attr_value):
        """Set a specific attribute on an object."""
        if hasattr(obj, attr_name):
            setattr(obj, attr_name, attr_value)
        else:
            raise AttributeError(f"'{obj.__class__.__name__}' object has no attribute '{attr_name}'") # TODO: check object_class.__name__

    @staticmethod
    def get_attribute(obj: AbstractObject, attr_name: str):
        """Retrieve a specific attribute from an object."""
        if hasattr(obj, attr_name):
            return getattr(obj, attr_name)
        raise AttributeError(f"'{obj.__class__.__name__}' object has no attribute '{attr_name}'") # TODO: check object_class.__name__

    @staticmethod
    def add_child(obj: AbstractObject, child_class: Type[AbstractObject], child_object_name: str):
        """Add a child object and store it as {class_name: [object_names]}."""
        child_class_name = child_class.__class__.__name__

        if child_class_name not in obj.children:
            obj.children[child_class_name] = []

        obj.children[child_class_name].append(child_object_name)

    @staticmethod
    def add_parent(obj: AbstractObject, parent_class: Type[AbstractObject], parent_object_name: str):
        """Add a parent object and store it as {class_name: [object_names]}."""
        parent_class_name = parent_class.__class__.__name__

        if parent_class_name not in obj.parent:
            obj.parent[parent_class_name] = []

        obj.parent[parent_class_name].append(parent_object_name)
