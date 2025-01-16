from src.objects import Fuel, Node, Generator, Load

class RelationshipManager:
    # Define the parent-child relationships using tuples of classes
    rules = {
        Node: {"children": (Generator, Load), "parent": ()},
        Generator: {"children": (), "parent": (Node,)},
        Load: {"children": (), "parent": (Node,)},
    }

    @classmethod
    def is_valid_child(cls, parent, child):
        """
        Check if the child is allowed for the given parent.

        Args:
            parent (AbstractObject): The parent object.
            child (AbstractObject): The child object.

        Returns:
            bool: True if valid, False otherwise.
        """
        allowed_children = cls.rules.get(type(parent), {}).get("children", [])
        return type(child) in allowed_children

    @classmethod
    def is_valid_parent(cls, child, parent):
        """
        Check if the parent is valid for the given child.

        Args:
            child (AbstractObject): The child object.
            parent (AbstractObject): The parent object.

        Returns:
            bool: True if valid, False otherwise.
        """
        required_parent = cls.rules.get(type(child), {}).get("parent", None)
        return isinstance(parent, required_parent) if required_parent else True
