

from abc import ABC, abstractmethod

### Core Objects ###

class CoreObject(ABC):
    def __init__(self, object_name):
        self.object_name = object_name
        self.parent = None
        self.children = []

    def add_child(self, child):
        if child not in self.children:
            self.children.append(child)
            child.parent = self

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)
            child.parent = None

class Node(CoreObject):
    def __init__(self, object_name, voltage=None):
        super().__init__(object_name)
        self.voltage = voltage

class Generator(CoreObject):
    def __init__(self, object_name, capacity=None):
        super().__init__(object_name)
        self.capacity = capacity

class Fuel(CoreObject):
    def __init__(self, object_name, fuel_type=None):
        super().__init__(object_name)
        self.fuel_type = fuel_type


### Object Collections ###

class ObjectCollection(ABC):
    def __init__(self):
        self.objects = {}

    def add_object(self, object_name, **kwargs):
        if object_name not in self.objects:
            self.objects[object_name] = self.create_object(object_name, **kwargs)

    def get_object(self, object_name):
        return self.objects.get(object_name)

    def add_property(self, object_name, property_name, property_value):
        obj = self.get_object(object_name)
        if obj:
            setattr(obj, property_name, property_value)

    @abstractmethod
    def create_object(self, object_name, **kwargs):
        pass

class NodeCollection(ObjectCollection):
    def create_object(self, object_name, **kwargs):
        return Node(object_name, **kwargs)

class GeneratorCollection(ObjectCollection):
    def create_object(self, object_name, **kwargs):
        return Generator(object_name, **kwargs)

class FuelCollection(ObjectCollection):
    def create_object(self, object_name, **kwargs):
        return Fuel(object_name, **kwargs)


### Managers ###

class DataCollectionsManager:
    def __init__(self):
        self.collections_storage = {}

    def _get_or_create_collection(self, collection_class):
        if collection_class not in self.collections_storage:
            self.collections_storage[collection_class] = collection_class()
        return self.collections_storage[collection_class]

    def add_object(self, object_class, object_name, **kwargs):
        collection = self._get_or_create_collection(object_class)
        collection.add_object(object_name, **kwargs)

    def add_property(self, object_class, object_name, property_name, property_value):
        collection = self._get_or_create_collection(object_class)
        collection.add_property(object_name, property_name, property_value)

    def add_membership(self, child_class, child_name, parent_class, parent_name):
        child_collection = self._get_or_create_collection(child_class)
        parent_collection = self._get_or_create_collection(parent_class)

        child = child_collection.get_object(child_name)
        parent = parent_collection.get_object(parent_name)

        if child and parent:
            parent.add_child(child)

class SystemManager:
    def __init__(self):
        self.data_manager = DataCollectionsManager()

    def add_object(self, object_class_name, object_name, **kwargs):
        class_map = {
            "Node": NodeCollection,
            "Generator": GeneratorCollection,
            "Fuel": FuelCollection
        }
        object_class = class_map.get(object_class_name)
        if object_class:
            self.data_manager.add_object(object_class, object_name, **kwargs)

    def add_property(self, object_class_name, object_name, property_name, property_value):
        class_map = {
            "Node": NodeCollection,
            "Generator": GeneratorCollection,
            "Fuel": FuelCollection
        }
        object_class = class_map.get(object_class_name)
        if object_class:
            self.data_manager.add_property(object_class, object_name, property_name, property_value)

    def add_membership(self, child_class_name, child_name, parent_class_name, parent_name):
        class_map = {
            "Node": NodeCollection,
            "Generator": GeneratorCollection,
            "Fuel": FuelCollection
        }
        child_class = class_map.get(child_class_name)
        parent_class = class_map.get(parent_class_name)
        if child_class and parent_class:
            self.data_manager.add_membership(child_class, child_name, parent_class, parent_name)


### Example Testing ###

def example_testing():
    manager = SystemManager()

    # Adding objects
    manager.add_object("Node", "Node1", voltage=110)
    manager.add_object("Node", "Node2", voltage=220)
    manager.add_object("Generator", "Gen1", capacity=100)

    # Adding properties
    manager.add_property("Node", "Node1", "voltage", 120)
    manager.add_property("Generator", "Gen1", "capacity", 150)

    # Creating memberships
    manager.add_membership("Generator", "Gen1", "Node", "Node1")

    # Validating relationships
    node1 = manager.data_manager.collections_storage[NodeCollection].get_object("Node1")
    generator = manager.data_manager.collections_storage[GeneratorCollection].get_object("Gen1")

    print(f"Node1 voltage: {node1.voltage}")
    print(f"Generator parent: {generator.parent.object_name}")

# Uncomment below to run the test
example_testing()
