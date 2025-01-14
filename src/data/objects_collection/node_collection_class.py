from src.data.core_objects.node import Node
from src.data.objects_collection import Collection


class NodeCollection(Collection):
    def __init__(self):
        super().__init__()

    def add(self, node: Node):
        if not self.find_by_name():
            self.items.append(node)
        else:
            print(f"Node with name {node.node_name} already exists.")