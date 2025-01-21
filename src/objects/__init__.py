from .abstract_object_class import AbstractObject
# Import all the specific object classes to ensure registration
from .specific_object_classes import *
from .registry_object_subclasses import SubClassesRegistry
# Instantiate the registry (it creates an instance of SubClassesRegistry, which is necessary for registering all subclasses)
ObjectClass = SubClassesRegistry()