class NamespaceTest:
    __class_attribute = None

    def __init__(self):
        # print(f"__class_attribute: {__class_attribute}") Unresolved reference
        print(f"NamespaceTest.__class_attribute at the very beginning: {NamespaceTest.__class_attribute}")
        print(f"self.__class_attribute at the very beginning: {self.__class_attribute}")
        NamespaceTest.__class_attribute = "Koshka"
        print(f"NamespaceTest.__class_attribute after koshka: {NamespaceTest.__class_attribute}")
        print(f"self.__class_attribute after koshka: {self.__class_attribute}")
        self.instance_attribute = "instance_kis"
        # print(self.__class_attribute)
        # print(self.instance_attribute)

    @staticmethod
    def get_instance():
        if NamespaceTest.__class_attribute is None:
            NamespaceTest()
        return NamespaceTest.__class_attribute

print(NamespaceTest.get_instance()  )
a = NamespaceTest()
a.get_instance()
b = NamespaceTest()
