from src import DataManager, ObjectClass
from src.managers.objects_attributes_manager import ObjectAttributesManager
from src.managers.relationship_validator import RelationshipValidator, AbstractObject

# Initialize DataManager
manager = DataManager()
with manager:
    manager.add_object(object_class=ObjectClass.Node, object_name='node_1')
    manager.add_object(object_class=ObjectClass.Generator, object_name='gen_1')
    manager.add_attribute(object_class=ObjectClass.Generator,
                         object_name='gen_1',
                         attr_name='nominal_power',
                         attr_value=400)
    manager.add_object(object_class=ObjectClass.Generator, object_name='gen_2')
    manager.add_attribute(object_class=ObjectClass.Generator,
                         object_name='gen_2',
                         attr_name='nominal_power',
                         attr_value=400)

    # manager.add_membership(child_object_class=ObjectClass.Generator,
    #                        child_object_name='gen_1',
    #                        parent_object_class=ObjectClass.Node,
    #                        parent_object_name='node_1')



