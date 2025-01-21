from src import DataManager, ObjectClass
from src.managers.relationship_validator import RelationshipValidator
# Initialize DataManager
manager = DataManager()

manager.add_object(object_class=ObjectClass.Node, object_name='node_1')
manager.add_object(object_class=ObjectClass.Generator, object_name='gen_1')
manager.add_attribute(object_class=ObjectClass.Generator,
                     object_name='gen_1',
                     attr_name='nominal_power',
                     attr_value=400)

manager.add_membership(child_object_class=ObjectClass.Generator,
                       child_object_name='gen_1',
                       parent_object_class=ObjectClass.Node,
                       parent_object_name='node_1')

r = RelationshipValidator
r.get_object_classes_with_required_parents()
r.has_required_parent(object_class=ObjectClass.Node, parent_class=ObjectClass.Generator)

