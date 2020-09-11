from collections import Counter

"""
https://www.youtube.com/watch?v=EiOglTERPEo&t=1208s

Raymond Hettinger Super considered super
"""


class MyCounter(Counter):
    pass


my_string = 'abracadabra'
# print(help(MyCounter))
"""
 Method resolution order:
 |      MyCounter
 |      collections.Counter
 |      builtins.dict
 |      builtins.object
 """

print(MyCounter(my_string))
