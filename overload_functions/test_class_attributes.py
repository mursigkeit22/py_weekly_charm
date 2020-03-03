class AttributeClass:
    """The class attribute (class_attr) is accessible
    as both a property of the class and as a property of objects,
    as it is shared between all of them."""
    class_attribute = 'class attribute'
    _private_class_attribute = 'private class attribute'
    __very_private_class_attribute = 'very private class attribute'

    def __init__(self):
        self.instance_attribute = 'instance attribute'
        self._private_instance_attribute = 'private instance attribute'
        self.__very_private_instance_attribute = 'very private instance attribute'
#       The instance_attribute is only accessible from the scope of an object.

print(AttributeClass.class_attribute)
print(AttributeClass._private_class_attribute)
# print(AttributeClass.__very_private_class_attribute)   #AttributeError
print(AttributeClass._AttributeClass__very_private_class_attribute)
print('----------')
class_instance = AttributeClass()
print(class_instance.instance_attribute)
print(class_instance._private_instance_attribute)
print(class_instance._AttributeClass__very_private_instance_attribute)
print('----------')
print(class_instance.class_attribute)
print(class_instance._private_class_attribute)
print(class_instance._AttributeClass__very_private_class_attribute)