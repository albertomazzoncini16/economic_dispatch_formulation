from src.data.core_objects.node import Node
from src.data.objects_collection import Collection
from typing import List


class NodeCollection(Collection):
    def __init__(self):
        Collection.__init__()

    def add(self, node: Node):
        if not self.find_by_name(node.node_name):
            self.items.append(node)
        else:
            print(f"Node with name {node.node_name} already exists.")