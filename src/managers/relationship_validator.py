from src.objects import ObjectClass, AbstractObject
from src.utils.abstract_object_subclasses import (
    get_object_class_name,
    get_abstract_object_subclass,
)
from typing import Type, Union


class RelationshipValidator:
    """
    A validation agent that checks if parent-child relationships
    are allowed based on predefined rules.
    """

    rules = {
        ObjectClass.Node:
            {"children": (ObjectClass.Generator, ObjectClass.Load),
             "parent": (),
             "required_parent": ()},
        ObjectClass.Generator:
            {"children": (ObjectClass.Fuel,),
             "parent": (ObjectClass.Node,),
             "required_parent": (ObjectClass.Node,)},
        ObjectClass.Load:
            {"children": (),
             "parent": (ObjectClass.Node,),
             "required_parent": (ObjectClass.Node,)},
        ObjectClass.Fuel:
            {"children": (),
             "parent": (ObjectClass.Generator,),
             "required_parent": ()},
    }

    @classmethod
    def is_valid_child(cls, parent_class: Union[Type[AbstractObject], str], child_class: Union[Type[AbstractObject], str]) -> bool:
        """Check if the child type is allowed for the given parent type."""
        try:
            parent_class = get_abstract_object_subclass(get_object_class_name(parent_class))
            child_class = get_abstract_object_subclass(get_object_class_name(child_class))
        except ValueError:
            return False  # Invalid class name provided

        allowed_children = cls.rules.get(parent_class, {}).get("children", [])
        return child_class in allowed_children

    @classmethod
    def is_valid_parent(cls, child_class: Union[Type[AbstractObject], str], parent_class: Union[Type[AbstractObject], str]) -> bool:
        """Check if the parent type is allowed for the given child type."""
        try:
            child_class = get_abstract_object_subclass(get_object_class_name(child_class))
            parent_class = get_abstract_object_subclass(get_object_class_name(parent_class))
        except ValueError:
            return False  # Invalid class name provided

        allowed_parents = cls.rules.get(child_class, {}).get("parent", None)
        return parent_class in allowed_parents if allowed_parents else True

    @classmethod
    def get_object_classes_with_required_parents(cls):
        """Return a set of object class names that have a non-empty required_parent list."""
        return [obj_class.__name__ for obj_class, rule in cls.rules.items() if rule.get("required_parent")]

    @classmethod
    def has_required_parent(cls, object_class: Union[Type[AbstractObject], str], parent_class: Union[Type[AbstractObject], str]) -> bool:
        """Check if the given object class requires the specified parent class."""
        try:
            object_class = get_abstract_object_subclass(get_object_class_name(object_class))
            parent_class = get_abstract_object_subclass(get_object_class_name(parent_class))
        except ValueError:
            return False  # Invalid class name provided

        required_parents = cls.rules.get(object_class, {}).get("required_parent", [])
        return parent_class in required_parents
