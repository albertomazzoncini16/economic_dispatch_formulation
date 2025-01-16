from src.managers.data_manager import DataManager
from src.objects import Node, Generator, Load, Fuel


def main():
    # Initialize DataManager
    manager = DataManager(filename="data.pkl")

    # Load existing data
    manager.load_data()

    # Create objects
    node1 = Node(1, "Node1")
    node2 = Node(2, "Node2")
    generator1 = Generator(object_name="Gen1")
    fuel1 = Fuel(4, "Fuel1")

    # Add objects to DataManager
    manager.add_object(node1)
    manager.add_object(node2)
    manager.add_object(generator1)
    manager.add_object(fuel1)

    # Add properties
    manager.add_property("Node", "Node1", "voltage", 110)
    manager.add_property("Node", "Node2", "voltage", 220)

    # Create relationships
    manager.add_membership("Node", "Node2", "Node", "Node1")
    manager.add_membership("Generator", "Gen1", "Node", "Node1")
    manager.add_membership("Fuel", "Fuel1", "Generator", "Gen1")

    # Export data to CSV
    manager.export_to_csv("exports/")

    # Display structure
    print("Nodes:", manager.list_all_names_for_class("Node"))
    print("Generators:", manager.list_all_names_for_class("Generator"))
    print("All objects:", [obj.name for obj in manager.get_all_objects()])

    # Save updated data
    manager.save_data()


if __name__ == "__main__":
    main()
