from src.objects import ObjectClass, AbstractObject

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
    def is_valid_child(cls, parent_class: type[AbstractObject], child_class: type[AbstractObject]):
        """Check if the child type is allowed for the given parent type."""
        allowed_children = cls.rules.get(parent_class, {}).get("children", [])
        return child_class in allowed_children

    @classmethod
    def is_valid_parent(cls, child_class: type[AbstractObject], parent_class: type[AbstractObject]):
        """Check if the parent type is allowed for the given child type."""
        allowed_parents = cls.rules.get(child_class, {}).get("parent", None)
        return parent_class in allowed_parents if allowed_parents else True

    @classmethod
    def get_object_classes_with_required_parents(cls):
        """Return a set of object class names that have a non-empty required_parent list."""
        return [obj_class.__name__ for obj_class, rule in cls.rules.items() if rule.get("required_parent")]

    @classmethod
    def has_required_parent(cls, object_class: type[AbstractObject], parent_class: type[AbstractObject]):
        """Check if the given object class requires the specified parent class."""
        required_parents = cls.rules.get(object_class, {}).get("required_parent", [])
        return parent_class in required_parents
