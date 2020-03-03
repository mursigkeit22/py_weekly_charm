from copy import copy


def area(radius):
    return 3.14 * radius ** 2


locals_caught_in_the_moment = copy(locals())   # deepcopy doesn't work: TypeError: can't pickle module objects


for key, value in locals_caught_in_the_moment.items():
    print(key, value)

print(locals())
