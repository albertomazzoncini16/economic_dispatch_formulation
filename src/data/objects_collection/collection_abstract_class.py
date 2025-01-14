from abc import ABC, abstractmethod
from typing import List

class Collection(ABC):
    """
    Abstract base class for managing a collection of objects.

    This class defines the common interface for all collections,
    including methods to add objects, find objects by name,
    and list all objects in the collection. Each specific collection
    (such as NodeCollection, GeneratorCollection, etc.) should inherit
    from this class and provide concrete implementations for the
    `add` and `find_by_name` methods.
    """
    def __init__(self, collection_name: str):
        self.items: List = []

    @abstractmethod
    def add(self, item) -> None:
        pass

    @abstractmethod
    def find_by_name(self, name: str):
        pass

    def list(self):
        for item in self.items:
            item.display_info()