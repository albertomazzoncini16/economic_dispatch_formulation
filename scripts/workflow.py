from src import DataManager, ObjectClass
from src.managers.objects_attributes_manager import ObjectAttributesManager
from src.managers.relationship_validator import RelationshipValidator, AbstractObject

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


rv = RelationshipValidator
for object_class_name in rv.get_object_classes_with_required_parents():
    for object_class_instance in manager.get_object_class_instances(object_class=object_class_name):
        object_class_instance: AbstractObject
        parent = ObjectAttributesManager.get_parent_object_class_name(object_class_instance)
        rv.has_required_parent(object_class=object_class_name, parent_class=parent[0])


