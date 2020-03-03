import ctypes
# https://repl.it/@arpitbbhayani/super-long-int?language=python3
"""
PyLongObject represents one bignum as defined
by CPython and will map to `_longobject` of
its internals.

Here we have preallocated ob_digit array to hold
at max 100 digits/elements.
"""


class PyLongObject(ctypes.Structure):
    _fields_ = [
        ("ob_refcnt", ctypes.c_long),
        ("ob_type", ctypes.c_void_p),
        ("ob_size", ctypes.c_ulong),
        ("ob_digit", ctypes.c_uint * 100)
    ]


"""
get_digits function returns ob_digits array
representing how a big number is stored
internally as "digits".

The function returns a list of digits starting
from least significant digit to most significant.
The length of the list implies `ob_size`.   # doesn't work for my laptop
"""


def get_digits(bignum):
    obj = PyLongObject.from_address(id(bignum))
    # return obj.ob_digit[:obj.ob_size]  # doesn't work on my laptop this way
    return obj.ob_digit[1:4]


if __name__ == '__main__':
    num = (2 ** 60) + 2 ** 30 + 5
    digits = get_digits(num)
    print(num, digits)
    num = (2 ** 60) + 2 ** 30 - 1
    digits = get_digits(num)
    print(num, digits)
    num = (2 ** 60) + 1073741823
    digits = get_digits(num)
    print(num, digits)
