from src.managers.data_manager import DataManager
import src.objects as ObjectClass

# Initialize DataManager
manager = DataManager()

manager.add_object(object_class=ObjectClass.Node, object_name='node_1')
manager.add_object(object_class=ObjectClass.Generator, object_name='gen_1')
manager.add_property(object_class=ObjectClass.Generator,
                     object_name='gen_1',
                     property_name='nominal_power',
                     property_value=400)