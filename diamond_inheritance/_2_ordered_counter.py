from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)



my_string = 'abracadabra'

print(OrderedCounter(my_string))