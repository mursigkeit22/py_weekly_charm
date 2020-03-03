from inspect import getfullargspec


class Function:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        return self.fn(*args, **kwargs)

    def key(self, args=None):
        if args is None:
            args = getfullargspec(self.fn).args
        return tuple([
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            len(args or []),
        ])


def area(l, b):
    return l * b


func = Function(area)
print(func.key())
# ('__main__', <class 'function'>, 'area', 2)


# the function area is wrapped in Function instantiated in func.
# The key() returns the tuple whose first element is the module name __main__,
# second is the class <class 'function'>,
# the third is the function name area while the fourth is the number of
# arguments that function area accepts which is 2.

print(func(3, 4))
# The overridden __call__ method invokes the wrapped function and returns the computed value (nothing fancy here right now).
# This makes the instance callable just like the function and it behaves exactly like the wrapped function
# 12

# print(func())
#TypeError: area() missing 2 required positional arguments: 'l' and 'b'

