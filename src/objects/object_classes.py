from src.objects.abstract_object_class import AbstractObject

class Node(AbstractObject):
    def __init__(self, object_name):
        super().__init__(object_name)

class Fuel(AbstractObject):
    def __init__(self, object_name,
                 price: float = 0):
        super().__init__(object_name)
        self.price = price

class Load(AbstractObject):
    def __init__(self, object_name,
                 load: float = 0.0):
        super().__init__(object_name)
        self.load = load

class Generator(AbstractObject):
    def __init__(self, object_name,
                 nominal_power: float = 0.0):
        super().__init__(object_name)
        self.nominal_power = nominal_power