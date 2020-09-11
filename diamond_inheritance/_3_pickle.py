from collections import Counter, OrderedDict
import pickle


class OrderedCounter(Counter, OrderedDict):
    pass


class OrderedCounterReduce(Counter, OrderedDict):
    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)


my_string = 'abracadabra'

my_dict = OrderedCounter(my_string)
my_dict_reduce = OrderedCounterReduce(my_string)


# no difference. maybe with a file it would be a problem
pickle.dumps(my_dict)
pickle.dumps(my_dict_reduce)