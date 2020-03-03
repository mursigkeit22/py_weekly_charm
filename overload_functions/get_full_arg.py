from inspect import getfullargspec

def area(radius):
    return 3.14 * radius ** 2


args = getfullargspec(area).args

print(args)
print(area.__module__)
print(area.__class__)
print(area.__name__)