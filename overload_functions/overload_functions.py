# https://arpitbhayani.me/blogs/function-overloading

# Function overloading is the ability to have multiple functions
# with the same name but with different signatures/implementations.
from inspect import getfullargspec


class Function:
    """We create a class called Function that wraps any function and makes it
    callable through an overridden __call__ method and also exposes a method
    called key that returns a tuple which makes this function unique
    in entire codebase.
    """

    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        """Overriding the __call__ function which makes the
  instance callable.
  """
  # fetching the function to be invoked from the virtual namespace
  # through the arguments.
        fn = Namespace.get_instance().get(self.fn, *args)
        if not fn:
            raise Exception("no matching function found")
        return fn(*args, **kwargs)

    def key(self, args=None):
        # print(args)
        """returns a tuple that uniquely identifies the function in the codebase and holds

            the module of the function
            class to which the function belongs
            name of the function
            number of arguments the function accepts
        """
        #       if args not specified, extract the arguments from
        #       the function definition
        if args is None:
            args = getfullargspec(self.fn).args
        return tuple([
            self.fn.__module__,
            self.fn.__class__,
            self.fn.__name__,
            len(args or []),
        ])


class Namespace:
    """Virtual Namespace we build here will store all the functions we gather
     during the definition phase. As there be only one namespace/registry
     we create a singleton class that holds the functions in a dictionary
     whose key will not be just a function name
      but the tuple we get from the key function,
      which contains elements that uniquely identify function in the entire codebase. """

    __instance = None

    def __init__(self):
        if self.__instance is None:  # why self.instance, not Namespace.instance?
            self.function_map = dict()
            Namespace.__instance = self
        else:
            raise Exception("cannot instantiate a virtual Namespace again ")

    @staticmethod
    def get_instance():
        if Namespace.__instance is None:
            Namespace()
        return Namespace.__instance

    def register(self, fn):
       func = Function(fn)
       self.function_map[func.key()] = fn
       return func

    def get(self, fn, *args):
        """get returns the matching function from the virtual namespace.
        The role of this get function is to decide
         which implementation of a function (if overloaded) is to be invoked.
         The process of getting the appropriate function is pretty simple -
         from the function and the arguments create the unique key
         using key function (as was done while registering)
         and see if it exists in the function registry;
        if it does then fetch the implementation stored against it.
            return None if it did not fund any matching function.
          """
        func = Function(fn)
        return self.function_map.get(func.key(args=args)) 


def overload(fn):
    """overload is the decorator that wraps the function
      and returns a callable object of type Function.
      """
    return Namespace.get_instance().register(fn)
# The overload decorator returns an instance of Function,
# as returned by .register() the function of the namespace.
# Now whenever the function (decorated by overload) is called,
# it invokes the function returned by the .register() function
# - an instance of Function and the __call__ method gets executed
# with specified args and kwargs passed during invocation.
















