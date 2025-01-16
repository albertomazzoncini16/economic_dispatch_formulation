from src.objects.abstract_object_class import AbstractObject

class Node(AbstractObject):
    def __init__(self, object_name):
        super().__init__(object_name)


class Fuel(AbstractObject):
    allowed_membership_child = ()  # Loads cannot have children
    def __init__(self, object_name,
                 price: float = 0):
        super().__init__(object_name)
        self.price = price

class Load(AbstractObject):
    allowed_membership_child = ()  # Loads cannot have children
    requires_parent = (Node,)      # Loads must have a Node as a parent

    def __init__(self, object_name,
                 load: float = 0.0):
        super().__init__(object_name)
        self.load = load

class Generator(AbstractObject):
    allowed_membership_child = (Fuel,)  # Loads cannot have children
    requires_parent = (Node,)      # Loads must have a Node as a parent
    def __init__(self, object_name,
                 nominal_power: float = 0.0):
        super().__init__(object_name)
        self.nominal_power = nominal_power

    @property
    def nominal_power(self):
        return self._nominal_power

    @nominal_power.setter
    def nominal_power(self, value: float):
        if value < 0:
            raise ValueError("Generator nominal power cannot be negative.")
        self._nominal_power = value