a = None
b = []
c = 0
d = False


def adding_func_NOT(element=1, starter_list=None):
    if not starter_list:
        print("function with check 'not': ")
        print(starter_list)


def adding_func_IS_NONE(element=1, starter_list=None):
    if starter_list is None:
        print("function with check 'is None': ")
        print(starter_list)


for el in [a, b, c, d]:
    adding_func_NOT(starter_list=el)
    adding_func_IS_NONE(starter_list=el)

print("================")
print("None is False:")  # False
print(None is False)
print("None == False:")  # False
print(None == False)
print("not None: ")  # True   (двойное отрицание)
# not и is not разные вещи
print(not None)





# None is falsy.
# The following objects are all falsy as well:
#
# Empty lists
# Empty dictionaries
# Empty sets
# Empty strings
# 0
# False
