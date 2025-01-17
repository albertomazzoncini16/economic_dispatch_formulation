from src.objects import Fuel, Node, Generator, Load

class RelationshipValidator:
    """
    A validation agent that checks if parent-child relationships
    are allowed based on predefined rules.
    """

    rules = {
        Node: {"children": (Generator, Load), "parent": ()},
        Generator: {"children": (Fuel,), "parent": (Node,)},
        Load: {"children": (), "parent": (Node,)},
        Fuel: {"children": (), "parent": (Generator,)}
    }

    @classmethod
    def is_valid_child(cls, parent_class, child_class):
        """Check if the child type is allowed for the given parent type."""
        allowed_children = cls.rules.get(parent_class, {}).get("children", [])
        return child_class in allowed_children

    @classmethod
    def is_valid_parent(cls, child_class, parent_class):
        """Check if the parent type is allowed for the given child type."""
        allowed_parents = cls.rules.get(child_class, {}).get("parent", None)
        return parent_class in allowed_parents if allowed_parents else True